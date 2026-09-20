# -*- coding: utf-8 -*-
from common import *

TITLE = "Admissions 2026-27 | Fees & Process | Vidyakunj Navsari"
DESC = ("Admission process, required documents, fee structure and school rules for Vidyakunj "
        "English Medium School, Navsari. Standards III-VIII annual fee Rs 19,900.")

DOCS = [
    "Verified copy of the pupil&rsquo;s Birth Certificate",
    "Original School Leaving Certificate with UID number",
    "Caste Certificate of the father, for SC / ST / OBC students",
    "Self-attested copy of the latest Report Card",
    "Self-attested copy of the Aadhaar Card",
]

# Source: /primary-admission/ on the live site, academic year 2025-26.
RULES = [
    "The use of any kind of fancy stationery items, mobiles or jewellery by students is not allowed in school.",
    "Birthday celebration is restricted to the distribution of pencils or ball pens.",
    "School fees may be revised from time to time as per instruction from the Governing Committee.",
    "Students are not permitted to have tattoos, mehendi, hair colour, nail polish or ornaments in school.",
    "Boys should keep their hair short and clean. Girls should tie their hair neatly.",
    "Students must not damage school property, whether in the classroom or on the premises.",
    "No entry is permitted for students once the morning prayer has begun.",
    "Parents and guardians are requested to check the diary, notebooks and Vidyasarathi workbooks regularly.",
    "Parents may meet the Head Teacher with their queries every Friday between 9.00 a.m. and 11.00 a.m.",
    "A written leave application for more than two days should be sanctioned by the Head Teacher in advance.",
]


