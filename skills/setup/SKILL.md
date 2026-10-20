---
name: setup
description: The first minutes with Phantra in Claude: what the person can plan and make here, the one sign-in, a look at what the workspace holds, and the one rule about spending. Use right after the plugin is installed, when the person asks how to start or what this can do, or when a call answers that the sign-in has no workspace yet. NOT for the work itself: writing a scene (write-scene), pricing and rendering (price-and-render) or explaining credits (credits-and-limits).
---

# Setting up Phantra

Phantra is an AI image and video studio the person already has an account
with. This plugin works inside that account from the chat: Claude plans,
writes, organises, prices and edits, and works on media the person provides;
new images and clips from a prompt are made in the studio, on their approval
there.

## 1. What they can do here

- **A still**: an ad image, a product shot, a cover. Write the prompt with
  them, then `open_in_studio` (`kind` image, an `aspect`) gives a link that
  opens the studio with the prompt in the box; they send it and approve the
  price there. A request to draw or make an image goes this way.
- **A video**: you write the scene with them as timed shots, `write_scene`
  saves it, `quote` prices it and answers `approve_url`, the scene's page in
  the studio where they render it, one clip per shot.
- **A change to their own image or clip**: `edit_image`, `remove_background`,
  `animate_still`, `camera_move`, `upscale_clip`, `add_sound` or
  `reframe_clip` make a new version of it here, by id from `library`, quoted
  first and run on their yes (effects).
- **A finished file**: `reformat` (a new shape), `trim_clip`, `assemble_clips`
  (join clips) and `share_link` (a download link). These run here and spend
  no credits.
- Everything made lands in their studio: `library` lists it, and `projects`
  keeps related scenes together with a brief and a look.

Start from what they want made. A sentence is enough for a still. A scene is
rendered against at least one picture, so before pricing one, ask for a
product or face photo (`upload_link` for a file on their device, `add_element`
for a picture or product page by its address, or a still from `library`,
whose `gen:<id>` is its `source`).

## 2. The sign-in

The person signs in once at https://phantra.ai to create their workspace,
then connects this plugin, which opens the studio's sign-in and a consent
page. If a call answers that the sign-in has no workspace yet, say exactly
that: sign in once on the site, then reconnect.

## 3. Look before you make

Call `whoami` (the workspace and who is signed in), then `recent` (the latest
projects, scenes and renders). Say in two sentences what is there. A new
workspace is empty: say so and offer one of the things above.

## 4. The one rule about spending

Reading, writing scenes, quotes, studio links, trims, reshapes and joins
spend nothing. An effect on their own media spends credits here: its first
call is the quote; show the price and the balance, wait for their yes in this
chat, and only then call again with its `quote_token`. Never say yes for them,
and never spend twice. A new still from a prompt and a scene's render spend
credits in the studio, where they see the price and approve it. If a quote
says the credits are short, say so and that credits are added in the studio.

## 5. Where to go next

- "Make me ads from this photo" → product-ad-set. "A cover" → thumbnails.
- "Start a project" → start-a-project. "Write the scene" → write-scene.
- "What would it cost, render it" → price-and-render.
- "What costs credits, where did my credits go" → credits-and-limits.
