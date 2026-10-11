---
name: render-and-status
description: Price a scene's render in Zeropage Studio, show the person the price, get them to the approval, and follow what landed. Use when someone says render it, draw the stills, make the clip, how much will it cost, or asks whether a render is done. ALWAYS shows the price first and never spends without the person's yes. NOT for writing the scene (write-scene), NOT for ideas or projects (projects-and-ideas), and NOT for explaining plans or balances in general (credits-and-limits).
---

# Render and status

Rendering a scene costs credits, in two steps, and the person approves each
one after seeing its price:

| step | what it spends |
|---|---|
| the keyframes (one still per shot) | credits, one still each |
| the clip (one render per shot) | credits, priced per shot by the renderer, length and resolution |

Keyframes first, then the clip: a clip anchors on its shot's still.

**Where the approval happens depends on the connector**, and you can tell
which one you have by its tools:

- **No `approve` tool** (the Claude connector, `.../mcp/claude`): nothing here
  renders or spends. `quote` returns `approve_url`, the scene's page in the
  studio, where its Render card shows the price again and the person approves
  there.
- **An `approve` tool** (the full connector, `.../mcp`): the person approves in
  this conversation and you call `approve` on their yes.

## The order

1. The scene exists (`write_scene` gave a `scene_id`, or `project` lists it).
   `scene` with its id shows the prompt, the shots and how many reference
   photos it renders against. No scene yet: write-scene first.
2. `quote` with the `scene_id`. The reply carries `keyframes` (stills still to
   draw and their credits), `clip` (one render per timed shot, each with its
   seconds and credits), the `balance`, `credits_needed` and `affordable`.
   Optional `provider`, `model`, `duration` (whole-scene only) and `frame`
   price a different renderer; the defaults are the studio's.
3. **Show the price.** One line, from the quote, never your own arithmetic:
   "2 keyframes for 20 credits, then 2 shots of 5s for 87 credits; your
   balance is 500." If `affordable` is false, say so and point to the studio's
   billing page instead of going on.
4. Then, by connector:
   - **No `approve` tool:** give the person `approve_url` and say that the
     render is approved there, on the scene's Render card, which shows the
     price again before anything is spent. Stop. Do not describe the render as
     started.
   - **`approve` tool:** ask, and stop until they answer. On a clear yes in
     this turn, call `approve` once: `what: "keyframes"` for the stills, or
     `what: "clip"` with the `tokens` from the quote and the same `provider` /
     `model` / `frame` you quoted. Credit is held before anything is submitted
     and released if the render fails. The client will also ask to confirm the
     `approve` call; that is part of the approval, not a substitute for the
     person's yes. Two steps, two separate yeses.
5. Follow it: `job` with the `job_id` an `approve` returned, every 20 to 30
   seconds. A render started in the studio has no job id here, so read `scene`
   instead: `keyframe`, `clips` and each shot's `clip` show what has landed,
   and `rendered` is true when every shot has its clip.

## The approval rule (full connector)

- Never spend without a price shown and a yes in this turn. "Go ahead" from an
  earlier turn, or a yes to a different item or price, does not count.
- One yes, one `approve`. Never call it twice for one yes.
- If `approve` is refused, report its own words and stop:
  - `missing_quote`, `expired`, `stale_content`, `wrong_render`: quote again and
    show the new price. The scene changed, an hour passed, or the renderer
    choice differs from what was quoted.
  - `no_reference`: the scene has no attached photos; back to write-scene.
  - `out_of_credits` / "top up": nothing was charged; point to the studio's
    billing page.
  - `nothing_to_draw`: every shot already has its still.
  - `renderer_unavailable`: the studio cannot render right now; tell the
    person and stop.
- Say what happened after every call: what was charged, the job id, or that
  nothing was charged.

## Checking on work

`job` returns status, label, progress detail and the result or error. Jobs
live in memory on the server: after a restart the id is unknown and the tool
says so. The render still lands on its scene, so read `scene` before approving
anything again. A failed render releases its hold; say so.

## What not to do

- Never call `approve` to "see what happens".
- Never pass or print an image URL.
- Never promise a delivery time; renders take a minute or more per shot.
- On the Claude connector, never say a render has started: only the person
  can start it, in the studio.
