/**
 * Drive Incoming uploader (Google Apps Script web app).
 * ONE deployment serves multiple "incoming" folders (creativesilva, lightwriterz, ...).
 * The Curriculum Catalog paperclip button POSTs JSON as text/plain (avoids a CORS
 * preflight) with { target, key, name, type, data(base64) } and the script saves the
 * file into the matching folder. Accepts ANY file type.
 *
 * SETUP (Chris, one time):
 *  1) Extensions ▸ Apps Script (or Drive ▸ New ▸ Apps Script), paste this file, Save.
 *  2) Deploy ▸ New deployment ▸ Web app ▸ Execute as: Me ▸ Who has access: Anyone ▸ Deploy ▸ authorize.
 *  3) Copy the Web app /exec URL and give it to Claude to paste into BOTH incoming rows'
 *     `endpoint` in curriculum.html (they share the same URL; `target` routes the file).
 * The folders are found by name and AUTO-CREATED on first upload if missing, so there is
 * no folder ID to copy. (LWZ keeps its existing folder by ID.)
 */
const TARGETS = {
  lightwriterz:  { folderId: "1p3IYB6lNez4Byv8yzMs3AsgBV7HzNPOV", key: "lwz-7a538caa4e2f" }, // existing LWZ_incoming
  creativesilva: { folderName: "creativesilva_incoming",          key: "cs-9d4f1a6b3e28" }, // auto-created if missing
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
    if (!t || d.key !== t.key) return out({ ok: false, error: "Not authorized" });
    const bytes = Utilities.base64Decode(d.data);
    if (bytes.length > MAX_BYTES) return out({ ok: false, error: "File over 45 MB" });
    const stamp = Utilities.formatDate(new Date(), "America/Los_Angeles", "yyyy-MM-dd");
    const clean = String(d.name || "file").replace(/[^\w.\- ]+/g, "_").slice(0, 120);
    const file = folderFor(t).createFile(Utilities.newBlob(bytes, d.type || "application/octet-stream", stamp + "_" + clean));
    return out({ ok: true, id: file.getId(), name: file.getName() });
  } catch (err) {
    return out({ ok: false, error: String(err) });
  }
}

function doGet() {
  return out({ ok: true, service: "Drive incoming", targets: Object.keys(TARGETS) });
}

function out(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
