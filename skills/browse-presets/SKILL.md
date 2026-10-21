---
name: browse-presets
description: Shows what Phantra can do before anything is made: the studio's effects (image edits, animated templates, camera moves, upscales, sound, cut-outs), saved recipes, and the video models. Browsing starts nothing. Use when someone asks what is possible, what effects, templates, styles or models there are, or wants to browse before choosing. NOT for running an effect (effects), pricing a scene (price-and-render) or choosing the best model for a job (model-prompting).
---

# Browse presets

Browsing spends nothing and changes nothing. Looking at a menu never starts an
effect, a still or a render: making one happens in the studio, where the
person sees its price in credits and approves it. Say that once, in one line,
if they seem unsure.

## 1. Find out what they want to browse

Ask only if it is not clear. Four shelves exist:

| they want to see | where |
|---|---|
| ways to change something already made, animate a still, add a camera move, upscale, add sound, cut out a subject | the studio's effects gallery (see the effects skill) |
| ways of working, saved by the studio or by them | `recipes` |
| video makers, lengths, frames and what each costs per second | `video_models` |
| image makers | the studio's image picker, opened by `open_in_studio` |

"What can you do?" is all four, kept short: one line each, then ask which
shelf to open.

## 2. Read the menu, never recite it from memory

- The effects: the studio's gallery lists every edit, template, camera move,
  upscale, sound and reframe with its price. `open_in_studio` with a render's
  `gen:<id>` as `source` opens that gallery on the render. Describe the kinds
  in plain words; never name a template or move as if you had read the list.
- `recipes` lists names with one line each. `recipe` with a name opens one.
- `video_models` lists the video models the studio runs now, with lengths,
  frames and prices in credits; `recommend_model` says which suits a job.
- Image models are chosen in the studio, in the composer the link opens.

If a list is long, show the five or six that fit what they said they are
making and offer more. Never paste a whole menu.

## 3. Show each choice the way a person would pick it

For every item give: its name, what it does in plain words, what it needs
(an image, a clip, a prompt) and, when the menu gives one, its price in
credits. A price read here is a guide: the studio shows the real one before
anything is approved. Do not call it the price.

Offer to make it concrete: with their own material, `library` lists what they
have (`gen:<id>` and `asset:<id>`), and a photo not in it yet comes in through
`upload_link`. An effect needs something to act on, so ask what to try it on.

## 4. When they pick one

- An effect: hand over to the effects skill, which writes the instruction
  and opens the studio on that render.
- A recipe: open it with `recipe` and follow it as the person's own way of
  working; anything that makes media goes to the studio by its link.
- A video model: for a recommendation, `recommend_model` with the job in
  words; the choice stays theirs, and `set_preferences` can make it the default.
- Nothing yet: leave it open. Offer to keep browsing another shelf.

## The rules

- Browsing never authorizes spending, and nothing here spends: every price is
  shown again and approved in the studio.
- Never invent an effect, template, camera move, model or price. If the menu
  does not list it, say so and show what is close.
- Never claim to have made an example "to show what it looks like".
- Credits are the only unit: never give dollars or compare plans.
