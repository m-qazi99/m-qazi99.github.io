# Coordinated repository upgrade — 21 October 2026

## Audit before implementation

All eight repositories were inspected through GitHub metadata and trees. The five apps already had runnable Python, native CLI/local HTTP interfaces, worker-based browser studios, synthetic fixtures and tests. Improvements needed to explain outputs and guide contributions; they did not require replacing the existing engine structure. Existing source entry points and public slugs were preserved.

| Repository | Purpose | Why this upgrade | Delivered scope |
|---|---|---|---|
| `pipeline-pulse` | Synthetic dependency scheduling and recovery | Raw simulation results need an investigation handoff | Failed activities, blocked assets, recovery/capacity review |
| `datalens` | CSV quality contracts and drift | A quality score omits contract coverage gaps | Uncovered columns, failed contracts and drift review |
| `recon-lab` | Key-based source-to-target reconciliation | Aggregate counts need field/key prioritization | Missing/target-only records and field mismatch review |
| `runbook-radar` | Explainable lexical retrieval | Attractive search results need evaluation context | Label coverage, top-K misses, no-match and sample-size review |
| `privacy-forge` | Column privacy policy experiments | Transformations need residual-signal review | Retained signals, singleton groups and QI selection review |
| `m-qazi99` | Public GitHub profile | Project screenshots alone lack a concise feature story | Original light SVG product cards with author, version and live/source links |
| `m-qazi99.github.io` | Portfolio and public evidence | Visitors need to find a relevant product quickly | Search/category project finder, docs/contribution links and v2.1 feature attribution |
| `Reverse` | Previously empty | An empty repository provides no usable entry point | Data Workbench Catalog: canonical project records, offline validator, tests and contributor hub |

## Research and design decisions

- GitHub documents README purpose, relative documentation links, and community health files. We added project-specific READMEs, user/API/development guides, contribution instructions, security reporting, conduct standards, issue forms and PR templates.
- Brittany Chiang's portfolio separates selected work, experience and an archive. The transferable idea here is readable project context and direct evidence links. No claim of affiliation and no copied visual assets.
- Bruno Simon's portfolio demonstrates interaction as part of exploring work. The transferable idea is purposeful interaction: run experiments, filter relevant projects, inspect evidence and export handoffs. The implementation retains accessible, light HTML/CSS/SVG rather than copying his site.
- GitHub README pages do not run arbitrary app JavaScript. Profile interaction uses clickable original cards and native disclosures; full interactive behavior remains on the live products.
- Technical terms describe actual code and verified existing skill categories. Developing areas remain labeled. No invented endorsements, certifications, usage counts, or production outcomes.

Primary references:

- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests
- https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
- https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
- https://brittanychiang.com/
- https://bruno-simon.com/

The earlier references mentioned in conversation were not attached as a concrete profile collection in this task. These public first-party examples are additional research, not a claim to have inspected unavailable attachments.

## Implementation boundary

The new Python `review.py` consumes an existing `lab` result and adds deterministic priorities plus Markdown/JSON artifacts. It does not call an LLM, mutate input datasets or execute fixes. The browser Review Desk consumes those priorities; filters and checkmarks are UI state. A new experiment or reload clears checkmarks. Full exports can include input; review exports can contain field names, activity IDs, queries and titles even when cell values are excluded.

The catalog retains the historic `Reverse` repository URL; its README now clearly states its purpose. Other public repository names and APIs remain stable. No activity, contribution totals, citations, users or performance claims were fabricated.
