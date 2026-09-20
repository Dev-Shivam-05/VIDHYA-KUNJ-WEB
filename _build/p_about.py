# -*- coding: utf-8 -*-
from common import *

TITLE = "About Vidyakunj | Our Story Since 1969 | Navsari"
DESC = ("The history of Vidyakunj English Medium School, Navsari - founded in 1969 by the "
        "Navsari Junior Chamber, registered 1970. Management committee, trustees and leadership.")

# Source: /management/ on the live site, transcribed exactly.
COMMITTEE = [
    ("Shri Anupbhai R. Rathod", "Chairman", "assets/img/people/Anupbhai.jpeg"),
    ("Shri Atulbhai H. Shah", "Vice Chairman", "assets/img/people/Atulbhai-Shah.jpeg"),
    ("Shri Subhashbhai Desai", "Secretary", "assets/img/people/Subhasbhai-Desai.jpeg"),
    ("Shri Hiteshbhai Desai", "Joint Secretary", None),
    ("Shri Darabhai K. Deboo", "Treasurer", None),
]
MEMBERS = [
    "Shri Pareshbhai R. Rathod", "Shri Chandrashekar P. Naik", "Shri Venilal M. Rana",
    "Dharmishthaben D. Rathod", "Shri Rajesh N. Shah",
]
TRUSTEES = [
    "Shri Vasantbhai S. Jogani", "Shri Hareshbhai P. Shah", "Shri Omprakash Gupta",
    "Shri Jayeshbhai Solanki", "Shri Thakorbhai Mistry", "Shri Arifbhai A. Usmani",
    "Shri Amrishbhai Sanghadia", "Shri Kamleshbhai Malani",
]
R_TRUSTEES = [
    "Shri Tusharbhai Desai", "Shri Komalbhai Shah",
    "Shri Hemalbhai Shah", "Shri Kevalbhai Shah",
]


def initials(name):
    parts = [p for p in name.replace("Shri ", "").replace("Mrs. ", "").replace("Mr. ", "").split() if p]
    return (parts[0][0] + (parts[-1][0] if len(parts) > 1 else "")).upper()


def person(name, role, img=None, meta=None):
    face = (f'<img class="person-img" src="{img}" alt="{name}" loading="lazy">' if img
            else f'<div class="person-ph" aria-hidden="true">{initials(name)}</div>')
    m = f'<div class="meta">{meta}</div>' if meta else ""
    return (f'<div class="person">{face}<h4>{name}</h4>'
            f'<div class="role">{role}</div>{m}</div>')