def build():
    docs = "".join(f"<li>{d}</li>" for d in DOCS)
    rules = "".join(
        f'<details class="acc"><summary>{i+1}. {r.split(".")[0]}.</summary>'
        f'<div class="acc-body">{r}</div></details>'
        for i, r in enumerate(RULES))

    return head(TITLE, DESC, "admissions.html") + header("admissions.html") + page_hero(
        "Admissions",
        "Vidyakunj provides admission to all boys and girls irrespective of caste, creed, race "
        "or status.",
        "assets/img/campus/admission-Copy.jpg",
        [("Admissions", None)],
    ) + f"""

<!-- ============ PROCESS ============ -->
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">How it works</p>
      <h2>Four steps to a seat</h2>
      <hr class="hr-gold">
    </div>
    <div class="grid g-4">
      <div class="tile reveal">
        <div class="tile-icon">{icon("phone")}</div>
        <h3>1. Enquire</h3>
        <p>Call the section you need &mdash; Pre-Primary, Primary or Secondary &mdash; and ask about
           vacant seats in the standard you want.</p>
      </div>
      <div class="tile reveal" data-d="1">
        <div class="tile-icon">{icon("file")}</div>
        <h3>2. Collect the form</h3>
        <p>Admission forms are issued at the school office. Bring the documents listed below when
           you come.</p>
      </div>
      <div class="tile reveal" data-d="2">
        <div class="tile-icon">{icon("users")}</div>
        <h3>3. Meet us</h3>
        <p>An interaction with the Head Teacher of the section, and a walk through the block your
           child would join.</p>
      </div>
      <div class="tile reveal" data-d="3">
        <div class="tile-icon">{icon("award")}</div>
        <h3>4. Confirm</h3>
        <p>Admission is granted on the basis of vacant seats. Pay the first-term fee at Bank of
           Baroda, Navsari, and the seat is confirmed.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============ DOCUMENTS ============ -->
<section class="section section-tint">
  <div class="container">
    <div class="split wide-left">
      <div class="reveal">
        <p class="eyebrow">Paperwork</p>
        <h2>Documents to bring</h2>
        <hr class="hr-gold">
        <ul class="list-check">{docs}</ul>
        <div class="form-note" style="margin-top:1.5rem">
          <strong>Admission status:</strong> Admission is given on the basis of vacant seats in the
          particular class. The decision of the school authorities is final and binding in all
          respects.
        </div>
      </div>
      <div class="img-frame reveal" data-d="1">
        <img src="assets/img/campus/admission-Copy.jpg" alt="Admissions at Vidyakunj Navsari" loading="lazy">
      </div>
    </div>
  </div>
</section>

<!-- ============ FEES ============ -->
<section class="section" id="fees">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Fee structure</p>
      <h2>What it costs, in full</h2>
      <hr class="hr-gold">
      <p class="lead">Published for Standards III to VIII. There are no hidden activity charges.
         For other standards, please ask the section office.</p>
    </div>

    <div class="reveal" style="max-width:720px;margin-inline:auto">
      <div class="table-wrap">
        <div class="table-scroll">
          <table class="data" style="min-width:460px">
            <thead>
              <tr><th>Standard</th><th>Instalment</th><th style="text-align:right">Amount</th></tr>
            </thead>
            <tbody>
              <tr><td style="width:auto" class="t-name">III to VIII</td><td>1st Term</td>
                  <td style="text-align:right">&#8377;&nbsp;10,000</td></tr>
              <tr><td style="width:auto"></td><td>2nd Term</td>
                  <td style="text-align:right">&#8377;&nbsp;9,900</td></tr>
              <tr class="fee-total"><td style="width:auto">Total</td><td>Annual academic fee</td>
                  <td style="text-align:right">&#8377;&nbsp;19,900</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <p class="table-cap">Applicable for the academic year 2025&ndash;26.
         New admissions pay a one-time admission fee of &#8377;600.</p>

      <div class="grid g-2" style="margin-top:2.5rem">
        <div class="tile">
          <div class="tile-icon">{icon("shield")}</div>
          <h3 style="font-size:1.05rem">What is included</h3>
          <p>No other activity charges are taken from parents. The annual academic fee is the
             academic cost in full.</p>
        </div>
        <div class="tile">
          <div class="tile-icon">{icon("book")}</div>
          <h3 style="font-size:1.05rem">What is extra</h3>
          <p>Parents bear the cost of textbooks, notebooks and related materials, uniforms and
             excursions.</p>
        </div>
      </div>

      <div class="form-note" style="margin-top:1.5rem">
        <strong>Fee policy.</strong> All fees are paid by cash, payable to Bank of Baroda, Navsari.
        The fee schedule above is subject to change; the school will communicate any revision to
        parents. Fees paid are not refunded under any circumstances.
      </div>
    </div>
  </div>
</section>

<!-- ============ RULES ============ -->
<section class="section section-tint" id="rules">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Rules &amp; regulations</p>
      <h2>What we ask of students and parents</h2>
      <hr class="hr-gold">
      <p class="lead">These apply from the day a child joins. We publish them before admission so
         there are no surprises afterwards.</p>
    </div>
    <div class="container-narrow reveal" style="padding:0">{rules}</div>
  </div>
</section>

<!-- ============ ENQUIRY ============ -->
<section class="section">
  <div class="container">
    <div class="split top">
      <div class="reveal">
        <p class="eyebrow">Admission enquiry</p>
        <h2>Send us your details</h2>
        <hr class="hr-gold">
        <p>Fill this in and the section office will call you back with what is available in the
           standard you need. If it is urgent, please call directly.</p>
        <div class="stack" style="margin-top:2rem">
          <div class="contact-row">
            <div class="contact-icon">{icon("phone")}</div>
            <div><h4>Pre-Primary</h4><a href="tel:+916355066847">{PH_PRE}</a></div>
          </div>
          <div class="contact-row">
            <div class="contact-icon">{icon("phone")}</div>
            <div><h4>Primary</h4><a href="tel:+916355065973">{PH_PRI}</a></div>
          </div>
          <div class="contact-row">
            <div class="contact-icon">{icon("phone")}</div>
            <div><h4>Secondary &amp; Higher Secondary</h4><a href="tel:+916355073795">{PH_SEC}</a></div>
          </div>
        </div>
      </div>

      <form class="flow reveal" data-validate data-d="1" novalidate>
        <div class="form-ok">Thank you. Your enquiry has been noted &mdash; the section office will
          call you back.</div>
        <div class="grid g-2" style="gap:1rem">
          <div class="field">
            <label for="a-parent">Parent&rsquo;s name <span class="req">*</span></label>
            <input id="a-parent" name="parent" type="text" required autocomplete="name">
            <span class="err">Please enter your name.</span>
          </div>
          <div class="field">
            <label for="a-phone">Mobile number <span class="req">*</span></label>
            <input id="a-phone" name="phone" type="tel" required autocomplete="tel" placeholder="10-digit mobile">
            <span class="err">Please enter a valid 10-digit mobile number.</span>
          </div>
        </div>
        <div class="grid g-2" style="gap:1rem">
          <div class="field">
            <label for="a-child">Child&rsquo;s name</label>
            <input id="a-child" name="child" type="text">
          </div>
          <div class="field">
            <label for="a-std">Standard applying for <span class="req">*</span></label>
            <select id="a-std" name="standard" required>
              <option value="">Select a standard</option>
              <option>Play School</option><option>Nursery</option>
              <option>Junior KG</option><option>Senior KG</option>
              <option>Standard I to V</option><option>Standard VI to VIII</option>
              <option>Standard IX / X</option>
              <option>Standard XI / XII - Science</option>
              <option>Standard XI / XII - Commerce</option>
            </select>
            <span class="err">Please choose a standard.</span>
          </div>
        </div>
        <div class="field">
          <label for="a-msg">Anything you would like to tell us</label>
          <textarea id="a-msg" name="message" rows="4"></textarea>
        </div>
        <div class="form-note">
          This form is a front-end demonstration. Connecting it to the school office inbox or a
          WhatsApp number is a one-line change once a mail endpoint is chosen.
        </div>
        <button class="btn btn-primary" type="submit">Send enquiry {icon("arrow")}</button>
      </form>
    </div>
  </div>
</section>

""" + footer()
