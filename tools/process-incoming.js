#!/usr/bin/env node
/*
 * process-incoming.js: CS Incoming intake processor (the brain of the auto-intake pipeline).
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
// Synced CS Incoming Drive folder (auto mode scans this for route__ tagged uploads).
const DRIVE = process.env.CS_INCOMING_DIR ||
  '/Users/riva/Library/CloudStorage/GoogleDrive-creativesilva1@gmail.com/My Drive/creativesilva_incoming';
const PROCESSED = path.join(DRIVE, '_processed'); // originals move here after a successful place
// git paths the processor is allowed to stage (never `-A`, so gitignored PII in _incoming can never ride along)
const GIT_PATHS = ['assets/images/characters', 'logos', 'assets/Icons', 'build-resources.html', 'build-resources-beta.html'];

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
  const os = require('os');
  // Copy to a local temp first. Reading all bytes forces a Google Drive online-only (placeholder)
  // file to fully download before sips touches it, so sips never fails with "cannot extract image".
  const tmp = path.join(os.tmpdir(), 'cs-intake-' + Date.now() + '-' + destAbs.split('/').pop());
  fs.copyFileSync(srcAbs, tmp);
  try {
    const srcPng = /\.png$/i.test(srcAbs);
    if (keepPng && srcPng){
      execFileSync('sips', ['-Z','1600', tmp, '--out', destAbs]);            // keep transparency
    } else {
      execFileSync('sips', ['-s','format','jpeg','-Z','1600', '-s','formatOptions','82', tmp, '--out', destAbs]); // -> jpeg
    }
  } finally { try { fs.unlinkSync(tmp); } catch(e){} }
}

// insert a reference entry as the FIRST element of the named array in each builder (no trailing-comma hazard)
// GROUPING RULE: keep every entry for one character together. A new image is inserted right after
// that character's last existing entry (grouped), never at the top. New characters append at the end.
function groupKey(label){ return String(label||'').split('(')[0].trim().toLowerCase(); }
function wireArray(arrayName, label, filePath){
  let touched = [];
  const key = groupKey(label);
  for (const f of BUILDERS){
    const abs = path.join(REPO, f);
    let src = fs.readFileSync(abs, 'utf8');
    const decl = src.match(new RegExp('var\\s+' + arrayName + '\\s*=\\s*\\['));
    if (!decl) { console.warn(`  (no ${arrayName} in ${f})`); continue; }
    if (src.indexOf(`file: '${filePath}'`) >= 0 || src.indexOf(`file:'${filePath}'`) >= 0){ console.warn(`  (${filePath} already in ${f})`); continue; }
    const start = decl.index + decl[0].length, end = src.indexOf('];', start);
    if (end < 0) continue;
    const spaced = /build-resources\.html$/.test(f) && !/beta/.test(f);
    const obj = spaced ? `{ label: '${label}', file: '${filePath}' }` : `{label:'${label}',file:'${filePath}'}`;
    const seg = src.slice(start, end);
    const objRe = /\{[^}]*label:\s*'([^']*)'[^}]*\}/g; let mm, groupEnd = -1, lastEnd = -1;
    while ((mm = objRe.exec(seg)) !== null){ const e = start + mm.index + mm[0].length; lastEnd = e; if (groupKey(mm[1]) === key) groupEnd = e; }
    const at = (groupEnd >= 0) ? groupEnd : lastEnd;
    if (at < 0){ src = src.slice(0, start) + '\n      ' + obj + '\n    ' + src.slice(start); }
    else { src = src.slice(0, at) + ',\n      ' + obj + src.slice(at); }
    fs.writeFileSync(abs, src);
    touched.push(f);
  }
  return touched;
}

// One-time (or repeatable) regroup: reorder an array so each character's entries are contiguous,
// preserving first-seen group order and intra-group order. Fixes any past intermixing.
function regroup(arrayName){
  for (const f of BUILDERS){
    const abs = path.join(REPO, f);
    let src = fs.readFileSync(abs, 'utf8');
    const decl = src.match(new RegExp('var\\s+' + arrayName + '\\s*=\\s*\\['));
    if (!decl){ continue; }
    const start = decl.index + decl[0].length, end = src.indexOf('];', start);
    if (end < 0) continue;
    const seg = src.slice(start, end);
    const objRe = /\{[^}]*\}/g; const objs = []; let mm;
    while ((mm = objRe.exec(seg)) !== null) objs.push(mm[0].trim());
    const order = [], groups = {};
    objs.forEach(function(o){ const lm = o.match(/label:\s*'([^']*)'/); const k = lm ? groupKey(lm[1]) : ''; if (!groups[k]){ groups[k] = []; order.push(k); } groups[k].push(o); });
    const sorted = []; order.forEach(function(k){ groups[k].forEach(function(o){ sorted.push(o); }); });
    const joined = sorted.map(function(o){ return '\n      ' + o; }).join(',');
    src = src.slice(0, start) + joined + '\n    ' + src.slice(end);
    fs.writeFileSync(abs, src);
    console.log('regrouped ' + arrayName + ' in ' + f + ' (' + sorted.length + ' entries, ' + order.length + ' groups)');
  }
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

// parse a route-tagged upload name: route__<dest>__<name>__<desc>__<stamp>__<original>.<ext>
function parseRoute(base){
  const parts = base.split('__');
  if (parts[0] !== 'route' || parts.length < 4) return null;
  return { dest: parts[1], name: (parts[2]||'').replace(/-/g,' ').trim(), desc: (parts[3]||'').replace(/-/g,' ').trim() };
}

function gitPublish(summary){
  try {
    execFileSync('git', ['add', ...GIT_PATHS], { cwd: REPO });
    const staged = execFileSync('git', ['diff', '--cached', '--name-only'], { cwd: REPO }).toString().trim();
    if (!staged){ console.log('  (nothing staged to publish)'); return; }
    execFileSync('git', ['commit', '-m', summary + '\n\nCo-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>'], { cwd: REPO });
    execFileSync('git', ['push', 'origin', 'main'], { cwd: REPO });
    console.log('  PUSHED: ' + summary);
  } catch (e){ console.error('  git publish failed: ' + (e.message||e)); }
}

function processAuto(push){
  if (!fs.existsSync(DRIVE)){ console.error('Drive folder not found: ' + DRIVE); process.exit(1); }
  fs.mkdirSync(PROCESSED, { recursive: true });
  const files = fs.readdirSync(DRIVE).filter(f => f.startsWith('route__'));
  if (!files.length){ return; } // silent when idle (this runs on a 60s poll)
  const done = [];
  for (const f of files){
    const abs = path.join(DRIVE, f);
    if (!fs.statSync(abs).isFile()) continue;
    const r = parseRoute(f);
    if (!r){ console.log('SKIP (bad route tag): ' + f); continue; }
    let res = null;
    try { res = processOne(abs, r.dest, r.name, r.desc); }
    catch (e){ console.log('RETRY later (' + String(e.message||e).split('\n')[0] + '): ' + f); continue; }
    if (res){ // placed: move the original out of the intake folder so it is not reprocessed
      try { fs.renameSync(abs, path.join(PROCESSED, f)); } catch (e){ /* leave it; still placed */ }
      done.push(res);
    }
  }
  if (done.length && push){
    const labels = done.map(d => d.label).join(', ');
    gitPublish('Intake: add ' + done.length + ' reference image' + (done.length>1?'s':'') + ' (' + labels + ')');
  } else if (done.length){
    console.log('auto: placed ' + done.length + ' file(s); run with --push to publish, or `git` them yourself.');
  }
}

function main(){
  const a = args();
  if (a.regroup){ regroup(typeof a.regroup === 'string' ? a.regroup : 'CHARACTERS'); return; }
  if (a.auto){ processAuto(!!a.push); return; }
  if (a.file){
    const fileAbs = path.resolve(a.file);
    if (!fs.existsSync(fileAbs)){ console.error('file not found: '+fileAbs); process.exit(1); }
    if (!a.dest){ console.error('need --dest'); process.exit(1); }
    const res = processOne(fileAbs, a.dest, a.name, a.desc);
    if (res && a.push) gitPublish('Intake: add ' + res.label);
    return;
  }
  console.log('Manual: --file <path> --dest character --name renee --desc "short hair: front" [--push]');
  console.log('Auto:   --auto [--push]   (scans ' + DRIVE + ' for route__ tagged files)');
}
main();
