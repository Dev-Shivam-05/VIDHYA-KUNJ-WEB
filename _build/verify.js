// Fast functional check: counters, lazy images, tabs, filters, lightbox, drawer.
const { chromium } = require('playwright');
const path = require('path');
const SITE = 'file:///' + path.resolve(__dirname, '..', 'site').split(path.sep).join('/');

(async () => {
  const b = await chromium.launch({ channel: 'chrome' });
  const ctx = await b.newContext({ viewport: { width: 1440, height: 1000 } });
  const page = await ctx.newPage();
  const fails = [];

  // ---------- counters on the homepage ----------
  await page.goto(SITE + '/index.html', { waitUntil: 'load' });
  await page.locator('.stats').scrollIntoViewIfNeeded();
  await page.waitForTimeout(2200);
  const counters = await page.$$eval('[data-count]', els => els.map(e => e.textContent));
  console.log('index counters     :', counters.join(' | '));
  if (counters.some(c => c === '0' || c === '')) fails.push('homepage counter stuck at 0');

  // ---------- lazy images actually load after scroll ----------
  await page.evaluate(async () => {
    const h = document.body.scrollHeight;
    for (let y = 0; y < h; y += window.innerHeight) {
      window.scrollTo(0, y); await new Promise(r => setTimeout(r, 90));
    }
  });
  await page.waitForTimeout(1200);
  const imgState = await page.evaluate(() => {
    const all = Array.from(document.images);
    return {
      total: all.length,
      loaded: all.filter(i => i.complete && i.naturalWidth > 0).length,
      broken: all.filter(i => i.complete && i.naturalWidth === 0).map(i => i.getAttribute('src')),
    };
  });
  console.log('index images       :', `${imgState.loaded}/${imgState.total} loaded`);
  if (imgState.broken.length) fails.push('broken images: ' + imgState.broken.join(', '));
  if (imgState.loaded < imgState.total) fails.push(`${imgState.total - imgState.loaded} image(s) never loaded`);

  // ---------- tabs on secondary ----------
  await page.goto(SITE + '/secondary.html', { waitUntil: 'load' });
  const tabCount = await page.locator('[data-tabs] .tab').count();
  await page.locator('[data-tabs] .tab').nth(3).click();
  await page.waitForTimeout(250);
  const panelVisible = await page.locator('[data-tabs] .tabpanel').nth(3).isVisible();
  const panel0Hidden = !(await page.locator('[data-tabs] .tabpanel').nth(0).isVisible());
  console.log('secondary tabs     :', `${tabCount} tabs, switch ok = ${panelVisible && panel0Hidden}`);
  if (!(panelVisible && panel0Hidden)) fails.push('secondary tabs do not switch');

  // ---------- faculty tables populated ----------
  await page.goto(SITE + '/faculty.html', { waitUntil: 'load' });
  const rows = await page.$$eval('table.data tbody tr', r => r.length);
  const facCounters = await page.$$eval('[data-count]', e => e.map(x => x.getAttribute('data-count')));
  console.log('faculty            :', `${rows} staff rows; stats ${facCounters.join('/')}`);
  if (rows < 90) fails.push(`faculty only has ${rows} rows, expected ~97`);

  // ---------- notices filter ----------
  await page.goto(SITE + '/notices.html', { waitUntil: 'load' });
  const before = await page.locator('#notices .notice:visible').count();
  await page.locator('.chip[data-value="results"]').click();
  await page.waitForTimeout(250);
  const after = await page.locator('#notices .notice:visible').count();
  console.log('notices filter     :', `${before} -> ${after} on "Results"`);
  if (!(after > 0 && after < before)) fails.push('notices filter did not narrow the list');

  // ---------- gallery lightbox ----------
  await page.goto(SITE + '/gallery.html', { waitUntil: 'load' });
  await page.locator('.gal-item').first().scrollIntoViewIfNeeded();
  await page.locator('.gal-item').first().click();
  await page.waitForTimeout(400);
  const lbOpen = await page.locator('#lightbox.open').count();
  const lbSrc = await page.locator('#lightbox img').getAttribute('src');
  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(300);
  const lbSrc2 = await page.locator('#lightbox img').getAttribute('src');
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);
  const lbClosed = await page.locator('#lightbox.open').count();
  console.log('gallery lightbox   :', `open=${!!lbOpen} arrowAdvances=${lbSrc !== lbSrc2} escCloses=${!lbClosed}`);
  if (!lbOpen) fails.push('lightbox did not open');
  if (lbSrc === lbSrc2) fails.push('lightbox arrow key did not advance');
  if (lbClosed) fails.push('lightbox did not close on Escape');

  // ---------- mobile drawer ----------
  const m = await b.newContext({ viewport: { width: 390, height: 844 } });
  const mp = await m.newPage();
  await mp.goto(SITE + '/index.html', { waitUntil: 'load' });
  await mp.locator('.nav-toggle').click();
  await mp.waitForTimeout(450);
  const drawerOpen = await mp.locator('.drawer.open').count();
  await mp.keyboard.press('Escape');
  await mp.waitForTimeout(450);
  const drawerClosed = await mp.locator('.drawer.open').count();
  console.log('mobile drawer      :', `opens=${!!drawerOpen} escCloses=${!drawerClosed}`);
  if (!drawerOpen) fails.push('mobile drawer did not open');
  if (drawerClosed) fails.push('mobile drawer did not close on Escape');

  // ---------- form validation ----------
  await mp.goto(SITE + '/contact.html', { waitUntil: 'load' });
  await mp.locator('form[data-validate] button[type=submit]').click();
  await mp.waitForTimeout(250);
  const invalid = await mp.locator('form[data-validate] .field.invalid').count();
  await mp.fill('#c-name', 'Test Parent');
  await mp.fill('#c-phone', '9876543210');
  await mp.fill('#c-msg', 'Enquiry about Standard 5 admission.');
  await mp.locator('form[data-validate] button[type=submit]').click();
  await mp.waitForTimeout(400);
  const okShown = await mp.locator('.form-ok.show').count();
  console.log('contact form       :', `blocksEmpty=${invalid > 0} (${invalid} fields) acceptsValid=${!!okShown}`);
  if (!invalid) fails.push('contact form did not block an empty submit');
  if (!okShown) fails.push('contact form did not confirm a valid submit');

  await b.close();
  console.log('\n===== FAILURES =====');
  console.log(fails.length ? fails.join('\n') : 'none');
})();
