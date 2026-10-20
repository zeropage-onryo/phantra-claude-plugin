# Phantra AI

Make AI images and video from an idea or a product photo, right in the chat
with Claude. Draw a still, write a scene as timed shots held to your own
photos and render it clip by clip, change what you made with an effect, and
trim, reshape, join and share the result. Each piece of work lives in a
project in [Phantra](https://phantra.ai) you can come back to.

**Every still, clip and effect is quoted in credits first and made only on
your yes.** Claude shows the price and your balance and waits; only then does
it make the call that spends, with the quote's one-time token. Nothing is
bought, posted or deleted through the plugin.

Documentation: https://phantra.ai/mcp

## What the plugin contains

- **A connector**: the studio's remote MCP server at
  `https://api.phantra.ai/mcp`. You sign in with your Phantra account; the
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
| pricing, rendering, delivering | `price-and-render`, `credits-and-limits`, `edit-and-deliver`, `platform-delivery` |
| a person's own style and clients | `brand-kit-from-my-work`, `client-treatment` |

No skill invents testimonials, reviews, numbers or awards: claims come from
you.

## The connector's tools

Forty-two. The ones marked **spends** are always two calls: the first returns
a quote and spends nothing; only a second call with that quote's token, made
after your yes, runs it.

| Tool | What it does |
|---|---|
| `projects` / `project` / `project_chat` / `create_project` | your projects: list, open one (brief, look, scenes, references, renders, recent chat), page its chat, start one |
| `elements` / `add_element` / `upload_link` | the characters, products and places a scene is held to, with their photos; add a picture from an address, a product page or a render; a one-time page to upload a file from your device |
| `image_models` / `generate_image` | the image models; draw a still (**spends**) |
| `write_scene` / `duplicate_scene` / `scene` | save a scene Claude wrote with you, copy one with changes, read one back |
| `quote` / `approve` / `job` | price a scene's keyframes and clips; render them (**spends**); follow a running job |
| `video_models` / `recommend_model` | the video models and their frames and lengths; which model suits a job |
| `edit_image` / `remove_background` / `animate_still` / `camera_move` / `upscale_clip` / `add_sound` / `reframe_clip` | the effects: edit a still by instruction, cut out a subject, animate a still with a template, a camera move, upscale a clip, add sound, reshape a clip to a new frame (each **spends**) |
| `library` / `share_link` | what is in your library (renders and uploads); a download link for one of them |
| `reformat` / `trim_clip` / `assemble_clips` | a clip or still in a new shape, a range of a clip, clips joined into one with an optional music bed |
| `balance` / `credit_history` / `whoami` / `recent` / `search` | your credits and where they went; your workspace; your latest work; search your studio |
| `preferences` / `set_preferences` | your workspace's defaults (frame, length, models, draft first) |
| `recipes` / `recipe` / `save_recipe` | the studio's recipes and your own |
| `feedback` | a note to the studio |
| `what_works` / `score_caption` | what you kept and what reached an audience; a caption scored against your own posts |

**Projects** are the same ones on your projects page in the studio.
`projects` lists them; `project` reopens one, whether you made it here or in
the studio. `create_project` starts a new one, and a still, a scene or a
render given a project's id is filed in it.

## Before you use it

1. Sign in once at https://phantra.ai. Your workspace is created on the
   first sign-in. The connector cannot create a workspace by itself; until
   you have one it answers "this sign-in has no workspace yet" and says where
   to sign in.
2. Add the plugin, then connect the Phantra connector on its Connectors tab
   and approve the sign-in.

## A short demo

1. "What am I working on?" → `whoami`, `recent`, `projects`.
2. "Draw an ad still of my bottle on a wet gym floor." → `generate_image`
   answers a quote: the model, the credits, your balance after. You say yes;
   the same call with the quote's token draws it, and `job` brings back the
   picture and its `gen:<id>`.
3. "Keep that as the Bottle element." → `add_element` with the still as its
   source.
4. "Write a 10-second spot around it." → Claude writes the scene as timed
   shots in the chat, takes your edits and saves it with `write_scene`, held
   to the bottle's photo.
5. "Render it." → `quote` prices the keyframes and each clip beside your
   balance. You say yes; `approve` renders with the quote's tokens and `job`
   follows it to the finished clip.
6. "Give it a slow push-in and some sound." → `camera_move` and `add_sound`,
   each quoted and run only on your yes.
7. "A square cut of the first two seconds, and a link I can send." →
   `trim_clip`, `reformat`, `share_link`.

## Data

The connector sends to your Phantra account at `api.phantra.ai`, over HTTPS,
with the OAuth sign-in you approve:

- the prompts for the stills, scenes and effects Claude makes with you, with
  a title, a length, a frame and what each photo is for;
- a project's name, brief and look when you create one;
- the ids of your projects, scenes, renders, uploads and element photos, and
  the quote tokens you approved;
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

It does not send the conversation. Stills, clips and effects are made by the
studio on its AI providers, from the prompt and the reference pictures you
chose, and are charged in credits from your balance only after the quote is
shown and you say yes. The studio stores the scenes, elements, uploads,
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

Nothing in the plugin can buy credits, change a plan, post anywhere, or
remove your work. Rewriting a scene replaces the text it had before.

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
