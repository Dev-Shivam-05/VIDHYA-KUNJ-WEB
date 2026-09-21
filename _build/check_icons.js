// Icon-size regression sweep: no inline svg should exceed 40px after the
// global icon-size rule, and the drawer brand must fit.
const { chromium } = require('playwright');
const path = require('path');
const SITE = 'file:///' + path.resolve(__dirname, '..').split(path.sep).join('/');
const OUT = path.resolve(__dirname, '..', '_shots');
const PAGES = ['index','about','pre-primary','primary','secondary','faculty','admissions','gallery','notices','contact'];

(async () => {
  const browser = await chromium.launch({ channel: 'chrome' });
  const ctx = await browser.newContext({ viewport:{width:1440,height:900}, deviceScaleFactor:1 });
  let bad = 0;
  for (const p of PAGES) {
    const page = await ctx.newPage();
    await page.goto(SITE + '/' + p + '.html', { waitUntil:'load' });
    await page.waitForTimeout(300);
    const r = await page.evaluate(() => {
      const out = [];
      for (const s of document.querySelectorAll('svg')) {
        const b = s.getBoundingClientRect();
        if (b.width > 40 || b.height > 40 || b.width < 6)
          out.push({cls: s.getAttribute('class')||s.parentElement.className, w:+b.width.toFixed(1), h:+b.height.toFixed(1)});
      }
      return {bad: out.slice(0,5), overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth};
    });
    if (r.bad.length || r.overflow) { bad++; console.log(p, JSON.stringify(r)); }
    await page.close();
  }
  // drawer at mobile width
  const mctx = await browser.newContext({ viewport:{width:390,height:844}, deviceScaleFactor:2 });
  const mp = await mctx.newPage();
  await mp.goto(SITE + '/index.html', { waitUntil:'load' });
  await mp.click('.nav-toggle');
  await mp.waitForTimeout(600);
  await mp.screenshot({ path: OUT + '/chk-drawer.png' });
  console.log(bad === 0 ? 'ICONS OK: no oversized or collapsed svg on 10 pages' : 'ISSUES: ' + bad);
  await browser.close();
})();
