# Phantra AI

Plan, write and price AI images and video from your own photos, in a
conversation with Claude. Open your projects in [Phantra](https://phantra.ai),
bring your photos and clips in as elements, write a scene as timed shots held
to them, see what it would cost in credits, and trim, reshape, join and share
what you already have. Each piece of work lives in a project you can come
back to.

**Images, video and audio are made in the Phantra studio, on your approval
there; nothing in the chat makes them.** When you ask for a new image or
clip, or a change to one you made (an edit, a cut-out, an animation, a camera
move, an upscale, sound, a new shape), Claude writes the prompt with you and
hands you a link: the studio's composer with the prompt already in the box,
on that render when it is a change (`open_in_studio`), or a scene's own page
(from `quote`). You see the price in credits there and approve it. Nothing in
the chat spends credits, and nothing is bought, posted or deleted through the
plugin.

Documentation: https://phantra.ai/mcp/claude

## What the plugin contains

- **A connector**: the studio's remote MCP server at
  `https://api.phantra.ai/mcp/claude`. You sign in with your Phantra account; the
  tools read and write your own projects, scenes, elements and library and
  nobody else's.
- **Thirty-two skills** that teach Claude the studio workflow. `setup` is the
  first minutes; `phantra-ai-use` holds the habits every other skill assumes.

| for | skills |
|---|---|
| getting started | `setup`, `phantra-ai-use`, `start-a-project`, `ideas-and-projects`, `browse-presets` |
| ads | `product-ad-set`, `ad-formats`, `ad-variations`, `product-shots`, `explainer` |
| creator-style video | `ugc-ad`, `ugc-review`, `ugc-unboxing`, `ugc-tutorial`, `ugc-try-on` |
| covers and scripts | `thumbnails`, `youtube-script` |
| changing what is made | `effects` |
| writing a scene | `write-scene`, `storyboard`, `hooks-and-first-seconds`, `camera-moves`, `look-matching`, `sound-plan`, `model-prompting`, `series-and-continuity` |
| pricing, studio links, delivering | `price-and-render`, `credits-and-limits`, `edit-and-deliver`, `platform-delivery` |
| a person's own style and clients | `brand-kit-from-my-work`, `client-treatment` |

No skill invents testimonials, reviews, numbers or awards: claims come from
you.

## The connector's tools

Thirty-three; none of them makes images, video or audio, and none spends credits.

| Tool | What it does |
|---|---|
| `projects` / `project` / `project_chat` / `create_project` | your projects: list, open one (brief, look, scenes, references, renders, recent chat), page its chat, start one |
| `elements` / `add_element` / `upload_link` | the characters, products and places a scene is held to, with their photos; add a picture from an address, a product page or a render; a one-time page to upload a file from your device |
| `write_scene` / `duplicate_scene` / `scene` | save a scene Claude wrote with you, copy one with changes, read one back |
| `quote` | price a scene's keyframes and clips in credits beside your balance, with the scene's page in the studio where you render it |
| `open_in_studio` | a link that opens the studio with a prompt in the box: a new image or clip, or (with a render as `source`) a change to one of yours, inside a project if you like |
| `video_models` / `recommend_model` | the video models with their frames, lengths and credits; which model suits a job |
| `library` / `share_link` | what is in your library (renders and uploads); a download link for one of them |
| `reformat` / `trim_clip` / `assemble_clips` / `job` | a clip or still in a new shape, a range of a clip, clips joined into one with an optional music bed, on the studio's server; follow the job |
| `balance` / `credit_history` / `whoami` / `recent` / `search` | your credits and where they went; your workspace; your latest work; search your studio |
| `preferences` / `set_preferences` | your workspace's defaults (frame, length, models, draft first) |
| `recipes` / `recipe` / `save_recipe` | the studio's recipes and your own |
| `feedback` | a note to the studio |
| `what_works` / `score_caption` | what you kept and what reached an audience; a caption scored against your own posts |

**Projects** are the same ones on your projects page in the studio.
`projects` lists them; `project` reopens one, whether you made it here or in
the studio. `create_project` starts a new one; a scene saved with a project's
id is filed in it, and a studio link with one opens inside it.

## Before you use it

1. Sign in once at https://phantra.ai. Your workspace is created on the
   first sign-in. The connector cannot create a workspace by itself; until
   you have one it answers "this sign-in has no workspace yet" and says where
   to sign in.
2. Add the plugin, then connect the Phantra connector on its Connectors tab
   and approve the sign-in.

## A short demo

1. "What am I working on?" → `whoami`, `recent`, `projects`.
2. "Draw an ad still of my bottle on a wet gym floor." → Claude writes the
   prompt with you and calls `open_in_studio`; you open the link, attach the
   bottle's photo, see the price and approve it in the studio.
3. "Keep that as the Bottle element." → `library` finds the still,
   `add_element` keeps it with the still as its source.
4. "Write a 10-second spot around it." → Claude writes the scene as timed
   shots in the chat, takes your edits and saves it with `write_scene`, held
   to the bottle's photo.
5. "What would it cost?" → `quote`: the keyframes, the clip per shot, your
   balance, and the scene's page in the studio, where you press Render.
6. "Give it a slow push-in and some sound." → `open_in_studio` with the clip
   as its source opens the studio's effects on it, with the instruction ready.
7. "A square cut of the first two seconds, and a link I can send." →
   `trim_clip`, `reformat`, `share_link`.

## Data

The connector sends to your Phantra account at `api.phantra.ai`, over HTTPS,
with the OAuth sign-in you approve:

- the scene prompts Claude writes with you, with a title, a length and what
  each photo is for, and the prompt, kind, frame and source of a studio link
  (`open_in_studio` puts the prompt in the link's address);
- a project's name, brief and look when you create one;
- the ids of your projects, scenes, renders, uploads and element photos;
- for `add_element`: the element's kind, name and a few words about it, and
  the address you gave. The studio fetches that one address itself (https
  only): an image file up to 15 MB, or a product page, whose main picture is
  taken and whose stated facts (name, brand, colour, size) are kept in the
  element's notes as text copied off the page;
- for `upload_link`: nothing but the request. The file goes from your device
  to the studio through the page the link opens, not through the chat;
- the words of a `feedback` note, the values of `set_preferences`, the text
  of a recipe you `save_recipe`, a caption you ask to `score_caption`, the
  words of a `search`, the job you describe to `recommend_model`, and a new
  scene text you give `duplicate_scene`.

It does not send the conversation. Stills, clips and effects are made in the
studio, on its AI providers, and are charged in credits from your balance only
after the price is shown there and you approve it. The studio stores the scenes, elements, uploads,
renders and projects you make under your account until you remove them in
the studio, and keeps your preferences, recipes and feedback notes as dated
entries (there is no page to remove those yet; ask through Support). Every
change but a scene rewrite is kept as a new item (a copy, a version, a new
render), and nothing is deleted through the connector. A `share_link` is a
time-limited download address for one of your own files: anyone holding it
can download that file until it expires. See the studio's
[privacy policy](https://phantra.ai/privacy) and
[terms](https://phantra.ai/terms) for what is kept and for how long. The
plugin itself runs no code, stores nothing, and sends nothing anywhere else.

Nothing in the plugin can draw, render, buy credits, change a plan, post
anywhere, or remove your work. Rewriting a scene replaces the text it had before.

## Rate limit

The connector allows a generous number of calls per minute per account (over a
hundred). A `429` carries `Retry-After` in seconds.

## Checks

    python3 scripts/check.py
    claude plugin validate .

`scripts/check.py` checks every skill against the tools the server has
(`scripts/mcp-tools.txt`, read off the studio server's code), the connector
address, and the listing text. It needs nothing but Python 3; add `--tools`
to list the tools each skill names.

## Support

`support@phantra.ai` · https://phantra.ai/support. Bugs in the plugin can
also be filed at https://github.com/zeropage-onryo/phantra-claude-plugin/issues.
