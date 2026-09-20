# -*- coding: utf-8 -*-
"""Faculty page. Staff rows are read verbatim from the tables published on the
school's own site (primary-teachers, pre-primary-teachers, secondary-staff)."""
import json
import os
import re
from common import *

TITLE = "Our Faculty | Teachers & Staff | Vidyakunj Navsari"
DESC = ("The teachers of Vidyakunj English Medium School, Navsari - 26 Pre-Primary, 53 Primary "
        "and the Secondary staff, with qualifications and years of service.")

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "_recon", "staff.json")

POS = {
    "Head Tea.": ("Head Teacher", "pill-head"),
    "Principal": ("Principal", "pill-head"),
    "AT": ("Assistant Teacher", "pill"),
    "TT": ("Trained Teacher", "pill"),
    "Asst.Teacher": ("Assistant Teacher", "pill"),
    "Assistant Teacher": ("Assistant Teacher", "pill"),
}


def tidy(s):
    """Normalise the mojibake and stray punctuation in the source tables."""
    if not s:
        return ""
    s = s.replace("�", "'").replace("–", "-").strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"^[-'\s]+$", "", s)
    return s


def year_of(dt):
    """Pull a 4-digit year out of either dd-mm-yyyy or m/d/yyyy."""
    m = re.search(r"(19|20)\d{2}", dt or "")
    return int(m.group(0)) if m else None


def rows_of(key):
    with open(DATA, encoding="utf-8") as f:
        d = json.load(f)
    t = d[key][0]
    return [[tidy(c) for c in r] for r in t[1:]]


def service_badge(dt):
    y = year_of(dt)
    if not y:
        return ""
    n = 2026 - y
    if n >= 25:
        return f'<span class="pill pill-head">{n} yrs</span>'
    if n >= 10:
        return f'<span class="pill">{n} yrs</span>'
    return f'<span class="muted" style="font-size:.8rem">{n} yrs</span>'


def table(head_cells, body, cap):
    th = "".join(f"<th>{h}</th>" for h in head_cells)
    return (f'<div class="table-wrap"><div class="table-scroll">'
            f'<table class="data"><thead><tr>{th}</tr></thead>'
            f'<tbody>{body}</tbody></table></div></div>'
            f'<p class="table-cap">{cap}</p>')


