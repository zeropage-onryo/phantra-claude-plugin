---
name: credits-and-limits
description: Explains what is free and what costs credits in Phantra, reads the balance and where credits went, sets up draft-first rendering, and explains a refusal or the connector's rate limit (429). Use when someone asks what something costs, what credits are, what their balance is, how to render cheaper, why a call was refused, or whether an action will charge them. NOT for pricing one scene and handing it to the studio (price-and-hand-off) or choosing ideas (ideas-and-projects).
---

# Credits and limits

## What is free

**Everything this connector does is free.** Every read spends nothing
(`projects`, `project`, `elements`, `scene`, `quote`, `library`, `balance`,
`credit_history`, `video_models`, `recommend_model`, `what_works`, `job`...),
and every write spends nothing either (`create_project`, `add_element`,
`upload_link`, `write_scene`, `duplicate_scene`, `set_preferences`,
`save_recipe`). The free edits -- `reformat`, `trim_clip`, `assemble_clips` --
run on the studio's own server and spend nothing: each starts a job you follow
with `job` (`wait` holds up to 15 seconds) and makes a NEW item in the
library, the source untouched. Writing the prompt happens in this chat.

## What costs credits

Only what the person approves **in the studio**:

- **Keyframes**: one still per shot of a scene. `quote` says how many are
  still to draw and the credits.
- **The clip**: one render per shot, priced by the model, the length and the
  frame (resolution). `quote` says each render's credits and the total.

Neither can be started from this connector. `quote` returns `approve_url`,
the scene's page in the studio, where each has its own button with the price
on it (price-and-hand-off). Credit is held when the person presses it and
released if the render fails.

Credits are bought in the studio under Settings → Plan & credits. A new
workspace gets a one-time trial grant. Prices are in credits in every tool
reply; repeat them as returned and never convert to money.

## The balance, and where credits went

- `balance`: what is available, what is held by renders in flight, the plan,
  and each credit lot with what is left and when it expires. Call it when
  the person asks what they have; never guess from an old quote.
- `credit_history`: every hold, charge, return, grant and expiry, newest
  first, each with what it was for and the balance it left. Pass the reply's
  `next` as `before` to page back. This answers "what did that cost me".
- `quote` also returns `balance`, `credits_needed` and `affordable` for one
  scene; report those three plainly beside the price (price-and-hand-off).

## Draft first: a cheaper frame to check a take

Some models have a cheaper **draft frame**; `video_models` shows it where a
model has one. Drafting pays when not every take is kept:

1. `recommend_model` with `draft` true ranks models with a draft frame first
   (the rest still appear), each with its reason and its credits at the model's
   default frame -- not the draft price; `quote` prices the draft exactly.
2. `set_preferences` with `video_model` set to one of those models and
   `draft_first` true makes `quote` (called with no renderer choice) price the
   draft frame and say so in `preference`; a value the catalogue lacks is refused.
3. The person approves the draft on the scene's page as usual. A take they
   like is **finished (upscaled) in the studio**, not here.

## Say the cost before the link

Before giving the studio link for a render, say what it would cost from the
quote: the keyframes and the clip, in credits, beside the balance. If
`affordable` is false, say so first and point to the Plan & credits page
rather than to the render.

## Refusals you will see (repeat them in their own words; never retry the same call)

- `needs_reference` on a saved scene: it has no photos, so it waits as a
  draft scene. Add one (`add_element`, `upload_link`, or a ref from
  `elements`) and save it again with its `scene_id`. It cannot be priced.
- A photo ref that is refused: it was not one `elements` listed for this
  person. Read `elements` again and use a ref exactly as listed.
- `add_element` refused: the address was not https, was neither an image
  file nor a product page, or the file was too large. Say which, and ask for
  the picture itself (or give an `upload_link`).
- `set_preferences` or a free edit refused: the value is not in the live
  catalogue (`preferences` lists the choices), the range lay outside the
  clip, the clips' shapes differ (`letterbox` on `assemble_clips`), or the
  id was not one `library` listed.
- "no scene N" / "no project N": the id is not one this person can see.
  Re-read `projects` or the project rather than retrying the id.
- "no workspace yet": the person has not signed in at https://phantra.ai.
  One web sign-in creates the workspace; then reconnect.
- `rate_limited` (HTTP 429): too many calls in one minute from this account.
  The response carries `Retry-After` in seconds. Wait that long, then
  continue; do not loop on it. The limit is generous (over a hundred calls a
  minute) and only a tight loop reaches it: read `scene` or `job` on request.

## What is never charged or changed through this connector

Nothing is rendered, posted or removed, and no payment method is touched.
Every edit makes a new item; rewriting a scene with `write_scene` replaces the
text it had, so show the new version and get a yes first. Buying credits,
changing a plan and approving a render all happen in the studio, never here.
