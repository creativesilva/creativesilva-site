# Reserve Store Build Framework

The single source of truth for **`reserve.html`**, the student-facing equipment reservation storefront at `www.creativesilva.com/reserve.html`. Read this before changing the store. It captures the architecture, the locked decisions, the color framework, and the flows so we don't lose the thread between sessions.

Modeled on lensprotogo-style browsing, reskinned to the Pioneer Valley dark teal aesthetic. It will eventually replace the old `calendar.html` student reserve flow (keep the calendar until Chris verifies the store is better).

---

## 1. Files & architecture

| File | Role |
|------|------|
| `reserve.html` | The whole storefront: markup + one inline `<script>` app. No build step. |
| `css/store.css` | The only stylesheet. Bump the `?v=NN` query in `reserve.html` on every CSS change to bust cache. Currently **v42**. |
| `pvhs-dashboard/server.py` | The backend (Render, `command.creativesilva.com`). The **source of truth** for inventory, availability, eligibility, reservations. Separate repo, auto-deploys from `main` (~60-90s). |

The store is a static page that calls the live backend. Deploy = push `main`, GitHub Pages serves in ~60-180s. Always confirm live on the public URL before telling Chris it's done.

**Backend data the store uses** (`GET /api/camera/calendar`, public, sanitized, CORS `*`): `cameras`, `checkouts[]` (camera reservations, no PII), `oos`, `no_card`, `equipment[]` (gear reservations), `equipment_oos`, `equipment_units{id:{type,label,pool,kit}}`, `equipment_types`, `pools`, `equipment_pools`, `blackouts`. Each reservation record carries `{item/camera, out, due, returned, status, period}`. `period` is the reserving student's class period only (a group, not a person): it is the ONE identifying-adjacent field allowed in the public feed, used by the day-detail panel. Still NO name, student ID, or phone, ever.

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
3. **Browse**: Popular Rentals is the home view; category nav (Camera Kits / Lenses / Lighting / Accessories); or the **Calendar View** accordion (a month with per-day free-camera counts). Tapping a day opens a **day-detail panel** (to the right of the calendar on desktop, stacked below on phone). The panel leads with **Available to reserve** (every item with a free unit that day, scoped to what the student can access, shown as clickable `N free` rows that open that item's detail/unit-picker for that day), then **Reserved this day** (each reserved camera + gear with a Booked/Out tag and the reserving student's **class period**, a group, never a name). On desktop the panel's height is JS-capped to the calendar's height (`matchMedia('(min-width:760px)')`), so a long list fills top-to-bottom then scrolls; on phone it stacks and the body caps at 62vh. Browsing a day needs no sign-in; adding from a day applies the usual sign-in/hold/time gates. **Reserve for this day** (button) runs the full guided flow. Tapping the same day closes the panel; changing months clears it. See §12.
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

The account chip opens a **My Account** sheet: name, period/course/teacher, student number, your cell, parent/guardian name and cell, then a **My reservations** section, plus **Edit my info** (prefilled form → `/api/camera/student_update`) and **Log out**. Opens for any signed-in student (hold or not).

**My reservations** (`loadMyReservations`/`resvSectionHtml`): on open, `POST /api/camera/my_reservations {student_id}` returns the student's own bookings grouped (camera + its linked gear = one reservation), split into `active` + `history`. Each active card shows the dates, the items, a status pill (Reserved / Waiting for OK / Picked up), and **Cancel reservation** when still `reserved` (an inline Yes/Keep confirm → `POST /api/camera/cancel {student_id, id}`; the backend refuses once picked up or returned, and refuses a reservation that is not this student's). Past (returned) bookings sit in a collapsed "Past reservations" accordion. Canceling frees the gear (`loadCal()` refreshes).

