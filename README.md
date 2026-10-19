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
