// Confirm the header bar fits, the footer logo renders, and the fee total row
// has readable contrast — the three defects reported from the browser.
const { chromium } = require('playwright');
const path = require('path');
const SITE = 'file:///' + path.resolve(__dirname, '..', 'site').split(path.sep).join('/');

const lum = c => {
  const [r, g, b] = c.match(/\d+/g).map(Number).map(v => {
    v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
};
const ratio = (a, b) => {
  const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p);
  return ((x + 0.05) / (y + 0.05));
};

(async () => {
  const b = await chromium.launch({ channel: 'chrome' });
  const fails = [];

  for (const w of [1920, 1440, 1366, 1280, 1230, 1100, 820, 390]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 } });
    const p = await ctx.newPage();
    await p.goto(SITE + '/index.html', { waitUntil: 'load' });
    await p.waitForTimeout(350);
    const r = await p.evaluate(() => {
      const brand = document.querySelector('.brand').getBoundingClientRect();
      const menuEl = document.querySelector('.nav-menu');
      const menu = menuEl && getComputedStyle(menuEl).display !== 'none'
        ? menuEl.getBoundingClientRect() : null;
      const cta = document.querySelector('.nav-cta').getBoundingClientRect();
      return {
        overlap: menu ? Math.round(brand.right - menu.left) : null,
        menuVisible: !!menu,
        ctaOverlap: menu ? Math.round(menu.right - cta.left) : null,
        overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      };
    });
    const mode = r.menuVisible ? 'full menu' : 'drawer   ';
    const bad = (r.overlap > 0) || (r.ctaOverlap > 0) || r.overflow > 2;
    console.log(`  ${String(w).padStart(4)}px  ${mode}  brand/menu gap ${r.overlap === null ? ' n/a' : String(-r.overlap).padStart(4)}px  menu/cta gap ${r.ctaOverlap === null ? ' n/a' : String(-r.ctaOverlap).padStart(4)}px  overflow ${r.overflow}px  ${bad ? '<< FAIL' : ''}`);
    if (r.overlap > 0) fails.push(`${w}px: brand overlaps menu by ${r.overlap}px`);
    if (r.ctaOverlap > 0) fails.push(`${w}px: menu overlaps CTA by ${r.ctaOverlap}px`);
    if (r.overflow > 2) fails.push(`${w}px: horizontal overflow ${r.overflow}px`);
    await ctx.close();
  }

  // ---- footer logo + fee table ----
  const ctx = await b.newContext({ viewport: { width: 1440, height: 1000 } });
  const p = await ctx.newPage();
  await p.goto(SITE + '/index.html', { waitUntil: 'load' });
  await p.locator('.footer-brand img').scrollIntoViewIfNeeded();
  await p.waitForTimeout(600);
  const logo = await p.evaluate(() => {
    const i = document.querySelector('.footer-brand img');
    const chip = i.closest('.logo-chip');
    return {
      loaded: i.complete && i.naturalWidth > 0,
      filter: getComputedStyle(i).filter,
      chipBg: chip ? getComputedStyle(chip).backgroundColor : 'none',
    };
  });
  console.log(`\n  footer logo: loaded=${logo.loaded} filter=${logo.filter} chip=${logo.chipBg}`);
  if (!logo.loaded) fails.push('footer logo did not load');
  if (logo.filter !== 'none') fails.push('footer logo still has a filter: ' + logo.filter);

  await p.goto(SITE + '/admissions.html', { waitUntil: 'load' });
  await p.locator('.fee-total').scrollIntoViewIfNeeded();
  await p.waitForTimeout(600);
  const fee = await p.evaluate(() => {
    const rows = Array.from(document.querySelectorAll('table.data tbody tr'));
    return rows.map(tr => {
      const td = tr.querySelector('td:last-child');
      return {
        text: td.textContent.trim(),
        fg: getComputedStyle(td).color,
        bg: getComputedStyle(tr).backgroundColor === 'rgba(0, 0, 0, 0)'
          ? getComputedStyle(document.body).backgroundColor
          : getComputedStyle(tr).backgroundColor,
      };
    });
  });
  console.log('');
  fee.forEach(r => {
    const c = ratio(r.fg, r.bg);
    const ok = c >= 4.5;
    console.log(`  fee row "${r.text}"  contrast ${c.toFixed(2)}:1  ${ok ? 'AA pass' : '<< FAIL'}`);
    if (!ok) fails.push(`fee row "${r.text}" contrast only ${c.toFixed(2)}:1`);
  });

  await b.close();
  console.log('\n===== FAILURES =====');
  console.log(fails.length ? fails.join('\n') : 'none');
})();
