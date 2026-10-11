# Zeropage Studio

Plan video scenes with [Zeropage Studio](https://zeropage.studio) from a
conversation with Claude: shape an idea together, write the scene against
your own reference photos, keep the work in a project you can come back to,
and see what it would cost to render. The render itself is approved by you,
in the studio, after the price is shown again.

Zeropage Studio is an AI production studio for brands, ad agencies, creators
and filmmakers. You give it an idea and reference photos; it holds a scene to
those photos, renders it one timed shot at a time, and shows a price in
credits before anything is spent.

## What the plugin contains

- **A connector**: the studio's remote MCP server at
  `https://api.zeropage.studio/mcp/claude`. You sign in with your Zeropage
  Studio account; the tools read and write your own projects and scenes and
  nobody else's. Nothing on this connector renders or spends credits.
- **Five skills** that teach Claude the studio workflow:
  - `projects-and-ideas`: a brief becomes two to four ideas you choose
    between, in the chat; your projects are listed, reopened or started.
  - `write-scene`: Claude writes the scene prompt in the studio's shape (an
    opening line naming your photos, a style block, timed shots, diegetic
    sound, an avoid list) and saves it as a scene against the photos you
    uploaded, in a project or on its own.
  - `look-matching`: the visual look, from your own element photos and from a
    frame you describe. The studio renders against photographs you uploaded,
    never a name and never an image off the web.
  - `render-and-status`: the price of the keyframes and the clip, the link to
    the scene's Render card in the studio, and what has landed since.
  - `credits-and-limits`: what is free, what costs credits, what a refusal or
    a 429 means.

The connector offers eight tools: `projects`, `project`, `project_chat`,
`create_project`, `elements`, `write_scene`, `scene`, `quote`. None of them
spends.

**Projects** are the same ones on your projects board in the studio.
`projects` lists them; `project` reopens one, whether you made it here or in
the studio, with its brief, its look, its scenes, the reference images those
scenes used, its renders and the latest turns of its chat in the studio;
`project_chat` pages back through that chat. `create_project` starts a new
one, and `write_scene` with its id files a scene in it.

### Two connector addresses

| address | for | renders from the chat? |
|---|---|---|
| `https://api.zeropage.studio/mcp/claude` | this plugin and the Claude directory | no: `quote` returns the scene's studio link, and you approve the render there |
| `https://api.zeropage.studio/mcp` | ChatGPT, or anyone who wants to approve renders in the chat | yes: `quote`, your yes, then `approve` (plus `job` to follow it) |

The skills work with either: `render-and-status` checks whether the connector
has an `approve` tool and follows that path.

## Before you use it

1. Sign in once at https://zeropage.studio. Your workspace is created on the
   first sign-in and comes with a one-time trial grant of credits. The
   connector cannot create a workspace by itself; until you have one it
   answers "no account".
2. Add the plugin, then connect the Zeropage Studio connector on its
   Connectors tab and approve the sign-in.

## A 60-second demo

1. "What projects do I have?" → Claude calls `projects` and lists them.
2. "I want a 10-second product spot for a matte black water bottle on a wet
   gym floor, no people." → Claude asks at most three short questions and
   proposes three ideas; you pick one.
3. "Write the scene, and keep it in a new project called Bottle ad." → Claude
   creates the project, reads your elements (the bottle you photographed, the
   gym floor), writes the scene as timed shots in the chat, takes your edits,
   and saves it with your photos attached.
4. "What would it cost?" → Claude quotes it: the keyframes, the clip per shot,
   your balance, and the link to the scene in the studio.
5. You open the link, check the price on the scene's Render card and approve
   it there. "Is it done?" → Claude reads `scene` and shows what has landed.
6. Next week, "open the bottle ad" brings back its brief, its scenes and the
   references they used.

## Data

The connector sends the scene prompts Claude writes with you, the ids of your
own element photos, projects and scenes, and a project's name, brief and look
when you create one, to your Zeropage Studio account at `api.zeropage.studio`,
over HTTPS, with the OAuth sign-in you approve. It does not send the text of
your conversation. The studio stores the projects and scenes under your
account. Renders run on the studio's AI providers only after you approve them
in the studio, and are charged in credits from your balance; see the studio's
[privacy policy](https://zeropage.studio/privacy) and
[terms](https://zeropage.studio/terms) for what is kept and for how long. The
plugin itself runs no code, stores nothing, and sends nothing anywhere else.

Nothing in the plugin can render, buy credits, change a plan, post anywhere,
or delete your work.

## Rate limit

The connector allows a generous number of calls per minute per account (over a
hundred). A `429` carries `Retry-After` in seconds. Checking a scene every 20
to 30 seconds never reaches it.

## Support

Open an issue at https://github.com/zeropage-onryo/zeropage-studio-plugin/issues.

## Validated

`claude plugin validate ./zeropage-studio-plugin` on 2026-10-11 (Claude Code 2.1.296): `Validation passed`.
