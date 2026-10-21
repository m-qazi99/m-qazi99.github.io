# Muzammil Qazi — Data Workbench portfolio

[Live portfolio](https://m-qazi99.github.io/) · [Projects](https://m-qazi99.github.io/projects/) · [Project guide](https://m-qazi99.github.io/project-guide/) · [Engineering notes](https://m-qazi99.github.io/notes/) · [Contact](https://m-qazi99.github.io/contact/)

A light, glass-style portfolio by **Muzammil Qazi**, Pune, India. It connects five independent Python products, a searchable technology atlas, résumé, experience, technical evidence and contribution paths.

## Version 2.1 — find, inspect, contribute

- Search the live product cards by name or problem and filter by pipelines, quality, retrieval or privacy.
- See authorship, version, Review Desk features, user guides, source and contribution links on each card.
- Explore five Python workspaces with synthetic examples, deterministic review priorities and exportable handoffs.
- Choose Champagne, Pearl, Aurora or Rose; retain accessible navigation, keyboard focus and reduced-motion support.
- Browse 43 technologies/practices, with developing skills labeled separately from existing areas.

[Coordinated upgrade research](research/v2-repository-audit.md) · [Launch post draft](content/launch-post.md) · [Contribution guide](CONTRIBUTING.md)

## Run and maintain

Python 3.10+ is sufficient for the dependency-free static build. The public app repositories use Python 3.11+.

```bash
python scripts/build.py --public --site-url https://m-qazi99.github.io
python scripts/check.py
python scripts/check_search.py
```

Serve `docs/` with a static server for local inspection, or commit the generated `docs/` and source changes to publish with GitHub Pages. `dist/` is ignored intermediate output. The existing approved résumé is at `assets/Muzammil_Qazi_Resume.pdf`; rebuilding copies it into the website. Optional résumé/social-image generation uses `reportlab`/`pillow`; neither is needed for normal builds.

## Code map

| Path | Purpose |
|---|---|
| `content/profile.json` | Existing résumé/profile content and public contact links |
| `content/live-projects.json` | Live product names, features, versions and review summaries |
| `content/search-profile.json` | First-party identity, scope and implementation evidence |
| `scripts/build.py` | Static HTML, navigation, metadata, sitemap and deployable output |
| `scripts/studio.py` | Technology atlas, project cards and portfolio demonstrations |
| `scripts/search_presence.py`, `discovery_content.py` | Profile, project evidence, comparison and engineering notes |
| `assets/catalog.js` | Local project search and discipline filtering |
| `assets/` | Light theme styles, browser behavior, local fonts and approved résumé |
| `docs/` | GitHub Pages publishing directory |
| `research/`, `reports/` | Research decisions, validation and honest visibility baseline |

## Identity, SEO and scope

Crawlable HTML, unique titles/descriptions, canonical URLs, consistent person/project JSON-LD, social previews, sitemap and search-agent access are generated from source. `llms.txt` is optional navigation, not ranking instructions. Indexing, AI citations and rankings are not guaranteed; owner-account search reporting remains a separate step.

Earlier résumé-based case studies are distinguished from public app implementations. New products use synthetic demonstrations and were developed with Codex assistance. No employer affiliation, client outcome, production adoption or third-party endorsement is implied. Existing professional content is preserved; this upgrade does not invent résumé experience or skills.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md), use the issue/PR templates, and retain content provenance. Avoid private logs and datasets. Personal résumé content and bundled third-party fonts retain their respective rights; this repo does not grant a new blanket license over those assets. Public app code retains the MIT licenses in its own repositories.

`_headers` supports compatible static hosts but is not applied by GitHub Pages. Contact links open an email draft; there is no server submission or hidden tracking.
