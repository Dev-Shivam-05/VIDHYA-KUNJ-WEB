# -*- coding: utf-8 -*-
"""Render every page module in _build/ to site/*.html."""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "site")
sys.path.insert(0, HERE)

PAGES = [
    ("p_index", "index.html"),
    ("p_about", "about.html"),
    ("p_preprimary", "pre-primary.html"),
    ("p_primary", "primary.html"),
    ("p_secondary", "secondary.html"),
    ("p_faculty", "faculty.html"),
    ("p_admissions", "admissions.html"),
    ("p_gallery", "gallery.html"),
    ("p_notices", "notices.html"),
    ("p_contact", "contact.html"),
]

if __name__ == "__main__":
    done, skipped = 0, []
    for mod, out in PAGES:
        try:
            m = importlib.import_module(mod)
        except ImportError:
            skipped.append(out)
            continue
        importlib.reload(m)
        html = m.build()
        path = os.path.join(OUT, out)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        done += 1
        print("  built  %-22s %7d bytes" % (out, len(html.encode("utf-8"))))
    if skipped:
        print("  pending: " + ", ".join(skipped))
    print("=== %d page(s) written to %s ===" % (done, OUT))
