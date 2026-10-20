---
name: credits-and-limits
description: Explains what costs credits and what does not in Phantra, reads the balance and where credits went, walks the quote, yes, spend flow of an effect, sets up draft-first rendering, and explains a refusal or a rate limit (429). Use when someone asks what something costs, what credits are, what their balance is, how to render cheaper, or why a call was refused. NOT for pricing and rendering one scene (price-and-render) or choosing ideas (ideas-and-projects).
---

# Credits and limits

## What spends nothing

**Every read and every write spends nothing.** Reads: `projects`, `project`, `elements`,
`scene`, `quote`, `video_models`, `library`, `balance`, `credit_history`,
`recommend_model`, `what_works`, `job`...; writes: `create_project`, `add_element`,
`upload_link`, `write_scene`, `duplicate_scene`, `set_preferences`, `save_recipe`,
`open_in_studio`. The edits -- `reformat`, `trim_clip`, `assemble_clips` -- run on the
studio's own server and spend nothing: each starts a job you follow with `job` (`wait`
holds up to 15 seconds) and makes a NEW item, the source untouched. Only an effect on
the person's own media spends here, quoted first; new media from a prompt and scene
renders are approved in the studio.

## What costs credits

- **A still**: drawn in the studio from the prompt `open_in_studio` puts in its box; the
  studio shows the model's credits and the person approves them there.
- **An effect on media they provide** (`edit_image`, `remove_background`,
  `animate_still`, `camera_move`, `upscale_clip`, `add_sound`, `reframe_clip`, on one of
  their own images or clips by id from `library`): the call WITHOUT `quote_token` runs
  nothing and answers the quote; on their yes, the SAME call WITH that token starts the
  job (effects). This is the one spend that happens in the chat.
- **Keyframes and the clip**: one still per shot, one render per shot without a clip.
  `quote` gives `each` still's credits and `clip.renders` (part, seconds, credits).

Keyframes and the clip are approved on the scene's page in the studio, `quote`'s
`approve_url`, where the price is shown again. Credit is held when a render starts and
released if it fails; `scene` and `library` show what landed. Credits are added in the
studio, never here. Prices are in credits in every tool reply; repeat them as returned and
never convert to money.

## The balance, and where credits went

- `balance`: what is available, what is held by renders in flight, the plan, and each
  credit lot with what is left and when it expires. Call it when the person asks what they
  have; never guess from an old quote.
- `credit_history`: every hold, charge, return, grant and expiry, newest first, with what
  it was for; pass `next` as `before` to page back. It answers "what did that cost me".
- `quote` also returns `balance`, `credits_needed` and `affordable`; say them beside the price.

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
   studio. A take they like is finished with `upscale_clip` on its `gen:<id>` (effects).

## Say the cost, then wait (an effect) or hand over the link (the studio)

Say what it would cost from the quote, in credits beside the balance. For an effect,
WAIT for an explicit yes in this chat before the call with the token: never on the
person's behalf, never twice. For a scene or new media, give the studio link. Never say
something was charged until `job`, `scene` or `credit_history` shows it.

## Refusals you will see (repeat them in their own words; never retry the same call)

- `insufficient_credits` (`needs`, `available`): stop; nothing was charged. Say `needs`
  against `available` and that credits are added in the studio; pass on no link.
- `already_used` on an effect's token: the first call started the job; poll `job`.
  Nothing new was charged; a changed request needs a new quote and a new yes.
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

Nothing is posted or removed, no payment method is touched, and nothing is charged
without a quote shown and a yes. Every edit and effect makes a new item; rewriting
a scene with `write_scene` replaces the text it had, so show the new version and get a yes
first. Buying credits and changing a plan happen in the studio, never here.
