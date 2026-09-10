# Acumen Junior College — revamped landing page

`index.html` is the working page. `code.html` is the untouched Google Stitch export, kept
for comparison. `DESIGN.md` is the Stitch design system and is still the source of truth for
tokens.

Run it locally:

```bash
python -m http.server 8000 --bind 127.0.0.1
# http://127.0.0.1:8000/index.html
```

## Assets

All images are local, in `assets/`. The Stitch export hotlinked eight
`lh3.googleusercontent.com/aida/...` URLs, which are temporary and expire; they were still
live when the page was built and have been downloaded.

| File | What it is |
|---|---|
| `logo.jpg` | College logo (also used as favicon and `og:image`) |
| `hero-graphic.png` | Decorative hero illustration |
| `director-sandeep-mukkala.png`, `director-shravan-kumar.png` | Director portraits |
| `results-batch1-2020-2022.png` | First batch results poster |
| `results-batch2-2021-2023.png` | Second batch results poster |
| `results-batch3-2022-2024.png` | Third batch results poster |
| `gallery/photos.json` | Gallery manifest — see [Gallery](#gallery) |

`campus-view.jpg` was an AI-rendered building, not a photograph of the campus. It has been
deleted and both references removed rather than shipped with a disclaimer.

## Open items

**1. Verify the batch-3 rank transcription.** The Results section now carries the ranker data
as real HTML text rather than only as a JPEG. Batches 1 and 2 were read cleanly. Batch 3 came
off a 404×512 poster and three things need checking against the original high-resolution file:

- V. Harini and A. Vedasri — rank badges unreadable, currently shown as an em dash.
- The poster's bottom row (A. Tejaswi, U. Sri Ramana, P. Dhanush, Md. Afzal Ahmed,
  A. Aishwarya, Ishrath Aiza) carries percentile figures, not All India Ranks. Omitted rather
  than guessed.
- The poster labels several campuses "IIT" where the institute is an IIIT (Madhya Pradesh,
  Bhubaneswar, Bangalore, Kurnool, Jaipur). Transcribed as IIIT. Confirm the intended wording.

**2. Give the enquiry form a backend.** `#apply-form` has no `action`. Client-side validation
runs, then the submit handler opens a prefilled `mailto:` draft so nothing is silently
dropped. Point `action` at a real endpoint (Formspree, Netlify Forms, Apps Script, PHP) and
delete the fallback block in the script at the bottom of `index.html`.

**3. Add a privacy notice.** The footer previously linked "Privacy Policy", "Terms of Service"
and "Faculty Portal" to `href="#"` with nothing behind them; those links were removed. The
form now collects names and phone numbers, so a privacy notice is worth having before launch.

**4. Real campus photos.** See below.

## Gallery

Two ways to add photos, both without touching HTML.

**In the browser.** Open the Gallery section, press **Add photos**, pick your images. They
appear in the grid immediately, badged "Preview only — not published yet", and the tool prints
the JSON to publish them. Previews live in that browser tab only; they are gone on reload.

**By hand.** Drop files into `assets/gallery/` and add an entry per photo to
`assets/gallery/photos.json`:

```json
[
  {
    "file": "front-gate.jpg",
    "alt": "The entrance to Acumen Junior College on Ambedkar Bhavan Road",
    "caption": "Main entrance",
    "width": 1600,
    "height": 1067
  }
]
```

`file` is relative to `assets/gallery/`. `alt` is the screen-reader description, `caption` the
visible label. `width`/`height` are the image's real pixel dimensions — they stop the grid
jumping while images load, so keep them accurate. See `photos.example.json`.

Cards are built with DOM APIs rather than `innerHTML`, so captions and filenames in the
manifest cannot inject markup. The five seed cards (two directors, three results posters) are
static HTML so the gallery still renders with JavaScript disabled; manifest photos are
appended to them.

### Why the gallery is not populated from Instagram or Google Maps

This was requested and is not something the page can do on its own:

