# Search and AI discovery implementation — 20 October 2026

## What was observed

- The root robots.txt already allowed general crawling. Search access was not blocked by that file.
- The sitemap contained the home page, About, Contact, and three older case studies. It omitted the five running applications and dedicated descriptions of their implementations.
- The portfolio's structured data used an inline Person without a shared stable entity ID. It did not connect authored projects and code to one consistent identity graph.
- The app entry points had an empty application container and relied on JavaScript for their important content.
- A limited public search surfaced the existing LinkedIn profile matching the supplied username and Pune context. It did not establish reliable portfolio placement. Absence from that search is not proof that Google or Bing has excluded the site.
- Live rankings, Search Console impressions, Bing citations, and answers from individual AI products were not measured. No position or citation improvement is claimed.

## Changes

- One consistent Person identity: Muzammil Qazi, m-qazi99, Pune, public GitHub and supplied LinkedIn URLs.
- Linked WebSite, ProfilePage/WebPage, WebApplication, SoftwareSourceCode, ItemList, TechArticle, and BreadcrumbList entities where the corresponding visible content exists.
- Five readable project evidence pages, a project index, a factual profile page, and two source-linked engineering notes with reproducible examples.
- Static app introductions and visible implementation/scope sections that exist without executing JavaScript or downloading Python.
- Canonical URLs, author and social metadata, indexable public pages, and noindex on the 404 page.
- Sitemap expanded to 21 unique URLs, including every canonical content page and all five app URLs.
- Explicit permissions for documented search crawlers, while retaining the pre-existing general Allow policy.
- An optional llms.txt navigation map and profile.json. These are convenience reference files, not ranking signals or instructions for AI systems to recommend this person.
- A concise, expandable attribution section in the existing image-led GitHub profile.

## Platform-specific scope

| Platform | Relevant implementation | Measurement boundary |
|---|---|---|
| Google Search / AI Overviews / AI Mode | Googlebot access, indexable HTML, canonical URLs, sitemap, visible evidence | Requires verified Search Console data to establish indexing and query performance |
| Gemini | Readable public content; existing general crawl policy retained, including Google-Extended eligibility | Inclusion and response placement are controlled by Google; no model answer test claimed |
| ChatGPT search | OAI-SearchBot allowed; consistent identity, source pages, and readable project text | No ChatGPT citation or position measured |
| Claude search | Claude-SearchBot allowed; source-linked summaries and explicit project scope | No Claude citation or position measured |
| Perplexity | PerplexityBot allowed; readable source pages and project attribution | No Perplexity citation or position measured |
| Grok | Publicly accessible, source-attributed HTML and normal search discoverability | No verified xAI-specific crawler control was identified in the official web-search documentation reviewed; no invented bot rule added |
| Bing / Copilot | bingbot access, sitemap, canonical content and stable authorship | Requires verified Bing Webmaster Tools data, including eligible AI citation reporting |

Crawler permission makes retrieval possible; it does not compel indexing, citation, endorsement, model training, or recommendation. Search visibility and inclusion in model training are different concepts. Training preferences were not changed to manufacture a ranking promise.

## Official references reviewed

- Google AI features: https://developers.google.com/search/docs/appearance/ai-features
- Google crawler and Google-Extended definitions: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers
- OpenAI search versus training crawlers: https://developers.openai.com/api/docs/bots
- Anthropic crawler roles: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity crawler roles: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- xAI web search: https://docs.x.ai/developers/tools/web-search
- Bing AI measurement: https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/

## Remaining owner-account steps

1. Verify the exact `https://m-qazi99.github.io/` URL-prefix property in Google Search Console. Add only a real issued HTML verification token or file; no placeholder verification is published.
2. Submit `https://m-qazi99.github.io/sitemap.xml` through the verified property and inspect the home, profile, project index, and key project URLs.
3. Verify the site in Bing Webmaster Tools and submit the same sitemap. Inspect crawl/index reports and available AI Performance citations.
4. Keep LinkedIn's website field and GitHub's public website field pointed at the canonical portfolio. No LinkedIn account changes were made in this task.
5. Measure a fixed set of branded and relevant project questions over time, recording actual citations and URLs rather than a fabricated universal AI rank.

No Search Console, Bing account verification, sitemap submission through those accounts, paid campaign, backlink purchase, or third-party endorsement was performed.
