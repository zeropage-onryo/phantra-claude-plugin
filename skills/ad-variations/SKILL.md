---
name: ad-variations
description: Make A/B variants of a scene in Zero Page Studio without rewriting it from scratch -- `duplicate_scene` with a changed hook, a changed length, a different first shot, a different product photo or a different video model -- each a new scene in the same project, told apart by their ids in the chat, priced one by one, and read back later with `what_works` to see which was kept. Use when someone asks for versions, variants, an A/B test, "try it shorter", "same ad with the other photo" or "which model would be cheaper for this one". NOT for writing the first version (write-scene, ugc-ad, product-shots), NOT for pricing in general (price-and-hand-off), and NOT for setting a look (look-matching).
---

# Ad variations

A variant is a **new scene** copied from one that exists, with one thing
changed, filed in the same project. The source is never touched, its stills
and clips are never copied, and nothing is spent until the person approves a
render in the studio. Change ONE thing per variant, so what gets kept says
something.

## The order

1. Find the source: `recent`, `search` or `project` gives its `scene_id`;
   `scene` reads it in full (prompt, seconds, title, the timed shots) and gives
   only the COUNT of its photos; the refs themselves are what you passed, or
   `project`'s `references` list, each naming the scenes it is on. Read it first.
2. Agree the variable with the person: hook, length, first shot, product
   photo or model. Draft the change, show it, get a yes.
3. `duplicate_scene` with the `scene_id` and ONLY the fields that change;
   the rest is copied. The reply gives the new `scene_id` and `copied_from`.
4. Note which is which (below), then `quote` each variant, say each price
   from its own quote and give each `approve_url`. The person approves in the
   studio.
5. Later, `what_works` reads what was kept.

## The five changes

- **Hook** (`prompt`): rewrite the first window's line only -- the first
  sentence said, or the first image -- in the person's own words, and keep
  every other window, the style block, the sound and the avoid list as is.
- **Length** (`prompt` + `seconds`): re-time the windows so they still run
  contiguously from 0 to the new total, each 2-10 s; drop or shorten a shot
  rather than squeeze them all; `seconds` is the last window's end.
- **First shot** (`prompt`): swap the opening window for a different image
  (the product before the face, or the reverse); the rest stays timed.
- **Product photo** (`refs` + `roles`): a different pack shot from `elements`
  as the first ref with role `product` (or a different face as `subject`).
  The first ref anchors the render, so this changes the picture most. A ref
  `elements` did not list is refused.
- **Model**: a scene carries no model; it is picked where the person approves
  in the studio, so no copy is needed. `recommend_model` ranks models for the job in words; `quote`
  with `model` (and `frame`) prices the same scene on another one;
  `set_preferences` with `video_model` makes it the default wherever a call
  passes nothing, and `draft_first` true prices the cheaper draft frame where
  a model has one. `video_models` lists them with credits per frame.

## Telling variants apart

A copy is titled "<source title> (copy)" and cannot be renamed from here (a
`write_scene` rewrite replaces a scene's text, never its title), so keep a
short table in the chat as you go and say which `scene_id` is which:

| scene_id | variable | change | credits (from quote) |
|---|---|---|---|
| 412 | source | -- | 87 |
| 418 | hook | opens on "two weeks" | 87 |
| 419 | length | 15 s to 10 s | 61 |

## Worked example

Source 412 is a 15 s to-camera ad with three windows and the person wants a
shorter one. Re-time it: (0-4s) the open unchanged, (4-10s) the product shot
two seconds shorter with the closing line moved to its end, the third window
dropped. Then `duplicate_scene` with `scene_id` 412, the re-timed `prompt`
and `seconds` 10: it gives scene 419. `quote` 419, say its credits and the
balance from the reply, and give its `approve_url`.

## Reading the result

`what_works` says, per model and per preset, how many outputs were made and
kept (downloaded, cut, starred, used again), how many tries a keeper takes,
and what was posted with a scene behind it. When `enough_data` is false,
say so rather than read a winner into two renders. `scene` on each variant
shows which clips landed.

## Do not

- Never change two variables in one copy and call it a test.
- Never say a render started; the person approves each one in the studio.
- Never put a URL in `refs`; refs are exactly as `elements` lists them.
- Never rewrite the source with `write_scene` to make a variant; copy it.
