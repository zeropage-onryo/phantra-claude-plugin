---
name: credits-and-limits
description: Explain what is free and what costs credits in Zeropage Studio, read the balance off a quote, warn before anything expensive, and explain a refusal or the connector's rate limit (a 429). Use when someone asks how much something costs, what credits are, what their balance is, why a call was refused, why they got "rate limited", or whether an action will charge them. NOT for performing a render or an approval (render-and-status) and NOT for ideas or projects (projects-and-ideas).
---

# Credits and limits

## What is free

Almost every call is free. Reading never charges: `projects`, `project`,
`project_chat`, `elements`, `scene`, `quote`, `job`, `image_models`. Writing
never charges either: `create_project`, `add_element` (the picture is saved as
it is, nothing is drawn), `write_scene`. Writing the scene prompt happens in
this chat, so it costs the studio nothing.

On the Claude connector nothing spends at all: renders are approved in the
studio. Only the full connector has calls that spend: `approve` (a scene's
keyframes or clip) and `generate_image` (one still). Each is priced first and
runs only after the person's yes.

## What costs credits

- **Keyframes**: one still per shot of a scene.
- **The clip**: one render per shot, priced by the renderer, the model, the
  length and the resolution.

`quote` says how many of each and the credits. Each is approved only after the
price is shown and the person says yes (render-and-status). Credit is held
before anything is submitted and released if the render fails.

Credits are bought in the studio, under Settings → Plan & credits, where a new
workspace also gets a one-time trial grant. Prices are in credits in every
tool reply; repeat them as returned and do not convert them to money.

## The balance

`quote` returns `balance`, `credits_needed` and `affordable`. Report those
three plainly. `charged: false` means this account is not charged for renders.
Without a quote in this conversation, point the person to
https://zeropage.studio/studio/settings/plan rather than guessing.

## Warn before anything expensive

Before a render is approved, here or in the studio, say what it is and the
credits. Anything above a single still counts as expensive: a strip of
keyframes, any clip. If `affordable` is false, say so and offer the billing
page instead.

## Refusals you will see, and what they mean

- `out_of_credits` / "top up": the balance does not cover it. Nothing was
  charged. Offer the billing page.
- `missing_quote`, `expired`, `stale_content`, `wrong_render`: the price shown
  no longer matches (an hour passed, the scene changed, or the renderer choice
  differs). Quote again. Nothing was charged.
- `no_reference`, or "attach at least one of your element photos": the scene
  has no attached photos. Write it again with `refs` from `elements`.
  `nothing_to_draw`: the stills already exist.
- "no scene N" / "no project N" / "no job N": the id is not one this person
  can see. Read `projects` or `project` again rather than retrying the id.
- "no workspace yet": the person has not signed in at https://zeropage.studio.
  One web sign-in creates the workspace; then reconnect.
- `rate_limited` (HTTP 429): too many calls in one minute from this account.
  The response carries `Retry-After` in seconds. Wait that long, then continue;
  do not loop on it. The limit is generous for a conversation (over a hundred
  calls a minute) and is only reached by polling in a tight loop. Poll every
  20 to 30 seconds, not continuously.

## What is never done through this connector

Nothing is posted anywhere, nothing is deleted, and no payment method is
touched. Buying credits or changing a plan happens in the studio, never here.