**Modify** (the other button on each active card): `modifyReservation(resv)` loads the reservation back into the bag as an edit session (`modifyMode`/`editingResvId`; `my_reservations` returns each item's `unit` id so the bag is rebuilt, dates set from the reservation). In modify mode the bag shows a banner, the dates (no times needed, the store always returns next-school-day), a "Change the day" (full planner), Add equipment / Remove, and a **Save changes** button. Adding gear skips the planner (dates already fixed). **Save changes** = `saveModify` → `POST /api/camera/modify {student_id, id, out, due, units:[{kind,unit}]}` (the complete desired set). The backend re-validates availability EXCLUDING the reservation's own records (via `exclude_ids` on `_camera_busy`/`_equipment_unit_busy`, so keeping a unit while changing the date does not self-conflict) and replaces the group atomically. Closing the bag mid-edit abandons the modify (restores it). Ownership + not-picked-up are enforced server-side.

---

## 8. Client state

Session storage: `pv_user` (the signed-in student), `pv_bag` (model names), `pv_req` (name→'photo2' for requested locked items), `pv_pick` (name→chosen unit). `CAL` holds the latest calendar fetch.

---

## 9. Hard rules

- Student-facing assets on `www.creativesilva.com` only. No em dashes. No "shoot/shot/screenshot". 5th-grade reading level.
- Mobile-first: the store is built for student iPads and phones. **Every dialog caps to the live viewport (`100dvh`) and scrolls its body** so the action button is always reachable on a short phone screen; verify at a short height, not just the emulator (which scales height and hides overflow).
- **Equipment photos are NEVER cropped.** The item-detail image banner (`.detail-img`) hugs the photo (no fixed aspect box): the image is fully contained (`object-fit:contain`, `max-width:100%`, `max-height:min(230px,34vh)`) and the container height follows the image plus padding. On a short window the photo shrinks and the card scrolls (`.sheet-bd`), it never clips. Do NOT reintroduce a fixed `aspect-ratio` + `object-fit:cover`/oversized image on the detail banner (that was the old clip bug).
- **Background scroll lock:** while any dialog is open the page behind does not scroll. `syncScrollLock()` (in `open()`/`close()`) pins `<body>` with `position:fixed` at `top:-scrollY` under `html.modal-lock` and restores the scroll position on close. Only the card body scrolls, and only when too tall.
- The reservation is a **soft gate**: client checks + server-validated override codes. Teacher override code (both gear-unlock and missing-work): **322331** (repo default; set a Render env var for a private code). Keep availability math matching the backend.

---

## 10. Decisions log (dated, newest first)

- **2026-10-23**: Added two Accessories items. **Bluetooth Remote** (Canon BR-E1): new backend `bluetooth` type (4 units, shared Photo pool, NOT Photo-2-only, NOT Digital Arts); image `assets/images/equipment/bluetooth-v1.png` (pulled from Drive); store CATS/EQTYPE/SPECS/modelOfType. Available to Photo 1 + Photo 2, locked for Mankin. **iPad Stylus**: the backend already had `apple_pencil` (Mankin pool, 38 units) but it was NOT in the store; added it to CATS (`da:true, tag:'Digital Arts'`, image `ipad-stylus-v2.png`) so Mankin students can reserve it and Photo students see it locked ("Digital Arts only"). No css change (still v40).
- **2026-10-23**: Hamburger quick-nav menu (css v42). Top-right `#navBtn` (animates to an X) opens `#navMenu`: Browse (Popular Rentals + the 4 categories + Calendar View), You (My Account, Equipment Bag, How it works), and Text us 805-631-0001. Closes on item pick, outside click, or Escape. An alternate to the category bar for students who prefer a dropdown.
- **STAGED (Chris 2026-10-23, next up)**: a catch-all **Digital Media Lab & Equipment Agreement** (synthesize the 3 Drive docs: Photography 1/2 + Digital Arts; cover lab + rentals + Chris's revoke terms: missing work uses the built-in `MISSING_LIMIT`, plus participation/behavior/mistreating gear/late returns/missing kit pieces/broken parts; privilege revocable) as a CARD that opens the full agreement (EN + ES). **Gate = TEACHER-MARKED "on file" (not in-app sign); for NOW default EVERY student to signed+returned so no one is blocked; the teacher mark/revoke UI comes later.** Also staged: a UX audit for redundant steps.
- **2026-10-23**: My Account reservations can now be MODIFIED, not just canceled (css v41, server.py commits d176df3 + 32f4dc3). New public `/api/camera/modify` replaces a reservation's group atomically after re-validating availability excluding its own records; the frontend reloads the reservation into the bag as an edit session (Change the day / Add / Remove / Save changes). See §7. (Bug caught in testing: `_equipment_unit_busy` was called with `exclude_ids` but its signature missed the param -> 502; fixed in 32f4dc3.)
- **2026-10-23**: My Account now shows the student's own reservations with Cancel (css v40, server.py commit 808b628). New PUBLIC student endpoints `/api/camera/my_reservations` (grouped active + history) and `/api/camera/cancel` (own, pre-pickup, ownership-verified). Inline Yes/Keep confirm; canceling frees the gear. No in-place date/item edit yet (cancel + re-reserve). Verified end-to-end against the live backend incl. the ownership guard.
- **2026-10-23**: Fixed a fully-booked item being addable (css v39). A product card's "Add to bag" button was always active even at 0 free, so `doAddToBag` pushed the item to the bag with NO unit (it showed in the bag with no unit chip, then failed at reserve). Now `cardHtml` renders a DISABLED muted "None free for your dates" button when `stockFor(it).free<=0` (matching the item detail + the new `.btn:disabled` style), and `addToBag` has a defensive guard: if `freeUnitsFor(it)` is empty it toasts "<item> is not free for your dates." and does not add. (`submitReservation` already rejected no-unit items; this blocks them at add time.) The zoom lenses really were booked Oct 23-26 by a Period 5 + Period 6 student.
- **2026-10-22**: Restored the how-it-works step markers to Chris's right-pointing TRIANGLE cards (css v38). When moving the strip into the hero (v37) I had swapped them for plain square badges, which Chris did not ask for. The hero strip now uses the original `.hiw-step` cards (`.hiw-num` teal `clip-path:polygon(0 0,66% 0,100% 50%,66% 100%,0 100%)` arrow + `.hiw-body` title/desc), kept over the bottom of the header image. LESSON: do not restyle Chris's existing design elements when the task was only to relocate them.
- **2026-10-22**: Calendar-pick reservations skip the day picker. Reserving from the calendar day panel (tap a day, then an available item) already fixes the checkout day, so the planner now opens at the PICKUP-time step, not the Checkout-day step. Implemented by threading `fromCalDay` through `openDetail(name, fromBag, fromCalDay)` -> `addToBag(name, skipDay)` -> `openPlan(skipDay?2:1)` (the day is still set by `calDayPick`, and the planner's Back button + the bag's "Change dates" both reopen the day picker so the student can still change it). Normal product-card adds are unchanged (still open at the Checkout-day picker). JS only, no css bump.
- **2026-10-22**: Hero reworked (css v37). (1) All three date boxes carry a permanent outline in their own accent (Checkout green, Return orange, Days teal-bright), not just Checkout. (2) Hero image dimmed ~25% more via a flat `rgba(10,13,13,.25)` layer in the `.store-hero` background (on top of the existing `::before` scrim). (3) The "How it works" accordion below the hero is REMOVED; its 5 steps now live in a `.hero-hiw` strip across the BOTTOM of the hero image (`.store-hero` is a flex column, strip `margin-top:auto`; `.hhiw-*` compact step = teal number badge + title + one short line; `auto-fit minmax(150px)` so 5-across desktop, 2-up phone). `#howitworks` id moved to the strip; the accordion-opening JS was deleted (footer link scrolls there natively). Kept `.hiw-sum`/`.hiw-chev` (shared by the Specs + Calendar accordions).
- **2026-10-22**: Item-detail specs are a collapsed accordion (css v36). `detailContentHtml` wraps the spec table in `<details class="spec-acc">` (closed by default, "Specs" summary + chevron, matches the `.hiw-sum` pattern), so the card stays compact and the unit picker + Add to bag show without scrolling; tap to expand. Covers all three detail surfaces (modal, in-place picker, bag). Per the LOCKED accordions-default-closed rule.
- **2026-10-22**: Day panel upgraded (css v35). It now leads with an **Available to reserve** list (clickable `N free` rows per rentable item the student can access; a tap opens that item's detail/unit-picker for the selected day via `calDayPick`), above **Reserved this day**. On desktop the panel height is JS-capped to the calendar height (keyed off `matchMedia('(min-width:760px)')`, NOT `innerWidth`, which is unreliable under the preview emulator) so a long list fills top-to-bottom then scrolls; phone body caps at 62vh.
- **2026-10-22**: Item-detail image never clips (css v34). The detail banner (`.detail-img`) used a fixed `aspect-ratio:16/10` box; a cached older build cropped the top of the flash photo. Rebuilt so the banner hugs the photo (contain, `max-height:min(230px,34vh)`, height follows the image); short windows shrink the photo and scroll the card instead of clipping. See §9.
- **2026-10-22**: Calendar day-detail panel (§12): tap a day to see every camera + gear reserved that day, grouped Cameras / Gear, Booked/Out tag + class period (group only, never a name). Panel is right of the calendar on desktop, stacked on phone; calendar now fills the wrap and keeps large cells beside it. Browsing a day needs no sign-in; "Reserve for this day" (in the panel) does. Backend: added `period` to the sanitized `/api/camera/calendar` records (the one identifying-adjacent field allowed; still no name/ID/phone). Teacher-portal version of this view is DEFERRED until the student store is done.
- **2026-10-22**: Availability color framework: GREEN all free / YELLOW some reserved / RED none (was a buggy "<=2 = yellow" scarcity rule). Desktop calendar accordion enlarged (bigger cells). Background scroll lock behind dialogs. SmallRig renamed to "SmallRig RGB LED Panel", 4 units, Magic Arm attached to the panel (not a phone mount). This framework doc created.
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
