---
name: storyboard
description: Plan a piece as a sequence of scenes in Zero Page Studio before any scene is written: a beat list agreed in the chat, then one `write_scene` per scene (timed shots inside each), all filed in one project and held to the same photos with the same roles so the scenes cut together. Use when someone wants a whole ad, short or sequence planned, asks for a storyboard or a beat sheet, has several places or moments in one idea, or wants alternates of a scene. NOT for writing one scene's prompt (write-scene), NOT for pricing or rendering (price-and-hand-off), and NOT for choosing between ideas before the piece is settled (ideas-and-projects).
---

# Storyboard

A piece in Zero Page Studio is a project holding several scenes. A scene is ONE
prompt of 4 to 30 seconds, rendered one timed shot at a time; separate scenes
are rendered separately and joined afterwards in the library. The storyboard
is the beat list that decides how many scenes there are, what each shows, and
which photos hold them together. Nothing here renders or spends.

## Several scenes, or more shots in one?

More shots in ONE scene when the beats share one look, one cast of photos and
one continuous memory (the scene's own continuity rides into each shot), and
the whole runs 30 seconds or less. One scene is one price and one approval in
the studio. Cuts and a change of place CAN happen between windows.

SEPARATE scenes when:
- the piece runs past 30 seconds;
- a part needs different photos (the person alone, then the product alone);
- the look changes (a daylight kitchen, then a night street);
- a part should be re-written or re-rendered without touching the rest;
- the person wants alternates of one part to choose between.

Rule of thumb: a scene is one block the camera could cover in one visit.

## Steps

1. `project` with its id for the brief and the look, or `create_project`
   (`title`, `brief`, `look`) when the piece has no project yet. Settle the
   look once, in cinematography terms; every scene keeps it word for word.
2. `elements`: list the photos. Decide the cast for the WHOLE piece: which
   refs, in which order, with which `roles` (subject, product, place; light,
   palette, framing, style for a look-only photo). The first ref is the anchor
   and should be the same photo in every scene where that subject appears. If
   a face, product or place has no photo, ask for one (look-matching).
3. Write the beat list in the chat and get a yes:

   ```
   Piece: 24s product short, 9:16. Look: one window, soft daylight, 35mm.
   1. Kitchen, 8s, 2 shots -- Sam finds the tin. Refs: Sam, the tin, kitchen.
   2. Hallway, 10s, 3 shots -- the door opens on its own. Refs: Sam, the tin.
   3. Doorstep, 6s, 1 shot -- the tin alone on the step. Refs: the tin, house.
   ```
   One line per scene: place, seconds, how many shots, what happens, refs.
4. Write scene 1 in write-scene's five-part shape and save it with
   `write_scene`: `prompt`, `seconds`, `refs`, `roles`, `title` ("1 of 3 --
   Kitchen"), `project_id`. Repeat for each scene, in order. Keep the opening
   line and the style block identical across scenes; only the beats change.
5. Alternates: `duplicate_scene` with the source `scene_id` and the changed
   `prompt` (or `refs`, `seconds`, `roles`). The copy is a fresh scene to price
   and render; its stills and clips are never carried over. The copy is titled
   after the source with "(copy)" added and cannot be renamed from here: tell
   the person which `scene_id` is which and what changed.
6. Read the project back: `project` lists every scene with its status; `scene`
   reads one with its shots and clips.

## Then

Hand each scene to price-and-hand-off (`quote`, then the studio link). Once
the clips have landed, `assemble_clips` with their `gen:<id>`s from `library`,
in order (cut or crossfade), joins them free as a new item in the library;
poll `job` for the result.

## Do not

- Never write a scene over 30 seconds or a window outside 2-10 seconds.
- Never change the look or the anchor photo between scenes without saying so;
  that is what makes a sequence read as one piece.
- Never rewrite a saved scene with `write_scene` and `scene_id` without showing
  the new version first; it replaces the text.
- Never say a render has started; the person approves it in the studio.
