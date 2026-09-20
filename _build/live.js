// Verify the DEPLOYED site, not the local files.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const BASE = process.argv[2] || 'https://dev-shivam-05.github.io/VIDHYA-KUNJ-WEB/';
const OUT = path.resolve(__dirname, '..', '_shots');
fs.mkdirSync(OUT, { recursive: true });
const PAGES = ['index', 'about', 'pre-primary', 'primary', 'secondary',
  'faculty', 'admissions', 'gallery', 'notices', 'contact'];

(async () => {
  const b = await chromium.launch({ channel: 'chrome' });
  const fails = [];
  console.log('Verifying ' + BASE + '\n');

  for (const view of [{ w: 1440, h: 1000, tag: 'desktop' }, { w: 390, h: 844, tag: 'mobile' }]) {
    const ctx = await b.newContext({ viewport: { width: view.w, height: view.h } });
    for (const p of PAGES) {
      const page = await ctx.newPage();
      const errs = [];
      page.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
      page.on('pageerror', e => errs.push('pageerror: ' + e.message));
      page.on('response', r => {
        if (r.status() >= 400 && new URL(r.url()).host.includes('github.io'))
          errs.push(`${r.status()}: ${r.url().replace(BASE, '')}`);
      });

      await page.goto(BASE + (p === 'index' ? '' : p + '.html'), { waitUntil: 'load', timeout: 60000 });
      await page.evaluate(async () => {
        const h = document.body.scrollHeight;
        for (let y = 0; y < h; y += window.innerHeight) {
          window.scrollTo(0, y); await new Promise(r => setTimeout(r, 110));
        }
        window.scrollTo(0, 0);
      });
      await page.waitForTimeout(1200);

      const state = await page.evaluate(() => ({
        overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
        broken: Array.from(document.images).filter(i => i.complete && i.naturalWidth === 0)
          .map(i => i.getAttribute('src')),
        imgs: document.images.length,
        counters: Array.from(document.querySelectorAll('[data-count]')).map(e => e.textContent),
        title: document.title,
      }));
      if (state.overflow > 2) errs.push(`h-overflow ${state.overflow}px`);
      state.broken.forEach(s => errs.push('broken img: ' + s));
      state.counters.forEach((c, i) => { if (c === '0') errs.push(`counter ${i} stuck`); });

      if (view.tag === 'desktop') {
        await page.evaluate(() => document.querySelectorAll('.reveal').forEach(e => e.classList.add('in')));
        await page.waitForTimeout(500);
        await page.screenshot({ path: path.join(OUT, `live-${p}.png`), fullPage: true });
      }

      console.log(`  ${view.tag.padEnd(7)} ${p.padEnd(13)} ${state.imgs} imgs  ${errs.length ? 'ISSUES: ' + [...new Set(errs)].join('; ') : 'ok'}`);
      if (errs.length) fails.push(`[${view.tag}] ${p}: ` + [...new Set(errs)].join('; '));
      await page.close();
    }
    await ctx.close();
  }

  await b.close();
  console.log('\n===== LIVE FAILURES =====');
  console.log(fails.length ? fails.join('\n') : 'none');
})();
