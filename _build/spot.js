// Tight crops of the three reported defects, for eyeball confirmation.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const SITE = 'file:///' + path.resolve(__dirname, '..', 'site').split(path.sep).join('/');
const OUT = path.resolve(__dirname, '..', '_shots');
fs.mkdirSync(OUT, { recursive: true });

(async () => {
  const b = await chromium.launch({ channel: 'chrome' });
  const ctx = await b.newContext({ viewport: { width: 1440, height: 950 } });
  const p = await ctx.newPage();

  await p.goto(SITE + '/index.html', { waitUntil: 'load' });
  await p.waitForTimeout(500);
  await p.locator('.site-header').screenshot({ path: path.join(OUT, 'fix-header.png') });

  await p.locator('.site-footer').scrollIntoViewIfNeeded();
  await p.waitForTimeout(900);
  await p.locator('.site-footer').screenshot({ path: path.join(OUT, 'fix-footer.png') });

  await p.goto(SITE + '/admissions.html', { waitUntil: 'load' });
  await p.locator('#fees').scrollIntoViewIfNeeded();
  await p.evaluate(() => document.querySelectorAll('.reveal').forEach(e => e.classList.add('in')));
  await p.waitForTimeout(900);
  await p.locator('#fees .table-wrap').screenshot({ path: path.join(OUT, 'fix-fees.png') });

  // 1366px laptop header, the width the user reported the overlap at
  const ctx2 = await b.newContext({ viewport: { width: 1366, height: 800 } });
  const p2 = await ctx2.newPage();
  await p2.goto(SITE + '/index.html', { waitUntil: 'load' });
  await p2.waitForTimeout(500);
  await p2.locator('.site-header').screenshot({ path: path.join(OUT, 'fix-header-1366.png') });

  await b.close();
  console.log('wrote fix-header.png, fix-header-1366.png, fix-footer.png, fix-fees.png');
})();
