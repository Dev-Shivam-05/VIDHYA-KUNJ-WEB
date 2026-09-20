# vidyakunjnavsari.edu.in — Full Site Audit

**Audited:** 20 September 2026
**Method:** All 48 published URLs fetched and parsed, WordPress REST media library enumerated (143 items), sitemaps and robots.txt read, every image downloaded and classified.
**Platform:** WordPress + Elementor 3.27.3, "Eastwood" education template kit, All-in-One SEO 4.7.8.

---

## Verdict

The site is not broken — it is **unfinished**. The Eastwood theme demo was installed, real Vidyakunj content was dropped into some sections, and the rest of the demo was left exactly as shipped. The result is a school website that currently publishes a **US phone number**, an **`@example.com` email address**, and a footer advertising **three British university campuses**.

Everything below is verifiable on the live site today.

---

## A. Placeholder data that is live right now

These are the findings that matter most, because a parent sees them before anything else.

| # | What is live | Where | Should be |
|---|---|---|---|
| A1 | `Tel: (+1) 767-123-786` | Top bar of **every** page on the main site | A real Indian number |
| A2 | `hello@example.com` | Header email (Cloudflare-obfuscated, decodes to example.com) | A real school inbox |
| A3 | `Mon → Sat : 6am-10pm` | Top bar, every page | Actual office hours |
| A4 | `Undergraduate` / `Postgraduate` | Main navigation | This is a K-12 school |
| A5 | Footer column "Study": *Undergraduate study, Postgraduate study, Short courses and CPD, International students, Study online, Apprenticeships* | Footer, every page | Removed |
| A6 | Footer column "Life": **Eastwood living, Eastwood Sport, Colchester Campus, Southend Campus, Loughton Campus** | Footer, every page | Removed — these are UK locations from the theme demo |
| A7 | Footer column "research": *Research excellence, Research showcase, Media requests, Research institutes, Enterprise* | Footer, every page | Removed |
| A8 | Footer "Explore" links go to **`kit.detheme.com/eastwood/template-kit/`** | Footer, every page | The site sends its own visitors to the theme vendor's demo |

**A2 is the worst of these.** The address is obfuscated by Cloudflare so it *looks* like a working mailto link. Decoded, it is `hello@example.com`. Any parent who emails the school is emailing nobody.

**A6 is the most embarrassing.** The school's footer currently lists Colchester, Southend and Loughton as its campuses.

### Contradiction worth noting

The **Contact Us** page carries the real numbers —

- Pre-Primary `+91 635 506 6847`
- Primary `+91 635 506 5973`
- Secondary & Higher Secondary `+91 635 507 3795`

— while the header *on that same page* still shows `(+1) 767-123-786`. The correct data exists; it was just never propagated into the theme's header and footer.

---

## B. Broken links

**31 of 31 footer links are dead or off-site.** Not one works as intended.

- 25 footer links point to `#`
- 6 footer links point to the theme vendor's demo site
- All 4 social icons (Facebook, Twitter, LinkedIn, YouTube) point to `#` — the school has no linked social presence

**3 of 9 main nav items are dead:** `Awards`, `Vidyasarathi` and `Special Corner` all resolve to `#`. Vidyasarathi is a real thing — the Rules page references "Vidyasarathi workbooks" — but the menu item goes nowhere.

---

## C. Content staleness

| Signal | Date | Age |
|---|---|---|
| Newest notice/result post | 17 Jan 2024 | ~2 yr 8 mo |
| Auto-generated meta description (site-wide) | quotes exams from 19 Aug 2022 | ~4 yr |
| Newest uploaded PDF | 8 Apr 2025 (`Timing_Schedule.pdf`) | ~1 yr 5 mo |
| Newest media upload | 28 Mar 2026 (a competition video) | ~6 mo |

The homepage's own SEO description reads: *"News Highlights All Students Parents All 11 & 12 Science Unit Test August 19, 2022…"* — this is what Google shows searchers today.

### The category filter does nothing

The homepage News Highlights has three tabs: **All**, **Students**, **Parents**. All three render the **identical ten posts**. The filter is decorative.

---

## D. Factual errors and typos on the live site

