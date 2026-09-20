# -*- coding: utf-8 -*-
from common import *

TITLE = "Contact Us | Vidyakunj English Medium School, Navsari"
DESC = ("Contact Vidyakunj School, Navsari. JN Tata Road, Near Tighra Jakat Naka, Jamalpore, "
        "Navsari, Gujarat 396445. Section-wise phone numbers for Pre-Primary, Primary and Secondary.")

MAP_Q = "JN+Tata+Road+Tighra+Jakat+Naka+Jamalpore+Navsari+Gujarat+396445"


def build():
    return head(TITLE, DESC, "contact.html") + header("contact.html") + page_hero(
        "Contact Us",
        "Three sections, three offices. Call the one you need and you will reach someone who can "
        "actually answer.",
        "assets/img/campus/contact-us.jpg",
        [("Contact", None)],
    ) + f"""

<section class="section">
  <div class="container">
    <div class="grid g-3">
      <div class="tile reveal">
        <div class="tile-icon" style="background:var(--pre-100);color:var(--pre-500)">{icon("heart")}</div>
        <h3 style="font-size:1.1rem">Pre-Primary</h3>
        <p>Play School, Nursery, Junior KG and Senior KG.</p>
        <p style="margin-top:.75rem"><a class="btn btn-ghost btn-sm" href="tel:+916355066847">
          {icon("phone")} {PH_PRE}</a></p>
      </div>
      <div class="tile reveal" data-d="1">
        <div class="tile-icon" style="background:var(--pri-100);color:var(--pri-500)">{icon("book")}</div>
        <h3 style="font-size:1.1rem">Primary</h3>
        <p>Standards I to VIII, admissions and fee queries.</p>
        <p style="margin-top:.75rem"><a class="btn btn-ghost btn-sm" href="tel:+916355065973">
          {icon("phone")} {PH_PRI}</a></p>
      </div>
      <div class="tile reveal" data-d="2">
        <div class="tile-icon">{icon("award")}</div>
        <h3 style="font-size:1.1rem">Secondary &amp; Higher Secondary</h3>
        <p>Standards IX to XII, board forms and certificates.</p>
        <p style="margin-top:.75rem"><a class="btn btn-ghost btn-sm" href="tel:+916355073795">
          {icon("phone")} {PH_SEC}</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section-tint">
  <div class="container">
    <div class="split top">
      <div class="reveal">
        <p class="eyebrow">Where we are</p>
        <h2>Visit the campus</h2>
        <hr class="hr-gold">

        <div class="contact-row">
          <div class="contact-icon">{icon("pin")}</div>
          <div>
            <h4>Address</h4>
            <p>{ADDRESS}</p>
            <a class="btn btn-ghost btn-sm" style="margin-top:.75rem"
               href="https://www.google.com/maps/search/?api=1&amp;query={MAP_Q}"
               target="_blank" rel="noopener">Open in Google Maps {icon("arrow")}</a>
          </div>
        </div>

        <div class="contact-row">
          <div class="contact-icon">{icon("clock")}</div>
          <div>
            <h4>Meeting the Head Teacher</h4>
            <p>Parents can meet the Head Teacher with their queries every Friday between
               9.00 a.m. and 11.00 a.m. Please call ahead.</p>
          </div>
        </div>

        <div class="contact-row">
          <div class="contact-icon">{icon("users")}</div>
          <div>
            <h4>Meeting a class teacher</h4>
            <p>Teacher meetings are arranged through the Head Teacher of the section, so that
               a class is never left unattended.</p>
          </div>
        </div>

        <div class="map-frame" style="margin-top:2rem">
          <iframe
            src="https://www.google.com/maps?q={MAP_Q}&amp;output=embed"
            title="Map showing Vidyakunj School, Navsari"
            loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>

      <form class="flow reveal" data-validate data-d="1" novalidate>
        <p class="eyebrow">Send a message</p>
        <h2 style="margin-bottom:1rem">Have a question?</h2>
        <div class="form-ok">Thank you &mdash; your message has been noted. The school office will
          get back to you.</div>
        <div class="field">
          <label for="c-name">Your name <span class="req">*</span></label>
          <input id="c-name" name="name" type="text" required autocomplete="name">
          <span class="err">Please enter your name.</span>
        </div>
        <div class="grid g-2" style="gap:1rem">
          <div class="field">
            <label for="c-phone">Mobile <span class="req">*</span></label>
            <input id="c-phone" name="phone" type="tel" required autocomplete="tel">
            <span class="err">Please enter a valid 10-digit mobile number.</span>
          </div>
          <div class="field">
            <label for="c-email">Email</label>
            <input id="c-email" name="email" type="email" autocomplete="email">
            <span class="err">Please enter a valid email address.</span>
          </div>
        </div>
        <div class="field">
          <label for="c-section">Which section?</label>
          <select id="c-section" name="section">
            <option>Pre-Primary</option><option>Primary</option>
            <option>Secondary &amp; Higher Secondary</option><option>General / Office</option>
          </select>
        </div>
        <div class="field">
          <label for="c-msg">Message <span class="req">*</span></label>
          <textarea id="c-msg" name="message" rows="5" required></textarea>
          <span class="err">Please write your message.</span>
        </div>
        <div class="form-note">
          This form is a front-end demonstration. It is ready to be wired to the school office
          inbox or a WhatsApp Business number.
        </div>
        <button class="btn btn-primary" type="submit">Send message {icon("arrow")}</button>
      </form>
    </div>
  </div>
</section>

""" + cta_band(
        "Planning to apply?",
        "The admissions page has the full process, the documents you need to bring and the "
        "published fee structure.",
        "Go to Admissions", "admissions.html",
    ) + footer()
