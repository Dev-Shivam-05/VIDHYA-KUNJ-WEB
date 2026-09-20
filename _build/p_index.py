# -*- coding: utf-8 -*-
from common import *

TITLE = "Vidyakunj English Medium School, Navsari | Since 1969"
DESC = ("English-medium school in Navsari, Gujarat, founded in 1969 by the Navsari Junior "
        "Chamber. Play School to Standard 12 (Science & Commerce), 2,500+ students, 85+ teachers.")


def build():
    return head(TITLE, DESC, "index.html") + header("index.html") + f"""

<!-- ============ HERO ============ -->
<section class="hero">
  <div class="hero-media" data-slider>
    <div data-slide><img src="assets/img/banner/vks-slider-1.jpg" alt="" aria-hidden="true"></div>
    <div data-slide><img src="assets/img/banner/vks-slider-2.jpg" alt="" aria-hidden="true"></div>
    <div data-slide><img src="assets/img/banner/vks-slider-3.jpg" alt="" aria-hidden="true"></div>
  </div>
  <div class="container">
    <div class="hero-inner">
      <span class="hero-badge">{icon("award")} Serving Navsari since 1969</span>
      <h1>An English-medium education, rooted in Indian culture.</h1>
      <p class="lead">Started by forty young Jaycees of the Navsari Junior Chamber who each put in
        &#8377;1,000, Vidyakunj has grown into a Play School&ndash;to&ndash;Standard&nbsp;12 institution
        serving over {N_STUDENTS:,} students on a single Navsari campus.</p>
      <div class="btn-row">
        <a class="btn btn-gold" href="admissions.html">Admissions 2026&ndash;27 {icon("arrow")}</a>
        <a class="btn btn-light" href="about.html#story">Read our story</a>
      </div>
    </div>
  </div>
</section>

<!-- ============ STATS (real figures from the school's own records) ============ -->
<section class="section-sm section-brand">
  <div class="container">
    <div class="stats reveal">
      <div class="stat">
        <div class="stat-num"><span data-count="{N_STUDENTS}">0</span><span class="stat-suffix">+</span></div>
        <div class="stat-label">Students</div>
        <div class="stat-sub">Play School to Std 12</div>
      </div>
      <div class="stat">
        <div class="stat-num"><span data-count="{N_TEACHERS}">0</span><span class="stat-suffix">+</span></div>
        <div class="stat-label">Teachers &amp; Staff</div>
        <div class="stat-sub">Across all three sections</div>
      </div>
      <div class="stat">
        <div class="stat-num"><span data-count="{N_LAND}">0</span></div>
        <div class="stat-label">Sq&nbsp;m of Land</div>
        <div class="stat-sub">Gandevi Road campus</div>
      </div>
      <div class="stat">
        <div class="stat-num"><span data-count="{N_BUILT}">0</span></div>
        <div class="stat-label">Sq&nbsp;m Constructed</div>
        <div class="stat-sub">Built-up school area</div>
      </div>
    </div>
  </div>
</section>

<!-- ============ THREE SECTIONS ============ -->
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">One school, one journey</p>
      <h2>Three sections, thirteen years, a single campus</h2>
      <hr class="hr-gold">
      <p class="lead">A child who joins our Play School can stay with the same institution right
        through the Standard&nbsp;12 board exam &mdash; no transfers, no new school to settle into.</p>
    </div>

    <div class="grid g-3">
      <article class="card card-pre reveal">
        <div class="card-media"><img src="assets/img/campus/Vidyakunj-navsari-pre-primary.jpg"
             alt="Pre-Primary children at Vidyakunj Navsari" loading="lazy"></div>
        <div class="card-body">
          <span class="card-tag">Play School &ndash; Sr. KG</span>
          <h3>Pre-Primary Section</h3>
          <p>15 air-conditioned classrooms with smart boards, CCTV throughout, a dedicated play
             station for hands-on Language, Maths and Science, plus a playground and school hall.</p>
          <a class="card-link" href="pre-primary.html">Explore Pre-Primary {icon("arrow")}</a>
        </div>
      </article>

      <article class="card card-pri reveal" data-d="1">
        <div class="card-media"><img src="assets/img/campus/primary-class.jpg"
             alt="A Primary classroom at Vidyakunj Navsari" loading="lazy"></div>
        <div class="card-body">
          <span class="card-tag">Standard I &ndash; VIII</span>
          <h3>Primary Section</h3>
          <p>53 teachers, most of them with a decade or more at Vidyakunj. A broad curriculum with
             English, Gujarati, Hindi, Sanskrit, Maths, EVS/Science and Social Science.</p>
          <a class="card-link" href="primary.html">Explore Primary {icon("arrow")}</a>
        </div>
      </article>

      <article class="card card-sec reveal" data-d="2">
        <div class="card-media"><img src="assets/img/campus/Acadmic-Copy.jpg"
             alt="Secondary students at Vidyakunj Navsari" loading="lazy"></div>
        <div class="card-body">
          <span class="card-tag">Standard IX &ndash; XII</span>
          <h3>Secondary &amp; Higher Secondary</h3>
          <p>Gujarat board SSC and HSC, with Science and Commerce streams in Standards 11 and 12.
             Twelve divisions, question banks and practice tests for every subject.</p>
          <a class="card-link" href="secondary.html">Explore Secondary {icon("arrow")}</a>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ============ STORY ============ -->
<section class="section section-tint">
  <div class="container">
    <div class="split wide-left">
      <div class="reveal">
        <p class="eyebrow">Our beginning</p>
        <h2>Forty young men, &#8377;1,000 each, and a rented building on Gandevi Road</h2>
        <hr class="hr-gold">
        <p>In 1968&ndash;69 a group of Jaycees from the Navsari Junior Chamber set out to build an
           English-medium school that taught modern subjects without letting go of Indian culture &mdash;
           and that ordinary families in Navsari could actually afford.</p>
        <p>The initiative was taken by <strong>Mrs. Meeraben J. Desai, Dr. Manharbhai I. Shah,
           Mr. Jal Baria, Mr. Bharat Gandhi</strong> and the Jaycees team of 1968&ndash;69. Around forty
           members contributed &#8377;1,000 each, and the school opened in rented premises on
           Gandevi Road.</p>
        <p>Land followed. <strong>Shri Ukabhai Patel</strong> and <strong>Shri Rambhai Patel</strong> of
           Kachhiyawadi donated roughly <strong>1.75 lakh square feet</strong> on Gandevi Road, and the
           family of social worker <strong>Shri Hargovan Kaka Rathod</strong> funded the Pre-Primary and
           Primary buildings.</p>
        <a class="btn btn-ghost" href="about.html#story">The full history {icon("arrow")}</a>
      </div>
      <div class="img-stack reveal" data-d="1">
        <div class="main"><img src="assets/img/campus/the-vidyakunj.jpeg"
             alt="The Vidyakunj school building, Navsari" loading="lazy"></div>
        <div class="inset"><img src="assets/img/campus/Vidyakunj-Celebration-1024x683.jpg"
             alt="A celebration on the Vidyakunj campus" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ WHY ============ -->
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">What the campus offers</p>
      <h2>Built for teaching, not for the brochure</h2>
      <hr class="hr-gold">
    </div>
    <div class="grid g-3">
      <div class="tile reveal">
        <div class="tile-icon">{icon("monitor")}</div>
        <h3>Smart classrooms</h3>
        <p>The Pre-Primary section runs 15 air-conditioned classrooms fitted with smart boards for
           audio-visual teaching.</p>
      </div>
      <div class="tile reveal" data-d="1">
        <div class="tile-icon">{icon("shield")}</div>
        <h3>CCTV across classrooms</h3>
        <p>All Pre-Primary classrooms are connected by closed-circuit cameras, so supervision does
           not depend on who is standing in the corridor.</p>
      </div>
      <div class="tile reveal" data-d="2">
        <div class="tile-icon">{icon("flask")}</div>
        <h3>Play station for practicals</h3>
        <p>A dedicated space where children perform basic Language, Maths and Science experiments
           rather than only reading about them.</p>
      </div>
      <div class="tile reveal">
        <div class="tile-icon">{icon("music")}</div>
        <h3>School hall</h3>
        <p>Poetry recitation, skits, elocution, storytelling and dance competitions are all held
           in-house, in our own hall.</p>
      </div>
      <div class="tile reveal" data-d="1">
        <div class="tile-icon">{icon("leaf")}</div>
        <h3>Playground</h3>
        <p>An open playground for physical education and free play, used daily across the Primary
           and Pre-Primary sections.</p>
      </div>
      <div class="tile reveal" data-d="2">
        <div class="tile-icon">{icon("book")}</div>
        <h3>Question banks</h3>
        <p>Subject-wise question banks and board practice tests published for Standards 9 to 12,
           free for every enrolled student.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============ RESULTS / TRACK RECORD ============ -->
<section class="section section-tint">
  <div class="container">
    <div class="split wide-right">
      <div class="img-frame reveal">
        <img src="assets/img/campus/Vidyakunj-Primary-School-Navsari-1.jpg"
             alt="Students at Vidyakunj School, Navsari" loading="lazy">
      </div>
      <div class="reveal" data-d="1">
        <p class="eyebrow">Track record</p>
        <h2>Where our students have gone</h2>
        <hr class="hr-gold">
        <p>Vidyakunj students have finished at the top in public examinations in Mathematics,
           Commercial Maths, Statistics, Economics and Gujarati, and have been nominated to the
           National Science Congress at national level on several occasions.</p>
        <ul class="list-check">
          <li>State-level champions in the Garba competition</li>
          <li>Repeated wins in inter-school Quiz competitions</li>
          <li>Top placements in Essay Writing and Elocution</li>
        </ul>
        <p>Alumni now work as doctors, chartered accountants, engineers, managers, architects,
           professors, lawyers and business owners.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============ NOTICES ============ -->
<section class="section">
  <div class="container">
    <div class="split top wide-left">
      <div class="reveal">
        <p class="eyebrow">Notice board</p>
        <h2>Latest notices &amp; results</h2>
        <hr class="hr-gold">
        <p>Examination schedules, unit-test timetables and division-wise results are published here
           for parents and students.</p>

        <a class="notice" href="notices.html">
          <div class="notice-date"><div class="notice-d">17</div><div class="notice-m">Jan</div></div>
          <div class="notice-body">
            <h4>Unit Test 4 Results &mdash; December, Std 9 to 12</h4>
            <p>Division-wise result sheets for 9-B, 9-C, 10-A/B/C, 11 &amp; 12 Science and Commerce.</p>
            <div class="notice-tags"><span class="pill">Results</span><span class="pill">Students</span></div>
          </div>
        </a>

        <a class="notice" href="notices.html">
          <div class="notice-date"><div class="notice-d">13</div><div class="notice-m">Feb</div></div>
          <div class="notice-body">
            <h4>Second Practice Test Schedule &mdash; Std X &amp; XII</h4>
            <p>Board practice test timetable ahead of the SSC and HSC examinations.</p>
            <div class="notice-tags"><span class="pill">Exams</span><span class="pill">Parents</span></div>
          </div>
        </a>

        <a class="notice" href="notices.html">
          <div class="notice-date"><div class="notice-d">08</div><div class="notice-m">Apr</div></div>
          <div class="notice-body">
            <h4>School Timing Schedule</h4>
            <p>Section-wise reporting and dispersal timings for the academic year.</p>
            <div class="notice-tags"><span class="pill">Circular</span></div>
          </div>
        </a>

        <div class="btn-row" style="margin-top:1.5rem">
          <a class="btn btn-ghost" href="notices.html">All notices &amp; results {icon("arrow")}</a>
        </div>
      </div>

      <div class="reveal" data-d="1">
        <div class="quote">
          <p>Our goal is for every student to reach his or her developmental potential; not just
             academically, but socially and emotionally as well. We emphasised the importance of each
             individual child, allowing the child to achieve maximum potential, no matter what the
             background.</p>
          <p>There is nothing that cannot be achieved if there is synergy in the team &mdash; curious
             children ever-willing to learn, concerned parents who support our ventures, and diligent
             staff who go beyond their call of duty.</p>
          <div class="quote-by">
            <img src="assets/img/people/Sapna_SIngh-removebg-preview.png" alt="Mrs. Sapna Singh" loading="lazy">
            <div>
              <div class="n">Mrs. Sapna Singh</div>
              <div class="r">Head Teacher, Primary</div>
            </div>
          </div>
        </div>
        <div class="btn-row" style="margin-top:1.5rem">
          <a class="btn btn-ghost btn-sm" href="about.html#messages">Read all messages {icon("arrow")}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ GALLERY STRIP ============ -->
<section class="section section-tint" data-gallery>
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Life at Vidyakunj</p>
      <h2>Festivals, sports days and competitions</h2>
      <hr class="hr-gold">
    </div>
    <div class="gal-grid reveal">
      <button class="gal-item" type="button" data-full="assets/img/campus/Vidyakunj-Celebration.jpg">
        <img src="assets/img/campus/Vidyakunj-Celebration-1024x683.jpg" alt="School celebration at Vidyakunj" loading="lazy">
        <span class="gal-cap">Campus celebration</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/Primary-plastaion.jpg">
        <img src="assets/img/campus/Primary-plastaion-1024x768.jpg" alt="Tree plantation drive by the Primary section" loading="lazy">
        <span class="gal-cap">Plantation drive</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/primary-play-grond.jpg">
        <img src="assets/img/campus/primary-play-grond-1024x768.jpg" alt="The Primary playground" loading="lazy">
        <span class="gal-cap">Playground</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/sports.jpg">
        <img src="assets/img/campus/sports.jpg" alt="Sports day at Vidyakunj" loading="lazy">
        <span class="gal-cap">Sports day</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/culture-Copy.jpg">
        <img src="assets/img/campus/culture-Copy.jpg" alt="Cultural programme at Vidyakunj" loading="lazy">
        <span class="gal-cap">Cultural programme</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/primary-play-station.jpg">
        <img src="assets/img/campus/primary-play-station-1024x768.jpg" alt="The play station used for practical learning" loading="lazy">
        <span class="gal-cap">Play station</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/play-schhol.png">
        <img src="assets/img/campus/play-schhol.png" alt="Play School activity" loading="lazy">
        <span class="gal-cap">Play School</span>
      </button>
      <button class="gal-item" type="button" data-full="assets/img/campus/IMG-20210912-WA0042-min.jpg">
        <img src="assets/img/campus/IMG-20210912-WA0042-min-1024x1024.jpg" alt="On the Vidyakunj campus" loading="lazy">
        <span class="gal-cap">On campus</span>
      </button>
    </div>
    <div class="center" style="margin-top:2rem">
      <a class="btn btn-ghost" href="gallery.html">See the full gallery {icon("arrow")}</a>
    </div>
  </div>
</section>

""" + cta_band(
        "Admissions for 2026&ndash;27 are open",
        "Admission is offered to all boys and girls irrespective of caste, creed, race or status, "
        "on the basis of vacant seats in the class applied for.",
        "View admission process", "admissions.html",
        ("Call the school", "contact.html")
    ) + lightbox() + footer()
