#!/usr/bin/env python3
"""Check the Claude plugin against the /mcp tool list and its own listing rules.

    python3 scripts/check.py            # the manifest, the connector, every skill
    python3 scripts/check.py --tools    # also print which tools each skill names

Standard library only. Exit 0 when nothing failed; warnings do not fail.
Run `claude plugin validate .` as well: this checks what that does not.

Ported from the ChatGPT plugin's scripts/check.py (zeropage-onryo/phantra-chatgpt-plugin),
which checks OpenAI's limits; this one checks the same skills against the same tool list
(scripts/mcp-tools.txt, read off the studio server's code) and Claude's listing rules:
  - the connector is the render server, https://api.phantra.ai/mcp;
  - the listing text (plugin.json description, README) names no other company's model
    and no price or promotion ("free", a plan price);
  - a skill description is at most 500 characters (this package's own rule since 0.6.0);
  - no skill says renders happen only in the studio: the connector renders in the chat.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONNECTOR = "https://api.phantra.ai/mcp"
SKILL_LINES = 100
SKILL_DESCRIPTION = 500
IDENTITY = 64              # "plugin-name:skill-name"
PRICE = re.compile(r"\b\d+\s+credits?\b|\$\s?\d", re.I)
PROMOTION = re.compile(r"\bfree\b|\bfree of charge\b|\bno cost\b|\bdiscount|\bper month\b"
                       r"|/mo\b|\bsale\b", re.I)
MODEL_NAMES = re.compile(r"\b(kling|veo|seedance|ltx|wan|flux|seedream|gpt[- ]image|ideogram"
                         r"|nano banana|gemini|imagen|topaz|mmaudio|pixverse|runway"
                         r"|higgsfield|sora|midjourney|minimax|hailuo|recraft|bria"
                         r"|openai|google|bytedance|alibaba|black forest)\b", re.I)
STUDIO_ONLY = re.compile(r"renders? (are|is) (approved and )?made in the (phantra )?studio"
                         r"|never in the chat|press(es)? render|nothing in this connector (draws|renders)"
                         r"|renders? only in the studio", re.I)

fails: list[str] = []
warns: list[str] = []


def fail(msg: str) -> None:
    fails.append(msg)


def warn(msg: str) -> None:
    warns.append(msg)


def names(path: str) -> tuple[list[str], list[str]]:
    """(names, names marked "?") from a one-per-line list with # comments."""
    plain, soft = [], []
    for line in (ROOT / path).read_text().splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        name, _, mark = line.partition(" ")
        (soft if mark.strip() == "?" else plain).append(name)
    return plain, soft


def listing_text(label: str, text: str) -> None:
    for pattern, what in ((PRICE, "a price"), (PROMOTION, "pricing or promotion wording"),
                          (MODEL_NAMES, "another company's model or name"),
                          (STUDIO_ONLY, "that renders happen only in the studio")):
        for m in pattern.finditer(text):
            fail(f"{label} states {what}: {m.group(0)!r}")


def check_manifest() -> dict:
    manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    mcp = json.loads((ROOT / ".mcp.json").read_text())
    servers = mcp.get("mcpServers", {})
    if len(servers) != 1:
        fail(".mcp.json must declare exactly one MCP server")
    for server in servers.values():
        if server.get("url") != CONNECTOR:
            fail(f".mcp.json url is {server.get('url')!r}; the connector is {CONNECTOR}")

    name = manifest.get("name", "")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", name):
        fail(f"name {name!r}: kebab-case, 1-64 characters")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        fail("version must be semantic (1.0.0)")
    desc = manifest.get("description", "")
    if not desc or len(desc) > 1024:
        fail(f"description is {len(desc)} characters (1-1,024)")
    for key in ("homepage", "repository"):
        if not str(manifest.get(key, "")).startswith("https://"):
            fail(f"{key} must be an https URL")
    if manifest.get("homepage") != "https://phantra.ai/mcp":
        fail(f"homepage is {manifest.get('homepage')!r}; it is https://phantra.ai/mcp")
    listing_text("plugin.json description", desc)
    listing_text("README.md", (ROOT / "README.md").read_text())
    return manifest


