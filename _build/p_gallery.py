# -*- coding: utf-8 -*-
"""Gallery. Album names and photo counts come from the school's Events page;
images are the school's own files pulled during the audit."""
import os
import re
from common import *

TITLE = "Gallery | Events & Celebrations | Vidyakunj Navsari"
DESC = ("Photographs from Vidyakunj Navsari - Diwali, Navratri, Sports Day 'Utkarsh Udaan', "
        "Story Telling Competition, Annual Day and everyday life on campus.")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (title, category, photo-count as published on the school's Events page)
ALBUMS = [
    ("Diwali Celebration", "festival", 48),
    ("Aluna Celebration", "festival", 12),
    ("Sports Day &mdash; Utkarsh Udaan", "sports", 9),
    ("Story Telling Competition", "academic", 6),
    ("Navratri Celebration", "festival", 4),
    ("Annual Day 2018", "cultural", None),
    ("Mother&rsquo;s Day Celebration", "cultural", None),
    ("Advertisement Day", "academic", None),
]

CATS = [("all", "All photos"), ("campus", "Campus"), ("festival", "Festivals"),
        ("sports", "Sports"), ("cultural", "Cultural"), ("academic", "Academic")]


def campus_shots():
    """Every school-owned campus photo we recovered, as gallery tiles."""
    d = os.path.join(ROOT, "assets", "img", "campus")
    out = []
    seen = set()
    for f in sorted(os.listdir(d)):
        if not re.search(r"\.(jpe?g|png|webp)$", f, re.I):
            continue
        # skip the resized duplicate when we also hold the full-size file
        base = re.sub(r"-\d+x\d+(?=\.)", "", f)
        if base != f and os.path.exists(os.path.join(d, base)):
            continue
        if base in seen:
            continue
        seen.add(base)
        out.append(f)
    return out


def caption_for(fn):
    n = fn.lower()
    if "plastaion" in n or "plantation" in n:
        return "Plantation drive", "campus"
    if "celebration" in n:
        return "Campus celebration", "festival"
    if "sport" in n:
        return "Sports day", "sports"
    if "culture" in n:
        return "Cultural programme", "cultural"
    if "play-grond" in n or "play-ground" in n:
        return "Playground", "campus"
    if "play-station" in n:
        return "Play station", "academic"
    if "play-schhol" in n or "preprimary" in n or "pre-primary" in n:
        return "Pre-Primary", "campus"
    if "class" in n:
        return "In the classroom", "academic"
    if "acadmic" in n or "academic" in n:
        return "Academics", "academic"
    if "admission" in n:
        return "Admissions", "campus"
    if "contact" in n:
        return "School office", "campus"
    if "wideangle" in n or "the-vidyakunj" in n:
        return "The campus", "campus"
    return "Life at Vidyakunj", "campus"


def build():
    chips = "".join(
        f'<button class="chip" data-value="{v}" aria-pressed="{"true" if v == "all" else "false"}">{t}</button>'
        for v, t in CATS)

    tiles = []
    for f in campus_shots():
        cap, cat = caption_for(f)
        src = f"assets/img/campus/{f}"
        tiles.append(
            f'<button class="gal-item" type="button" data-cat="{cat}" data-full="{src}">'
            f'<img src="{src}" alt="{cap} at Vidyakunj School, Navsari" loading="lazy">'
            f'<span class="gal-cap">{cap}</span></button>')

    # gallery-album thumbnails recovered from the school's NextGEN albums
    gdir = os.path.join(ROOT, "assets", "img", "gallery")
    for f in sorted(os.listdir(gdir)):
        if not re.search(r"\.(jpe?g|png|webp)$", f, re.I):
            continue
        src = f"assets/img/gallery/{f}"
        cat = "festival" if re.search(r"diwali|navratri|aluna", f, re.I) else \
              "sports" if "sport" in f.lower() else \
              "academic" if "story|advertis" in f.lower() else "cultural"
        tiles.append(
            f'<button class="gal-item" type="button" data-cat="{cat}" data-full="{src}">'
            f'<img src="{src}" alt="Event photograph, Vidyakunj Navsari" loading="lazy">'
            f'<span class="gal-cap">School event</span></button>')

    albums = "".join(
        f'<div class="tile reveal"><div class="tile-icon">{icon("camera")}</div>'
        f'<h3 style="font-size:1.05rem">{t}</h3>'
        f'<p>{str(n) + " photographs" if n else "Photo album"}</p></div>'
        for t, c, n in ALBUMS)

    return head(TITLE, DESC, "gallery.html") + header("gallery.html") + page_hero(
        "Gallery",
        "Festivals, sports days, competitions and the ordinary working days in between.",
        "assets/img/campus/Vidyakunj-Celebration.jpg",
        [("Gallery", None)],
    ) + f"""

<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow center">Our albums</p>
      <h2>What the school year looks like</h2>
      <hr class="hr-gold">
    </div>
    <div class="grid g-4">{albums}</div>
  </div>
</section>

<section class="section section-tint" data-gallery>
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Photographs</p>
      <h2>Browse the collection</h2>
      <hr class="hr-gold">
      <p>Click any photograph to open it full size. Use the arrow keys to move through the set.</p>
    </div>
    <div class="filter-row reveal" data-filter-group="#gal">{chips}</div>
    <div id="gal">
      <div class="gal-grid reveal">{''.join(tiles)}</div>
      <p class="empty-state" style="display:none">No photographs in this category yet.</p>
    </div>
  </div>
</section>

""" + cta_band(
        "See it in person",
        "Photographs only go so far. Call the section office and arrange to walk through the "
        "campus on a working day.",
        "Arrange a visit", "contact.html",
    ) + lightbox() + footer()
