// Screenshot + console/network error check for every built page.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const SITE = 'file:///' + path.resolve(__dirname, '..', 'site').replace(/\\/g, '/');
const OUT = path.resolve(__dirname, '..', '_shots');
fs.mkdirSync(OUT, { recursive: true });

const PAGES = ['index', 'about', 'pre-primary', 'primary', 'secondary',
  'faculty', 'admissions', 'gallery', 'notices', 'contact'];

(async () => {
  // Playwright's own chromium download timed out in this environment, so we
  // drive the Chrome already installed on the machine instead.
  const browser = await chromium.launch({ channel: 'chrome' });
  const problems = [];

  for (const view of [{ w: 1440, h: 1000, tag: 'desktop' }, { w: 390, h: 844, tag: 'mobile' }]) {
    const ctx = await browser.newContext({
      viewport: { width: view.w, height: view.h },
      deviceScaleFactor: 1,
    });
    for (const p of PAGES) {
      const page = await ctx.newPage();
      const errs = [];
      page.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
      page.on('pageerror', e => errs.push('pageerror: ' + e.message));
      page.on('requestfailed', r => {
        const u = r.url();
        if (u.startsWith('file:')) errs.push('404: ' + u.split('/site/')[1]);
      });

      await page.goto(`${SITE}/${p}.html`, { waitUntil: 'load' });
      await page.waitForTimeout(500);

      // Scroll the whole page so lazy-loaded images fetch and the
      // IntersectionObserver-driven counters and reveals actually fire.
      await page.evaluate(async () => {
        const h = document.body.scrollHeight;
        for (let y = 0; y < h; y += window.innerHeight * 0.8) {
          window.scrollTo(0, y);
          await new Promise(r => setTimeout(r, 120));
        }
      });
      // wait for every <img> to finish decoding
      await page.evaluate(() => Promise.all(
        Array.from(document.images)
          .filter(i => !i.complete)
          .map(i => new Promise(r => { i.onload = i.onerror = r; }))
      ));
      await page.evaluate(() => document.querySelectorAll('.reveal').forEach(e => e.classList.add('in')));
      // back to the top, otherwise the sticky header paints wherever we stopped
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(900);

      await page.screenshot({
        path: path.join(OUT, `${p}-${view.tag}.png`),
        fullPage: view.tag === 'desktop',
      });

      // check for horizontal overflow
      const overflow = await page.evaluate(() =>
        document.documentElement.scrollWidth - document.documentElement.clientWidth);
      if (overflow > 2) errs.push(`h-overflow: ${overflow}px`);

      // counters must have counted past zero, and no image may be broken
      const state = await page.evaluate(() => ({
        counters: Array.from(document.querySelectorAll('[data-count]')).map(e => e.textContent),
        broken: Array.from(document.images)
          .filter(i => i.complete && i.naturalWidth === 0)
          .map(i => i.getAttribute('src')),
      }));
      state.counters.forEach((v, i) => {
        if (v === '0' || v === '') errs.push(`counter ${i} stuck at "${v}"`);
      });
      state.broken.forEach(s => errs.push('broken img: ' + s));
      if (view.tag === 'desktop' && state.counters.length)
        console.log(`           counters: ${state.counters.join(' | ')}`);

      if (errs.length) problems.push(`[${view.tag}] ${p}.html\n    ` + [...new Set(errs)].join('\n    '));
      console.log(`  ${view.tag.padEnd(7)} ${p.padEnd(13)} ${errs.length ? 'ISSUES(' + errs.length + ')' : 'ok'}`);
      await page.close();
    }
    await ctx.close();
  }

  await browser.close();
  console.log('\n===== PROBLEMS =====');
  console.log(problems.length ? problems.join('\n') : 'none');
})();
