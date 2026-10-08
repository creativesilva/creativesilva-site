/**
 * Print Party uploader (Google Apps Script web app).
 * Receives one image from www.creativesilva.com/print-party.html and saves it
 * into a Google Drive folder. Same pattern as the Light Writerz uploader, but a
 * SEPARATE deployment so it can only reach the Print Party folder.
 *
 * SETUP (Chris, one time):
 *  1) In Google Drive, make a folder for submissions, e.g. "Print_Party_Incoming".
 *     Open it and copy its ID from the URL (the long string after /folders/).
 *     Paste it into PRINT_FOLDER below.
 *  2) drive.google.com -> New -> More -> Google Apps Script. Paste this whole file. Save.
 *  3) Deploy -> New deployment -> type Web app ->
 *        Execute as: Me, Who has access: Anyone -> Deploy -> authorize.
 *  4) Copy the Web app /exec URL and either give it to Claude, or paste it into
 *     print-party.html at PP_ENDPOINT. The key below must match PP_KEY on the page.
 *
 * Files land named like 2026-10-16_PRINT_611691_Jane-Doe_sunset.jpg, with the
 * student number kept in the file's Drive description as well.
 */
const PRINT_FOLDER = "PASTE_YOUR_PRINT_PARTY_FOLDER_ID_HERE";
const TARGETS = {
  "print-party": { folderId: PRINT_FOLDER, key: "print-party-2026", imgOnly: true, prefix: "PRINT" },
};
const MAX_BYTES = 45 * 1024 * 1024; // ~45 MB per file

function doPost(e) {
  try {
    const d = JSON.parse(e.postData.contents);
    const t = TARGETS[d.target];
    if (!t || String(d.key) !== t.key) return out({ ok: false, error: "Not authorized" });
    if (t.imgOnly && !/^image\/(jpeg|png)$/.test(d.type || "")) return out({ ok: false, error: "JPG or PNG only" });
    const bytes = Utilities.base64Decode(d.data);
    if (bytes.length > MAX_BYTES) return out({ ok: false, error: "File over 45 MB" });
    const stamp = Utilities.formatDate(new Date(), "America/Los_Angeles", "yyyy-MM-dd");
    const safe = function (v, n) { return String(v || "").replace(/[^\w.\- ]+/g, "_").trim().slice(0, n); };
    const clean = safe(d.name || "image", 120);
    const parts = [stamp, t.prefix, safe(d.studentId, 20), safe(d.student, 40).replace(/ +/g, "-"), clean].filter(Boolean);
    const blob = Utilities.newBlob(bytes, d.type || "application/octet-stream", parts.join("_"));
    const file = DriveApp.getFolderById(t.folderId).createFile(blob);
    const note = [d.student && "Name: " + d.student, d.studentId && "Student #: " + d.studentId].filter(Boolean).join("\n");
    if (note) file.setDescription(note);
    return out({ ok: true, id: file.getId(), name: file.getName() });
  } catch (err) {
    return out({ ok: false, error: String(err) });
  }
}

function doGet() {
  return out({ ok: true, service: "Print Party incoming", targets: Object.keys(TARGETS) });
}

function out(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
