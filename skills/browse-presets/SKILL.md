---
name: browse-presets
description: Shows what Phantra can do before anything is made: the effects for the person's own images and clips (edits, animated templates, camera moves, upscales, sound, cut-outs, new shapes), saved recipes, and the video models. Browsing starts nothing. Use when someone asks what is possible, what effects, templates, styles or models there are, or wants to browse before choosing. NOT for running an effect (effects), pricing a scene (price-and-render) or choosing a model for a job (model-prompting).
---

# Browse presets

Browsing spends nothing and changes nothing. Looking at a menu never starts an
effect, a still or a render: an effect is quoted in credits and runs only on
the person's yes; a new still or a render is approved in the studio. Say that
once, in one line, if they seem unsure.

## 1. Find out what they want to browse

Ask only if it is not clear. Four shelves exist:

| they want to see | where |
|---|---|
| ways to change their own image or clip: edit it, animate it, add a camera move, upscale, add sound, cut out a subject, reshape | the seven effect tools' own choices (see the effects skill) |
| ways of working, saved by the studio or by them | `recipes` |
| video makers, lengths, frames and what each costs per second | `video_models` |
| image makers | the studio's image picker, opened by `open_in_studio` |

"What can you do?" is all four, kept short: one line each, then ask which
shelf to open.

## 2. Read the menu, never recite it from memory

- The effects are seven tools (`edit_image`, `remove_background`,
  `animate_still`, `camera_move`, `upscale_clip`, `add_sound`,
  `reframe_clip`); each one's schema lists its templates, moves, shapes and
  colours. Name one only from those lists. Their price comes in the quote.
- `recipes` lists names with one line each. `recipe` with a name opens one.
- `video_models` lists the video models the studio runs now, with lengths,
  frames and prices in credits; `recommend_model` says which suits a job.
- Image models are chosen in the studio, in the composer the link opens.

If a list is long, show the five or six that fit what they said they are
making and offer more. Never paste a whole menu.

## 3. Show each choice the way a person would pick it

For every item give: its name, what it does in plain words, what it needs
(an image, a clip, a prompt) and, when the menu gives one, its price in
credits. A price read here is a guide, not a quote: an effect's price comes
only in its quote, and some depend on the clip. Do not call it the price.

Offer to make it concrete: with their own material, `library` lists what they
have (`gen:<id>` and `asset:<id>`), and a photo not in it yet comes in through
`upload_link`. An effect needs something to act on, so ask what to try it on.

## 4. When they pick one

- An effect: hand over to the effects skill. Quote, wait for yes, then run.
- A recipe: open it with `recipe` and follow it as the person's own way of
  working, quoting any effect before it runs; new media goes to the studio.
- A video model: for a recommendation, `recommend_model` with the job in
  words; the choice stays theirs, and `set_preferences` can make it the default.
- Nothing yet: leave it open. Offer to keep browsing another shelf.

## The rules

- Browsing never authorizes spending. A "that looks great" is not a yes to a
  price they have not seen; quote it, then wait.
- Never invent an effect, template, camera move, model or price. If the menu
  does not list it, say so and show what is close.
- Never run anything while browsing, even to "show what it looks like". An
  example costs credits like any other run, and needs its own quote and yes.
- Credits are the only unit: never give dollars or compare plans.
