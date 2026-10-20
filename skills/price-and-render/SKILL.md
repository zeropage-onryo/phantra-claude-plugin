---
name: price-and-render
description: Prices a Phantra scene in credits and sends the person to the studio to render it, opens a still or an effect in the studio with its prompt ready, and reports where a scene stands. Nothing here makes or spends: `quote` gives the scene's studio page, `open_in_studio` a studio link. Use when someone says render it, draw it or how much will it cost, or asks whether a scene is done. NOT for writing the scene (write-scene), effects (effects) or credits in general (credits-and-limits).
---

# Price and render

Rendering costs credits, and on this connector it is approved **in the
studio**, where the price is shown again before anything is spent. Nothing in
the chat renders, draws or spends. What you do here:

| step | tool | what it costs |
|---|---|---|
| price a scene's keyframes and clip, get its studio page | `quote` | nothing |
| a still, a clip from a prompt, or an effect: a studio link | `open_in_studio` | nothing |
| see where a scene stands, and its clips | `scene` | nothing |
| follow a reshape, trim or join while it runs | `job` | nothing |

## A scene

1. The scene exists and is held to at least one photo. `write_scene` saved it
   and gave its id; a scene saved with no photos is a draft and cannot be
   priced (write-scene and look-matching add a photo first).
2. `quote` with the scene's id. The reply carries `keyframes` (stills still to
   draw, in credits), `clip` (one render per timed shot, each with its seconds
   and credits), the `balance`, `credits_needed`, `affordable`, `preference`
   when the workspace set a default renderer, and `approve_url`: the scene's
   page in the studio. Optional `provider`, `model`, `duration` (whole-scene
   only) and `frame` price a different renderer; the defaults are the studio's.
3. **Say the price, from the quote, never your own arithmetic**, and give the
   link: "2 keyframes for <their credits>, then 2 shots of 6s for <the clip's
   credits>; your balance is <balance>. Open the scene to render it:
   <approve_url>". A timed beat is fitted up to the model's shortest length,
   so say the quote's seconds, not the scene's.
4. The person approves on that page. The keyframes and the clip are two
   buttons there, each with its price; the clip starts on its shot's still
   when one was drawn. A model or frame other than the default: say which one
   was priced, so they pick the same there.
5. When they ask how it went, call `scene`: the status, the shots, the
   keyframe and the clips that have landed, with the studio link.

## A still, a clip from a prompt, or an effect (`open_in_studio`)

When the person asks for an image, a quick clip without a saved scene, or a
change to one of their renders, write the prompt with them in the chat first,
as you would for the studio. Then `open_in_studio` with:

- `prompt`: what to make, up to 4,000 characters;
- `kind`: `image` or `video`;
- `aspect`: an image 4:5, 1:1, 16:9 or 9:16; a video 9:16, 16:9, 1:1, 4:3, 3:4
  or 21:9 (omit for the studio's default);
- `project_id` (from `projects`) to open it inside that project;
- `source`: a render's `gen:<id>` from `library`, to edit or animate it (the
  studio opens its effects on that render).

It answers a `url`. Give it to the person: the studio opens with the prompt in
the box; they send it, see the price in credits and approve it there. Nothing
is made, written or spent here. A still made there lands in `library` as a
`gen:<id>`, which `add_element` takes as a `source`.

## What you can and cannot do

- You cannot approve, start or cancel a render, a still or an effect. "Go
  ahead" or "render it" gets the link (`approve_url` or `open_in_studio`'s
  `url`) and the words "it starts when you approve it in the studio".
- If `affordable` is false, say the numbers before giving the link and that
  credits are added in the studio. Never pass on a link to buy credits or
  change a plan, even when a refusal carries one.
- If `quote` is refused, report its own words:
  - the scene has no photos (a draft): add one with `add_element` or pick one
    from `elements`, then save the scene again with its `scene_id` and `refs`;
  - "no scene N": the id is not one this person can see. Re-read the project
    rather than retrying the id.
- If `open_in_studio` is refused (an empty prompt, an unknown frame, a
  `source` that is not their render), say why and fix that one argument.
- A quote is information, not a reservation: the studio confirms the price
  again at the moment of approval.

## Checking on work (`scene`)

`scene` reads one scene back in a short form: its status, its shots, the
keyframe and the clips so far, and its studio link. It is the status that
lasts: read it rather than assuming a render finished because time has passed.
Renders take a minute or more per shot. A still or an effect made from a link
shows up in `library` once it lands.

## What not to do

- Never say a render, a still or an effect has started; the person starts it
  in the studio. Say it finished only when `scene` or `library` shows it.
- Never print an image or clip address the tools did not return.
- Never promise a delivery time.
- Never name a plan or a price in general; the quote's own numbers, said to
  the person, are the only prices here.
