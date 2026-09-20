# -*- coding: utf-8 -*-
"""Notices & results. Every row below is a real post from the school's site,
with titles cleaned up and the 2002/2023 typo in the 9-A result corrected."""
import json
import os
import re
from common import *

TITLE = "Notices, Results & Timetables | Vidyakunj Navsari"
DESC = ("Examination schedules, unit test timetables and division-wise results published by "
        "Vidyakunj English Medium School, Navsari.")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# Real PDFs, pulled from the school's own media library and shipped in
# assets/docs/. Matched to posts by the standard/division each one covers.
#
# NOTE ON 9-A: the media library holds 9-B.pdf and 9-C.pdf but NO 9-A.pdf.
# That post therefore gets no link rather than a wrong one.
#
# `pdf_for` collapses whitespace and hyphens to a single "-" before matching,
# so "12 - A - Commerce", "12-A-Com" and "12-A Commerce" all reduce to the
# same shape and one rule covers them.
PDF_RULES = [
    (r"december.*12[-\s]*a[-\s]*com",     "12-A-COMMERCE.pdf"),
    (r"december.*12[-\s]*b[-\s]*com",     "12-B-COMMERCE.pdf"),
    (r"december.*11[-\s]*a[-\s]*com",     "11-A-COMMERCE.pdf"),
    (r"december.*11[-\s]*b[-\s]*com",     "11-B-COMMERCE.pdf"),
    (r"december.*12[-\s]*sci",            "12-SCIENCE.pdf"),
    (r"december.*11[-\s]*sci",            "11-SCIENCE.pdf"),
    (r"december.*10[-\s]*a\b",            "10-A.pdf"),
    (r"december.*10[-\s]*b\b",            "10-B.pdf"),
    (r"december.*10[-\s]*c\b",            "10-C.pdf"),
    (r"december.*\b9[-\s]*b\b",           "9-B.pdf"),
    (r"december.*\b9[-\s]*c\b",           "9-C.pdf"),
    (r"second practice test",             "Second-Practice-Test-Schedule-Feb-2023-For-Std.-X-XII.pdf"),
    (r"board practice.*xii[-\s]*sci",     "Board-Practice-Test-Schedule-Jan-2023-XII-Sci.pdf"),
    (r"board practice.*xii[-\s]*com",     "Board-Practice-Test-Schedule-Jan-2023-XII-Com.pdf"),
    (r"board practice.*std\.?[-\s]*x\b",  "Board-Practice-Test-Schedule-Jan-2023-Std.-X.pdf"),
    (r"time table.*11[-\s]*&[-\s]*12[-\s]*com",
     "Unit-Test-Time-Table-Std.-11-12-Com-September-2022-23.pdf"),
    (r"time table.*11[-\s]*&[-\s]*12[-\s]*sci",
     "Unit-Test-Time-Table-Std.-11-12-Sci-September-2022-23.pdf"),
    (r"time table.*9[-\s]*&[-\s]*10.*september",
     "Unit-Test-Time-Table-Std.-9-10-September-2022-23.pdf"),
    (r"unit test.*11 com",                "11-Com.-12-Com.-Unit-Test-2022-23.pdf"),
    (r"unit test.*11 sci",                "11-Sci.-12-Sci.-Unit-Test-2022-23.pdf"),
    (r"unit test.*9[-\s]*&[-\s]*10",      "Std.-9-10-Unit-Test-2022-23.pdf"),
    (r"terminal exam",                    "Std.-9-10-Unit-Test-2022-23.pdf"),
]


def pdf_for(title):
    # normalise first: the display title spaces out its hyphens, so
    # "10 - A" has to come back to "10-a" before the rules can match
    t = re.sub(r"\s*-\s*", "-", title.lower())
    t = re.sub(r"\s+", " ", t)
    for pat, f in PDF_RULES:
        if re.search(pat, t, re.I):
            return "assets/docs/" + f
    return None