def build():
    # ---- Pre-Primary: Sr | Name | Designation | Qualification | DOJ | Class ----
    pre = rows_of("pre-primary-teachers")
    pre_body = ""
    for r in pre:
        r = (r + [""] * 6)[:6]
        label, cls = POS.get(r[2], (r[2] or "Teacher", "pill"))
        pre_body += (f'<tr><td>{r[0]}</td><td class="t-name">{r[1]}</td>'
                     f'<td><span class="{cls}">{label}</span></td>'
                     f'<td>{r[3]}</td><td>{r[5]}</td><td>{service_badge(r[4])}</td></tr>')

    # ---- Primary: No | Name | Position | Subject | Qualification | DOJ ----
    pri = rows_of("primary-teachers")
    pri_body = ""
    for r in pri:
        r = (r + [""] * 6)[:6]
        label, cls = POS.get(r[2], (r[2] or "Teacher", "pill"))
        pri_body += (f'<tr><td>{r[0]}</td><td class="t-name">{r[1]}</td>'
                     f'<td><span class="{cls}">{label}</span></td>'
                     f'<td>{r[3]}</td><td>{r[4]}</td><td>{service_badge(r[5])}</td></tr>')

    # ---- Secondary: Sr | Name | Qualification | Subject | Designation | DOJ ----
    sec = rows_of("secondary-staff")
    sec_body = ""
    for r in sec:
        r = (r + [""] * 6)[:6]
        label, cls = POS.get(r[4], (r[4] or "Staff", "pill"))
        sec_body += (f'<tr><td>{r[0].rstrip(".")}</td><td class="t-name">{r[1].title()}</td>'
                     f'<td><span class="{cls}">{label}</span></td>'
                     f'<td>{r[3] or "&mdash;"}</td><td>{r[2]}</td>'
                     f'<td>{service_badge(r[5])}</td></tr>')

    # longest-serving, across all three tables
    veterans = []
    for r, ni, di in ((pre, 1, 4), (pri, 1, 5), (sec, 1, 5)):
        for row in r:
            row = (row + [""] * 6)[:6]
            y = year_of(row[di])
            if y:
                veterans.append((y, row[ni]))
    veterans.sort()
    n_20plus = len([v for v in veterans if 2026 - v[0] >= 20])
    vet_html = "".join(
        f'<div class="person"><div class="person-ph" aria-hidden="true">'
        f'{"".join(p[0] for p in n.replace("Mrs.", "").replace("Mr.", "").replace("Mrs ", "").replace("Miss.", "").split() if p)[:2].upper()}</div>'
        f'<h4>{n.title() if n.isupper() else n}</h4>'
        f'<div class="role">Since {y}</div>'
        f'<div class="meta">{2026 - y} years at Vidyakunj</div></div>'
        for y, n in veterans[:8])

    return head(TITLE, DESC, "faculty.html") + header("faculty.html") + page_hero(
        "Our Faculty",
        "Ninety-five teachers and staff across three sections &mdash; many of whom have "
        "taught here for more than twenty-five years.",
        "assets/img/campus/vidyakunj-primary-photos-5.jpg",
        [("Faculty", None)],
    ) + f"""

<section class="section-sm">
  <div class="container">
    <div class="stats reveal">
      <div class="stat">
        <div class="stat-num"><span data-count="{len(pre)}">0</span></div>
        <div class="stat-label">Pre-Primary Teachers</div>
        <div class="stat-sub">Play School to Sr. KG</div>
      </div>
      <div class="stat">
        <div class="stat-num"><span data-count="{len(pri)}">0</span></div>
        <div class="stat-label">Primary Teachers</div>
        <div class="stat-sub">Standards I to VIII</div>
      </div>
      <div class="stat">
        <div class="stat-num"><span data-count="{len(sec)}">0</span></div>
        <div class="stat-label">Secondary Staff</div>
        <div class="stat-sub">Standards IX to XII</div>
      </div>
      <div class="stat">
        <div class="stat-num"><span data-count="{n_20plus}">0</span></div>
        <div class="stat-label">Serving 20+ Years</div>
        <div class="stat-sub">Continuity for families</div>
      </div>
    </div>
  </div>
</section>

<!-- ============ VETERANS ============ -->
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Continuity</p>
      <h2>Teachers who have stayed</h2>
      <hr class="hr-gold">
      <p class="lead">The longest-serving members of our staff. Several joined Vidyakunj in the
         early 1990s and have taught two generations of the same Navsari families.</p>
    </div>
    <div class="grid g-4 reveal">{vet_html}</div>
  </div>
</section>

<!-- ============ TABLES ============ -->
<section class="section section-tint">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">The full list</p>
      <h2>Every teacher, by section</h2>
      <hr class="hr-gold">
    </div>
    <div class="reveal" data-tabs>
      <div class="tabs" role="tablist" aria-label="Faculty by section">
        <button class="tab" role="tab" aria-selected="true" id="tab-pre" aria-controls="p-pre">Pre-Primary ({len(pre)})</button>
        <button class="tab" role="tab" aria-selected="false" id="tab-pri" aria-controls="p-pri">Primary ({len(pri)})</button>
        <button class="tab" role="tab" aria-selected="false" id="tab-sec" aria-controls="p-sec">Secondary ({len(sec)})</button>
      </div>

      <div class="tabpanel" role="tabpanel" id="p-pre" aria-labelledby="tab-pre">
        <div id="pre-primary"></div>
        {table(["#", "Teacher", "Designation", "Qualification", "Class", "Service"], pre_body,
               "Pre-Primary teaching staff, as published by the school.")}
      </div>

      <div class="tabpanel" role="tabpanel" id="p-pri" aria-labelledby="tab-pri" hidden>
        <div id="primary"></div>
        {table(["#", "Teacher", "Position", "Subject", "Qualification", "Service"], pri_body,
               "Primary teaching staff, as published by the school.")}
      </div>

      <div class="tabpanel" role="tabpanel" id="p-sec" aria-labelledby="tab-sec" hidden>
        <div id="secondary"></div>
        {table(["#", "Name", "Designation", "Subject", "Qualification", "Service"], sec_body,
               "Secondary and Higher Secondary staff, as published by the school.")}
      </div>
    </div>
  </div>
</section>

""" + cta_band(
        "Want to teach at Vidyakunj?",
        "We recruit carefully and we train continuously. If you are a qualified teacher looking "
        "for a school where staff stay, write to the school office.",
        "Contact the office", "contact.html",
    ) + footer()