def build():
    officers = "".join(person(n, r, i) for n, r, i in COMMITTEE)
    members = "".join(person(n, "Committee Member") for n in MEMBERS)
    trustees = "".join(person(n, "Trustee") for n in TRUSTEES)
    r_trustees = "".join(person(n, "Representative Trustee") for n in R_TRUSTEES)

    return head(TITLE, DESC, "about.html") + header("about.html") + page_hero(
        "Fifty-seven years of Vidyakunj",
        "From a rented building on Gandevi Road in 1969 to a Play School&ndash;to&ndash;Standard&nbsp;12 "
        "institution serving over 2,500 students.",
        "assets/img/campus/the-vidyakunj.jpeg",
        [("About", None)],
    ) + f"""

<!-- ============ STORY ============ -->
<section class="section" id="story">
  <div class="container">
    <div class="split top wide-left">
      <div class="reveal">
        <p class="eyebrow">Our story</p>
        <h2>It began with forty Jaycees and &#8377;1,000 each</h2>
        <hr class="hr-gold">
        <p>In the year 1968&ndash;1969, some young and enthusiastic Jaycees from the Navsari Junior
           Chamber got together in Navsari. Their mission was to establish an English-medium school
           imparting quality education from Pre-Primary to High School, based on Indian culture.</p>
        <p>The initiative was taken by <strong>Mrs. Meeraben J. Desai</strong>,
           <strong>Dr. Manharbhai I. Shah</strong>, <strong>Mr. Jal Baria</strong>,
           <strong>Mr. Bharat Gandhi</strong> and the Jaycees team of 1968&ndash;1969.</p>
        <p>In the beginning they collected &#8377;1,000 each from around forty Jaycees members, and the
           school started functioning in rented premises at Gandevi Road, Navsari.</p>
        <p>Impressed by the performance of the Jaycees leadership, leading personalities including
           <strong>Sheth Shri Hasmukhbhai R. Shah</strong>, <strong>Shri Naranjibhai Desai</strong>,
           <strong>Shri Dhirubhai Naik</strong>, <strong>Shri Ukabhai Patel</strong> and
           <strong>Shri Rambhai Patel</strong> of Kachhiyawadi also helped build the institution during
           its formative years.</p>
        <p>Thereafter, cash donations and donations of land and building began to arrive. Shri Ukabhai
           Patel and Shri Rambhai Patel donated around <strong>1.75 lakh square feet of land</strong> on
           Gandevi Road. The family of the well-known social worker
           <strong>Shri Hargovan Kaka Rathod</strong> donated a substantial amount towards the school
           building for the Pre-Primary and Primary sections.</p>
      </div>

      <div class="reveal" data-d="1">
        <div class="img-frame" style="margin-bottom:2rem">
          <img src="assets/img/campus/17EPBSWIDEANGLEjpg.jpg" alt="The Vidyakunj campus, Navsari" loading="lazy">
        </div>
        <div class="timeline">
          <div class="tl-item gold">
            <div class="tl-year">1968&ndash;69</div>
            <h4>The idea</h4>
            <p>Jaycees of the Navsari Junior Chamber resolve to open an English-medium school rooted
               in Indian culture, at fees local families can afford.</p>
          </div>
          <div class="tl-item gold">
            <div class="tl-year">1969</div>
            <h4>Vidyakunj opens</h4>
            <p>Classes begin in rented premises on Gandevi Road, Navsari.</p>
          </div>
          <div class="tl-item">
            <div class="tl-year">1970</div>
            <h4>Registered</h4>
            <p>Vidyakunj English Medium School is formally registered.</p>
          </div>
          <div class="tl-item">
            <div class="tl-year">1970s</div>
            <h4>Our own land</h4>
            <p>Roughly 1.75 lakh sq ft on Gandevi Road donated by Shri Ukabhai Patel and
               Shri Rambhai Patel.</p>
          </div>
          <div class="tl-item">
            <div class="tl-year">1980</div>
            <h4>Construction</h4>
            <p>The school moves into its own purpose-built campus.</p>
          </div>
          <div class="tl-item gold">
            <div class="tl-year">Today</div>
            <h4>Play School to Standard 12</h4>
            <p>Over {N_STUDENTS:,} students and {N_TEACHERS}+ teaching and support staff across three
               sections, on {N_BUILT:,} sq m of built-up area.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ PURPOSE ============ -->
<section class="section section-tint">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Why the school exists</p>
      <h2>A long-felt need, met at affordable fees</h2>
      <hr class="hr-gold">
      <p class="lead">There was a long-felt need for a school that would meet the hunger for learning
         in the area &mdash; and do it at fees families could manage. Vidyakunj was established with the
         noble cause of maintaining Indian culture through value-based education.</p>
    </div>
    <div class="grid g-4">
      <div class="tile reveal">
        <div class="tile-icon">{icon("globe")}</div>
        <h3>English medium</h3>
        <p>Quality English-medium teaching from Pre-Primary right through to High School.</p>
      </div>
      <div class="tile reveal" data-d="1">
        <div class="tile-icon">{icon("heart")}</div>
        <h3>Indian culture</h3>
        <p>Value-based education that keeps Indian culture at the centre, not at the margins.</p>
      </div>
      <div class="tile reveal" data-d="2">
        <div class="tile-icon">{icon("users")}</div>
        <h3>Open to all</h3>
        <p>Admission to all boys and girls irrespective of caste, creed, race or status.</p>
      </div>
      <div class="tile reveal" data-d="3">
        <div class="tile-icon">{icon("award")}</div>
        <h3>Affordable</h3>
        <p>Fees kept within reach of ordinary Navsari families &mdash; a founding commitment.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============ ACHIEVEMENTS ============ -->
<section class="section">
  <div class="container">
    <div class="split wide-right">
      <div class="img-frame reveal">
        <img src="assets/img/campus/culture-Copy.jpg" alt="Cultural programme at Vidyakunj" loading="lazy">
      </div>
      <div class="reveal" data-d="1">
        <p class="eyebrow">What our students have done</p>
        <h2>Top of the class, on stage and in the lab</h2>
        <hr class="hr-gold">
        <p>School students have remained at the top in public examinations in subjects such as
           Mathematics, Commercial Maths, Statistics, Economics and Gujarati.</p>
        <ul class="list-check">
          <li>State-level champions in the Garba competition</li>
          <li>Repeated top placements in inter-school Quiz competitions</li>
          <li>Consistent wins in Essay Writing and Elocution</li>
          <li>Students nominated to the National Science Congress at national level on many occasions</li>
        </ul>
        <p>Many of our students are now successful professionals. Vidyakunj has given the society
           doctors, chartered accountants, engineers, managers, architects, professors, lawyers and
           business owners.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============ MESSAGES ============ -->
<section class="section section-tint" id="messages">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">From our leadership</p>
      <h2>Messages from the Heads</h2>
      <hr class="hr-gold">
    </div>
    <div class="grid g-2">
      <div class="quote reveal">
        <p>Our goal is for every student to reach his or her developmental potential; not just
           academically, but socially and emotionally as well. We emphasised the importance of each
           individual child, allowing the child to achieve maximum potential, no matter what the
           background.</p>
        <p>There is nothing that cannot be achieved if there is synergy in the team &mdash; curious
           children ever-willing to learn, concerned parents who support our ventures, diligent staff
           who go beyond their call of duty and who are safety conscious. Each of them complements
           the other, bringing goals to fruition.</p>
        <p>The connection between home and school is an essential component in laying the foundation
           for our youngest learners. I encourage you to play an active role in your child&rsquo;s
           education. We are looking forward to watching your child grow and mature this year.</p>
        <div class="quote-by">
          <img src="assets/img/people/Sapna_SIngh-removebg-preview.png" alt="Mrs. Sapna Singh" loading="lazy">
          <div>
            <div class="n">Mrs. Sapna Singh</div>
            <div class="r">Head Teacher, Primary Section</div>
          </div>
        </div>
      </div>

      <div class="quote reveal" data-d="1">
        <p>The children are very special individuals who need a happy, secure and challenging
           environment in which they can grow. Children have a natural curiosity that makes them
           explore their world, and that gives teachers the basis on which to build learning
           experiences.</p>
        <p>For parents it is vital that your child receives an excellent start to schooling in a
           friendly, caring and homely atmosphere. At Vidyakunj we aim to foster sound academics,
           self-discipline and self-worth, respect for others, and co-operative learning and
           living skills.</p>
        <p>Our dedicated staff take a real interest in all children and are committed to each
           child&rsquo;s future success. I assure you that your child&rsquo;s future is secure with us
           at Vidyakunj.</p>
        <div class="quote-by">
          <img src="assets/img/people/pre-principal-1-1024x992.jpg" alt="Mrs. Ragini Desai" loading="lazy">
          <div>
            <div class="n">Mrs. Ragini Desai</div>
            <div class="r">Head Teacher, Pre-Primary Section</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ MANAGEMENT ============ -->
<section class="section" id="management">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Governance</p>
      <h2>Management Committee &amp; Trustees</h2>
      <hr class="hr-gold">
      <p class="lead">Vidyakunj is run by an honorary management committee and a board of trustees
         drawn from the Navsari community &mdash; twenty-two members in all.</p>
    </div>

    <h3 style="margin-bottom:1.5rem">Office Bearers</h3>
    <div class="grid g-4 reveal" style="margin-bottom:3rem">{officers}</div>

    <h3 style="margin-bottom:1.5rem">Committee Members</h3>
    <div class="grid g-4 reveal" style="margin-bottom:3rem">{members}</div>

    <h3 style="margin-bottom:1.5rem">Trustees</h3>
    <div class="grid g-4 reveal" style="margin-bottom:3rem">{trustees}</div>

    <h3 style="margin-bottom:1.5rem">Representative Trustees</h3>
    <div class="grid g-4 reveal">{r_trustees}</div>
  </div>
</section>

""" + cta_band(
        "Come and see the campus",
        "The best way to judge a school is to walk through it during a working day. "
        "Call the section you are interested in and we will arrange a visit.",
        "Contact the school", "contact.html",
        ("Admission details", "admissions.html"),
    ) + footer()
