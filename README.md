# Muzammil Qazi — Portfolio

**Live website: https://m-qazi99.github.io/**

Personal portfolio for Azure data engineering, AI workflow automation and intelligent data operations. Built with semantic HTML, responsive CSS, a small JavaScript navigation enhancement and a Python static-site generator. No JavaScript framework, API credentials or server is required.

## Structure

- `content/profile.json` — profile, projects, experience, skills, education and professional links.
- `assets/` — styles, navigation, local fonts, social image and résumé PDF.
- `scripts/build.py` — renders the home page, three case studies, metadata, sitemap, robots rules and source download.
- `scripts/check.py` — validates local links, anchors, metadata and output assets.
- `scripts/resume.py` — optional résumé generator (requires ReportLab).
- `scripts/social.py` — optional social-card generator (requires Pillow).
- `docs/` — generated public site, published by GitHub Pages from the `main` branch.

## Edit and publish

1. Edit `content/profile.json` for project details and professional content. Page structure and fixed section copy are in `scripts/build.py`.
2. Update `assets/style.css` for appearance. To replace the résumé, put the approved PDF at `assets/Muzammil_Qazi_Resume.pdf`.
3. Run:

```sh
python3 scripts/build.py
python3 scripts/check.py
```

4. Commit and push the updated source **and `docs/`** to `main`. GitHub Pages automatically publishes the generated `docs/` folder. Build output in `dist/` is an intermediate and is ignored.

Python 3.10+ is sufficient for normal builds. The bundled font and PDF assets mean no dependency install is needed. A custom domain requires updating `siteUrl` in the profile, configuring the domain and DNS in GitHub Pages, and rebuilding.

## Features

Responsive layouts; dedicated case-study URLs; accessible navigation and focus states; reduced-motion support; native FAQ disclosures; email and LinkedIn contact; downloadable résumé; crawlable HTML; per-page SEO, canonical URLs, Open Graph PNG, JSON-LD, sitemap and robots file. The confirmed GitHub profile is linked consistently. Project diagrams illustrate documented workflows, not product screenshots. Case studies are résumé-based and do not claim independent verification, deployments or unsupported performance metrics.

No tracking, fake contact form or private operational documents are included. Email uses the visitor's mail application. Public indexing is enabled, with no promise of indexing or ranking. `_headers` is available for compatible alternative static hosts; GitHub Pages does not apply custom headers from that file.

## Optional authoring dependencies

```sh
python3 -m pip install reportlab pillow
python3 scripts/resume.py
python3 scripts/social.py
python3 scripts/build.py
python3 scripts/check.py
```

DejaVu fonts are bundled under `assets/FONT-LICENSE.txt`. All website source and assets needed to maintain or redeploy the site are included here. No Site hosting identity or credentials are required for GitHub Pages.


## Interactive Data Workbench upgrade

The site uses a light glass visual identity and an original orbital monogram. Visitors can choose Champagne (default), Pearl, Aurora, or Rose. The selection persists locally across visits. New visitor features:

- Searchable atlas of 43 technologies and practices across six disciplines.
- Project category filters and three selectable synthetic pipeline scenarios.
- Dedicated `/about/` and `/contact/` pages.
- A contact brief builder that opens a prepared email in the visitor's mail application.
- Keyboard controls, focus outlines, responsive layouts, and reduced-motion support.

`content/profile.json` remains the professional content source. `scripts/studio.py` contains the additional components and technology groups. `assets/app.js` handles filters, scenarios, navigation, and mailto composition. The build mirrors `dist/` to `docs/` for GitHub Pages.

### Verification

```sh
python3 scripts/build.py
python3 scripts/check.py
node --check assets/app.js
```

The route checker validates all seven pages, local links, metadata, structured data, sitemap, résumé, and source archive. Browser checks cover the main interactions.

### Research and scope

See [the review of all 19 supplied references](research/profile-inspiration.md). The GitHub profile's matching banners and expandable technology atlas live in [m-qazi99/m-qazi99](https://github.com/m-qazi99/m-qazi99). Project summaries retain their original evidence boundaries; the pipeline explorer uses synthetic data and makes no live AI calls.

### Light glass themes

The shared CSS uses semantic palette variables. `assets/theme.js` applies a saved palette before first paint; the header selector saves changes locally. All four palettes remain light. Glass uses readable surface tints, modest blur on key panels, and a no-blur fallback. The existing skill search, project filters, pipeline scenarios, and contact builder are retained.
