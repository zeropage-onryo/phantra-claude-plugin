---
name: credits-and-limits
description: Explain what is free and what costs credits in Zero Page Studio, read the balance off a quote, and explain a refusal or the connector's rate limit (a 429). Use when someone asks how much something costs, what credits are, what their balance is, why a call was refused, why they got "rate limited", or whether an action will charge them. NOT for pricing a particular scene and handing it to the studio (price-and-hand-off) and NOT for choosing ideas (ideas-and-projects).
---

# Credits and limits

## What is free

**Everything this connector does is free.** Reading never charges:
`projects`, `project`, `project_chat`, `elements`, `scene`, `quote`. Writing
never charges either: `create_project`, `add_element`, `write_scene`. Writing
the scene prompt happens in this chat, so it costs the studio nothing.

## What costs credits

Only what the person approves **in the studio**:

- **Keyframes**: one still per shot of a scene. `quote` says how many are
  still to draw and the credits.
- **The clip**: one render per shot, priced by the renderer, the model, the
  length and the resolution. `quote` says each render's credits and the total.

Neither can be started from this connector. `quote` returns `approve_url`,
the scene's page in the studio, where each has its own button with the price
on it (price-and-hand-off). Credit is held when the person presses it and
released if the render fails.

Credits are bought in the studio under Settings → Plan & credits. A new
workspace gets a one-time trial grant. Prices are in credits in every
tool reply; repeat them as returned and do not convert to money.

## The balance

`quote` returns `balance`, `credits_needed` and `affordable`. Report those
three plainly. Without a quote in this conversation, point the person to
https://zeropage.studio/studio/settings/plan rather than guessing.

## Say the cost before the link

Before giving the studio link for a render, say what it would cost from the
quote: the keyframes and the clip, in credits, beside the balance. If
`affordable` is false, say so first and point to the Plan & credits page rather than
to the render.

## Refusals you will see, and what they mean

- `needs_reference` on a saved scene: it has no photos, so it is a draft.
  Add one (`add_element`, or a ref from `elements`) and save it again with
  its `scene_id`. A draft cannot be priced.
- A photo ref that is refused: it was not one `elements` listed for this
  person. Read `elements` again and use a ref exactly as listed.
- `add_element` refused: the address was a page rather than an image file,
  was not https, or the file was too large. Say which, and ask for the image
  itself.
- "no scene N" / "no project N": the id is not one this person can see.
  Re-read `projects` or the project rather than retrying the id.
- "no workspace yet": the person has not signed in at https://zeropage.studio.
  One web sign-in creates the workspace; then reconnect.
- `rate_limited` (HTTP 429): too many calls in one minute from this account.
  The response carries `Retry-After` in seconds. Wait that long, then
  continue; do not loop on it. The limit is generous for a conversation (over
  a hundred calls a minute) and is only reached by calling in a tight loop.
  Read `scene` when the person asks, not continuously.

## What is never charged or changed through this connector

Nothing is rendered, nothing is posted anywhere, nothing is removed, and no
payment method is touched. Rewriting a scene replaces the text it had before.
Buying credits, changing a plan and approving a render all happen in the
studio, never here.
