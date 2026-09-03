# Incoming drop zone (STAGING ONLY, ends empty)

Drop raw files here for Claude to process. This folder is a move-through
staging area, **not storage**. After a work session it should be **empty
except this README**.

When you drop something, tell Claude in chat what it is for (which course /
module / step, hero vs float, or that it is an icon / logo / source master).
Claude will:

1. View it, then resize / optimize for web + Canvas
2. Rename to the project convention (e.g. `pictograms-step01-float-v2.png`)
3. Move it to the correct home:
   - web images -> `assets/images/<course>/<module>/`
   - editable **source masters** (SVG / PSD / AI / vector originals) ->
     a permanent `_src/` folder beside their output
     (e.g. `assets/Icons/assignment/_src/`), never left here
4. Wire it into the page, commit, push, and confirm it is live
5. Delete the raw original(s) from here, including superseded versions

Everything in this folder except this README is gitignored: contents are
local staging only, never committed.

**Not for long-term storage.** Rosters, student submissions, schedules, or
unrelated design source do not belong here. If they land here, Claude will
surface them and move them to their proper home (or out of the repo) on
your say-so, not delete them silently.
