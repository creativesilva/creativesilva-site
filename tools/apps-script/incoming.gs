/**
 * Drive Incoming uploader (Google Apps Script web app).
 * ONE deployment serves multiple "incoming" folders (LWZ, Curriculum, ...).
 * The Curriculum Catalog paperclip button POSTs JSON as text/plain (avoids a CORS
 * preflight) with { target, key, name, type, data(base64) } and the script saves the
 * file into the matching folder. Accepts ANY file type.
 *
 * SETUP (Chris, one time):
 *  1) In Google Drive, create a "Curriculum_incoming" folder (LWZ_incoming already exists).
 *     Open each folder and copy its ID from the URL (…/folders/<THIS_ID>).
 *  2) Paste the Curriculum folder ID below (LWZ is already filled).
 *  3) Extensions ▸ Apps Script, paste this file, Save.
 *  4) Deploy ▸ New deployment ▸ Web app ▸ Execute as: Me ▸ Who has access: Anyone ▸ Deploy.
 *  5) Copy the Web app /exec URL and give it to Claude to paste into BOTH incoming rows'
 *     `endpoint` in curriculum.html (they share the same URL; `target` routes the file).
 */
const TARGETS = {
  lwz:        { folder: "1p3IYB6lNez4Byv8yzMs3AsgBV7HzNPOV", key: "lwz-7a538caa4e2f" }, // LWZ_incoming
  curriculum: { folder: "PASTE_CURRICULUM_FOLDER_ID_HERE",   key: "cur-2f9b1e7c4a6d" }, // Curriculum_incoming
};
const MAX_BYTES = 45 * 1024 * 1024; // ~45 MB per file (Apps Script POST payload ceiling is ~50 MB)

function doPost(e) {
  try {
    const d = JSON.parse(e.postData.contents);
    const t = TARGETS[d.target];
    if (!t || d.key !== t.key) return out({ ok: false, error: "Not authorized" });
    if (!t.folder || /PASTE_/.test(t.folder)) return out({ ok: false, error: "Folder not set for " + d.target });
    const bytes = Utilities.base64Decode(d.data);
    if (bytes.length > MAX_BYTES) return out({ ok: false, error: "File over 45 MB" });
    const stamp = Utilities.formatDate(new Date(), "America/Los_Angeles", "yyyy-MM-dd");
    const clean = String(d.name || "file").replace(/[^\w.\- ]+/g, "_").slice(0, 120);
    const file = DriveApp.getFolderById(t.folder)
      .createFile(Utilities.newBlob(bytes, d.type || "application/octet-stream", stamp + "_" + clean));
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
