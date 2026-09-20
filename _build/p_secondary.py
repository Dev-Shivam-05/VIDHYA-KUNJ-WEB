# -*- coding: utf-8 -*-
from common import *

TITLE = "Secondary & Higher Secondary | Std IX to XII | Vidyakunj Navsari"
DESC = ("Standards IX to XII at Vidyakunj Navsari - Gujarat board SSC and HSC, with Science and "
        "Commerce streams, question banks, unit tests and board practice papers.")

# Subject lists transcribed from the school's own Question Bank index.
SUBJECTS = {
    "Std. 9": ["English", "Mathematics", "Science", "Social Science", "Gujarati",
               "Hindi", "Sanskrit", "P.T.", "Drawing"],
    "Std. 10": ["English", "Mathematics", "Science", "Social Science", "Gujarati",
                "Hindi", "Sanskrit", "Computer", "P.T."],
    "Std. 11 Science": ["Physics", "Chemistry", "Maths", "Biology", "English", "Computer"],
    "Std. 11 Commerce": ["English", "Elements of Accounts", "Statistics", "Economics",
                         "Organisation of Commerce &amp; Management", "Gujarati", "Computer", "C.T."],
    "Std. 12 Science": ["Physics", "Chemistry", "Mathematics", "Biology", "English", "Computer"],
    "Std. 12 Commerce": ["English", "Elements of Accounts", "Statistics", "Economics",
                         "Organisation of Commerce &amp; Management", "Gujarati", "Computer", "C.T."],
}

DIVISIONS = ["9-A", "9-B", "9-C", "10-A", "10-B", "10-C",
             "11-A Com.", "11-B Com.", "11 Sci.", "12-A Com.", "12-B Com.", "12 Sci."]

SERVICES = [
    ("Duplicate Marksheet &mdash; S.S.C.", "Apply at the school office for a duplicate Standard 10 marksheet."),
    ("Duplicate Marksheet &mdash; H.S.C.", "Apply at the school office for a duplicate Standard 12 marksheet."),
    ("Duplicate Leaving Certificate", "Request a duplicate school leaving certificate."),
    ("S.S.C. Exam School Level Form", "School-level examination form for Standard 10 board candidates."),
    ("H.S.C. Exam School Level Form", "School-level examination form for Standard 12 board candidates."),
    ("Parents Meeting", "Schedule and circulars for the parent&ndash;teacher meetings."),
]


