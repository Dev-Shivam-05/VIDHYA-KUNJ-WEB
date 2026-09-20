// Find which elements stick out past the viewport on mobile.
const { chromium } = require('playwright');
const path = require('path');
const SITE = 'file:///' + path.resolve(__dirname, '..', 'site').split(path.sep).join('/');

(async () => {
  const b = await chromium.launch({ channel: 'chrome' });
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
  const page = await ctx.newPage();
  await page.goto(SITE + '/index.html', { waitUntil: 'load' });
  await page.waitForTimeout(500);
  const bad = await page.evaluate(() => {
    const w = document.documentElement.clientWidth;
    const out = [];
    document.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.right > w + 1 || r.left < -1) {
        out.push({
          tag: el.tagName.toLowerCase(),
          cls: (el.className || '').toString().slice(0, 45),
          left: Math.round(r.left), right: Math.round(r.right), w: Math.round(r.width),
          parent: el.parentElement
            ? el.parentElement.tagName.toLowerCase() + '.' + (el.parentElement.className || '').toString().slice(0, 28)
            : ''
        });
      }
    });
    return { clientWidth: w, scrollWidth: document.documentElement.scrollWidth, items: out.slice(0, 25) };
  });
  console.log('clientWidth', bad.clientWidth, ' scrollWidth', bad.scrollWidth);
  bad.items.forEach(i =>
    console.log(`  ${i.tag}.${i.cls}  L${i.left} R${i.right} W${i.w}   <- ${i.parent}`));
  await b.close();
})();
