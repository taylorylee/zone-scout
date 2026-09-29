# Zone Scout

Draw a zone on a map and get every business inside it: name, category, address, phone, website, public emails, social links, and whether they run an email newsletter. Export to CSV.

Built for mapping businesses. Works anywhere OpenStreetMap has coverage.

## What works where

| Where it runs | Business list + CSV | Website scan (emails, newsletters) |
|---|---|---|
| GitHub Pages | Yes | No |
| Vercel | Yes | Yes |
| Your computer (`server.py`) | Yes | Yes |

The website scan needs a server because browsers block pages from reading other sites.

## Run it

**GitHub Pages (list and CSV only):** Settings → Pages → Deploy from branch → `main` / root. Open `https://<user>.github.io/zone-scout/`.

**Vercel (full version):** In Vercel, choose Add New → Project → Import this repo. Leave Framework as "Other" and deploy. No settings or keys needed.

**Locally (full version):**

```bash
python3 server.py
# open http://localhost:8765
```

Python 3.8+ only, no installs.

## How to use

1. Draw a zone with the square or polygon tool (top left of the map).
2. **Find places** pulls shops, restaurants, cafes, bars, venues, offices and studios from OpenStreetMap.
3. **Scan websites** checks each homepage, plus up to 2 contact/about pages if no email is found.
4. Filter by Has website / Has email / Newsletter. Tick rows and use **Export selected**, or **Export all**.
5. Click the zone name in the header to rename it.

**Newsletter (green):** the site loads a known email tool (Mailchimp, Klaviyo, Substack, Beehiiv, Kit, Constant Contact, Flodesk, MailerLite, Brevo, HubSpot, Omnisend, Squarespace or Shopify signup blocks, and others).
**Signup form (amber):** an email field next to words like "newsletter" or "subscribe".

## Deals tab

Track businesses for sale and check whether the numbers work.

- **Add a deal** with New deal, Paste listing (reads asking price, cash flow, EBITDA, revenue, real estate, year established and reason for selling from pasted listing text), or **+ Deal** on any row in the Businesses tab.
- **Financials by year:** revenue, cash flow (SDE) and EBITDA for as many years as you have, each with a context note (source, add-backs, tax return vs P&L).
- **Every figure has a context field** for what's included, lease terms, and questions to ask.

What it calculates:

| Metric | Formula |
|---|---|
| The ask | Asking price, split into business and real estate, plus your down payment |
| Headline multiple | Asking price ÷ latest SDE |
| Business multiple | (Asking price − included real estate) ÷ latest SDE, also shown on average SDE and on EBITDA |
| Debt service coverage | (Latest SDE − manager salary − yearly reinvestment) ÷ annual loan payments |

Loan payments use your own down payment, rate, terms and seller financing. Real estate is amortized over its own term. DSCR is green at 1.25x or higher, amber from 1.0x to 1.25x, red below 1.0x.

Deals are saved in your browser. Use **Back up** to download them as a file and **Restore** to load them on another computer. The numbers are a screening tool, not financial advice; confirm them with the seller's tax returns, a lender and an advisor.

## Files

```
index.html      Businesses (map + table) and Deals tabs
api/index.py    Python API: website scanner + server-side place lookup (Vercel function)
server.py       Runs index.html + the API on your computer
vercel.json     Vercel function settings
```

## Limits

- Coverage comes from OpenStreetMap. Some small businesses are missing or have no website listed.
- Sites built entirely in JavaScript can hide signup forms, so a few show "none found" incorrectly.
- Keep zones neighborhood-sized (under ~30 km²). The free Overpass API can time out on large areas.
- Collects public information only. Follow CAN-SPAM if you email anyone: identify yourself and include an opt-out.

## Data sources

Map data © OpenStreetMap contributors (ODbL). Basemap © CARTO.
