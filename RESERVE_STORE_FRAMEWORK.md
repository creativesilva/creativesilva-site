# Reserve Store Build Framework

The single source of truth for **`reserve.html`**, the student-facing equipment reservation storefront at `www.creativesilva.com/reserve.html`. Read this before changing the store. It captures the architecture, the locked decisions, the color framework, and the flows so we don't lose the thread between sessions.

Modeled on lensprotogo-style browsing, reskinned to the Pioneer Valley dark teal aesthetic. It will eventually replace the old `calendar.html` student reserve flow (keep the calendar until Chris verifies the store is better).

---

## 1. Files & architecture

| File | Role |
|------|------|
| `reserve.html` | The whole storefront: markup + one inline `<script>` app. No build step. |
| `css/store.css` | The only stylesheet. Bump the `?v=NN` query in `reserve.html` on every CSS change to bust cache. Currently **v30+**. |
| `pvhs-dashboard/server.py` | The backend (Render, `command.creativesilva.com`). The **source of truth** for inventory, availability, eligibility, reservations. Separate repo, auto-deploys from `main` (~60-90s). |

The store is a static page that calls the live backend. Deploy = push `main`, GitHub Pages serves in ~60-180s. Always confirm live on the public URL before telling Chris it's done.

**Backend data the store uses** (`GET /api/camera/calendar`, public, sanitized, CORS `*`): `cameras`, `checkouts[]` (camera reservations, no PII), `oos`, `no_card`, `equipment[]` (gear reservations), `equipment_oos`, `equipment_units{id:{type,label,pool,kit}}`, `pools`, `equipment_pools`, `blackouts`. Each reservation record carries `{item/camera, out, due, returned, status}`.

---

## 2. Color framework (LOCKED)

Two different surfaces, two color systems. Do not confuse them.

### Student store = AVAILABILITY colors (what a count means)
The student sees **counts**, not per-unit status. Each item card's "X / Y available" and the calendar day counts use:

