---
name: write-scene
description: Write a scene prompt in the shape Zeropage Studio renders from, and save it as a scene with the `write_scene` tool against the photos the person uploaded, in a project or on its own. Use when someone asks to write the scene, the prompt, the shots or the script for an idea, says "make the scene" after choosing one, or wants to change a scene they saved. NOT for coming up with ideas or opening projects (projects-and-ideas), NOT for pricing or rendering (render-and-status), and NOT for finding references (look-matching).
---

# Write the scene

A scene in Zeropage Studio is ONE paste-ready prompt a video model reads top
to bottom. The studio renders it one timed shot at a time, against the
photographs the person uploaded as elements. You write the prompt in the chat
(no model credit is spent for that), then save it with `write_scene`.

## Before writing

1. The chosen idea is in this conversation (projects-and-ideas). If the scene
   belongs to a project, `project` with its id gives the brief and look the
   scene must follow. To change a scene saved before, `scene` with its id
   gives the prompt as it stands.
2. `elements`: the person's characters, props and places with their photo
   refs. Decide which photos the scene needs. If the scene needs a face, a
   product or a room and no element has a photo of it, ask the person for one:
   an image file they give you as an https address goes in with `add_element`
   (`kind`, `name`, a few words of `notes`, and the address as `source`; never
   an address you guessed, and the image itself, not the page it is on), or
   they upload it in the studio (Elements). The studio does not render a scene
   with no attached photos, and never from a name.
3. Settle the length in seconds (4 to 30; 10 is the default) and whether the
   idea wants cuts or one continuous take. Default to cuts: two or more shots.
   One continuous shot only when the person asked for one.

## The shape (five parts, in this order)

Write every look in cinematography and colour-grade terms. Never name a film,
a director, a brand or a real person.

1. **Opening line.** "Ultra-realistic grounded [tone] video in 9:16," then say
   which attached photo is the EXACT face, the EXACT outfit, the EXACT product
   or the EXACT place ("the attached photo of Sam is his exact face and
   clothing"). Name the photos; do not re-describe what they show. With no
   photos for a character, describe the person plainly.
2. **Style.** The look in two or three sentences: palette, light (source,
   direction, colour, hardness), lens and framing height, depth of field,
   finish and grade. Realism comes from practical light, believable physics
   and bodies, and restraint. Do not reach for "raw handheld, matte, muted"
   by habit.
3. **Beats, as timed shots.** Each shot opens with its window, written like
   `(0-4s)`. Windows start at 0s, are contiguous, never overlap, and end at the
   total length. Each window is rendered as its own clip by a model that sees
   only that window, so **each window is ONE shot**: one camera setup, one
   clear action that fits its length, 2 to 10 seconds. Cuts and location
   changes happen between windows, never inside one; say them ("hard cut to",
   "reverse on"). Open on an arresting image, turn or reveal, and end abruptly.
   Reactions are serious and physically believable, never cartoon. Use as many
   shots as the idea needs, not a habitual three.
4. **Sound.** Begin "No background music." then only the diegetic sound: what
   you would hear in that scene, nothing else.
5. **Avoid.** "Avoid: plastic AI sheen, CGI-looking skin or fabric, cartoon
   reactions, dramatic slow motion, named films, brands or actors."

A worked skeleton (replace everything in it):

```
Ultra-realistic grounded deadpan comedy in 9:16. The attached photo of Sam is
his exact face and clothing. Style: soft daylight from one window, true-to-life
colour with gentle contrast, a 35mm frame at chest height, shallow depth when
close, practical light only, a real lived-in kitchen.
(0-4s) Sam lifts the lid of a dented biscuit tin and freezes, both hands still
on it.
(4-10s) Hard cut to the hallway: Sam backs away from the open front door, the
tin held against his chest, and the door swings wider on its own. End abruptly.
No background music. Only diegetic sound: the tin lid's scrape, a floorboard,
the door's hinge.
Avoid: plastic AI sheen, CGI-looking skin or fabric, cartoon reactions,
dramatic slow motion, named films, brands or actors.
```

## Save it

Show the prompt to the person first and take their edits. Then call
`write_scene` with:

- `prompt`, `seconds`, and a short `title` (a few words);
- `refs`: the photo refs from `elements`, exactly as listed, **the most
  important one first** (the first ref is what the render anchors on: the face
  before the room). It refuses any ref `elements` did not list. A scene with
  no refs is saved only as a DRAFT: it cannot be priced or rendered until you
  call `write_scene` again with its `scene_id` and at least one ref;
- `project_id` when the scene belongs to a project;
- `scene_id` only to REWRITE a scene saved before. Without it a new scene is
  made. A rewrite replaces the scene's prompt; any stills or clips it had stay
  in the studio's Library but are no longer the scene's, and the reply says so.
  Say that to the person before rewriting a scene that has renders.

The reply carries the `scene_id`, how many shots were written, the seconds and
`studio_url`, the scene's page in the studio. Nothing is spent.

## Then

Hand over to render-and-status: `quote` the scene, show the price, and go on
only on the person's yes.

## Do not

- Never invent a photo ref, and never pass a URL.
- Never leave a `{placeholder}` in the prompt; the tool refuses it.
- Never write a window longer than 10 seconds or shorter than 2.
- Never describe the look by naming a film, a brand or a person.
