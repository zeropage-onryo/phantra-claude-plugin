# Zero Page Studio Skills

The Claude plugin for the **Zero Page Studio** connector. Two things with one name are easy to
mix up, so: the *connector* is the studio's remote MCP server (`https://api.zeropage.studio/mcp/claude`,
listed as "Zero Page Studio"); this *plugin*, `zeropage-studio-skills`, is the set of skills that
teaches Claude how to work in it, and it declares that connector.

Work in [Zero Page Studio](https://zeropage.studio) from a conversation with
Claude: open your projects, bring in your own photos and clips, write scenes
held to them, see what rendering would cost in credits and approve the render
in the studio; trim, reshape, join and share what you made for free; and read
what has worked for you. Each piece of work lives in a project you can come
back to.

Zero Page Studio is an AI pre-production studio for creators and filmmakers.
You give it an idea and reference photos; a scene is one paste-ready prompt,
rendered one timed shot at a time, with a price in front of every spend.

**Nothing in this connector renders, draws or spends credits.** Claude writes
and saves the scene and prices it; the render is approved by you, in the
studio, on the scene's own page. The edits the connector can make (trim,
reshape, join) run on the studio's own server and cost nothing.

## What the plugin contains

- **A connector**: the studio's remote MCP server at
  `https://api.zeropage.studio/mcp/claude`. You sign in with your Zero Page
  Studio account; the tools read and write your own projects, scenes,
  elements and library and nobody else's.
- **Twenty-two skills** that teach Claude the studio workflow. Start with
  `zeropage-use`, which Claude loads before any write:
  - the work: `zeropage-use`, `start-a-project`, `ideas-and-projects`,
    `storyboard`, `write-scene`, `series-and-continuity`, `ad-variations`,
    `price-and-hand-off`
  - the look and the pictures: `look-matching`, `brand-kit-from-my-work`,
    `product-shots`, `camera-moves`, `model-prompting`, `sound-plan`
  - the kinds of piece: `ad-formats`, `ugc-ad`, `explainer`,
    `hooks-and-first-seconds`, `client-treatment`
  - finishing: `edit-and-deliver`, `platform-delivery`
  - the money: `credits-and-limits`

No skill invents testimonials, reviews, numbers or awards: claims come from
you.

## The connector's tools

Thirty-two tools; none of them renders, draws or spends credits.

| Tool | What it does |
|---|---|
| `projects` / `project` / `project_chat` / `create_project` | your projects: list, open one (brief, look, scenes, references, renders, recent chat), page its chat, start one |
| `elements` / `add_element` | the characters, props and places a scene is held to, with their photos; add one picture from an image address or a product page you give |
| `upload_link` | a one-time page where you upload a picture or a clip from your device into your studio (optionally straight onto an element) |
| `write_scene` / `duplicate_scene` / `scene` | save a scene Claude wrote with you (with what each photo is for), copy one with changes, read one back |
| `quote` / `video_models` / `recommend_model` | price a scene in credits with the studio link where you approve it; the models and what each costs; which model suits a job |
| `library` / `share_link` | what is in your library (renders and uploads); a download link for one of them |
| `reformat` / `trim_clip` / `assemble_clips` / `job` | a clip or still in a new shape, a range of a clip, clips joined into one — free, on the studio's server; check a job |
| `balance` / `credit_history` / `whoami` / `recent` / `search` | your credits and where they went; your workspace and plan; your latest work; search your studio |
| `preferences` / `set_preferences` | your workspace's defaults (frame, length, models, draft first) |
| `recipes` / `recipe` / `save_recipe` | the studio's recipes and your own |
| `feedback` | a note to the studio |
| `what_works` / `score_caption` | what you kept and what reached an audience; a caption scored against your own posts |

**Projects** are the same ones on your projects page in the studio.
`projects` lists them; `project` reopens one, whether you made it here or in
the studio. `create_project` starts a new one, and a scene saved with a
project's id is filed in it.

## Before you use it

1. Sign in once at https://zeropage.studio. Your workspace is created on the
   first sign-in and comes with a one-time trial grant of credits. The
   connector cannot create a workspace by itself; until you have one it
   answers "this sign-in has no workspace yet" and says where to sign in.
2. Add the plugin, then connect the Zero Page Studio connector on its
   Connectors tab and approve the sign-in.

## A 90-second demo

1. "What am I working on?" → Claude calls `projects` and lists them.
2. "I want a 10-second product spot for a matte black water bottle on a wet
   gym floor, no people." → Claude asks at most three short questions and
   proposes three ideas. You pick one.
3. "Here is the bottle." → Claude calls `upload_link`; you open the page on
   your phone and pick the photo, and it lands on a Bottle element. A photo
   that is already at a web address, or a product page, goes in with
   `add_element`.
4. "Write the scene." → Claude writes it as timed shots in the chat, takes
   your edits, and saves it with `write_scene`, held to your photos.
5. "What would it cost?" → Claude calls `quote`: the keyframes, the clip per
   shot, your balance, and the scene's link in the studio. "Which model?" →
   `recommend_model`.
6. You open the link and press Render on the scene's page. The price is shown
   again there before anything is spent.
7. "How is it going?" → Claude calls `scene`, then `library` once the clip has
   landed.
8. "Make me a square cut of the first second and a link I can send." →
   `trim_clip`, `reformat`, `share_link`: two free edits, one link.

## Data

The connector sends to your Zero Page Studio account at
`api.zeropage.studio`, over HTTPS, with the OAuth sign-in you approve:

- the scene prompts Claude writes with you, with a title, a length and what
  each photo is for;
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

It does not send the conversation. The studio stores the scenes, elements,
uploads and projects you make under your account until you remove them in
the studio, and keeps your preferences, recipes and feedback notes as dated
entries (there is no page to remove those yet; ask through Support); every
change but a scene rewrite is kept as a new item (a copy, a version, a new
entry), and nothing is deleted through the connector. Keyframes and renders are made in the studio, on its AI providers,
and are charged in credits from your balance only after the price is shown
there and you approve. A `share_link` is a time-limited download address for
one of your own files: anyone holding it can download that file until it
expires. See the studio's [privacy policy](https://zeropage.studio/privacy)
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

`claude plugin validate .` on 2026-10-12 (Claude Code 2.1.285; again after the rename to `zeropage-studio-skills`, 0.3.1):

```
✔ Validation passed
```
