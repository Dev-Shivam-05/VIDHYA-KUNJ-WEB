const { chromium } = require('playwright');
const BASE = 'https://dev-shivam-05.github.io/VIDHYA-KUNJ-WEB/';
(async () => {
  const b = await chromium.launch({ channel: 'chrome' });
  const ctx = await b.newContext({ viewport: { width: 1440, height: 1000 } });
  const p = await ctx.newPage();
  await p.goto(BASE, { waitUntil: 'load', timeout: 60000 });
  await p.evaluate(async () => {
    const h = document.body.scrollHeight;
    for (let y = 0; y < h; y += 400) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 200)); }
  });
  await p.waitForTimeout(4000);
  const r = await p.evaluate(() => {
    const all = Array.from(document.images);
    return {
      total: all.length,
      rendered: all.filter(i => i.naturalWidth > 0).length,
      notStarted: all.filter(i => !i.complete).map(i => i.getAttribute('src')),
      zeroWidth: all.filter(i => i.complete && i.naturalWidth === 0).map(i => i.getAttribute('src')),
    };
  });
  console.log(`total ${r.total} | rendered ${r.rendered}`);
  console.log('still loading :', r.notStarted.length ? r.notStarted : 'none');
  console.log('zero-width    :', r.zeroWidth.length ? r.zeroWidth : 'none');
  await b.close();
})();
