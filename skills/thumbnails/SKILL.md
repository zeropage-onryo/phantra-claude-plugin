---
name: thumbnails
description: Writes a cover image for Phantra (a YouTube thumbnail, a Reels, TikTok or Shorts cover, a feed cover) as one still prompt in the platform's frame, with a few words that stay readable small, and opens it in the studio with `open_in_studio` to be drawn on the person's approval. Use when someone asks for a thumbnail, a cover, a title card or a poster frame. NOT for editing a still (effects), the first seconds (hooks-and-first-seconds) or a set of ad stills (product-ad-set).
---

# Thumbnails and covers

A cover is one still. You write its prompt with the person here; it is drawn
in the studio, where they see the price in credits and approve it.
`open_in_studio` gives the link that opens the studio with the prompt ready.
Writing the prompt and making other shapes afterwards spend no credits.

## 1. What it is a cover for, and its frame

Ask what the video or post is about in one sentence, and where the cover
will be seen. Frames the studio advises (its advice, not a platform's rule):

| where | `aspect` |
|---|---|
| a YouTube video | 16:9 |
| a Reels, TikTok or Shorts cover | 9:16 |
| a feed post | 1:1, or 3:4 and a 4:5 copy with `reformat` |

Draw the cover AT the frame it will be shown in: text placed for 16:9 does
not survive a crop.

## 2. One idea, readable small

A cover is seen at the size of a postage stamp. Agree with the person:

- **One subject, large**: a face with one clear expression, or one object.
  Close framing, off-centre, with clean space on one side for the words.
- **Few words**: four or fewer, in their words. The video's title already
  sits beside the cover, so the text adds to it and never repeats it.
- **Contrast**: a simple background, light against dark, one accent colour.
- **Clear edges**: keep text off the bottom of a 9:16 cover and the
  bottom-right of a 16:9 one, where apps draw their own labels.

Never put a claim, a number, a price, a quote or a result on a cover that
the person did not give you, and never draw a fake screenshot, a made-up
review or another company's logo.

## 3. The model and the photo

The image model is picked in the studio, in the box the link opens.

- **Words on the image**: tell them to pick a model whose line there says it
  is good at text or typography.
- **Their own face or product**: it must come from a photo. Check it is in
  `elements` (or `library`); in the studio they attach it to the prompt, on a
  model that takes reference pictures. A model that draws from the prompt
  alone will not show their face or product; say so.

No photo yet? `upload_link` (with `element_kind` and `element_name`) for a
file on their device, or `add_element` for a picture at an address they gave.

## 4. The prompt

Write it as one still, in this order: the subject and what it is doing or
feeling; the framing (close, off-centre, which side is left clear); the
light; the background; then the exact words in quotes with where they sit
and how they look in plain craft terms (a heavy sans-serif, white with a
dark outline, two lines), and "no other text". Name no brand, film or
person for the look.

```
Close portrait, off-centre left, of the woman in the attached photo, eyebrows
raised, holding a cracked phone toward the lens. Hard key from the right,
deep blue shadow side. Plain dark teal background with a soft falloff. On
the right third, two lines of heavy white sans-serif with a thin dark
outline: "I FIXED IT" above "IN 5 MIN". No other text, no logos.
```

## 5. Open it in the studio

1. `open_in_studio` with `prompt`, `kind` image, the `aspect`, and
   `project_id` when the cover belongs to a project. It answers a `url`.
2. Give them the link: the studio opens with the prompt in the box; they
   attach the photo if there is one, send it, see the price and approve it.
   Nothing is drawn or spent until they do.
3. When they come back, `library` lists the cover as a `gen:<id>`.

Never say the cover was drawn or what it cost; the studio shows both.

## 6. Options and other shapes

- **A second option** is a second prompt and a second link, each approved
  in the studio. Change one thing (the words, the expression, the colour) so
  the choice means something.
- **Another shape of the same cover**: `reformat` with its `gen:<id>`,
  `aspect` (9:16, 16:9, 1:1 or 4:5) and `fit` pad or crop. It costs no
  credits and the original is untouched. A crop can cut the words off: when
  the text matters in the new shape, draw the cover again at that `aspect`.
- **The file**: `share_link` with the `gen:<id>` gives a download link.
  Uploading the cover to the platform is the person's; nothing here posts.
