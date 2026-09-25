/**
 * Creative Silva Incoming uploader (Google Apps Script web app).
 * CREATIVE SILVA ONLY: it can reach creativesilva_incoming and nothing else.
 * Light Writerz has its own, completely separate uploader in its own repo,
 * so the two never cross.
 * The Curriculum Catalog paperclip button POSTs JSON as text/plain (avoids a CORS
 * preflight) with { target, key, name, type, data(base64) } and the script saves the
 * file into the matching folder. Accepts ANY file type.
 *
 * SETUP (Chris, one time):
 *  1) Extensions ▸ Apps Script (or Drive ▸ New ▸ Apps Script), paste this file, Save.
 *  2) Deploy ▸ New deployment ▸ Web app ▸ Execute as: Me ▸ Who has access: Anyone ▸ Deploy ▸ authorize.
 *  3) Copy the Web app /exec URL and give it to Claude to paste into the
 *     Creative Silva Incoming row's `endpoint` in curriculum.html.
 * The folder is found by name and AUTO-CREATED on first upload if missing.
 */
const TARGETS = {
  creativesilva: { folderName: "creativesilva_incoming", key: "cs-9d4f1a6b3e28" }, // auto-created if missing
};
const MAX_BYTES = 45 * 1024 * 1024; // ~45 MB per file (Apps Script POST payload ceiling is ~50 MB)

function folderFor(t) {
  if (t.folderId) return DriveApp.getFolderById(t.folderId);
  const it = DriveApp.getFoldersByName(t.folderName);
  return it.hasNext() ? it.next() : DriveApp.createFolder(t.folderName);
}

function doPost(e) {
  try {
    const d = JSON.parse(e.postData.contents);
    const t = TARGETS[d.target];
    if (!t || String(d.key) !== t.key) return out({ ok: false, error: "Not authorized" });
    if (t.imagesOnly && !/^image\//.test(d.type || "")) return out({ ok: false, error: "Images only" });
    const bytes = Utilities.base64Decode(d.data);
    if (bytes.length > MAX_BYTES) return out({ ok: false, error: "File over 45 MB" });
    const stamp = Utilities.formatDate(new Date(), "America/Los_Angeles", "yyyy-MM-dd");
    const safe = function (v, n) { return String(v || "").replace(/[^\w.\- ]+/g, "_").trim().slice(0, n); };
    const clean = safe(d.name || "file", 120);
    // Intake routing (catalog "Send to" tags): bake a route prefix into the name so the local
    // process-incoming.js watcher knows exactly where each image goes. Untagged uploads keep the
    // old naming and are never auto-published.
    const dslug = function (v) { return String(v || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, ""); };
    var finalName;
    if (d.dest) {
      finalName = ["route", dslug(d.dest), dslug(d.character) || "none", dslug(d.label) || "untitled", stamp, clean].join("__");
    } else {
      // Optional credit fields (student page): 2026-09-23_STUDENT_Jane-Doe_Orbit_IMG_1234.jpg
      finalName = [stamp, t.prefix, safe(d.student, 40).replace(/ +/g, "-"), safe(d.title, 40).replace(/ +/g, "-"), clean].filter(String).join("_");
    }
    const blob = Utilities.newBlob(bytes, d.type || "application/octet-stream", finalName);
    const file = folderFor(t).createFile(blob);
    const note = [d.dest && "Send to: " + d.dest, d.character && "Character: " + d.character, d.label && "Label: " + d.label, d.student && "Student: " + d.student, d.title && "Title: " + d.title, d.category && "Collection: " + d.category, d.message && "Note: " + d.message].filter(Boolean).join("\n");
    if (note) file.setDescription(note);
    return out({ ok: true, id: file.getId(), name: file.getName() });
  } catch (err) {
    return out({ ok: false, error: String(err) });
  }
}

function doGet() {
  return out({ ok: true, service: "Creative Silva incoming", targets: Object.keys(TARGETS) });
}

function out(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
