---
name: projects-and-ideas
description: Turn a brief into a few story ideas in the chat, get the person's choice, and keep the work in a Zeropage Studio project they can come back to. Use when someone describes a video, ad, short or scene they want made, wants to bounce ideas, asks what projects they have, or wants to reopen or start one. NOT for writing the scene prompt itself (write-scene), NOT for pricing or rendering (render-and-status), and NOT for choosing a visual look (look-matching).
---

# Projects and ideas

Ideas live in this conversation, not on a list in the studio: nothing is saved
until a scene is written (write-scene). What the studio keeps is the
**project**: a name, a brief, an optional look, and the scenes written into
it. Nothing on this skill's path spends credits.

## Before you start

Call `projects` first when the person mentions earlier work, a client or a
piece they are continuing. If one fits, `project` with its id brings back the
brief, the look, the scenes so far (each with its status, and its still or
clip), the reference photos those scenes used, and the latest turns of the
project's chat in the studio. Read it before proposing anything new: a
project's brief and look are what every scene in it is held to.

If a call answers "no account" or a sign-in message, the person has not
created their workspace yet: ask them to sign in once at
https://zeropage.studio (the workspace is created on the first sign-in) and
reconnect.

## Turning a brief into ideas

1. Read the brief. Ask at most **three** short questions, and only when the
   answer changes the idea: who it is for, how long (seconds), and what must be
   in frame (a product, a place, a person they will attach photos of). Offer
   choices as short options, not open questions. Do not ask about budget,
   tools or style here.
2. Propose **two to four** ideas in the chat, each as: a working title, one
   sentence of what we see, one sentence of why it holds attention. Keep them
   different from each other.
3. Wait for the person to choose. Then go on to write-scene with the chosen
   one. Do not write scenes for ideas they did not choose.

## Projects

- `create_project` when the work is a piece the person will come back to (a
  client's ad, a series, a short): a `name`, an optional `brief` (who it is
  for, what it must always have and never show) and an optional `look` (the
  style every scene in it is held to). Offer it; do not create one unasked.
  It appears on their projects board in the studio.
- A scene goes into a project when write-scene passes its `project_id`.
  Without one, the scene stands on its own and is still in the studio.
- `project_chat` pages further back through a project's studio chat (`before`
  = the oldest turn id you hold). Read it only when the latest turns from
  `project` do not answer what was asked.

## What to say and not say

- Summaries, not dumps: say how many projects or scenes there are and the few
  that fit what was asked.
- Never invent an id. Every project or scene id you use comes from a reply in
  this conversation.
- Never say anything is rendering, drawn or scheduled. This skill ends at a
  chosen idea, or an open project.