| Where | Published | Should be |
|---|---|---|
| Post title & URL slug | `Results-4 Unit Test December-2002-9-A` | 2023, not 2002 |
| Management page | `Shri Atulbahi H. Shah` | Atulbhai |
| Management page | Designation `Treasure` | Treasurer |
| Pre-Primary nav | `ADDMISSIONS` | ADMISSIONS |
| Primary nav | `Achivements` | Achievements |
| About Us | `1.75 lakh sqare feet` | square |
| Pre-Primary / Primary | "A comprehensive curriculum ensure that students have an enriching **experiment**" | experience |
| Homepage counters | Renders as `Sq mtTotal Area of Land` | missing line break between prefix and label |
| Pre-Primary pages | Header shows `+91 635 507 3795` | that is the **Secondary** number, per Contact Us |

### Two different founding years

- **About Us:** "established in 1969 and got registered in 1970"
- **Primary Section → Important Years:** "1970 Established"

The site contradicts itself on its own founding date.

### A 10× discrepancy in land area

- **About Us:** land donated ≈ **1.75 lakh square feet** (≈ 16,258 sq m)
- **Homepage counter:** *Total Area of Land* = **1,590 sq m**

One of these is wrong by roughly a factor of ten. Note also that the homepage reports **Construction = 3,606 sq m** — larger than the stated land area, which is only possible across multiple floors.

### An unmaintained age claim

About Us says the school has served *"more than 45 years."* Founded 1969, it is **57 years** in 2026. That sentence was written around 2014 and never touched again.

### Default WordPress page still published

`/sample-page/` is live, indexed in the sitemap, and contains WordPress boilerplate.

### Duplicate content

`/secondary/` and `/standard-9-10/` are **byte-for-byte the same content**. Two URLs, one page — a straightforward SEO penalty.

### Two "Video" pages that contain no video

`/pre-primary-video/` and `/primary-video/` are both published and both in the sitemap. Across all 48 URLs on the site there are **zero `<video>` elements and zero `<iframe>` embeds** — so neither page has any video on it. Worse, both render the **Secondary section's** navigation (Duplicate Marksheet S.S.C., Board Exam Practice Test, 12-Sci…), which is the wrong menu for a Pre-Primary or Primary page.

Meanwhile `Monoacting-Competition-25-26.mp4`, uploaded **28 March 2026** and the newest content on the entire site, is **not linked from any page**. It sits orphaned in the media library while two pages named "Video" show nothing.

### A result post with no result attached

The media library holds `9-B.pdf` and `9-C.pdf` but **no `9-A.pdf`**. The post *"Results-4 Unit Test December-2002-9-A"* is published, indexed, and links to nothing a 9-A parent can open. So that post carries two defects at once: the wrong year in its title, and no attachment.

(In the rebuild, 23 of the 24 notices link to the school's real PDF. The 9-A post is deliberately left unlinked rather than pointed at another division's file.)

### No map on the Contact page

There is no `<iframe>` anywhere on the site, which means the Contact page gives an address with no embedded map and no directions link — for a school on JN Tata Road near Tighra Jakat Naka, that is a real friction point for a first-time visitor.

---

## E. Media library

143 items. Of the 120 image files, **50 are Eastwood theme demo stock photos that were never removed**, including:

- `college-life-at-columbia-university-KZ7HGNA.jpg`
- `arab-woman-student-beautiful-muslim-female-student-SL6DTPR.jpg`
- `engineering-students-working-in-the-lab-PPFAGTH.jpg`
- `Antonin-Scalia-Signature-2016021501.png`
- `eastwood-dark-1.png`, `eastwood-light.png`
- 6 × `EDUCATION-Black-**-35G4L6.png`

These are not Vidyakunj's students, Vidyakunj's staff, or Vidyakunj's campus. They sit in the library consuming hosting and are available at public URLs.

**96 images are genuinely the school's own** — campus photographs, the logo set, management portraits, and eight event albums. All 96 were recovered and are used in the rebuild.

---

## F. Technical

