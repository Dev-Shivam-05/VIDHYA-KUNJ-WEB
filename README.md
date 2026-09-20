# Vidyakunj Navsari — Website Audit & Redesign

Two deliverables, built 20 September 2026 from a full crawl of **vidyakunjnavsari.edu.in**.

| | |
|---|---|
| **[AUDIT.md](AUDIT.md)** | What is wrong with the live site, ranked by urgency, with every finding traceable to a URL |
| **[site/](site/)** | A complete 10-page redesign built from that audit. Open `site/index.html` — no build step, no server, no dependencies |
| [site/README.md](site/README.md) | What changed, the technology choices, and what still needs the school's input |

---

## The headline

The live site is running the **Eastwood** WordPress template kit with the demo content never removed. Today it publishes, on every page:

- a **US phone number** — `(+1) 767-123-786`
- an email that decodes to **`hello@example.com`**
- a footer advertising **Colchester, Southend and Loughton campuses** (UK locations from the theme demo)
- six footer links pointing at **the theme vendor's own demo site**

**31 of 31 footer links are dead or off-site. 3 of 9 nav items go to `#`.** The newest published notice is from **January 2024**.

Meanwhile the school's genuinely strong material — a 1969 founding story with named founders, 95 staff including teachers who joined in 1991, published fees, real facility numbers — is buried or unstyled.

---

## What the crawl covered

| | |
|---|---|
| Pages fetched and parsed | 48 (24 pages + 24 posts) |
| Media library enumerated | 143 items via the open WP REST API |
| Images downloaded | 96 genuine school images |
| Notice PDFs downloaded | 22, all shipped and linked |
| Theme stock identified and excluded | 50 files |
| Real data recovered | 2,500+ students · 85+ teachers · 1,590 sq m land · 3,606 sq m built · 95 staff with qualifications and joining dates · full fee table · 22-member trust |

Every one of those figures was already on the school's site. The homepage counters held the four statistics; they just animate from zero and nobody reads them.

---

## The rebuild, verified

Checked in real Chrome at 1440px and 390px across all 10 pages:

```
counters             2,500 | 85 | 1,590 | 3,606     animate correctly
images               21/21 loaded, 0 broken
secondary tabs       6 tabs, switching works
faculty              95 staff rows rendered
notices filter       24 -> 12 on "Results"
gallery lightbox     opens, arrow keys advance, Escape closes
mobile drawer        opens, Escape closes
contact form         blocks empty submit (3 fields), accepts valid
horizontal overflow  none, at either width
console errors       none
broken links         none  (653 links, 141 images, 22 PDFs, all resolve)
placeholder leaks    none  (no example.com, no +1, no Eastwood, no Colchester)
```

Screenshots of every page at both widths are in [`_shots/`](_shots/).

---

## Repo layout

```
AUDIT.md                     the audit
README.md                    this file
site/                        the deliverable — open index.html
_build/                      page generators (python _build/build.py to re-render)
  common.py                  shared header, footer, nav, icons, verified facts
  p_*.py                     one module per page
  build.py                   renders all 10
  shoot.js                   screenshots + error/overflow checks
  verify.js                  functional checks (counters, tabs, lightbox, forms)
  diag.js                    finds elements causing horizontal overflow
_recon/                      raw crawl: HTML, extracted text, staff.json, posts.json
_shots/                      20 screenshots (10 pages × desktop/mobile)
Vidya_Kunj_School_Navsari_Management_Intelligence_Report.md
                             the earlier strategy document, analysed separately
```

`_build/`, `_recon/` and `_shots/` are working artifacts. Only `site/` needs to ship.

---

## Note on the earlier strategy document

The management intelligence report in this folder listed "Exact built-up area, Number of classrooms, Total student capacity" as *"Information Requiring Verification."*

All three were published on the school's own homepage the entire time. The report's central recommendation — a tagline reading *"50 years of trust"* — also undercounts the school by seven years; 1969 to 2026 is **57**.
