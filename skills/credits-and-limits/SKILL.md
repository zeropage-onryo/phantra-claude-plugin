---
name: credits-and-limits
description: Explains what costs credits and what does not in Phantra, reads the balance and where credits went, explains where spending is approved (the studio), sets up draft-first rendering, and explains a refusal or a rate limit (429). Use when someone asks what something costs, what credits are, what their balance is, how to render cheaper, or why a call was refused. NOT for pricing and rendering one scene (price-and-render) or choosing ideas (ideas-and-projects).
---

# Credits and limits

## What spends nothing

**Every read and every write spends nothing.** Reads: `projects`, `project`, `elements`,
`scene`, `quote`, `video_models`, `library`, `balance`, `credit_history`,
`recommend_model`, `what_works`, `job`...; writes: `create_project`, `add_element`,
`upload_link`, `write_scene`, `duplicate_scene`, `set_preferences`, `save_recipe`,
`open_in_studio`. The
edits -- `reformat`, `trim_clip`, `assemble_clips` -- run on the studio's own server
and spend nothing: each starts a job you follow with `job` (`wait` holds up to 15 seconds)
and makes a NEW item in the library, the source untouched. Writing the prompt happens in
this chat. Nothing in this connector spends credits: making media is approved in the studio.

## What costs credits (approved in the studio)

- **A still**: drawn in the studio from the prompt `open_in_studio` puts in its box; the
  studio shows the model's credits and the person approves them there.
- **An effect** (an edit, a cut-out, a template, a camera move, an upscale, sound, a new
  shape): `open_in_studio` with the render as `source` opens the studio's effects on it,
  each with its price (effects).
- **Keyframes**: one still per shot. `quote` says how many are still to draw and the
  credits for `each`.
- **The clip**: one render per shot still without a clip, priced by model, length and
  frame. `quote` lists `clip.renders` (part, seconds, credits) and the total.

Keyframes and the clip are approved on the scene's page in the studio, `quote`'s
`approve_url`, where the price is shown again. Credit is held when a render starts and
released if it fails; `scene` and `library` show what landed. Credits are added in the
studio, never here. Prices are in credits in every tool reply; repeat them as returned and
never convert to money.

## The balance, and where credits went

- `balance`: what is available, what is held by renders in flight, the plan, and each
  credit lot with what is left and when it expires. Call it when the person asks what they
  have; never guess from an old quote.
- `credit_history`: every hold, charge, return, grant and expiry, newest first, each with
  what it was for and the balance it left. Pass the reply's `next` as `before` to page
  back. This answers "what did that cost me".
- `quote` also returns `balance`, `credits_needed` and `affordable` for one scene; report
  those three plainly beside the price (price-and-render).

## Draft first: a cheaper frame to check a take

Some models have a cheaper **draft frame**; `video_models` shows it where a model
has one. Drafting pays when not every take is kept:

1. `recommend_model` with `draft` true ranks models with a draft frame first (the rest
   still appear), each with its reason and its credits at the model's default frame -- not
   the draft price; `quote` prices the draft exactly.
2. `set_preferences` with `video_model` set to one of those models and `draft_first` true
   makes `quote` (called with no renderer choice) price the draft frame and say so in
   `preference`; a value the catalogue lacks is refused.
3. Show the draft price and give `approve_url`; the person renders the draft in the
   studio. A take they like is **finished (upscaled) in the studio**, not here.

## Say the cost, then hand over the link

Before the person goes to make anything, say what it would cost from the quote, in
credits beside the balance, then give the studio link. Never say something was made or
charged until `scene`, `library` or `credit_history` shows it. If `affordable` is false,
say so first and that credits are added in the studio.

## Refusals you will see (repeat them in their own words; never retry the same call)

- `insufficient_credits` (`needs`, `available`): stop; nothing was charged. Say `needs`
  against `available` and that credits are added in the studio; pass on no link.
- `open_in_studio` refused: an empty prompt, a frame not on its list, or a `source`
  that is not one of their renders in `library`. Fix that one argument.
- `needs_reference` on a saved scene: it has no photos, so it waits as a draft scene. Add
  one (`add_element`, `upload_link`, or a ref from `elements`) and save it again with its
  `scene_id`. It cannot be priced.
- A photo ref that is refused: it was not one `elements` listed for this person. Read
  `elements` again and use a ref exactly as listed.
- `add_element` refused: the address was not https, neither an image file nor a product
  page, or too large. Say which; ask for the picture itself (or give an `upload_link`).
- `set_preferences` or an edit refused: the value is not in the live catalogue
  (`preferences` lists the choices), the range lay outside the clip, the clips' shapes
  differ (`letterbox` on `assemble_clips`), or the id was not one `library` listed.
- "no scene N" / "no project N": the id is not one this person can see. Re-read `projects`
  or the project rather than retrying the id.
- "no workspace yet": the person has not signed in at https://phantra.ai. One web
  sign-in creates the workspace; then reconnect.
- `rate_limited` (HTTP 429): too many calls in one minute from this account. The response
  carries `Retry-After` in seconds. Wait that long, then continue; do not loop on it. The
  limit is generous (over a hundred calls a minute) and only a tight loop reaches it: read
  `scene` or `job` on request.

## What is never charged or changed through this connector

Nothing is posted or removed, no payment method is touched, and nothing is rendered,
drawn or charged from the chat: making is approved in the studio. Every edit makes a new item; rewriting
a scene with `write_scene` replaces the text it had, so show the new version and get a yes
first. Buying credits and changing a plan happen in the studio, never here.
