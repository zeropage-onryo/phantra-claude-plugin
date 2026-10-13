---
name: write-scene
description: Write the scene prompt for an idea the person chose, in the shape Phantra renders from, and save it with the `write_scene` tool against their own photos. Use when someone asks to write the scene, the prompt, the shots or the script, says "make the scene" after choosing an idea, or wants a saved scene changed. NOT for choosing between ideas (ideas-and-projects), NOT for pricing or rendering (price-and-hand-off), and NOT for choosing photos or a look (look-matching).
---

# Write the scene

A scene in Phantra is ONE paste-ready prompt a video model reads top
to bottom. The studio renders it one timed shot at a time, against the
photographs the person uploaded as elements. You write the prompt in the chat
(no model credit is spent for that), then save it with `write_scene`.

## Before writing

1. Have the idea in one or two sentences: what we see, and why it holds. It
   comes from this conversation (ideas-and-projects) or from the person. When
   the scene belongs to a project, `project` with its id gives the brief and
   the look the scene must keep to.
2. `elements`: the person's characters, props and places with their photo
   refs. Decide which photos the scene needs. If the scene needs a face, a
   product or a room and no element has a photo of it, ask the person for one:
   a picture they give you can be added with `add_element` (look-matching),
   or they can upload it in the studio (Elements). A scene is never rendered
   from a name, and not at all until it is held to at least one photo.
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

- `prompt`: the full scene, all five parts.
- `seconds`: its total length.
- `refs`: the photo refs from `elements` (or from an `add_element` reply),
  exactly as listed, **the most important one first**. The first ref is what
  the render anchors on: the face before the room.
- `title`: a few words to call it.
- `project_id`: when it belongs to a project (from `projects`).

The reply gives the scene's id, how many shots were written, and its link in
the studio. Nothing is spent.

**A scene with no photos is saved as a draft.** The reply says so
(`needs_reference`) and what to do next. A draft cannot be priced or
rendered: add a photo (`add_element`, or one already in `elements`) and call
`write_scene` again with the draft's `scene_id` and the `refs`.

**To change a scene**, call `write_scene` with its `scene_id` and the whole
new prompt. This replaces the text the scene had, so show the person the new
version and get their yes first. A ref `elements` did not list is refused.

## Then

Hand over to price-and-hand-off: `quote` the scene, say the price, and give
the person the studio link where they approve the render. Nothing renders
from this connector.

## Do not

- Never invent a photo ref, and never pass a URL.
- Never leave a `{placeholder}` in the prompt; the tool refuses it.
- Never write a window longer than 10 seconds or shorter than 2.
- Never describe the look by naming a film, a brand or a person.
