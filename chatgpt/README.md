# Zero Page Studio for ChatGPT (the plugin package)

The Agent Plugins package submitted to OpenAI's plugin directory (`https://platform.openai.com/plugins`):
`plugin.json` (identity, listing, review cases, publication), `mcp.json` (the render door,
`https://api.zeropage.studio/mcp`, OAuth with dynamic client registration) and the four icons.
No skills and no UI: it is the MCP server alone.

Build the ZIP from inside this folder, so the manifest sits at the ZIP's root:

    cd chatgpt && zip -r ../zeropage-studio-chatgpt-1.0.0.zip plugin.json mcp.json assets README.md

The Claude plugin at the repository root (`.claude-plugin/plugin.json`, the skills) is a different
package for a different directory and points at the other door, `/mcp/claude`.
