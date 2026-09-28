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

## Files

```
index.html      Map + table app (Leaflet, OpenStreetMap lookup in the browser)
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
