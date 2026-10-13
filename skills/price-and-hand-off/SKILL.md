---
name: price-and-hand-off
description: Price a Phantra scene and hand the person to the studio to approve its render, then report where the scene stands. Use when someone says render it, draw the stills, make the clip, how much will it cost, or asks whether a scene is done. This connector renders nothing: it quotes, gives the studio link, and reads the status back. NOT for writing the scene (write-scene), NOT for choosing ideas (ideas-and-projects), and NOT for explaining plans or balances in general (credits-and-limits).
---

# Price and hand off

Rendering a scene costs credits, and it is approved **in the studio**, on the
scene's own page, where the price is shown again. Nothing in this connector
renders, draws or spends. What you do here:

| step | tool | what it costs |
|---|---|---|
| price the keyframes and the clip | `quote` | nothing |
| see where a scene stands, and its clips | `scene` | nothing |

## The order

1. The scene exists and is held to at least one photo. `write_scene` saved it
   and gave its id; a scene saved with no photos is a draft and cannot be
   priced (see write-scene and look-matching to add a photo first).
2. `quote` with the scene's id. The reply carries `keyframes` (stills still
   to draw, in credits), `clip` (one render per timed shot, each with its
   seconds and credits), the `balance`, `credits_needed`, `affordable`, and
   `approve_url`: the scene's page in the studio. Optional `provider`,
   `model`, `duration` (whole-scene only) and `frame` price a different
   renderer; the defaults are the studio's.
3. **Say the price, from the quote, never your own arithmetic**, and give
   the link: "2 keyframes for 20 credits, then 2 shots of 5s for 87 credits;
   your balance is 500. Open the scene to render it: <approve_url>".
4. The person approves on that page. The keyframes and the clip are two
   separate buttons there, each with its price; the clip starts on its
   shot's still when one was drawn.
5. When they ask how it went, call `scene`: it returns the status, the shots
   and the clips that have landed, with the studio link.

## What you can and cannot do

- You cannot approve, start, cancel or follow a render from here. If the
  person says "go ahead" or "render it", give them `approve_url` and say that
  the render starts when they press it in the studio.
- If `affordable` is false, say so before giving the link, and point to the
  studio's Plan & credits page (https://phantra.ai/studio/settings/plan)
  instead of promising a render.
- If `quote` is refused, report its own words:
  - the scene has no photos (a draft): add one with `add_element` or pick one
    from `elements`, then save the scene again with its `scene_id` and `refs`;
  - "no scene N": the id is not one this person can see. Re-read the project
    rather than retrying the id.
- A quote is information, not a reservation. The price is confirmed again in
  the studio at the moment of approval.

## Checking on work (`scene`)

`scene` reads one scene back in a short form: its status, its shots, the
clips so far and its studio link. It is the status that lasts: read it rather
than assuming a render finished because time has passed. Renders take a
minute or more per shot.

## What not to do

- Never say a render has started unless `scene` shows it.
- Never pass or print an image URL other than the studio links the tools
  return.
- Never promise a delivery time.
