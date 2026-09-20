# -*- coding: utf-8 -*-
from common import *

TITLE = "Pre-Primary Section | Vidyakunj School, Navsari"
DESC = ("Play School, Nursery, Jr. KG and Sr. KG at Vidyakunj Navsari - 15 air-conditioned "
        "classrooms with smart boards, CCTV, a play station, playground and school hall.")


def build():
    return head(TITLE, DESC, "pre-primary.html") + header("pre-primary.html") + page_hero(
        "Pre-Primary Section",
        "Play School, Nursery, Junior KG and Senior KG &mdash; where a thirteen-year journey with "
        "Vidyakunj begins.",
        "assets/img/campus/navsari-vidyakunjschool-pre-primary.jpg",
        [("Academics", None), ("Pre-Primary", None)],
    ) + f"""

<section class="section">
  <div class="container">
    <div class="split wide-left">
      <div class="reveal">
        <p class="eyebrow">Welcome</p>
        <h2>A progressive, passionate and purposeful place</h2>
        <hr class="hr-gold">
        <p>Vidyakunj English Medium School operates with the prime purpose of building young minds
           to spearhead a dynamic future globally. Our stated vision is a commitment to run a quality
           school focused on the development of the individual child in an era of globalisation.</p>
        <p>Vidyakunj Pre-Primary is a place where independent thinking is encouraged and excellence
           is nurtured &mdash; a place that takes great pleasure in the pursuit of knowledge and
           understanding, and that wants children to use their skills and intelligence to benefit
           society.</p>
        <p>Children are encouraged to take part in activities beyond the normal school day, with a
           wide variety of hobbies to choose from.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="admissions.html">Admission enquiry {icon("arrow")}</a>
          <a class="btn btn-ghost" href="tel:+916355066847">{icon("phone")} {PH_PRE}</a>
        </div>
      </div>
      <div class="img-stack reveal" data-d="1">
        <div class="main"><img src="assets/img/campus/FOR-WERBSITE-PREPRIMARY.jpeg"
             alt="Pre-Primary children at Vidyakunj Navsari" loading="lazy"></div>
        <div class="inset"><img src="assets/img/campus/play-schhol.png"
             alt="Play School activity" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ FACILITIES ============ -->
<section class="section section-tint">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Our facilities</p>
      <h2>What the Pre-Primary block actually has</h2>
      <hr class="hr-gold">
    </div>
    <div class="grid g-2">
      <article class="card reveal">
        <div class="card-media"><img src="assets/img/campus/primary-class.jpg"
             alt="An air-conditioned classroom with a smart board" loading="lazy"></div>
        <div class="card-body">
          <h3>Classrooms</h3>
          <p>Our Pre-Primary section has <strong>15 air-conditioned classrooms</strong> with smart
             boards used for audio-visual teaching. All classrooms are connected by closed-circuit
             cameras.</p>
        </div>
      </article>
      <article class="card reveal" data-d="1">
        <div class="card-media"><img src="assets/img/campus/primary-play-station-1024x768.jpg"
             alt="The play station used for practical learning" loading="lazy"></div>
        <div class="card-body">
          <h3>Play Station</h3>
          <p>A dedicated play station for practical knowledge of Language, Mathematics and Science.
             Children perform basic experiments to understand the wonders of science, which builds
             their curiosity in the field.</p>
        </div>
      </article>
      <article class="card reveal" data-d="2">
        <div class="card-media"><img src="assets/img/campus/primary-play-grond-1024x768.jpg"
             alt="The school playground" loading="lazy"></div>
        <div class="card-body">
          <h3>Playground</h3>
          <p>An open playground for the physical progress of the children, used every working day.</p>
        </div>
      </article>
      <article class="card reveal" data-d="3">
        <div class="card-media"><img src="assets/img/campus/culture-Copy.jpg"
             alt="A programme in the school hall" loading="lazy"></div>
        <div class="card-body">
          <h3>School Hall</h3>
          <p>All in-house activities &mdash; poetry recitation, skits, elocution, storytelling and
             dance competitions &mdash; are held in our own school hall.</p>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ============ HEAD TEACHER ============ -->
<section class="section">
  <div class="container-narrow">
    <div class="quote reveal">
      <p>The children are very special individuals who need a happy, secure and challenging
         environment in which they can grow. Children have a natural curiosity that makes them
         explore their world, which gives teachers the basis on which to build learning experiences
         that will in turn provide a solid foundation for the early years of schooling.</p>
      <p>For parents it is vital that your child receives an excellent start to schooling in a
         friendly, caring and homely atmosphere.</p>
      <p><strong>At Vidyakunj we aim to foster:</strong></p>
      <ul class="list-check">
        <li>Sound academics</li>
        <li>Self-discipline and self-worth</li>
        <li>Respect for others</li>
        <li>Co-operative learning and living skills</li>
      </ul>
      <p>Our dedicated staff take a real interest in all children and are committed to each
         child&rsquo;s future success, providing challenging programmes that promote individual growth,
         achievement, leadership and co-operation with others.</p>
      <div class="quote-by">
        <img src="assets/img/people/pre-principal-1-1024x992.jpg" alt="Mrs. Ragini Desai" loading="lazy">
        <div>
          <div class="n">Mrs. Ragini Desai</div>
          <div class="r">Head Teacher, Pre-Primary</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ CLASSES ============ -->
<section class="section section-tint">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">The ladder</p>
      <h2>Four years before Standard I</h2>
      <hr class="hr-gold">
    </div>
    <div class="grid g-4">
      <div class="tile reveal">
        <div class="tile-icon">{icon("heart")}</div>
        <h3>Play School</h3>
        <p>The first step. Settling in, routines, play-led learning and lots of reassurance.</p>
      </div>
      <div class="tile reveal" data-d="1">
        <div class="tile-icon">{icon("star")}</div>
        <h3>Nursery</h3>
        <p>Early language, numbers and motor skills through structured play and activity.</p>
      </div>
      <div class="tile reveal" data-d="2">
        <div class="tile-icon">{icon("book")}</div>
        <h3>Junior KG</h3>
        <p>Pre-reading and pre-writing, number sense, and the beginnings of classroom habits.</p>
      </div>
      <div class="tile reveal" data-d="3">
        <div class="tile-icon">{icon("award")}</div>
        <h3>Senior KG</h3>
        <p>Readiness for Standard I &mdash; reading, writing, arithmetic and independence.</p>
      </div>
    </div>
    <div class="center" style="margin-top:2.5rem">
      <a class="btn btn-ghost" href="faculty.html#pre-primary">Meet the 26 Pre-Primary teachers {icon("arrow")}</a>
    </div>
  </div>
</section>

""" + cta_band(
        "Thinking about Play School?",
        "Pre-Primary admissions are handled directly by the section office. "
        "Call us and we will tell you what is available this year.",
        "Call Pre-Primary", "tel:+916355066847",
        ("Admission details", "admissions.html"),
    ) + footer()
