"""Visitor-focused answers and a reproducible retrieval note, shared by the build."""
from xml.sax.saxutils import escape

FAQ = [
 ('Who built these Python applications?', 'Muzammil Qazi maintains the five independent projects under the GitHub handle m-qazi99. The builds used Codex assistance. Their public source, tests, and examples can be inspected; they are not claims of employer deployment.'),
 ('Which project checks CSV quality?', 'DataLens checks a single dataset against explicit contracts and can compare distribution drift. Recon Lab compares source and target records using business keys. Use quality checks to ask whether records satisfy a rule; use reconciliation to ask whether two snapshots agree.'),
 ('Does Runbook Radar use a generative AI model?', 'No. The public application retrieves source passages using BM25 or TF-IDF cosine similarity. It exposes matching terms and labeled retrieval evaluation. It does not call an LLM or generate operational instructions.'),
 ('Can the browser apps run Python without a server?', 'The live apps load Pyodide and execute Python in a background browser worker. The first run needs an internet connection to download the runtime. The repositories also include native Python interfaces. Browser-local processing does not make a webpage suitable for confidential data by default; use the supplied synthetic examples when exploring.'),
 ('How can I discuss a role or project?', 'Use the Contact page to share the problem, expected outcome, relevant technology, and timeline. Muzammil is based in Pune, India. Availability, working arrangements, and the scope of any engagement need a direct conversation.'),
]


def answers():
    return '<h2>Questions about the portfolio</h2><p>Short answers grounded in the public implementations.</p>' + ''.join(
      '<section class="answer-card"><h3>'+escape(q)+'</h3><p>'+escape(a)+'</p></section>' for q,a in FAQ
    ) + '<p><a href="/project-guide/">Choose a project to explore</a> · <a href="/contact/">Contact Muzammil Qazi</a></p>'


def guide():
    rows=[
      ('pipeline-pulse','Pipeline Pulse','What happens when a dependency fails?','Synthetic DAG definition, retry policy and worker budget','Completed, failed and blocked activities; recovery comparison','A scheduler model, not an Azure control plane.'),
      ('datalens','DataLens','Does this CSV satisfy our quality rules?','Dataset and explicit contracts; optional reference dataset','Record-level violations and distribution comparisons','Pass rates do not establish real-world accuracy.'),
      ('recon-lab','Recon Lab','Do source and target records agree?','Two CSV snapshots, unique keys and comparison policies','Matched, changed, missing and target-only records','Tolerances and keys need a business decision.'),
      ('runbook-radar','Runbook Radar','Which runbook passage matches this question?','Markdown notes, query, chunk controls and optional labels','Ranked passages, term contributions, MRR and Hit@K','Lexical retrieval; scores are not confidence.'),
      ('privacy-forge','Privacy Forge','What changes under a CSV privacy policy?','Synthetic CSV, column policy and quasi-identifiers','Transformed records, residual signals and audit receipt','No guarantee of anonymity or legal compliance.'),
    ]
    out='<p>Choose the tool by the question you need to answer. These five independent Python projects cover different parts of a data investigation; none substitutes for reviewing the input, policy, and result.</p><div class="comparison-scroll" role="region" aria-label="Comparison of five Python projects" tabindex="0"><table class="project-comparison"><caption>Five public Python projects by Muzammil Qazi: inputs, evidence and limits</caption><thead><tr><th scope="col">Project</th><th scope="col">Question</th><th scope="col">Inputs</th><th scope="col">Evidence</th><th scope="col">Boundary</th></tr></thead><tbody>'
    for slug,name,question,inputs,evidence,boundary in rows:
      out+='<tr><th scope="row"><a href="/projects/'+slug+'/">'+name+'</a></th>'+''.join('<td>'+escape(x)+'</td>' for x in [question,inputs,evidence,boundary])+'</tr>'
    out+='</tbody></table></div>'
    out+='''<h2>Data quality and reconciliation answer different questions</h2>
<p>A CSV can pass a not-null contract and still omit an expected customer. Conversely, two snapshots can agree while both contain the same invalid value. DataLens evaluates rules about records; Recon Lab evaluates agreement between records. A complete investigation may need both.</p>
<h2>A synthetic investigation you can reproduce</h2>
<ol><li>Open Pipeline Pulse to inspect which assets a failed dependency blocks. A blocked downstream asset is an effect, not automatically another root cause.</li><li>Use DataLens with a synthetic CSV to inspect nulls, duplicate values, ranges, and the rules chosen for that dataset.</li><li>Use Recon Lab with two snapshots to distinguish absent business keys from changed fields. Keep the selected keys and tolerance policy with the exceptions.</li><li>Use Runbook Radar to retrieve relevant notes and inspect the source passage. Relevance is not permission to execute a change.</li><li>Use Privacy Forge on a synthetic extract to examine column policies and remaining signals before considering a sharing workflow.</li></ol>
<p>The apps are separate experiments. There is no automatic connection to cloud services or cross-app transfer of your input. Use their exports to retain the evidence you choose to inspect.</p>
<h2>What to inspect in a technical review</h2>
<p>Start with the <a href="/projects/">implementation pages</a>, follow each source repository, run the supplied synthetic examples, and inspect the tests at policy boundaries. Ask whether the stated limitations match the decisions the code makes. The public work demonstrates inspectable implementation choices; it does not establish client outcomes or production scale.</p>
<h2>Read the reasoning</h2><ul><li><a href="/notes/pipeline-failure-recovery/">Pipeline failures, retries and recovery coverage</a></li><li><a href="/notes/csv-reconciliation/">Why equal row counts are insufficient</a></li><li><a href="/notes/evaluating-runbook-retrieval/">How to evaluate lexical runbook retrieval</a></li></ul>
<p><a href="/profile/">About Muzammil Qazi and the project scope</a> · <a href="/contact/">Discuss a data or automation problem</a></p>'''
    return out


