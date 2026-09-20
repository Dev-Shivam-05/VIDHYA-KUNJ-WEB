# -*- coding: utf-8 -*-
from common import *

TITLE = "Primary Section | Standard I to VIII | Vidyakunj Navsari"
DESC = ("The Primary Section at Vidyakunj English Medium School, Navsari - Standards I to VIII, "
        "53 teachers, English-medium teaching with Gujarati, Hindi and Sanskrit.")


def build():
    return head(TITLE, DESC, "primary.html") + header("primary.html") + page_hero(
        "Primary Section",
        "Standards I to VIII &mdash; the eight years where reading, arithmetic and study habits are "
        "settled for life.",
        "assets/img/campus/Vidyakunj-Primary-School-Navsari-1.jpg",
        [("Academics", None), ("Primary", None)],
    ) + f"""

<section class="section">
  <div class="container">
    <div class="split wide-left">
      <div class="reveal">
        <p class="eyebrow">Welcome</p>
        <h2>Teaching that leans on experience, not turnover</h2>
        <hr class="hr-gold">
        <p>The school has managed to achieve the success it has had because of its carefully
           recruited teaching team and its focus on technology. Extensive training is given to all
           teachers, and the use of technology in teaching is strongly emphasised.</p>
        <p>Our Primary section is staffed by <strong>53 teachers</strong>. Many of them joined
           Vidyakunj in the 1990s and early 2000s and have taught here ever since &mdash; the same
           teacher often sees a family&rsquo;s second and third child through the same classroom.</p>
        <p>Students are encouraged to take part in activities beyond the normal school day, and are
           given a choice from a wide variety of hobbies. A comprehensive curriculum ensures an
           enriching experience.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="admissions.html">Admission &amp; fees {icon("arrow")}</a>
          <a class="btn btn-ghost" href="tel:+916355065973">{icon("phone")} {PH_PRI}</a>
        </div>
      </div>
      <div class="img-stack reveal" data-d="1">
        <div class="main"><img src="assets/img/campus/primary-class.jpg"
             alt="A Primary classroom at Vidyakunj" loading="lazy"></div>
        <div class="inset"><img src="assets/img/campus/Primary-plastaion-1024x768.jpg"
             alt="Plantation drive by Primary students" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SUBJECTS ============ -->
<section class="section section-tint">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">What is taught</p>
      <h2>Subjects across the Primary years</h2>
      <hr class="hr-gold">
      <p class="lead">English is the medium of instruction throughout. Gujarati, Hindi and Sanskrit
         are taught alongside it, so children leave Standard VIII comfortable in four languages.</p>
    </div>
    <div class="grid g-3">
      <div class="tile reveal">
        <div class="tile-icon">{icon("globe")}</div>
        <h3>Languages</h3>
        <p>English, Gujarati, Hindi and Sanskrit &mdash; taught by subject specialists rather than by
           a single class teacher.</p>
      </div>
      <div class="tile reveal" data-d="1">
        <div class="tile-icon">{icon("flask")}</div>
        <h3>Mathematics &amp; Science</h3>
        <p>Maths and EVS in the early years, moving into formal Science as students approach
           Standard VIII.</p>
      </div>
      <div class="tile reveal" data-d="2">
        <div class="tile-icon">{icon("book")}</div>
        <h3>Social Science</h3>
        <p>History, geography and civics, taught in English with Gujarat-board continuity in mind.</p>
      </div>
      <div class="tile reveal">
        <div class="tile-icon">{icon("monitor")}</div>
        <h3>Computer</h3>
        <p>Computer education as a regular timetabled subject, not an optional extra.</p>
      </div>
      <div class="tile reveal" data-d="1">
        <div class="tile-icon">{icon("music")}</div>
        <h3>Drawing &amp; Craft</h3>
        <p>Art, craft and drawing taught by dedicated teachers, with work shown at school functions.</p>
      </div>
      <div class="tile reveal" data-d="2">
        <div class="tile-icon">{icon("leaf")}</div>
        <h3>Physical Training</h3>
        <p>P.T. on the school playground, plus sports day and inter-house competitions.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============ HEAD TEACHER ============ -->
<section class="section">
  <div class="container-narrow">
    <div class="quote reveal">
      <p>Our goal is for every student to reach his or her developmental potential; not just
         academically, but socially and emotionally as well. We emphasised the importance of each
         individual child, allowing the child to achieve maximum potential, no matter what the
         background.</p>
      <p>There is nothing that cannot be achieved if there is synergy in the team &mdash; curious
         children ever-willing to learn, concerned parents who support our ventures, diligent staff
         who go beyond their call of duty and who are safety conscious. Each of them complements the
         other, bringing goals to fruition.</p>
      <p>The connection between home and school is an essential component in laying the foundation
         for our youngest learners and all their educational experiences that lie ahead. A positive
         partnership builds children&rsquo;s confidence and encourages them to see learning as both
         enjoyable and purposeful. I encourage you to play an active role in your child&rsquo;s
         education.</p>
      <div class="quote-by">
        <img src="assets/img/people/Sapna_SIngh-removebg-preview.png" alt="Mrs. Sapna Singh" loading="lazy">
        <div>
          <div class="n">Mrs. Sapna Singh</div>
          <div class="r">Head Teacher, Primary &middot; M.Sc., B.Ed.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ BEYOND CLASS ============ -->
<section class="section section-tint" data-gallery>
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Beyond the classroom</p>
      <h2>Plantation drives, sports and stage</h2>
      <hr class="hr-gold">
    </div>
    <div class="gal-grid reveal">
      <button class="gal-item" type="button" data-full="assets/img/campus/Primary-plastaion.jpg">
        <img src="assets/img/campus/Primary-plastaion-1024x768.jpg" alt="Plantation drive" loading="lazy">
        <span class="gal-cap">Plantation drive</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/sports.jpg">
        <img src="assets/img/campus/sports.jpg" alt="Sports day" loading="lazy">
        <span class="gal-cap">Sports day</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/primary-play-grond.jpg">
        <img src="assets/img/campus/primary-play-grond-1024x768.jpg" alt="Playground" loading="lazy">
        <span class="gal-cap">Playground</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/vidyakunj-primary-photos-4.jpg">
        <img src="assets/img/campus/vidyakunj-primary-photos-4.jpg" alt="School activity" loading="lazy">
        <span class="gal-cap">School activity</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/vidyakunj-primary-photos-12.jpg">
        <img src="assets/img/campus/vidyakunj-primary-photos-12.jpg" alt="Classroom session" loading="lazy">
        <span class="gal-cap">In class</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/vidyakunj-primary-photos-19.jpg">
        <img src="assets/img/campus/vidyakunj-primary-photos-19.jpg" alt="School programme" loading="lazy">
        <span class="gal-cap">School programme</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/vidyakunj-primary-photos-8.jpg">
        <img src="assets/img/campus/vidyakunj-primary-photos-8.jpg" alt="Students at Vidyakunj" loading="lazy">
        <span class="gal-cap">Students</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/vidyakunj-primary-photos-21.jpg">
        <img src="assets/img/campus/vidyakunj-primary-photos-21.jpg" alt="Activity day" loading="lazy">
        <span class="gal-cap">Activity day</span>
      </button>
    </div>
    <div class="center" style="margin-top:2rem">
      <a class="btn btn-ghost" href="gallery.html">Full gallery {icon("arrow")}</a>
    </div>
  </div>
</section>

""" + cta_band(
        "Fees for Standards III to VIII are published",
        "&#8377;19,900 for the full academic year, in two terms, with no hidden activity charges. "
        "The complete fee policy is on the admissions page.",
        "See fee structure", "admissions.html#fees",
        ("Meet the faculty", "faculty.html#primary"),
    ) + lightbox() + footer()
