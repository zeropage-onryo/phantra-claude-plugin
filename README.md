# Zero Page Studio

Plan video scenes for [Zero Page Studio](https://zeropage.studio) from a
conversation with Claude: turn a brief into a few ideas you choose between,
write the scene against your own photos, see what rendering it would cost,
and open it in the studio to approve the render. Each piece of work lives in
a project you can come back to.

Zero Page Studio is an AI pre-production studio for creators and filmmakers.
You give it an idea and reference photos; a scene is one paste-ready prompt,
rendered one timed shot at a time, with a price in front of every spend.

**Nothing in this connector renders or spends credits.** Claude writes and
saves the scene and prices it; the render is approved by you, in the studio,
on the scene's own page.

## What the plugin contains

- **A connector**: the studio's remote MCP server at
  `https://api.zeropage.studio/mcp/claude`. You sign in with your Zero Page
  Studio account; the tools read and write your own projects, scenes and
  elements and nobody else's.
- **Five skills** that teach Claude the studio workflow:
  - `ideas-and-projects` — a brief becomes two to four ideas you choose
    between in the chat; a project keeps the work together.
  - `write-scene` — Claude writes the scene prompt in the studio's shape (an
    opening line naming your photos, a style block, timed shots, diegetic
    sound, an avoid list) and saves it against your photos.
  - `look-matching` — the visual look, from your own element photos and from
    a frame you describe. A scene is rendered against photographs you
    provided, never a name.
  - `price-and-hand-off` — what the keyframes and the clip would cost, and
    the link to the scene's page in the studio where you approve the render.
  - `credits-and-limits` — what is free, what costs credits, what a refusal
    or a 429 means.

The connector offers nine tools:

| Tool | What it does |
|---|---|
| `projects` | lists your projects |
| `project` | opens one: its brief, look, scenes, the references they used, its renders and recent chat |
| `project_chat` | pages back through a project's chat history |
| `create_project` | starts a project |
| `elements` | lists your elements: the characters, props and places a scene is held to, with their photos |
| `add_element` | adds one picture as an element, from an image address you give or one of your own renders |
| `write_scene` | saves a scene Claude wrote with you, or rewrites one |
| `scene` | reads one scene back: where it stands, its shots and its clips |
| `quote` | prices rendering a scene, in credits, and gives the studio link where you approve it |

None of them spends credits.

**Projects** are the same ones on your projects board in the studio.
`projects` lists them; `project` reopens one, whether you made it here or in
the studio. `create_project` starts a new one, and a scene saved with a
project's id is filed in it.

## Before you use it

1. Sign in once at https://zeropage.studio. Your workspace is created on the
   first sign-in and comes with a one-time trial grant of credits. The
   connector cannot create a workspace by itself; until you have one it
   answers "no account".
2. Add the plugin, then connect the Zero Page Studio connector on its
   Connectors tab and approve the sign-in.

## A 60-second demo

1. "What am I working on?" → Claude calls `projects` and lists them.
2. "I want a 10-second product spot for a matte black water bottle on a wet
   gym floor, no people." → Claude asks at most three short questions and
   proposes three ideas. You pick one.
3. "Here is the bottle: https://…/bottle.jpg" → Claude adds it as an element
   with `add_element`. Photos you already uploaded in the studio are listed by
   `elements`.
4. "Write the scene." → Claude writes it as timed shots in the chat, takes
   your edits, and saves it with `write_scene`, held to your photos.
5. "What would it cost?" → Claude calls `quote`: the keyframes, the clip per
   shot, your balance, and the scene's link in the studio.
6. You open the link and press Render on the scene's page. The price is shown
   again there before anything is spent.
7. "How is it going?" → Claude calls `scene` and reports the status and any
   clips that have landed.

## Data

The connector sends to your Zero Page Studio account at
`api.zeropage.studio`, over HTTPS, with the OAuth sign-in you approve:

- the scene prompts Claude writes with you, with a title and a length;
- a project's name, brief and look when you create one;
- the ids of your projects and scenes, and the refs of your own element
  photos;
- for `add_element`: the element's kind, name and a few words about it, and
  the address of the picture you gave. The studio fetches that one image
  itself (https only, an image file up to 15 MB) and saves it as it is.

It does not send the conversation. The studio stores the scenes, elements and
projects you write under your account until you remove them in the studio.
Keyframes and renders are made in the studio, on its AI providers, and are
charged in credits from your balance only after the price is shown there and
you approve; see the studio's [privacy policy](https://zeropage.studio/privacy)
and [terms](https://zeropage.studio/terms) for what is kept and for how long.
The plugin itself runs no code, stores nothing, and sends nothing anywhere
else.

Nothing in the plugin can render, buy credits, change a plan, post anywhere,
or remove your work. Rewriting a scene replaces the text it had before.

## Rate limit

The connector allows a generous number of calls per minute per account (over a
hundred). A `429` carries `Retry-After` in seconds.

## Support

Open an issue at https://github.com/zeropage-onryo/zeropage-studio-plugin/issues.

## Validated

`claude plugin validate ./zeropage-studio-plugin` on 2026-10-11 (Claude Code 2.1.285):

```
Validating plugin manifest: ./zeropage-studio-plugin/.claude-plugin/plugin.json

✔ Validation passed
```
