---
name: product-ad-set
description: Turns one product photo into a set of Phantra ads: three or four ad still prompts in different styles, opened in the studio to be drawn, and, when wanted, two or three short video ads with different hooks, each priced with `quote` and rendered in the studio. Use when someone asks for ads, a campaign or a launch set, or gives a product photo and says "make me ads". NOT for one product film (product-shots), a person to camera (ugc-ad) or versions of an existing ad (ad-variations).
---

# A set of ads from one product photo

One photo of the product in, a handful of finished ads out. A still is written
here and drawn in the studio from the link `open_in_studio` gives; a video ad
is a scene, priced by `quote` and rendered at its `approve_url`. Every still
and every render is priced and approved in the studio, one at a time.
Planning, writing and saving here spend no credits.

## 1. Get the product in

`elements`: is the product there as a **prop** with a photo? If not, ask:

- a file on their device: `upload_link` with `purpose` reference,
  `element_kind` prop and `element_name`; give them the `url`, they pick the
  file, then call `elements` again;
- a picture or the product's own page at an address THEY gave you:
  `add_element` with `kind` prop, a `name` and that address as `source`
  (from a page, its main picture is taken and what the page states about
  the product is kept in the notes). Never an address you found.

No photo at all? A still can be drawn from words alone, but it will not be
their exact product or label. Say so and let them choose.

## 2. Agree the set before anything is quoted

Offer directions in craft terms, never as a brand's or an artist's name:

- **Studio hero**: the product alone on a seamless sweep, one soft key and
  a rim, a clean reflection under it.
- **In use**: in a hand or on a real surface (a desk, a gym bench, a
  kitchen counter) in daylight.
- **Macro**: a few centimetres from one detail, shallow depth.
- **Bold graphic**: a flat colour field, the product large, a short
  headline in their words.

Then say the size of the set plainly: "four stills is four approvals in the
studio, and each video ad is its own". Agree the frame (1:1 or 3:4 for a
feed, with 4:5 copies by `reformat`; 9:16 for a story), and keep the set together with `create_project` (a title, a
brief, a look), passing its `project_id` on every call below.

Every headline, claim, number, price and offer on an ad comes from the
person. Never write a discount, a review, a "best-selling" or a result they
did not give you.

## 3. The stills

1. Write one prompt per style: the product ("the attached photo is the
   exact product and label"), where it sits, the light, the lens, the
   background, any words in quotes with their place, and "no other text".
   Show them together and take edits.
2. For each still the person wants, `open_in_studio` with `prompt`, `kind`
   image, the `aspect` and the `project_id`. Give them the links, one line
   each.
3. In the studio they attach the product photo, pick a model that takes
   reference pictures (one good at text for a headline), see the price and
   approve it. A model that draws from the prompt alone will not show their
   exact product; say so.
4. Each still lands in `library` with its `gen:<id>`.

## 4. The video ads (when wanted)

1. Write the first ad as a scene: two or three timed shots, 6 to 15 seconds,
   the pack shot the FIRST ref with role `product` (write-scene and
   product-shots have the shape). Save it with `write_scene`.
2. For each other hook, `duplicate_scene` with that `scene_id` and a
   `prompt` whose FIRST window alone is rewritten (the product arriving in
   frame, a hand reaching for it, a detail first). One change per copy.
3. `quote` each `scene_id`: the keyframes and the clip, one render per timed
   shot. Show the quotes side by side with each scene's `approve_url`.
4. The person renders the ones they want in the studio; `scene` shows the
   clips once they land.

## 5. Hand over the set

`library` (with `project_id`) lists everything made, by `gen:<id>`.
`reformat` makes another shape of any still or clip (`aspect` 9:16, 16:9,
1:1 or 4:5; `fit` pad or crop) at no credit cost, and `share_link` gives a
download link for each. Later, `what_works` reads which they kept.

## The spending rules

- Nothing here draws, renders or spends: each still and each render is
  priced and approved in the studio. Never say one was made until `library`
  or `scene` shows it.
- `affordable` false on a quote: say so and that credits are added in the
  studio. Offer a smaller set.
- Never state a price yourself or add quotes up in your head: read each
  number from its quote.
