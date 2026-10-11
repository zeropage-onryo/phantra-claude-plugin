---
name: look-matching
description: Set the visual look of a scene in Zero Page Studio from the person's own reference photos and from an image or video frame they describe or attach, and explain what the studio can and cannot match. Use when someone says "make it look like this", attaches or describes a reference image or frame, asks for a mood, light or texture, or asks which photos a scene is rendered against. NOT for writing the whole scene (write-scene), NOT for rendering or prices (price-and-hand-off), and NOT for finding or copying a real person's face.
---

# Look matching

Zero Page Studio renders a scene against **the person's own photographs,
kept as elements** (characters, props, places), never against a name and
never against an image somebody else chose for them. A look is written into
the scene's style block in cinematography terms; the photos decide identity,
wardrobe, product and place.

## The rule on people

Never look for, describe for copying, or ask for a specific real person's
face. If the scene needs a face, it is the person's own or someone they have
the right to use, provided by them as an element. Say this plainly when asked
for a celebrity, a public figure or "someone who looks like X", and do not
add a picture of one with `add_element`.

## Working with the person's photos

- `elements` lists their characters, props and places with photo refs and a
  short description. Read it before writing a look: a room they photographed
  is a room the scene can be set in; a product they photographed is the exact
  product on screen.
- If the look needs a photo they do not have (a product, a location, a
  wardrobe), say which and ask them for it. Two ways in:
  - `add_element` files ONE picture as a character, prop or location. Its
    `source` is the https address of an image file **the person gave you** in
    this conversation (the image itself, not the page it is on; jpg, png or
    webp), or `gen:<id>` of one of their own renders that `project` lists.
    Give it a `kind`, a `name` and a few words of `notes`. A name they already
    have of that kind gains the picture instead of making a second element.
    It draws nothing and spends nothing.
  - or they upload it in the studio (Elements), and `elements` lists it.
- Never give `add_element` an address you found or guessed, and never search
  for a picture on the person's behalf. The photo is theirs to choose.
- Refs go into `write_scene` as listed by `elements`, most important first:
  the face before the room, the product before the backdrop. The first ref is
  what the render anchors on.

## Reading an attached image or video frame

When the person shares an image or a frame, translate it into the terms the
scene's style block uses, and offer that back for their yes:

- light: source, direction, colour temperature, hardness, time of day
- surfaces and textures: wet, dusty, matte, worn
- framing: how close, what height, what lens feel, depth of field
- palette and grade: what is saturated, what is muted, contrast
- motion: what moves, how fast, handheld or locked
- finish: grain, softness, sharpness

Say what the studio will match (light, surfaces, framing, palette) and what it
will not (a specific film's or campaign's authorship, a brand's logo, a
person's likeness). Do not promise it will "reproduce" the reference.

## Writing the look into the scene

The look lives in part 2 of the scene prompt (see write-scene): two or three
sentences in cinematography and colour-grade terms, with the attached photos
winning over the look on anything they show. Realism comes from practical
light, believable physics and restraint, not from roughness. Never name a
film, a director, a brand or a real person in it.

## Reply shape

One short block: which element photos the scene is held to (by name and ref),
and the look in the words that will go into the prompt. Short enough to read
on a phone.