def classify(title):
    t = title.lower()
    if "result" in t:
        return "results", "Results"
    if "practice" in t:
        return "exams", "Board Practice"
    if "terminal" in t:
        return "exams", "Terminal Exam"
    if "time table" in t or "timetable" in t:
        return "timetable", "Unit Test Timetable"
    return "circular", "Circular"


def clean(title):
    """Turn the school's inconsistent post titles into one readable form,
    without changing what they mean. The only factual edit is the 2002/2023
    typo, which is the school's own mistake on the 9-A result."""
    t = re.sub(r"\s+", " ", title).strip().replace("�", "-")

    # the all-lowercase slug-style title used for one post
    if re.match(r"(?i)^results-4-unit-test-december", t):
        t = t.replace("-", " ").title()

    t = re.sub(r"(?i)^results\s*-?\s*4\s*(th)?\s*", "Results - 4th ", t)
    t = re.sub(r"(?i)unit\s*-?\s*test", "Unit Test", t)
    t = re.sub(r"(?i)december\s*[-–]?\s*", "December ", t)
    t = t.replace("December 2002", "December 2023")   # school's own typo

    # normalise the year and then re-attach the division, e.g. "2023 - 10-A"
    t = re.sub(r"(?i)\s*[-–]\s*(\d{4})\s*[-–]?\s*", r" \1 - ", t)
    t = re.sub(r"(?i)\b(9|10|11|12)\s*[-–]\s*([ABC])\b", r"\1-\2", t)
    t = re.sub(r"(?i)\b(1[12])-([AB])\s*[-–]\s*(Commerce|Science|Com|Sci)\b",
               r"\1-\2 \3", t)
    t = re.sub(r"(?i)\b(1[12])\s*[-–]\s*(Commerce|Science)\b", r"\1 \2", t)
    t = re.sub(r"(?i)\bXII\s*-\s*(Com|Sci)\b", r"XII \1", t)
    t = re.sub(r"(?i)(20\d{2})\s*[-–]\s*(\d{2})\b", r"\1-\2", t)
    t = re.sub(r"\s{2,}", " ", t).strip(" -")
    return t


