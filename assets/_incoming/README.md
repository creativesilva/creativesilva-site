# Incoming image drop zone

Drop raw images here for Claude to process. Claude will:
1. View it, then resize / optimize for web + Canvas
2. Rename to the project convention (e.g. `pictograms-step01-float-v2.png`)
3. Move it to the correct `assets/images/<course>/<module>/` folder
4. Wire it into the page, commit, push, and confirm it is live

Files here are ignored by git (they get moved out). Tell Claude in chat what
the image is for (which course / module / step / hero vs float) so it lands right.
