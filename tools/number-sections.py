#!/usr/bin/env python3
"""Number main section chips as "LABEL / NN / TT" so a student sees the
section number out of the page total (navigation + length). Each
language block (English, then the Spanish mirror after #espanol) is its
own series that restarts at 01. Category and term chips (their own
sub-counts) are left untouched.

LOCKED behavior: chips read LABEL / NN / TT. Two-level pages keep their
CATEGORY NN / 08 and TERM NN / 50 sub-series; only the top-level
section chips get the page total.

Refuses to write a div-imbalanced result.
Usage: python3 tools/number-sections.py <file.html> [more...]
"""
import re, sys, os

CHIP = re.compile(r'(<strong>)(.+?)((?: / \d{2}){1,2})(</strong>)')
# A sub-series chip's label STARTS with the keyword (CATEGORY 01,
# TERM 05, CATEGORÍA, TÉRMINO). A main section like "THE EIGHT
# CATEGORIES" merely contains the word, so anchor the match at the start.
SUBSERIES = re.compile(r'^\s*(CATEGOR(Y|[IÍ]A|&IACUTE;A|&Iacute;A)|TERM[\s0-9]|T([EÉ]|&E?ACUTE;|&Eacute;)RMINO)', re.I)

def is_subseries(label):
    return SUBSERIES.match(label) is not None

CAT_VERBOSE = re.compile(r'(CATEGOR\S*?)\s+(\d+)\s+(?:OF|DE)\s+(\d+)', re.I)

def renumber_block(block):
    # First pass: count main-section chips (not sub-series)
    mains=[m for m in CHIP.finditer(block) if not is_subseries(m.group(2))]
    total=len(mains)
    if total==0:
        return block
    idx=[0]
    def repl(m):
        label=m.group(2)
        if is_subseries(label):
            # Normalize a verbose "CATEGORY 1 OF 8 / 07" (with stale
            # counter) into the clean "CATEGORY 01 / 08". Clean
            # categories and term chips are left as-is.
            cv=CAT_VERBOSE.match(label)
            if cv:
                return f'{m.group(1)}{cv.group(1)} {int(cv.group(2)):02d} / {int(cv.group(3)):02d}{m.group(4)}'
            return m.group(0)
        idx[0]+=1
        return f'{m.group(1)}{label} / {idx[0]:02d} / {total:02d}{m.group(4)}'
    return CHIP.sub(repl, block)

def process(html):
    i=html.find('id="top"')
    if i==-1:
        return html
    j=html.find('<script', i)
    if j==-1: j=len(html)
    head, body, tail = html[:i], html[i:j], html[j:]
    es=body.find('id="espanol"')
    if es==-1:
        body=renumber_block(body)
    else:
        body=renumber_block(body[:es]) + renumber_block(body[es:])
    return head+body+tail

def main():
    for path in sys.argv[1:]:
        h=open(path).read()
        new=process(h)
        if new==h:
            continue
        if new.count('<div')!=new.count('</div>'):
            print(f'  CHECK {os.path.basename(path)}: imbalance -- NOT WRITTEN'); continue
        open(path,'w').write(new)
        print(f'  OK {os.path.basename(path)}')

if __name__=='__main__':
    main()