def retrieval_note():
    return '''<h2>Evaluate the source passage before the answer</h2>
<p>A search interface can appear helpful while returning an irrelevant passage. Before adding a generated answer, inspect whether the retrieval step finds useful source evidence. <a href="/projects/runbook-radar/">Runbook Radar</a> isolates that step: it compares BM25 with TF-IDF cosine similarity and returns passages from supplied Markdown notes.</p>
<p>The public project is lexical search, not a generative assistant. It does not call an LLM, use embeddings, or determine whether operational instructions are correct.</p>
<h2>Keep a labeled query set separate from the demo query</h2>
<p>The <a href="https://github.com/m-qazi99/runbook-radar/blob/main/examples/studio.json">versioned synthetic example</a> contains runbook headings and four labeled queries. Each label specifies the expected document title. The query “watermark missing records” expects “Missing records and watermark gaps”. Inspect the returned passage as well as the title: a title-level hit can still contain insufficient context.</p>
<p>Use varied phrasing and keep some queries out of the tuning loop. Include questions that the corpus cannot answer. A tiny synthetic set can validate a calculation or illustrate a tradeoff; it cannot establish general retrieval quality.</p>
<h2>What do MRR and Hit@K measure here?</h2>
<p>For each labeled query, the engine finds the first positive-scoring chunk whose title matches the expected document. Reciprocal rank is one divided by that rank; it is zero when there is no matching result. Mean reciprocal rank averages those values across the supplied questions.</p>
<pre><code>Expected-title ranks: 1, 2, no match, 4
MRR = (1 + 1/2 + 0 + 1/4) / 4 = 0.4375
Hit@3 = (1 + 1 + 0 + 0) / 4 = 0.5</code></pre>
<p>These ranks are an illustrative calculation, not a measured benchmark from the app. The implementation rounds aggregate scores to three decimal places. Its MRR uses the full positive-scoring ranking; Hit@K applies the chosen K cutoff. It evaluates document-title labels against a chunk ranking, so several chunks from one title can affect the rank positions.</p>
<h2>Change chunking as a controlled experiment</h2>
<p>Runbook Radar splits each Markdown document into word windows. The studio accepts 30–300 words per chunk, overlap smaller than the chunk size, and K from 1–10. Larger overlap repeats context and increases the chunk count. It also changes the corpus statistics used by the scorers, so a score from one chunk configuration is not directly comparable with a score from another.</p>
<p>Keep the documents and labeled questions fixed while changing one control. Compare the first relevant rank, source coverage, and failure cases. The tool exposes term contributions so you can see which shared words raised a passage in the ranking.</p>
<h2>A retrieval score is not confidence</h2>
<p>BM25 ranks shared terms with frequency saturation and length normalization. TF-IDF uses weighted term vectors and cosine similarity. Neither score is a probability that a passage is correct, current, safe, or relevant to a particular production system. The implementation retains only positive-scoring matches; a query with no lexical match produces an empty result rather than fabricated evidence.</p>
<h2>Reproduce and review</h2>
<ol><li>Load the synthetic studio example in the <a href="https://m-qazi99.github.io/runbook-radar/">live Python application</a>.</li><li>Run both retrieval methods with the same chunk size, overlap, query set, and K.</li><li>Inspect the passages, matching terms, and expected-title ranks.</li><li>Export the experiment JSON to keep the inputs, scores, and evaluation context together.</li></ol>
<p>Inspect <a href="https://github.com/m-qazi99/runbook-radar/blob/main/src/lab.py">the scoring and evaluation implementation</a> and <a href="https://github.com/m-qazi99/runbook-radar/blob/main/tests/test_studio.py">tests for reciprocal rank, no-match behavior, and term contributions</a>. For adjacent tasks, read the <a href="/project-guide/">five-project guide</a>. All examples here describe independent portfolio work with synthetic content.</p>'''
