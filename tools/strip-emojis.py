#!/usr/bin/env python3
"""Remove emojis from student-facing Canvas content. Standing rule:
no emojis in student content (they read cheap). Scope is the #top copy
region only, so the builder nav icons (Copy/Download HTML buttons) and
the copy-feedback <script> are left alone. Arrows and typographic
entities (&larr; &rarr; &bull; &middot;) are kept.

Strips:
  - literal emoji pictographs (U+1F300-1FAFF, U+2600-27BF, U+2B00-2BFF)
  - decimal HTML entities &#N; with N >= 127000 (the emoji block)
Then tidies the leading/duplicate spaces an emoji leaves behind inside
<strong> labels.

Usage: python3 tools/strip-emojis.py <file.html> [more...]
"""
import re, sys, os

EMOJI_CHARS = re.compile('[\U0001F300-\U0001FAFF☀-➿⬀-⯿️]')
EMOJI_ENTITY = re.compile(r'&#(\d+);')

def strip_region(region):
    # literal emoji chars
    region = EMOJI_CHARS.sub('', region)
    # decimal entity emojis (>=127000), keep arrows/typographic (<127000)
    region = EMOJI_ENTITY.sub(lambda m: '' if int(m.group(1)) >= 127000 else m.group(0), region)
    # tidy: "<strong> Word" -> "<strong>Word"; "> word" leading space after tag
    region = re.sub(r'(<strong>)\s+', r'\1', region)
    region = re.sub(r'(>)[ \t]{2,}', r'\1 ', region)
    # collapse a stray double space left mid-label
    region = re.sub(r'([^\s>])[ \t]{2,}([^\s<])', r'\1 \2', region)
    return region

def main():
    changed = 0
    for path in sys.argv[1:]:
        with open(path) as f: html = f.read()
        i = html.find('id="top"')
        if i == -1:
            # no canvas root; process whole body conservatively (chars only)
            new = EMOJI_CHARS.sub('', html)
        else:
            j = html.find('<script', i)
            if j == -1: j = len(html)
            new = html[:i] + strip_region(html[i:j]) + html[j:]
        if new != html:
            with open(path,'w') as f: f.write(new)
            print(f'  stripped {os.path.basename(path)}')
            changed += 1
    print(f'done: {changed} file(s) changed')

if __name__ == '__main__':
    main()
