/* ==========================================================================
   Vidyakunj School Navsari - site behaviour
   Vanilla JS, no dependencies. Every block guards for its own markup,
   so the same file is safe to load on every page.
   ========================================================================== */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1. Sticky header shadow ---------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- 2. Mobile drawer ---------- */
  var drawer = document.getElementById('drawer');
  var openBtn = document.querySelector('.nav-toggle');
  if (drawer && openBtn) {
    var lastFocus = null;
    var openDrawer = function () {
      lastFocus = document.activeElement;
      drawer.classList.add('open');
      openBtn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      var first = drawer.querySelector('.drawer-close');
      if (first) first.focus();
    };
    var closeDrawer = function () {
      drawer.classList.remove('open');
      openBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    };
    openBtn.addEventListener('click', openDrawer);
    drawer.querySelectorAll('.drawer-close, .drawer-scrim').forEach(function (el) {
      el.addEventListener('click', closeDrawer);
    });
    drawer.querySelectorAll('nav a').forEach(function (a) {
      a.addEventListener('click', closeDrawer);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('open')) closeDrawer();
    });
  }

  /* ---------- 3. Reveal on scroll ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      reveals.forEach(function (el) { el.classList.add('in'); });
    } else {
      var ro = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('in'); ro.unobserve(en.target); }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      reveals.forEach(function (el) { ro.observe(el); });
    }
  }

  /* ---------- 4. Count-up stats ---------- */
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    var runCount = function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      if (isNaN(target)) return;
      if (reduceMotion) { el.textContent = target.toLocaleString('en-IN'); return; }
      var dur = 1500, t0 = null;
      var step = function (ts) {
        if (!t0) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1);
        // easeOutCubic
        var v = Math.round(target * (1 - Math.pow(1 - p, 3)));
        el.textContent = v.toLocaleString('en-IN');
        if (p < 1) requestAnimationFrame(step);
        else el.textContent = target.toLocaleString('en-IN');
      };
      requestAnimationFrame(step);
    };
    if (!('IntersectionObserver' in window)) {
      counters.forEach(runCount);
    } else {
      var co = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { runCount(en.target); co.unobserve(en.target); }
        });
      }, { threshold: 0.4 });
      counters.forEach(function (el) { co.observe(el); });
    }
  }

  /* ---------- 5. Tabs ---------- */
  document.querySelectorAll('[data-tabs]').forEach(function (root) {
    var tabs = Array.prototype.slice.call(root.querySelectorAll('.tab'));
    var panels = Array.prototype.slice.call(root.querySelectorAll('.tabpanel'));
    if (!tabs.length) return;
    var select = function (i) {
      tabs.forEach(function (t, j) {
        t.setAttribute('aria-selected', j === i ? 'true' : 'false');
        t.setAttribute('tabindex', j === i ? '0' : '-1');
      });
      panels.forEach(function (p, j) { p.hidden = j !== i; });
    };
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(i); });
      t.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight') n = (i + 1) % tabs.length;
        if (e.key === 'ArrowLeft') n = (i - 1 + tabs.length) % tabs.length;
        if (e.key === 'Home') n = 0;
        if (e.key === 'End') n = tabs.length - 1;
        if (n !== null) { e.preventDefault(); select(n); tabs[n].focus(); }
      });
    });
    select(0);
  });

  /* ---------- 6. Chip filters (notices / gallery) ---------- */
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var chips = Array.prototype.slice.call(group.querySelectorAll('.chip'));
    var targetSel = group.getAttribute('data-filter-group');
    var items = Array.prototype.slice.call(document.querySelectorAll(targetSel + ' [data-cat]'));
    var empty = document.querySelector(targetSel + ' .empty-state');
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var want = chip.getAttribute('data-value');
        chips.forEach(function (c) { c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
        var shown = 0;
        items.forEach(function (it) {
          var cats = (it.getAttribute('data-cat') || '').split(/\s+/);
          var show = want === 'all' || cats.indexOf(want) !== -1;
          it.style.display = show ? '' : 'none';
          if (show) shown++;
        });
        if (empty) empty.style.display = shown ? 'none' : '';
      });
    });
  });

  /* ---------- 7. Lightbox ---------- */
  var lb = document.getElementById('lightbox');
  if (lb) {
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('.lb-cap');
    var group = [];
    var idx = 0;
    var show = function (i) {
      idx = (i + group.length) % group.length;
      var it = group[idx];
      lbImg.src = it.src;
      lbImg.alt = it.alt;
      lbCap.textContent = it.cap + '  (' + (idx + 1) + ' / ' + group.length + ')';
    };
    var openLb = function () {
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
      lb.querySelector('.lb-close').focus();
    };
    var closeLb = function () {
      lb.classList.remove('open');
      document.body.style.overflow = '';
      lbImg.src = '';
    };
    document.querySelectorAll('.gal-item').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var scope = btn.closest('[data-gallery]') || document;
        group = Array.prototype.slice.call(scope.querySelectorAll('.gal-item'))
          .filter(function (b) { return b.style.display !== 'none'; })
          .map(function (b) {
            var im = b.querySelector('img');
            var cp = b.querySelector('.gal-cap');
            return {
              src: b.getAttribute('data-full') || im.src,
              alt: im.alt,
              cap: cp ? cp.textContent.trim() : im.alt
            };
          });
        var me = group.findIndex(function (g) {
          return g.src === (btn.getAttribute('data-full') || btn.querySelector('img').src);
        });
        show(me < 0 ? 0 : me);
        openLb();
      });
    });
    lb.querySelector('.lb-close').addEventListener('click', closeLb);
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(idx - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') closeLb();
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
  }

  /* ---------- 8. Hero slider ---------- */
  document.querySelectorAll('[data-slider]').forEach(function (root) {
    var slides = Array.prototype.slice.call(root.querySelectorAll('[data-slide]'));
    if (slides.length < 2) return;
    var i = 0;
    slides.forEach(function (s, j) {
      s.style.transition = 'opacity 1.1s ' + 'cubic-bezier(.22,.61,.36,1)';
      s.style.opacity = j === 0 ? '1' : '0';
      s.style.position = j === 0 ? 'relative' : 'absolute';
      s.style.inset = j === 0 ? '' : '0';
    });
    if (reduceMotion) return;
    setInterval(function () {
      slides[i].style.opacity = '0';
      i = (i + 1) % slides.length;
      slides[i].style.opacity = '1';
    }, 6000);
  });

  /* ---------- 9. Contact form (front-end validation only) ---------- */
  document.querySelectorAll('[data-validate]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (input) {
        var field = input.closest('.field');
        var valid = input.value.trim() !== '';
        if (valid && input.type === 'email') valid = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(input.value.trim());
        if (valid && input.type === 'tel') valid = input.value.replace(/\D/g, '').length >= 10;
        if (field) field.classList.toggle('invalid', !valid);
        if (!valid && ok) { input.focus(); ok = false; }
      });
      if (!ok) return;
      var note = form.querySelector('.form-ok');
      if (note) {
        note.classList.add('show');
        note.setAttribute('role', 'status');
        note.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
      }
      form.reset();
    });
    form.querySelectorAll('input, textarea, select').forEach(function (input) {
      input.addEventListener('input', function () {
        var f = input.closest('.field');
        if (f) f.classList.remove('invalid');
      });
    });
  });

  /* ---------- 10. Current year in footer ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