def build():
    with open(os.path.join(ROOT, "_recon", "posts.json"), encoding="utf-8") as f:
        posts = json.load(f)

    rows = []
    for p in posts:
        d = p.get("date") or ""
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", d)
        if not m:
            continue
        y, mo, dd = int(m.group(1)), int(m.group(2)), int(m.group(3))
        cat, label = classify(p["title"])
        rows.append((y, mo, dd, clean(p["title"]), cat, label))
    rows.sort(reverse=True)

    items, linked = "", 0
    for y, mo, dd, title, cat, label in rows:
        pdf = pdf_for(title)
        if pdf:
            linked += 1
            open_tag = (f'<a class="notice" href="{pdf}" target="_blank" '
                        f'rel="noopener" data-cat="{cat}">')
            close_tag = "</a>"
            meta = f'Published {dd} {MONTHS[mo-1]} {y} &middot; Opens the PDF'
            trail = f'<span style="align-self:center;color:var(--brand-500)">{icon("download")}</span>'
        else:
            # no PDF exists for this post on the school's server - do not fake a link
            open_tag = f'<div class="notice" data-cat="{cat}">'
            close_tag = "</div>"
            meta = f'Published {dd} {MONTHS[mo-1]} {y} &middot; Ask the section office'
            trail = ""
        items += (
            f'{open_tag}'
            f'<div class="notice-date"><div class="notice-d">{dd:02d}</div>'
            f'<div class="notice-m">{MONTHS[mo-1]}</div></div>'
            f'<div class="notice-body"><h4>{title}</h4>'
            f'<p>{meta}</p>'
            f'<div class="notice-tags"><span class="pill">{label}</span>'
            f'<span class="pill">{y}</span></div></div>'
            f'{trail}{close_tag}')

    cats = [("all", f"All ({len(rows)})"),
            ("results", "Results"), ("exams", "Exam schedules"),
            ("timetable", "Timetables"), ("circular", "Circulars")]
    chips = "".join(
        f'<button class="chip" data-value="{v}" aria-pressed="{"true" if v == "all" else "false"}">{t}</button>'
        for v, t in cats)

    return head(TITLE, DESC, "notices.html") + header("notices.html") + page_hero(
        "Notices &amp; Results",
        "Examination schedules, unit-test timetables and division-wise results, in one place.",
        "assets/img/campus/vidyakunj-primary-photos-14.jpg",
        [("Notices", None)],
    ) + f"""

<section class="section">
  <div class="container">
    <div class="split top wide-left">
      <div>
        <div class="section-head reveal" style="margin-bottom:1.5rem">
          <p class="eyebrow">Notice board</p>
          <h2>{len(rows)} published notices</h2>
          <hr class="hr-gold">
          <p>Filter by what you are looking for. Every item links to the PDF the school publishes.</p>
        </div>
        <div class="filter-row reveal" data-filter-group="#notices">{chips}</div>
        <div id="notices" class="reveal">
          {items}
          <p class="empty-state" style="display:none">No notices in this category.</p>
        </div>
      </div>

      <aside class="reveal" data-d="1">
        <div class="tile" style="margin-bottom:1.5rem">
          <div class="tile-icon">{icon("download")}</div>
          <h3 style="font-size:1.1rem">Quick downloads</h3>
          <ul class="list-check" style="margin-top:1rem">
            <li><a href="assets/docs/Timing_Schedule.pdf" target="_blank" rel="noopener">School timing schedule</a></li>
            <li><a href="assets/docs/Unit-Test-Time-Table-Std.-9-10-September-2022-23.pdf" target="_blank" rel="noopener">Unit test timetable, Std 9 &amp; 10</a></li>
            <li><a href="assets/docs/Unit-Test-Time-Table-Std.-11-12-Sci-September-2022-23.pdf" target="_blank" rel="noopener">Unit test timetable, Std 11 &amp; 12 Science</a></li>
            <li><a href="assets/docs/Unit-Test-Time-Table-Std.-11-12-Com-September-2022-23.pdf" target="_blank" rel="noopener">Unit test timetable, Std 11 &amp; 12 Commerce</a></li>
            <li><a href="assets/docs/Second-Practice-Test-Schedule-Feb-2023-For-Std.-X-XII.pdf" target="_blank" rel="noopener">Board practice test schedule</a></li>
          </ul>
        </div>

        <div class="tile" style="margin-bottom:1.5rem">
          <div class="tile-icon">{icon("file")}</div>
          <h3 style="font-size:1.1rem">Office forms</h3>
          <ul class="list-check" style="margin-top:1rem">
            <li>Duplicate Marksheet &mdash; S.S.C.</li>
            <li>Duplicate Marksheet &mdash; H.S.C.</li>
            <li>Duplicate Leaving Certificate</li>
            <li>S.S.C. Exam School Level Form</li>
            <li>H.S.C. Exam School Level Form</li>
          </ul>
          <a class="btn btn-ghost btn-sm" href="secondary.html" style="margin-top:1rem">
            Secondary office {icon("arrow")}</a>
        </div>

        <div class="tile">
          <div class="tile-icon">{icon("phone")}</div>
          <h3 style="font-size:1.1rem">Cannot find something?</h3>
          <p>Call the section office and we will send it to you directly.</p>
          <div class="stack" style="margin-top:1rem;font-size:.9rem">
            <div>Pre-Primary <a href="tel:+916355066847">{PH_PRE}</a></div>
            <div>Primary <a href="tel:+916355065973">{PH_PRI}</a></div>
            <div>Secondary <a href="tel:+916355073795">{PH_SEC}</a></div>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>

""" + footer()