- **GREEN (`--green` #3fd27f)** = all units free (`free == total`). Fully available.
- **YELLOW (#ffd166)** = some reserved, some still free (`0 < free < total`).
- **RED (#ff9a8a)** = none free (`free == 0`). All out for those dates.

(The old "<=2 left = yellow" scarcity rule was WRONG: it made a fully-available 2-unit item like the zoom lenses show 2/2 in yellow. Fixed 2026-10-23.)

Students never see **orange**: orange ("picked up / out") is a teacher-board per-unit status, and the student store only shows availability, not who has what.

### Teacher board (`camera-manager.html`) = per-unit STATUS colors
Separate surface, its own framework: **green = available, yellow = reserved, orange = picked up / out, red = overdue.** This is per-physical-unit status, not a count.

Brand chrome (buttons, nav, accents) stays **teal** (`--teal` #007474 / `--teal-bright` #19d3c5) on both surfaces; the green/yellow/orange/red are **status indicators only**.

---

## 3. Availability logic (LOCKED)

Per-unit, mirroring the backend so the store never offers what the server rejects and never falsely blocks what it accepts.

- **Half-open overlap** (`overlaps(out,due,co,ret) = out<ret && due>co`). A reservation blocks a new request only on a half-open overlap, so a **same-day handoff is allowed**: an item reserved *from* the day you return it is still available to you. (Closed intervals wrongly flagged the return-day boundary: fixed 2026-10-23.)
- `freeUnitsFor(it)` → the free unit ids/cam numbers for the chosen `[checkout, returnDay]` span. `allUnitsFor(it)` → every unit (free + busy) for the detail picker. `stockFor(it)` → `{free, total}`.
- The calendar's per-day count (`freeCamsOnDay`) is a single-day check (closed is correct for "free to START on day X").
- Known gap: the store does not replicate the backend's gear "physically OUT held from pickup forward" rule, so a stale overdue-out gear unit can show available then 409 (rare, server-caught).

---

## 4. The student flow

1. **Sign in**: student number only (`POST /api/camera/student_info`), confirm contact on a second step. Auto sign-in popup 3s after load. Eligibility gate: too many missing assignments in Silva's class → on hold.
2. **Dates**: the one-box planner (`planOv`): checkout day → **pickup time** → **return time**. Pickup options: Nutrition, Lunch, After 6th period, and a single **"During class"** showing the student's own period (not P1-P7 chips). Return auto-defaults to the next school day.
3. **Browse**: Popular Rentals is the home view; category nav (Camera Kits / Lenses / Lighting / Accessories); or the **Calendar View** accordion (a month with per-day free-camera counts; tap a day to reserve from there).
4. **Pick a unit**: each item's detail shows a per-unit selector: free numbers selectable, checked-out ones greyed/struck-through. The student picks the exact unit (e.g. Cam 17); quick-add auto-assigns the first free unit. Stored in `PICK{model->unitId}`.
5. **The Equipment Bag (cart)**: see §5.
6. **Reserve**: `submitReservation` resolves each item to its picked unit (falls back to another free one if taken) and POSTs `/api/camera/checkout`. On-screen receipt (no email). Camera + its gear post as one linked reservation; gear-only posts independently.
7. **Request anyway**: a student blocked by a lock (Photo-2 item) or a missing-work hold can "request anyway" → a PENDING reservation the teacher approves/denies from the board.

---

## 5. The Equipment Bag = Amazon-style cart (LOCKED)

The bag behaves like a shopping cart:
- Dates summary (pick up / return / where) with **Change dates** (re-opens the planner, refreshes the cart).
- Each line: thumbnail, name, its **unit chip** (e.g. CAM 09), a **"›"** to tap and change that item's unit (opens its detail on top, "Save this one" returns), and **Remove**.
- An always-present **Add equipment** (continue shopping) that opens the category→item picker on top of the cart and returns on Done.
- **Reserve this gear** (or "Set checkout dates" when dates aren't set yet; "Send request" when it's a pending request).

---

## 6. The picker (Add equipment)

Category tiles → item grid → **in-place detail** (the selected item takes over the card with a "‹ Back to <category>" button, the unit picker, and Add to bag → returns to the grid). Never open the separate `#detailOv` from inside the picker (it stacks behind: use the in-place `pickerItem` view).

**Overlay DOM / stacking order** (all `.sov` share `z-index:200`, later in DOM = on top): `bagOv < detailOv < rcptOv < pickerOv < acctOv`. So the detail layers over the bag, and the picker over both.

---

## 7. Account card

The account chip opens a **My Account** sheet: name, period/course/teacher, student number, your cell, parent/guardian name and cell, plus **Edit my info** (prefilled form → `/api/camera/student_update`) and **Log out**. Opens for any signed-in student (hold or not).

---

## 8. Client state

Session storage: `pv_user` (the signed-in student), `pv_bag` (model names), `pv_req` (name→'photo2' for requested locked items), `pv_pick` (name→chosen unit). `CAL` holds the latest calendar fetch.

---

## 9. Hard rules

- Student-facing assets on `www.creativesilva.com` only. No em dashes. No "shoot/shot/screenshot". 5th-grade reading level.
- Mobile-first: the store is built for student iPads and phones. **Every dialog caps to the live viewport (`100dvh`) and scrolls its body** so the action button is always reachable on a short phone screen; verify at a short height, not just the emulator (which scales height and hides overflow).
- The reservation is a **soft gate**: client checks + server-validated override codes. Teacher override code (both gear-unlock and missing-work): **322331** (repo default; set a Render env var for a private code). Keep availability math matching the backend.

---

## 10. Decisions log (dated, newest first)

- **2026-10-23**: Availability color framework: GREEN all free / YELLOW some reserved / RED none (was a buggy "<=2 = yellow" scarcity rule). Desktop calendar accordion enlarged (`max-width:1000px`, bigger cells).
- **2026-10-22**: Half-open overlap fix (same-day handoff). Account card (profile + Edit + Log out). In-place picker detail + Amazon-style cart (Add equipment always present, tap-to-change-unit). Per-unit picker on the detail screen. "Option B" lifted teal-charcoal background. Pickup "During class" single option. Calendar View accordion. Teacher override code set to 322331.
- **2026-10-20**: Submission + on-screen receipt (Phase A). Request → approval queue (Phase B). SmallRig overhead light kit added. "How it works" collapsed to an accordion.
- **2026-10-16**: Store shell live: lensprotogo dense layout reskinned dark PV-teal; sign-in + eligibility gate; date planner with bell-schedule windows; live stock counters; item detail pop-out; Godox kit.

---

## 11. Pending / next

- Firebase reservation history (a My Account "past reservations" view; currently session-only).
- PII-safe per-teacher roster-history so Popular Rentals reflects the student's own course (currently global frequency).
- Mankin's Apple Pencils in the store (image ready).
- Teacher "Digital Media Educators" bio cards (on hold).
- Verify on a real student iPad; mirror `schedule-data.js` onto creativesilva.com if github.io is blocked on student devices.
