# Vidyakunj Navsari — Website Redesign

A complete 10-page rebuild of vidyakunjnavsari.edu.in, built from the findings in [`../AUDIT.md`](../AUDIT.md).

## How to view it

**Live:** https://vidyakunj-navsari.vercel.app
(mirror: https://dev-shivam-05.github.io/VIDHYA-KUNJ-WEB/)

Locally: no build step, no server, no dependencies — open `index.html` in any browser.
To exercise the Google Maps embed on the contact page, serve it over HTTP instead:

```
python -m http.server 8000
```
then open `http://localhost:8000`.

## Pages

| File | What it covers |
|---|---|
| `index.html` | Home — hero, the four real statistics, three sections, founding story, facilities, track record, notices, gallery |
| `about.html` | Full founding history with named founders and donors, 1968→today timeline, achievements, both Head Teachers' messages, all 22 management and trust members |
| `pre-primary.html` | Play School to Sr. KG, the four real facilities, Mrs. Ragini Desai's message |
| `primary.html` | Standards I–VIII, subjects, Mrs. Sapna Singh's message, activities gallery |
| `secondary.html` | Standards IX–XII, 12 divisions, Science/Commerce streams, tabbed question bank for all 6 standard-streams, assessment structure, office services |
| `faculty.html` | All 95 published staff in three tabbed tables, plus a longest-serving teachers panel computed from dates of joining |
| `admissions.html` | 4-step process, required documents, the published fee table, full fee policy, 10 rules as an accordion, enquiry form |
| `gallery.html` | The 8 event albums, plus every recovered school photograph with category filtering and a keyboard-navigable lightbox |
| `notices.html` | All 24 published notices, sorted newest-first, filterable by Results / Exams / Timetables / Circulars. 23 link to the school's real PDF (all 22 are shipped in `assets/docs/`) |
| `contact.html` | Section-wise contact cards, address, map, Friday meeting window, contact form |

## Coverage — every original URL accounted for

| Original page | Handled in rebuild |
|---|---|
| `/` | index.html |
| `/about-us/` | about.html — expanded with timeline + named founders |
| `/management/` | about.html#management — all 22 members |
| `/headteacher-message/` | about.html#messages + primary.html |
| `/pre-primary-head-teacher/` | about.html#messages + pre-primary.html |
| `/pre-primary-section/` | pre-primary.html |
| `/pre-primary-teachers/` | faculty.html (Pre-Primary tab, 26 rows) |
| `/pre-primary-gallery/` | gallery.html |
| `/pre-primary-video/` | DROPPED — page contains no video (see AUDIT D) |
| `/primary-section/` | primary.html |
| `/primary-about-us/` | primary.html |
| `/primary-teachers/` | faculty.html (Primary tab, 53 rows) |
| `/primary-gallery/` | gallery.html |
| `/primary-admission/` | admissions.html |
| `/primary-contact-us/` | contact.html |
| `/primary-video/` | DROPPED — page contains no video (see AUDIT D) |
| `/secondary/` | secondary.html |
| `/standard-9-10/` | MERGED into secondary.html — was a byte-identical duplicate |
| `/secondary-staff/` | faculty.html (Secondary tab, 16 rows) |
| `/rules-and-regulation/` | admissions.html#rules |
| `/infrastructure/` | folded into pre-primary + primary facilities (page had 1 line of content) |
| `/events/` | gallery.html — 8 albums |
| `/contact-us/` | contact.html — plus a map embed the original lacks |
| `/sample-page/` | DROPPED — WordPress default boilerplate |
| `24 result/exam posts` | notices.html — all 24, filterable |

Nothing was silently dropped: the three omissions are stated above with the reason.

## Structure

```
site/
├── index.html … contact.html      10 pages
├── assets/
│   ├── css/styles.css             one stylesheet, ~20 token-driven sections
│   ├── js/main.js                 one file, no dependencies
│   └── img/
│       ├── brand/   11            logos and favicons
│       ├── banner/   6            hero slides
│       ├── people/   8            management and head teacher portraits
│       ├── campus/  60            campus and activity photographs
│       ├── gallery/  8            event album covers
│       ├── icons/    3            96 image files, 13 MB total
│       └── docs/    22            the school's own notice and result PDFs
└── README.md
```

**Every link in this build resolves.** 653 links, 141 images, 22 PDFs — validated, none dead. The one notice deliberately left without a link is the Std 9-A result, because the school's media library has `9-B.pdf` and `9-C.pdf` but no `9-A.pdf`. Pointing it at another division's file would have been worse than leaving it.

Pages are generated from `../_build/*.py` — edit a page module and run `python _build/build.py` to re-render. The generated HTML is plain and standalone; the generator is a convenience, not a runtime requirement.

## Technology, and why

**No framework.** One hand-written stylesheet and one vanilla JS file. Bootstrap or Tailwind would have added a CDN dependency and a class-soup layer for a 10-page brochure site that needs neither. This way the whole site is three files plus images, it renders instantly, it works offline, and the school's next developer can read all of it.

- **CSS custom properties** for every colour, space, radius, shadow and type step — rebranding is a change to `:root`.
- **Brand colour `#303078`** was sampled from the school's own logo file, not chosen. A warm gold `#D4A72C` pairs with it for the heritage accent. Pre-Primary teal and Primary green mark the sections.
- **Fonts:** Fraunces for display, Inter for text, both from Google Fonts with system fallbacks.
- **Fluid type and space** via `clamp()` — no breakpoint jumps in the type scale.

## Accessibility and behaviour

- Skip link, landmark elements, and `aria-current` on the active nav item
- Tabs implement the ARIA tabs pattern with arrow / Home / End key support
- Lightbox is a labelled modal: Escape closes, arrow keys navigate, focus moves into it on open and returns on close
- Mobile drawer traps nothing it shouldn't, closes on Escape, scrim click and link click, and restores focus
- Every interactive element has a visible `:focus-visible` ring
- `prefers-reduced-motion` disables the reveal animations, the hero crossfade and the counter count-up
- Verified: 0 console errors, 0 broken images, 0 horizontal overflow at 1440px and 390px across all 10 pages

## What changed from the live site

**Removed** — every item was live before this rebuild:

- `Tel: (+1) 767-123-786` (a US number) and `hello@example.com`
- `Mon → Sat : 6am-10pm`
- `Undergraduate` / `Postgraduate` navigation
- The footer's "Colchester Campus / Southend Campus / Loughton Campus", "Eastwood living", "Eastwood Sport", the research columns and the study columns
- Six footer links pointing at `kit.detheme.com/eastwood/template-kit/`
- 25 further footer links pointing at `#`, and the dead `Awards` / `Vidyasarathi` / `Special Corner` nav items
- All 50 Eastwood theme demo stock photographs
- The default WordPress `sample-page`

**Fixed:**

- `Atulbahi` → Atulbhai · `Treasure` → Treasurer · `ADDMISSIONS` → Admissions · `Achivements` → Achievements · `sqare` → square · `experiment` → experience
- The `Results-4 Unit Test December-2002-9-A` post, which should read 2023
- The `Sq mtTotal Area of Land` counter label, which ran two strings together
- Pre-Primary pages that displayed the Secondary phone number
- `/secondary/` and `/standard-9-10/` which were byte-identical duplicates — now one page

**Promoted** — real material that existed but was buried:

- The 1968–69 founding story, with founders and donors named, moved onto the homepage and given a full timeline on the About page
- The four real figures (2,500+ students, 85+ teachers, 1,590 sq m land, 3,606 sq m built) taken out of the theme's counter markup and made a headline band
- Staff longevity — teachers who joined in 1991, 1993, 1998 and 1999 and are still here — computed from the published dates of joining and given its own section
- The published fee structure, presented as a clear table rather than a text block
- 96 genuine school photographs, all used; none of the theme's stock

## Before this goes live

The images are the school's originals, straight off their server, and they are heavy — roughly **13 MB across 96 files**, with the campus folder alone at 9.7 MB. Several are 1–2 MB JPEGs being displayed at a few hundred pixels wide. For a demo on a laptop this is fine; on a parent's phone over mobile data it is not.

One pass with `cwebp` or `squoosh` at 1600px max width would cut this to well under 2 MB with no visible difference. That is a build step, not a redesign, and is deliberately left out so the deliverable contains the school's files unmodified.

Also worth doing before launch: `<link rel="canonical">` per page, an `og:image`, a `sitemap.xml`, and `width`/`height` attributes on the content images to stop layout shift.

## Deliberately left as decisions for the school

These need information only the school holds, so the rebuild does not invent them:

1. **A real email address.** Every `mailto` is currently omitted rather than guessed.
2. **Social media URLs.** The footer icons point to the contact page until real profiles exist.
3. **Form delivery.** Both forms validate on the client and show a success state. Wiring them to an inbox or a WhatsApp Business number is a one-line change once an endpoint is chosen.
4. **1969 vs 1970.** The live site says both. The rebuild uses "Established 1969 · Registered 1970", which is what the About Us page states — confirm before printing.
5. **Land area.** About Us says ~1.75 lakh sq ft; the homepage counter says 1,590 sq m. These differ by roughly 10×. Both are shown in their original context, unreconciled, pending the school's answer.
6. **Fees beyond Std III–VIII.** Only III–VIII are published; the rest say to ask the section office.
7. **Current results.** The newest published result is from January 2024. The notices page shows what exists.
