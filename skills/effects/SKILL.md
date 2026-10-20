---
name: effects
description: Changes something already in the person's Phantra library with a studio effect (an edit by instruction, a cut-out, a template, a camera move, an upscale, sound, a new shape): writes the instruction and opens the studio's effects on that render with `open_in_studio`. Use when someone asks to edit, animate, cut out, upscale, reshape or add sound to something made. NOT for a new still (thumbnails), trims and joins (edit-and-deliver) or a scene's sound line (sound-plan).
---

# Effects

An effect takes something that already exists in the person's library and
makes a NEW item from it; the source is never changed. Effects spend credits
and run in the studio: here you settle what to do, write the instruction, and
hand over a link that opens the studio's effects on that render, where the
person sees the price and approves it. Nothing is made or spent in the chat.

## 1. Is there a way with no credits first?

A new shape by padding or cropping is `reformat`; a shorter clip or clips
joined is `trim_clip` or `assemble_clips`. These run here and spend no
credits. Use an effect when the picture itself has to change, and say so when
a trim, reshape or join would do.

## 2. What the studio's effects do

| they want | the effect | what to settle first |
|---|---|---|
| a change to an image by instruction | an image edit | the change in one sentence, and what must stay the same |
| the subject cut out | background removal | a person or an object; for a clip, see-through or a flat colour |
| a still turned into a short animated clip | an animated template | which template; the studio's gallery shows them |
| a still turned into a clip with a camera move | a camera move | the move (camera-moves) and what happens in the shot |
| a clip sharper or smoother | an upscale | sharper, smoother (a higher frame rate) or both |
| sound for a clip | added sound | what it should sound like, in a line |
| a clip in a new shape, the new area generated | a reframe | the shape, and what belongs in the new area |

Never name a template, a move or an option from memory as if it were on the
menu; the studio's effects gallery lists the legal choices for that render.
Say that a generated area or added sound is generated, not filmed.

## 3. What it acts on

The source is a render in their library: a `gen:<id>` from `library` (a
still, a rendered clip, an earlier effect's result). A file they uploaded
(`asset:<id>`) or a picture not in the library yet comes in through
`upload_link`; once it is made into a still or a clip in the studio it has a
`gen:<id>`. A web address or a photo that is only an element is not a source.

## 4. Write it, then open it in the studio

1. Settle the effect and its instruction in the chat (section 2). Keep the
   instruction short and concrete: what changes, what stays.
2. `open_in_studio` with:
   - `source`: the render's `gen:<id>`;
   - `prompt`: the instruction, as the studio's box should hold it;
   - `kind`: `image` for an edit of a still, `video` for a clip or for
     turning a still into one;
   - `aspect` when the shape matters (9:16, 16:9, 1:1, 4:3, 3:4, 21:9);
   - `project_id` when the work belongs to a project.
3. Give the person the `url`: "This opens the studio on that render with the
   instruction ready; you pick the effect there, see its price in credits and
   approve it." Nothing has run yet, and nothing is spent until they approve.
4. When they come back, `library` lists the result as a new `gen:<id>`.

If `open_in_studio` is refused (a `source` that is not their render, an
unknown frame, an empty prompt), say why and fix that one argument.

## 5. Chains

A result is an ordinary library item, so it can be the next source: a still
given a camera move, that clip given sound, that clip upscaled. Each link is
its own trip to the studio and its own approval there. Say the whole chain
before starting, give one link at a time, and stop after any step they do not
like.

## The rules

- Never say an effect has run or what it cost; the studio shows the price
  and the person approves it there. Say it is done only when `library` shows
  the new item.
- Never state a price yourself, and never promise how a result will look.
- A person's face is edited only at their own request, on their own photo.
  Never use an edit to put someone where they were not, to change what a
  product is, or to remove a mark that is not theirs.
