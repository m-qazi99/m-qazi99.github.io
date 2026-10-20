# Search content improvements — 20 October 2026

## Published content scope

- `/project-guide/`: a comparison of all five independent Python projects by question, inputs, evidence and limitations; a synthetic investigation workflow; links to reproducible notes.
- `/notes/evaluating-runbook-retrieval/`: an implementation-backed explanation of lexical retrieval, title labels, chunk ranking, MRR, Hit@K, chunk controls and no-match behavior. The arithmetic example is explicitly illustrative, not a benchmark.
- `/profile/`: visible direct answers about authorship, appropriate tool choice, the lexical retrieval implementation, browser Python execution and contact.
- Contextual links from project evidence pages to their corresponding technical notes, and shared navigation to the comparison guide.
- Technical notes use `og:type=article`; the existing author and TechArticle graph remain consistent with the displayed content.

## Validation

The existing site checks cover 19 HTML pages, one H1 per page, internal links, metadata, structured data, and assets. The search suite includes 12 checks covering canonical identity, sitemap coverage, public crawler access, visible project scope, source links and the new comparison/walkthrough content. The sitemap contains 23 canonical URLs including the five separate applications.

The runbook note was checked against `runbook-radar/src/lab.py`, `examples/studio.json`, and `tests/test_studio.py`. No application engines changed.

## Measurement boundary

No new claim is made about indexing, first-place rankings, AI citations, impressions or traffic. Search Console and Bing owner accounts were not accessed. The existing measurement baseline remains unmeasured; it is not overwritten with fabricated improvements.

Google's official guidance recommends crawlable, useful visible text and discoverable internal links. It does not require special AI markup or guarantee inclusion: https://developers.google.com/search/docs/appearance/ai-features