def build():
    tabs, panels = [], []
    for i, (std, subs) in enumerate(SUBJECTS.items()):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button class="tab" role="tab" aria-selected="{sel}" '
                    f'id="tab-{i}" aria-controls="panel-{i}">{std}</button>')
        chips = "".join(f'<li>{s}</li>' for s in subs)
        panels.append(
            f'<div class="tabpanel" role="tabpanel" id="panel-{i}" aria-labelledby="tab-{i}"'
            f'{"" if i == 0 else " hidden"}>'
            f'<ul class="list-check" style="columns:2;column-gap:2.5rem">{chips}</ul></div>')

    divs = "".join(f'<span class="pill" style="font-size:.85rem;padding:.4rem 1rem">{d}</span>'
                   for d in DIVISIONS)
    svc = "".join(
        f'<div class="tile reveal"><div class="tile-icon">{icon("file")}</div>'
        f'<h3 style="font-size:1.05rem">{t}</h3><p>{d}</p></div>' for t, d in SERVICES)

    return head(TITLE, DESC, "secondary.html") + header("secondary.html") + page_hero(
        "Secondary &amp; Higher Secondary",
        "Standards IX to XII &mdash; Gujarat board SSC and HSC, with Science and Commerce streams.",
        "assets/img/campus/Acadmic-Copy.jpg",
        [("Academics", None), ("Secondary", None)],
    ) + f"""

<section class="section">
  <div class="container">
    <div class="split wide-left">
      <div class="reveal">
        <p class="eyebrow">Standards IX to XII</p>
        <h2>Two board exams, twelve divisions, one campus</h2>
        <hr class="hr-gold">
        <p>The Secondary and Higher Secondary section prepares students for the Gujarat board
           <strong>S.S.C.</strong> examination at the end of Standard 10 and the
           <strong>H.S.C.</strong> examination at the end of Standard 12.</p>
        <p>From Standard 11, students choose between the <strong>Science</strong> and
           <strong>Commerce</strong> streams. The section runs twelve divisions in all.</p>
        <p>Our Principal, <strong>Mr. Ashishkumar R. Lad</strong> (M.Sc., B.Ed., Chemistry), has led
           the section since joining the school in 2006.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="notices.html">Results &amp; timetables {icon("arrow")}</a>
          <a class="btn btn-ghost" href="tel:+916355073795">{icon("phone")} {PH_SEC}</a>
        </div>
      </div>
      <div class="img-frame reveal" data-d="1">
        <img src="assets/img/campus/17EPBSWIDEANGLEjpg.jpg"
             alt="The Secondary block at Vidyakunj, Navsari" loading="lazy">
      </div>
    </div>
  </div>
</section>

<!-- ============ DIVISIONS ============ -->
<section class="section-sm section-tint">
  <div class="container">
    <div class="center reveal">
      <p class="eyebrow center">Divisions</p>
      <h3 style="margin-bottom:1.5rem">Twelve divisions from Standard 9 to 12</h3>
      <div style="display:flex;gap:.6rem;flex-wrap:wrap;justify-content:center;max-width:820px;margin-inline:auto">
        {divs}
      </div>
    </div>
  </div>
</section>

<!-- ============ STREAMS ============ -->
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Standards 11 &amp; 12</p>
      <h2>Choose Science or Commerce</h2>
      <hr class="hr-gold">
    </div>
    <div class="grid g-2">
      <article class="card reveal">
        <div class="card-media"><img src="assets/img/campus/vidyakunj-primary-photos-3.jpg"
             alt="Science students at Vidyakunj" loading="lazy"></div>
        <div class="card-body">
          <span class="card-tag">Std 11 &amp; 12</span>
          <h3>Science Stream</h3>
          <p>Physics, Chemistry, Mathematics, Biology, English and Computer &mdash; the route towards
             engineering, medicine and the pure sciences.</p>
          <ul class="list-check" style="margin-top:1rem">
            <li>Both Maths and Biology groups supported</li>
            <li>Board practice tests for Std 12 Science</li>
            <li>Subject-wise question banks published free</li>
          </ul>
        </div>
      </article>
      <article class="card reveal" data-d="1">
        <div class="card-media"><img src="assets/img/campus/Acadmic-Copy.jpg"
             alt="Commerce students at Vidyakunj" loading="lazy"></div>
        <div class="card-body">
          <span class="card-tag">Std 11 &amp; 12</span>
          <h3>Commerce Stream</h3>
          <p>Elements of Accounts, Statistics, Economics, Organisation of Commerce &amp; Management,
             English, Gujarati, Computer and C.T. &mdash; two divisions in each of Standards 11 and 12.</p>
          <ul class="list-check" style="margin-top:1rem">
            <li>Our students have topped public exams in Commercial Maths, Statistics and Economics</li>
            <li>Board practice tests for Std 12 Commerce</li>
            <li>Route towards C.A., B.Com and management</li>
          </ul>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ============ QUESTION BANK ============ -->
<section class="section section-tint" id="question-bank">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Question bank</p>
      <h2>Subject-wise papers for every standard</h2>
      <hr class="hr-gold">
      <p class="lead">Question banks are published for each standard and subject, free for every
         enrolled student. Select a standard to see what is covered.</p>
    </div>
    <div class="reveal" data-tabs>
      <div class="tabs" role="tablist" aria-label="Question bank by standard">{''.join(tabs)}</div>
      {''.join(panels)}
    </div>
  </div>
</section>

<!-- ============ EXAMS ============ -->
<section class="section">
  <div class="container">
    <div class="split wide-right">
      <div class="img-frame reveal">
        <img src="assets/img/campus/vidyakunj-primary-photos-14.jpg"
             alt="Examination hall at Vidyakunj" loading="lazy">
      </div>
      <div class="reveal" data-d="1">
        <p class="eyebrow">Assessment</p>
        <h2>Unit tests, terminals and board practice</h2>
        <hr class="hr-gold">
        <p>Students are assessed continuously through the year, not only at the board exam:</p>
        <ul class="list-check">
          <li><strong>Unit tests</strong> &mdash; four across the academic year, with division-wise
              results published for parents</li>
          <li><strong>Terminal examinations</strong> &mdash; first and second terminal exams with
              published timetables</li>
          <li><strong>Board practice tests</strong> &mdash; dedicated practice papers for Standard 10,
              Standard 12 Science and Standard 12 Commerce, run twice before the board exam</li>
        </ul>
        <a class="btn btn-ghost" href="notices.html">All schedules &amp; results {icon("arrow")}</a>
      </div>
    </div>
  </div>
</section>

<!-- ============ SERVICES ============ -->
<section class="section section-tint">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Office services</p>
      <h2>Forms and certificates</h2>
      <hr class="hr-gold">
      <p class="lead">These are handled at the Secondary section office. Call
         <a href="tel:+916355073795">{PH_SEC}</a> before visiting so the paperwork is ready.</p>
    </div>
    <div class="grid g-3">{svc}</div>
  </div>
</section>

""" + cta_band(
        "Joining us in Standard 9 or 11?",
        "Admission is granted on the basis of vacant seats in the standard applied for. "
        "Speak to the Secondary office about availability this year.",
        "Call Secondary office", "tel:+916355073795",
        ("Admission details", "admissions.html"),
    ) + footer()
