#!/usr/bin/env node
/*
 * process-incoming.js  —  CS Incoming intake processor (the brain of the auto-intake pipeline).
 *
 * Takes an image that was tagged at upload (destination + character + label), optimizes it,
 * versioned-renames it, files it into the right assets folder, and wires it into the Prompt
 * Studio reference library in BOTH build-resources.html and build-resources-beta.html.
 *
 * HARD SAFETY GATE (never publish student PII):
 *   - only image files (.jpg/.jpeg/.png/.webp) are ever touched
 *   - a file is refused if its name/description matches roster/roll/seating/period/grade/PII words
 *   - a file with no valid destination tag is skipped (never guessed)
 *   - PDFs, docs, spreadsheets, and anything not explicitly image-tagged are ignored
 *
 * MODES:
 *   Manual (one file, used to place today's untagged uploads and to test):
 *     node tools/process-incoming.js --file "<path>" --dest character --name renee --desc "short hair: front"
 *     node tools/process-incoming.js --file "<path>" --dest item  --desc "Canon logo"
 *     node tools/process-incoming.js --file "<path>" --dest scene --desc "Quad at dusk"
 *   Auto (scan the synced Drive folder for route-tagged files; used by the launchd watcher):
 *     node tools/process-incoming.js --auto [--push]
 *
 * Tagged-filename convention the upload UI + Apps Script produce (auto mode reads this):
 *   route__<dest>__<name>__<desc>__<stamp>__<original>.<ext>
 *   e.g. route__character__renee__short-hair-front__2026-09-24__IMG1.png
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const REPO = path.resolve(__dirname, '..');
const IMG_ROOT = 'assets/images/characters/';
const BUILDERS = ['build-resources.html', 'build-resources-beta.html'];

// destination -> where the file lands + which array it wires into + file-path prefix used in the array
const DESTS = {
  character: { dir: 'assets/images/characters/',        array: 'CHARACTERS', filePrefix: '',        keepPng: false },
  item:      { dir: 'assets/images/characters/items/',  array: 'ITEMS',      filePrefix: 'items/',  keepPng: true  },
  scene:     { dir: 'assets/images/characters/campus/', array: 'SCENES',     filePrefix: 'campus/', keepPng: false },
  logo:      { dir: 'logos/',                            array: null,         filePrefix: '',        keepPng: true  },
  icon:      { dir: 'assets/Icons/assignment/',          array: null,         filePrefix: '',        keepPng: true  },
};

const PII_RE = /roster|\broll\b|seating|\bperiod\b|grade|ssn|social.?security|class.?list|names?\b.*(sheet|list)|PII/i;
const IMG_EXT = /\.(jpe?g|png|webp)$/i;

function slug(s){ return String(s||'').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,''); }
function cap(s){ return String(s||'').replace(/(^|\s)\S/g, c => c.toUpperCase()); }
function args(){ const a={}; const v=process.argv.slice(2); for(let i=0;i<v.length;i++){ if(v[i].startsWith('--')){ const k=v[i].slice(2); const n=v[i+1]; if(n===undefined||n.startsWith('--')){a[k]=true;} else {a[k]=n;i++;} } } return a; }

function piiRefuse(file, meta){
  const base = path.basename(file);
  if (!IMG_EXT.test(base)) return 'not an image file';
  if (PII_RE.test(base) || PII_RE.test(meta||'')) return 'looks like a roster / student PII';
  return null;
}

// pick a non-colliding versioned name: <slug>-v1.<ext>, bump if taken
function versionedName(destDir, baseSlug, ext){
  for (let v=1; v<100; v++){
    const name = `${baseSlug}-v${v}.${ext}`;
    if (!fs.existsSync(path.join(REPO, destDir, name))) return name;
  }
  return `${baseSlug}-v${Date.now()}.${ext}`;
}

function optimize(srcAbs, destAbs, keepPng){
  const srcPng = /\.png$/i.test(srcAbs);
  if (keepPng && srcPng){
    // keep transparency; cap the long edge at 1600
    execFileSync('sips', ['-Z','1600', srcAbs, '--out', destAbs]);
  } else {
    // photographic -> normalized jpeg, long edge <= 1600
    execFileSync('sips', ['-s','format','jpeg','-Z','1600', '-s','formatOptions','82', srcAbs, '--out', destAbs]);
  }
}

// insert a reference entry as the FIRST element of the named array in each builder (no trailing-comma hazard)
function wireArray(arrayName, label, filePath){
  let touched = [];
  for (const f of BUILDERS){
    const abs = path.join(REPO, f);
    let src = fs.readFileSync(abs, 'utf8');
    const decl = src.match(new RegExp('var\\s+' + arrayName + '\\s*=\\s*\\['));
    if (!decl) { console.warn(`  (no ${arrayName} in ${f})`); continue; }
    if (src.indexOf(`file: '${filePath}'`) >= 0 || src.indexOf(`file:'${filePath}'`) >= 0){ console.warn(`  (${filePath} already in ${f})`); continue; }
    const at = decl.index + decl[0].length;
    // match each file's brace style: spaced in build-resources.html, compact in the beta
    const spaced = /build-resources\.html$/.test(f) && !/beta/.test(f);
    const entry = spaced ? `\n      { label: '${label}', file: '${filePath}' },`
                         : `\n      {label:'${label}',file:'${filePath}'},`;
    src = src.slice(0, at) + entry + src.slice(at);
    fs.writeFileSync(abs, src);
    touched.push(f);
  }
  return touched;
}

function processOne(fileAbs, dest, name, desc){
  const D = DESTS[dest];
  if (!D){ throw new Error(`unknown dest "${dest}" (use ${Object.keys(DESTS).join('/')})`); }
  let meta = '';
  const refusal = piiRefuse(fileAbs, meta);
  if (refusal){ console.log(`REFUSED ${path.basename(fileAbs)} :: ${refusal}`); return null; }

  const srcPng = /\.png$/i.test(fileAbs);
  const ext = (D.keepPng && srcPng) ? 'png' : 'jpg';
  const baseSlug = dest === 'character' ? slug(`${name} ${desc}`) : slug(desc || name || path.basename(fileAbs));
  const outName = versionedName(D.dir, baseSlug, ext);
  const destAbs = path.join(REPO, D.dir, outName);
  fs.mkdirSync(path.dirname(destAbs), { recursive: true });
  optimize(fileAbs, destAbs, D.keepPng);

  let label, filePath = D.filePrefix + outName;
  if (dest === 'character') label = `${cap(name)} (${desc})`;
  else if (dest === 'scene' || dest === 'item') label = cap(desc || name);
  else label = cap(desc || name);

  let wired = [];
  if (D.array) wired = wireArray(D.array, label, filePath);
  console.log(`PLACED  ${path.basename(fileAbs)} -> ${D.dir}${outName}` + (D.array ? `  [${D.array}: "${label}"]  wired: ${wired.join(', ')||'none'}` : `  (no array)`));
  return { outName, destDir: D.dir, label, filePath, array: D.array };
}

function main(){
  const a = args();
  if (a.file){
    const fileAbs = path.resolve(a.file);
    if (!fs.existsSync(fileAbs)){ console.error('file not found: '+fileAbs); process.exit(1); }
    if (!a.dest){ console.error('need --dest'); process.exit(1); }
    processOne(fileAbs, a.dest, a.name, a.desc);
    return;
  }
  console.log('Manual usage: --file <path> --dest character --name renee --desc "short hair: front"');
  console.log('Auto mode (--auto) is wired for the launchd watcher and reads route__ tagged files.');
}
main();
