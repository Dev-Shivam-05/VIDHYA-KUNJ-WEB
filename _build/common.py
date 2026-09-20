# -*- coding: utf-8 -*-
"""Shared chrome for the Vidyakunj Navsari static site.

Every fact rendered by these templates was taken from the school's own live
site (vidyakunjnavsari.edu.in) during the September 2026 audit. Nothing here
is invented; placeholders inherited from the old theme were removed, not
replaced with guesses.
"""

SCHOOL = "Vidyakunj English Medium School"
SHORT = "Vidyakunj"
CITY = "Navsari"

# --- verified contact facts (source: /contact-us/ on the live site) ---
ADDRESS = "JN Tata Road, Near Tighra Jakat Naka, Jamalpore, Navsari, Gujarat 396445"
PH_PRE = "+91 635 506 6847"
PH_PRI = "+91 635 506 5973"
PH_SEC = "+91 635 507 3795"

# --- verified counters (source: homepage Elementor counter data-to-value) ---
N_STUDENTS = 2500
N_TEACHERS = 85
N_LAND = 1590      # sq m
N_BUILT = 3606     # sq m

ICONS = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.69 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.33 1.85.56 2.81.69A2 2 0 0 1 22 16.92z"/>',
    "mail": '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "arrow": '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
    "menu": '<line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/>',
    "close": '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
    "chev-l": '<polyline points="15 18 9 12 15 6"/>',
    "chev-r": '<polyline points="9 18 15 12 9 6"/>',
    "caret": '<polyline points="6 9 12 15 18 9"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>',
    "camera": '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    "flask": '<path d="M9 2v6L4.6 17.2A2 2 0 0 0 6.4 20h11.2a2 2 0 0 0 1.8-2.8L15 8V2"/><line x1="8" y1="2" x2="16" y2="2"/><line x1="7" y1="14" x2="17" y2="14"/>',
    "music": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>',
    "heart": '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
    "award": '<circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "fb": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
    "ig": '<rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>',
    "yt": '<path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/>',
    "wa": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8z"/>',
}


def icon(name, cls=""):
    """Inline stroked SVG. Kept inline so the page has zero icon-font requests."""
    c = ' class="%s"' % cls if cls else ""
    return ('<svg%s viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">%s</svg>' % (c, ICONS[name]))


NAV = [
    ("Home", "index.html", []),
    ("About", "about.html", [
        ("Our Story since 1969", "about.html#story"),
        ("Management & Trust", "about.html#management"),
        ("Messages from Heads", "about.html#messages"),
    ]),
    ("Academics", "secondary.html", [
        ("Pre-Primary Section", "pre-primary.html"),
        ("Primary Section", "primary.html"),
        ("Secondary & Higher Secondary", "secondary.html"),
    ]),
    ("Faculty", "faculty.html", []),
    ("Admissions", "admissions.html", []),
    ("Gallery", "gallery.html", []),
    ("Notices", "notices.html", []),
    ("Contact", "contact.html", []),
]