def check_skills(plugin: str, tools: set[str], show_tools: bool) -> None:
    banned, soft = names("scripts/other-tools.txt")
    seen: dict[str, str] = {}
    folders = sorted(p for p in (ROOT / "skills").iterdir())
    for folder in folders:
        if not folder.is_dir() or folder.name.startswith("."):
            warn(f"skills/{folder.name} is not a skill folder; it is not loaded")
            continue
        path = folder / "SKILL.md"
        if not path.is_file():
            fail(f"skills/{folder.name} has no SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or lines[0] != "---" or "---" not in lines[1:]:
            fail(f"{folder.name}: no front matter between --- lines")
            continue
        end = lines.index("---", 1)
        front = {}
        for line in lines[1:end]:
            key, sep, value = line.partition(":")
            if not sep or not key.strip():
                fail(f"{folder.name}: front matter line {line!r} is not `key: value`")
            front[key.strip()] = value.strip()
        name, description = front.get("name", ""), front.get("description", "")
        if name != folder.name:
            fail(f"{folder.name}: name is {name!r}; it must match its folder")
        if name in seen:
            fail(f"{folder.name}: the name {name!r} is also used by {seen[name]}")
        seen[name] = folder.name
        if len(f"{plugin}:{name}") > IDENTITY:
            fail(f"{folder.name}: `{plugin}:{name}` is over {IDENTITY} characters")
        if not description or len(description) > SKILL_DESCRIPTION:
            fail(f"{folder.name}: description is {len(description)} characters "
                 f"(1-{SKILL_DESCRIPTION})")
        if "Use " not in description or "NOT for" not in description:
            warn(f"{folder.name}: description has no 'Use ...' or no 'NOT for' clause")
        if not "\n".join(lines[end + 1:]).strip():
            fail(f"{folder.name}: nothing below the front matter")
        if len(lines) > SKILL_LINES:
            fail(f"{folder.name}: {len(lines)} lines (at most {SKILL_LINES})")
        named = set()
        for n, line in enumerate(lines, 1):
            for token in re.findall(r"`([a-z][a-z0-9_]*)`", line):
                if token in tools:
                    named.add(token)
                elif token in banned:
                    fail(f"{folder.name}:{n} names `{token}`, which is not a tool on /mcp")
                elif token in soft:
                    warn(f"{folder.name}:{n} `{token}` is not a tool on /mcp; fine as a "
                         f"field or a value: {line.strip()[:90]}")
            if n > end and PRICE.search(line):
                fail(f"{folder.name}:{n} types a price; the tools give prices: "
                     f"{line.strip()[:90]}")
            if STUDIO_ONLY.search(line):
                fail(f"{folder.name}:{n} says renders happen only in the studio; the "
                     f"connector renders in the chat: {line.strip()[:90]}")
        for other in re.findall(r"\(([a-z][a-z0-9-]+)\)", description):
            if other not in {f.name for f in folders} and "-" in other:
                fail(f"{folder.name}: its description points at ({other}), "
                     "which is not a skill here")
        if show_tools:
            print(f"  {folder.name}: {', '.join(sorted(named)) or '(no tool named)'}")
    print(f"{len(seen)} skills")


def main() -> int:
    tools = set(names("scripts/mcp-tools.txt")[0])
    print(f"{len(tools)} tools on /mcp (scripts/mcp-tools.txt)")
    manifest = check_manifest()
    print(f"{manifest['name']} {manifest['version']}, description "
          f"{len(manifest['description'])}/1024")
    check_skills(manifest["name"], tools, "--tools" in sys.argv)
    for line in warns:
        print("warning:", line)
    for line in fails:
        print("FAIL:", line)
    print("ok" if not fails else f"{len(fails)} failed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
