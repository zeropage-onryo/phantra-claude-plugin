---
name: phantra-ai-use
description: The habits every Phantra skill assumes, loaded before any writing tool: reuse what the person has, hold every scene to a photo, quote before anything costs, send making to the studio, and never overwrite. Use when work on the connector starts, before the first `write_scene`, `create_project` or `add_element`, or when unsure what a tool spends or changes. NOT for one job's steps: a scene (write-scene), a render (price-and-render) or credits (credits-and-limits).
---

# Use the studio well

Every other skill in this plugin assumes these five habits. Read this once,
then keep to it on every call. This connector works on media the person
provides: the effect tools make a new version of one of their own images or
clips, each after a quote and their yes. A new still or clip from a prompt,
and a scene's render, are made in the studio on their approval there. The
rest reads, saves text, prices, hands over studio links, or starts an edit
that spends nothing.

## 1. Reuse what exists before making anything

Before a new project, element, scene or recipe, look for the one already there:

- `projects`, then `project` with its id: the brief, look, scenes, references,
  renders and chat the person already has. A scene belongs in an existing
  project when one fits; `search` with a few words finds it.
- `elements`: the characters, props and places with their photo refs. A name
  already there gains a photo instead of becoming a second element.
- `library`: renders (`gen:<id>`) and uploads (`asset:<id>`), the ids the
  edits, the effects and `share_link` take.
- `recipes`, then `recipe`: the studio's shelf and the person's own, so a way
  of working they saved is used, not reinvented.
- `recent`: the latest projects, open scenes and renders, in one call.

## 2. A picture on every scene

A scene needs at least one element picture from the person. With none it is saved as a draft
and can be neither priced nor rendered. The refs you pass are photo refs
exactly as `elements` lists them, the anchor first (a face before a room); a
look-only photo (`roles` light, palette, framing, style) is never first. When
no element fits:

- a picture at a web address the PERSON gave you: `add_element` with `kind`,
  `name` and that address as `source`. It is the one tool that takes an
  address, and never one you found or guessed.
- a picture on their phone or computer: `upload_link` with `purpose` reference,
  `element_kind` and `element_name`; give them the `url`, wait for them to come
  back, then call `elements` again.

## 3. Quote before anything costs credits

Making media is the only thing that costs. For a scene, `quote` with the
`scene_id` before anyone decides: the keyframes, the clip per shot, the
balance, and `approve_url`, the scene's page in the studio. Say the price in
the quote's own words: never your own arithmetic, never a currency; credits
only. `recommend_model` and `video_models` help choose a model; `quote` with
`model` or `frame` prices that choice exactly.

## 4. Nothing spends without a yes; new media is made in the studio

`reformat`, `trim_clip` and `assemble_clips` spend nothing; they start jobs,
so poll `job` (`wait` holds up to 15 seconds). Three things cost:

- an effect on their own media (`edit_image`, `remove_background` and the
  rest, a `gen:<id>` or `asset:<id>` from `library`): the first call, with no
  `quote_token`, IS the quote. Show it, wait for an explicit yes in this chat
  (never on their behalf), then the SAME call plus its `quote_token`, once;
  `job` until done. A token works once, for one hour;
- a scene's keyframes or clip: `quote`'s `approve_url`, rendered in the studio;
- a new still or clip from a prompt: `open_in_studio` with the `prompt` you
  wrote together, `kind`, an `aspect` and a `project_id`; made in the studio.

`refused: insufficient_credits` or `affordable` false: stop, and say that
credits are added in the studio.

## 5. Nothing is overwritten

Every edit makes a new item: `reformat` and `trim_clip` make copies,
`assemble_clips` a new clip, `duplicate_scene` a fresh scene, `save_recipe` a
new version, `set_preferences` a new entry, an effect or a still a new item. The
one exception is `write_scene` with a `scene_id`: it replaces that scene's TEXT.
Show the person the whole new version and get a yes before calling it.

## Three smaller rules

- **Defaults.** `preferences` holds `aspect`, `seconds`, `video_model`,
  `image_model` and `draft_first`; they are read only where a call passes
  nothing. Change them with `set_preferences` only when the person asks.
- **Refusals** come back in plain words. Repeat them to the person and change
  something; never retry the identical call. "no scene N" or "no project N"
  means the id is not this person's: re-read `project` or `recent`.
- **Ids are never invented.** Every id, photo ref or quote token comes from a
  tool's reply in this conversation, never from memory or a guess.

## Worked example

"Make my coffee ad vertical and send me the file."

1. `recent` shows project 12 "Coffee" with render `gen:88` in 16:9.
2. `reformat` with `ref` `gen:88`, `aspect` 9:16, `fit` pad, `project_id` 12;
   `job` with `wait` 15 until it finishes; it returns `gen:91`, a new item.
3. `share_link` with `ref` `gen:91`: hand over the link and when it expires.

Nothing was rendered, nothing was spent, and `gen:88` is untouched.