def head(title, desc, current, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#303078">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_IN">
<link rel="icon" href="assets/img/brand/cropped-vks-icon2-192x192.jpg">
<link rel="apple-touch-icon" href="assets/img/brand/cropped-vks-icon2-180x180.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/css/styles.css">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(current):
    items = []
    for label, href, subs in NAV:
        cur = ' aria-current="page"' if href == current else ""
        if subs:
            sub = "".join(
                '<li><a href="%s">%s</a></li>' % (h, t) for t, h in subs)
            items.append(
                f'<li><a href="{href}"{cur}>{label}{icon("caret","caret")}</a>'
                f'<ul class="dropdown">{sub}</ul></li>')
        else:
            items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    menu = "".join(items)

    drawer_items = []
    for label, href, subs in NAV:
        drawer_items.append(f'<a href="{href}">{label}</a>')
        if subs:
            drawer_items.append('<div class="sub">' + "".join(
                '<a href="%s">%s</a>' % (h, t) for t, h in subs) + '</div>')
    drawer = "".join(drawer_items)

    return f"""<div class="topbar">
  <div class="container">
    <div class="topbar-links">
      <span class="hide-sm">{icon("pin")} {CITY}, Gujarat</span>
      <a href="tel:+916355065973">{icon("phone")} {PH_PRI}</a>
    </div>
    <div class="topbar-links">
      <span class="hide-sm">{icon("clock")} Office: Mon&ndash;Sat</span>
      <a href="admissions.html">Admissions 2026&ndash;27</a>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="container">
    <div class="nav">
      <a class="brand" href="index.html">
        <img src="assets/img/brand/vks-new-Logo.png" alt="{SCHOOL} logo" width="432" height="147">
        <span class="brand-text">
          <span class="brand-name">Vidyakunj</span>
          <span class="brand-sub">English Medium &middot; Navsari</span>
        </span>
      </a>
      <nav aria-label="Main">
        <ul class="nav-menu">{menu}</ul>
      </nav>
      <div class="nav-cta">
        <a class="btn btn-primary btn-sm" href="admissions.html">Apply for Admission</a>
        <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="drawer">
          {icon("menu")}
        </button>
      </div>
    </div>
  </div>
</header>

<div class="drawer" id="drawer">
  <div class="drawer-scrim"></div>
  <div class="drawer-panel" role="dialog" aria-modal="true" aria-label="Menu">
    <div class="drawer-top">
      <span class="brand-name">Vidyakunj</span>
      <button class="drawer-close" type="button" aria-label="Close menu">{icon("close")}</button>
    </div>
    <nav>{drawer}
      <a class="btn btn-primary" href="admissions.html">Apply for Admission</a>
    </nav>
  </div>
</div>

<main id="main">
"""


def footer():
    return f"""</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <span class="logo-chip"><img src="assets/img/brand/vks-new-Logo.png"
              alt="{SCHOOL}" width="432" height="147"></span>
        <p>Founded in 1969 by the Jaycees of Navsari Junior Chamber. English-medium
           education rooted in Indian culture, from Play School to Standard 12.</p>
        <div class="socials">
          <a href="contact.html" aria-label="Contact us on WhatsApp">{icon("wa")}</a>
          <a href="contact.html" aria-label="Facebook">{icon("fb")}</a>
          <a href="contact.html" aria-label="Instagram">{icon("ig")}</a>
          <a href="contact.html" aria-label="YouTube">{icon("yt")}</a>
        </div>
      </div>
      <div>
        <h4>Academics</h4>
        <ul>
          <li><a href="pre-primary.html">Pre-Primary Section</a></li>
          <li><a href="primary.html">Primary Section</a></li>
          <li><a href="secondary.html">Secondary &amp; Higher Secondary</a></li>
          <li><a href="faculty.html">Our Faculty</a></li>
          <li><a href="secondary.html#question-bank">Question Bank</a></li>
        </ul>
      </div>
      <div>
        <h4>For Parents</h4>
        <ul>
          <li><a href="admissions.html">Admission Process</a></li>
          <li><a href="admissions.html#fees">Fee Structure</a></li>
          <li><a href="admissions.html#rules">Rules &amp; Regulations</a></li>
          <li><a href="notices.html">Notices &amp; Results</a></li>
          <li><a href="gallery.html">Photo Gallery</a></li>
        </ul>
      </div>
      <div>
        <h4>Reach Us</h4>
        <ul class="footer-contact">
          <li>{icon("pin")}<span>{ADDRESS}</span></li>
          <li>{icon("phone")}<span>Pre-Primary <a href="tel:+916355066847">{PH_PRE}</a></span></li>
          <li>{icon("phone")}<span>Primary <a href="tel:+916355065973">{PH_PRI}</a></span></li>
          <li>{icon("phone")}<span>Secondary <a href="tel:+916355073795">{PH_SEC}</a></span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> {SCHOOL}, {CITY}. All rights reserved.</span>
      <span>Established 1969 &middot; Registered 1970</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
"""


def lightbox():
    return f"""<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button class="lb-btn lb-close" type="button" aria-label="Close">{icon("close")}</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous image">{icon("chev-l")}</button>
  <button class="lb-btn lb-next" type="button" aria-label="Next image">{icon("chev-r")}</button>
  <div>
    <!-- src is set by main.js on open; a transparent pixel avoids an empty src="" request -->
    <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="">
    <p class="lb-cap"></p>
  </div>
</div>
"""


def page_hero(title, sub, img, crumbs):
    c = '<a href="index.html">Home</a>'
    for t, h in crumbs:
        c += f'<span>/</span>' + (f'<a href="{h}">{t}</a>' if h else f'<span style="opacity:1;color:#fff">{t}</span>')
    return f"""<section class="page-hero">
  <div class="page-hero-media"><img src="{img}" alt="" aria-hidden="true"></div>
  <div class="container">
    <div class="page-hero-inner">
      <nav class="crumbs" aria-label="Breadcrumb">{c}</nav>
      <h1>{title}</h1>
      <p>{sub}</p>
    </div>
  </div>
</section>
"""


def cta_band(title, text, btn_text, btn_href, btn2=None):
    b2 = f'<a class="btn btn-light" href="{btn2[1]}">{btn2[0]}</a>' if btn2 else ""
    return f"""<section class="section-sm">
  <div class="container">
    <div class="cta-band reveal">
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn-gold" href="{btn_href}">{btn_text} {icon("arrow")}</a>
        {b2}
      </div>
    </div>
  </div>
</section>
"""