- **`xmlrpc.php` is exposed** — a standard brute-force and DDoS amplification target on WordPress. Should be blocked unless something specifically needs it.
- **WP REST API is fully open** — `/wp-json/wp/v2/media` returns the entire media library to anyone. Not a vulnerability by itself, but it is how this audit enumerated all 143 files, including unpublished stock.
- **Two separate header systems.** The main site header (About Us / Pre Primary / …) and the Primary sub-site header (ADMISSIONS / Headteacher Message / Leave Application / …) are different navigations with different phone numbers. The site is effectively two sites bolted together, and a visitor can end up in a section with no route back.
- **Heavy stack for a small site.** Elementor renders 1,427 references on the homepage alone, for roughly 400 words of actual content.

---

## G. What the site does have — and buries

The audit found genuinely strong material that is either hidden below dead links or presented so plainly that nobody reads it:

**The founding story.** In 1968–69, Jaycees of the Navsari Junior Chamber resolved to build an affordable English-medium school rooted in Indian culture. Around **forty members contributed ₹1,000 each**. Named founders: **Mrs. Meeraben J. Desai, Dr. Manharbhai I. Shah, Mr. Jal Baria, Mr. Bharat Gandhi**. Land donors: **Shri Ukabhai Patel** and **Shri Rambhai Patel** (~1.75 lakh sq ft on Gandevi Road); the family of **Shri Hargovan Kaka Rathod** funded the Pre-Primary and Primary buildings.

This is the single best asset the school owns and it sits in an unstyled paragraph on a page most visitors never open.

**Hard numbers, already published.** 2,500+ students · 85+ teachers · 1,590 sq m land · 3,606 sq m constructed. (These were sitting in the homepage's counter markup all along.)

**A complete staff register.** 26 Pre-Primary teachers, 53 Primary teachers, 16 Secondary staff (95 in all) — with names, qualifications and dates of joining. Several joined in **1991, 1993, 1998, 1999** and are still teaching. A school where teachers stay 30+ years is making an argument most schools cannot make, and it is currently presented as a bare HTML table.

**Real leadership.** Principal (Secondary) **Mr. Ashishkumar R. Lad**, M.Sc. B.Ed., Chemistry, joined 2006. Head Teacher (Primary) **Mrs. Sapna Singh**, M.Sc. B.Ed. Head Teacher (Pre-Primary) **Mrs. Ragini Desai**. A 22-member management committee and trustee board.

**Published fees.** Standards III–VIII: ₹10,000 + ₹9,900 = **₹19,900/year**, admission fee ₹600, no other activity charges. Publishing fees openly is a trust signal and most competitors do not.

**Concrete facilities.** 15 air-conditioned Pre-Primary classrooms with smart boards, CCTV in all classrooms, a dedicated play station, playground and school hall.

---

## H. Findings ranked by urgency

**Fix this week — reputational**
1. `hello@example.com` email (A2)
2. `(+1) 767-123-786` phone (A1)
3. Colchester / Southend / Loughton footer (A6)
4. Footer links to the theme vendor's demo site (A8)
5. `Undergraduate` / `Postgraduate` in the nav (A4)

**Fix this month — credibility**
6. 31 dead footer links, 3 dead nav items (B)
7. Delete `/sample-page/` and the 50 stock demo images (D, E)
8. Resolve the 1969-vs-1970 and 1,590-vs-1.75-lakh contradictions (D)
9. Fix the `2002` result typo, `Achivements`, `ADDMISSIONS`, `Treasure`, `Atulbahi` (D)
10. De-duplicate `/secondary/` and `/standard-9-10/` (D)
11. Either put the March 2026 Monoacting video on the two "Video" pages or unpublish them, and fix the Secondary menu showing on Pre-Primary and Primary pages (D)
12. Add a map embed to the Contact page (D)

**Fix this quarter — growth**
13. Publish 2025–26 and 2026–27 results so the newest item is not from Jan 2024 (C)
14. Write a real meta description; the current one is auto-generated from 2022 exam names (C)
15. Merge the two header systems into one navigation (F)
16. Block `xmlrpc.php` (F)
17. Lead with the founding story and the staff-retention record (G)

---

## What was rebuilt

A complete 10-page redesign is in [`site/`](site/), built from this audit. Every fact on it came from the school's own pages; nothing was invented. All 96 genuine school images are used; none of the 50 stock demo images are.

See [`site/README.md`](site/README.md) for what changed and why.