- **Instagram.** The logged-out profile page no longer exposes post IDs, so the 16 posts on
  [@acumeneduclasses](https://www.instagram.com/acumeneduclasses/) cannot be enumerated
  without an app token. Its CDN URLs are also signed and expiring, so hotlinking them would
  break the same way the Stitch URLs would have. A live feed needs either the Instagram Graph
  API oEmbed endpoint with a token, or a widget service. What the page does instead: two
  individual public posts are embedded via Instagram's keyless post embed (these do not
  expire), plus a follow card.
- **Google Maps photos.** Fetching these needs the Places Photo API with a key and billing
  enabled, and the photos belong to the contributors who uploaded them, not the college.
  Street View is embedded instead, which is the sanctioned keyless route.

The reliable path for campus photos is to shoot them or pull them from the college's own
files, then use either method above.

## Social links

Verified live against each platform's OG metadata when the page was built:

| Platform | Handle |
|---|---|
| Instagram | [@acumeneduclasses](https://www.instagram.com/acumeneduclasses/) — 300 followers, 16 posts |
| Instagram (alt) | [@acumenjuniorcollege](https://www.instagram.com/acumenjuniorcollege/) — 85 followers, 3 posts, no display name. Not linked from the page; confirm whether it is in use. |
| Facebook | [Acumen classes](https://www.facebook.com/p/Acumen-classes-100065057646214/) |
| YouTube | [@acumenclassesiitjee496](https://www.youtube.com/@acumenclassesiitjee496) |
| WhatsApp | `wa.me/917075585772` (the primary listed number) |

## Map and Street View

Both live in the `#visit` section ("Visit the Campus"), using Google's keyless embed
endpoints centred on `18.0105631, 79.5475652`. The Stitch export used a fabricated place ID
(`0x3a334f9999999999`) pointing at open farmland; the map now resolves to the real listing,
which renders as "Acumen IITJEE & NEET College".

**The Street View heading needs your eyes on it.** Six headings (0, 60, 120, 180, 240, 300)
were checked at this panorama and none shows Acumen's own signage — the nearest imagery is a
residential stretch. Heading 0 is dominated by a *different* school's parked bus, so it is
deliberately not used; the embed sits at heading 120, the cleanest neutral view.

To pin the exact frontage: open Street View on Google Maps, drag to the view you want, then
copy `cbll` (position) and the second value of `cbp` (heading) out of the URL into the
`src` on the Street View iframe.

## Changes to the Stitch export

- **`borderRadius` restored** to the `DESIGN.md` scale (`sm` 0.125 → `xl` 0.75rem,
  `full` 9999px). The export had `full: 0.75rem`, which made `rounded-full` a 12px square
  instead of a circle. Utilities were then remapped to design intent: buttons `rounded`
  (4px), cards `rounded-lg` (8px), feature banners `rounded-xl` (12px).
- **Mobile menu works** — panel with `aria-expanded`/`aria-controls`, Escape to close, closes
  on link tap, resets at the `md` breakpoint. The export's hamburger had no handler.
- **`#apply` exists.** The "Apply Now" CTA pointed at a missing anchor.
- **Gallery section** with an accessible lightbox (Escape, backdrop click, focus restored),
  driven by `assets/gallery/photos.json`, plus an in-page **Add photos** helper.
- **`#visit` section** giving Street View and the map real space, replacing the cramped
  tabbed pair that was buried in the footer. The footer now links down to it.
- **Removed** the stray `flat no shadows` classes on `<footer>` and a duplicated Material
  Symbols stylesheet link.
- **Added** meta description, Open Graph and Twitter card tags, favicon, a skip link, visible
  focus rings, `prefers-reduced-motion` handling, `width`/`height` on images, `loading="lazy"`
  below the fold, clickable `tel:`/`mailto:` contacts, and a scroll-spy nav highlight.
- Copyright year is set from the clock instead of being hardcoded to 2024.

## Note on Tailwind

The page loads Tailwind from `cdn.tailwindcss.com`, which is a development convenience — it
compiles CSS in the browser on every page load. Before launch, build the CSS with the Tailwind
CLI and ship a static stylesheet.
