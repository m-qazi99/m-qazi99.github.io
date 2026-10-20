"""Build human-readable, source-attributed search surfaces from first-party project facts."""
import html,json
from discovery_content import answers, guide, retrieval_note
from pathlib import Path
from xml.sax.saxutils import escape as xml
H=html.escape
ROOT=Path(__file__).resolve().parents[1]
SEARCH=json.loads((ROOT/'content/search-profile.json').read_text())
PROJECTS=json.loads((ROOT/'content/live-projects.json').read_text())


def person(profile):
    url=profile['siteUrl'].rstrip('/')
    return {'@type':'Person','@id':url+'/#person','name':profile['name'],'alternateName':SEARCH['handle'],
      'url':url+'/', 'description':SEARCH['summary'], 'jobTitle':profile['headline'],
      'sameAs':[profile['github'],profile['linkedin']],
      'homeLocation':{'@type':'Place','name':profile['location'],
       'address':{'@type':'PostalAddress','addressLocality':'Pune','addressRegion':'Maharashtra','addressCountry':'IN'}},
      'knowsAbout':['Data engineering','Python','Data quality','Pipeline investigation','AI workflow automation']}


def software(profile,p):
    url=profile['siteUrl'].rstrip('/');app=url+'/'+p['slug']+'/'
    return [{'@type':'WebApplication','@id':app+'#software','name':p['name'],'url':app,
       'description':p['summary'],'author':{'@id':url+'/#person'},'creator':{'@id':url+'/#person'},
       'applicationCategory':'DeveloperApplication','operatingSystem':'Any',
       'browserRequirements':'JavaScript and WebAssembly; internet access for the initial Python runtime download.',
       'isAccessibleForFree':True,'featureList':p['features'],
       'mainEntityOfPage':{'@id':url+'/projects/'+p['slug']+'/#webpage'}},
      {'@type':'SoftwareSourceCode','@id':'https://github.com/m-qazi99/'+p['slug']+'#sourcecode',
       'name':p['name']+' Python source','codeRepository':'https://github.com/m-qazi99/'+p['slug'],
       'programmingLanguage':['Python','JavaScript'],'author':{'@id':url+'/#person'},
       'runtimePlatform':'Python 3.11+; Pyodide 0.27.7','targetProduct':{'@id':app+'#software'}}]


def schema(profile,title,description,path,home=False):
    url=profile['siteUrl'].rstrip('/');canonical=url+path
    page={'@type':'ProfilePage' if home or path in {'/about/','/profile/'} else 'CollectionPage' if path in {'/projects/','/notes/','/project-guide/'} else 'WebPage',
      '@id':canonical+'#webpage','url':canonical,'name':title,'description':description,
      'isPartOf':{'@id':url+'/#website'},'about':{'@id':url+'/#person'},'inLanguage':'en-IN'}
    if home or path in {'/about/','/profile/'}:page['mainEntity']={'@id':url+'/#person'}
    graph=[person(profile),{'@type':'WebSite','@id':url+'/#website','url':url+'/',
       'name':profile['name']+' — Data Engineering & AI Workflow Automation',
       'publisher':{'@id':url+'/#person'},'inLanguage':'en-IN'},page]
    for p in PROJECTS:
      if path=='/projects/' or home or path=='/projects/'+p['slug']+'/':graph+=software(profile,p)
      if path=='/projects/'+p['slug']+'/':page['mainEntity']={'@id':url+'/'+p['slug']+'/#software'}
    if path=='/projects/':
      listing={'@type':'ItemList','@id':canonical+'#projects','itemListElement':[
        {'@type':'ListItem','position':i,'url':url+'/projects/'+p['slug']+'/','name':p['name']} for i,p in enumerate(PROJECTS,1)]}
      graph.append(listing);page['mainEntity']={'@id':listing['@id']}
    if path.startswith('/notes/') and path!='/notes/':
      article={'@type':'TechArticle','@id':canonical+'#article','headline':title.split(' | ')[0],
        'description':description,'author':{'@id':url+'/#person'},'publisher':{'@id':url+'/#person'},
        'datePublished':SEARCH['reviewed'],'dateModified':SEARCH['reviewed'],'inLanguage':'en-IN',
        'mainEntityOfPage':{'@id':page['@id']},'isAccessibleForFree':True}
      graph.append(article);page['mainEntity']={'@id':article['@id']}
    if path!='/':
      parts=[{'@type':'ListItem','position':1,'name':'Home','item':url+'/'}]
      if path.startswith('/projects/') and path!='/projects/':parts.append({'@type':'ListItem','position':2,'name':'Projects','item':url+'/projects/'})
      if path.startswith('/notes/') and path!='/notes/':parts.append({'@type':'ListItem','position':2,'name':'Engineering notes','item':url+'/notes/'})
      parts.append({'@type':'ListItem','position':len(parts)+1,'name':title.split(' | ')[0],'item':canonical})
      graph.append({'@type':'BreadcrumbList','@id':canonical+'#breadcrumbs','itemListElement':parts});page['breadcrumb']={'@id':canonical+'#breadcrumbs'}
    return {'@context':'https://schema.org','@graph':graph}


def identity_intro():
    return '<p class="identity-answer">Muzammil Qazi · Pune, India · Data engineering &amp; AI workflow automation. Explore my <a href="/projects/">five independent Python projects</a>, <a href="/notes/">engineering notes</a>, and <a href="/profile/">profile and source links</a>.</p>'


def article_shell(title,kicker,intro,body):
    return '<main id="main"><section class="case-hero wrap"><div class="eyebrow">'+H(kicker)+'</div><h1>'+H(title)+'</h1><p class="lead">'+H(intro)+'</p></section><article class="wrap search-article">'+body+'</article></main>'


def build(profile,dest,page):
    url=profile['siteUrl'].rstrip('/');routes=[]
    def write(route,title,description,body):
      path=dest/route.strip('/');path.mkdir(parents=True,exist_ok=True)
      (path/'index.html').write_text(page(title,description,body,path=route));routes.append(route)
    facts='<div class="fact-grid"><section class="glass"><h2>Who is Muzammil Qazi?</h2><p>'+H(SEARCH['summary'])+'</p><p>Public handle: <strong>m-qazi99</strong>. Based in <strong>Pune, Maharashtra, India</strong>.</p></section><section class="glass"><h2>What can you inspect?</h2><p>Five running Python applications, public source repositories, tests, architecture notes, and synthetic demonstrations.</p><p>'+H(SEARCH['scope'])+'</p></section></div>'
    facts+=answers()
    facts+='<h2>Canonical profiles and contact</h2><ul><li><a href="'+url+'/">Muzammil Qazi portfolio</a></li><li><a href="'+H(profile['github'])+'">GitHub: m-qazi99</a></li><li><a href="'+H(profile['linkedin'])+'">LinkedIn: Muzammil Qazi</a></li><li><a href="/contact/">Contact and project enquiries</a></li></ul><h2>Public project evidence</h2>'+project_list()+'<p class="note">Profile reviewed '+SEARCH['reviewed']+'. This page provides first-party identity and project information. It is not an independent endorsement, review, certification, or ranking.</p>'
    write('/profile/','Muzammil Qazi — Profile, Projects & Official Links',SEARCH['summary'],article_shell('Muzammil Qazi','PROFILE / FIRST-PARTY SOURCES',SEARCH['focus'],facts))
    write('/projects/','Python Projects by Muzammil Qazi | Data Engineering Portfolio','Five independent Python applications by Muzammil Qazi: pipeline simulation, data quality, CSV reconciliation, runbook retrieval, and privacy policy experiments.',article_shell('Python projects by Muzammil Qazi','PROJECTS / LIVE APPS + SOURCE','Inspect the working applications, the algorithms behind them, and their practical limits.','<p><a href="/project-guide/">Compare the five projects by question, inputs and evidence →</a></p>'+project_list()))
    write('/project-guide/','Compare Python Data Tools | Muzammil Qazi','Choose between Pipeline Pulse, DataLens, Recon Lab, Runbook Radar and Privacy Forge by the question, inputs, evidence and limitations.',article_shell('Which Python project fits your question?','A GUIDE TO THE FIVE PROJECTS','Compare data quality, reconciliation, pipeline investigation, retrieval and privacy experiments.',guide()))
    for p in PROJECTS:
      detail=SEARCH['projects'][p['slug']];app=url+'/'+p['slug']+'/';repo='https://github.com/m-qazi99/'+p['slug']
      body='<p><strong>'+H(p['name'])+'</strong> is an independent Python project by <a href="/profile/">Muzammil Qazi</a> in the area of '+H(detail['category'].lower())+'.</p>'
      body+='<div class="actions"><a class="button primary" href="'+app+'">Launch '+H(p['name'])+' ↗</a><a class="text-link" href="'+repo+'">Source repository ↗</a></div>'
      body+='<figure><img class="project-evidence-image" src="'+app+'studio-preview.jpg" alt="'+H(p['name'])+' interactive Python workspace" width="1204" height="709" loading="lazy"><figcaption>Screenshot of the independent portfolio application using synthetic inputs.</figcaption></figure>'
      body+='<h2>What does '+H(p['name'])+' do?</h2><p>'+H(p['summary'])+'</p><ul>'+''.join('<li>'+H(f)+'</li>' for f in p['features'])+'</ul><h2>How does the Python implementation work?</h2><p>'+H(detail['technical'])+'</p><p>The live browser application runs Python through Pyodide in a background worker. The repository includes a native Python CLI and a local HTTP API using the same engine.</p>'
      body+='<h2>Evidence and reproducibility</h2><ul>'+''.join('<li><a href="'+repo+'/'+target+'">'+label+'</a></li>' for target,label in [('tree/main/src','Python engine source'),('tree/main/tests','Automated tests'),('tree/main/examples','Synthetic example inputs'),('blob/main/docs/ARCHITECTURE.md','Architecture and tradeoffs')])+'</ul>'
      related={'pipeline-pulse':('pipeline-failure-recovery','Pipeline failure recovery'),'recon-lab':('csv-reconciliation','CSV reconciliation'),'runbook-radar':('evaluating-runbook-retrieval','Evaluating runbook retrieval')}
      if p['slug'] in related:
        slug,label=related[p['slug']];body+='<h2>Engineering walkthrough</h2><p><a href="/notes/'+slug+'/">'+label+'</a>: inspect the reasoning and reproduce the example.</p>'
      body+='<p><a href="/project-guide/">Compare this project with the other four tools</a></p>'
      body+='<h2>Scope and limitations</h2><p>'+H(detail['limitation'])+'</p><p>'+H(SEARCH['scope'])+'</p><p class="note">Project description reviewed '+SEARCH['reviewed']+'. <a href="/projects/">Compare the five projects</a> · <a href="/contact/">Contact Muzammil Qazi</a></p>'
      write('/projects/'+p['slug']+'/',p['name']+' by Muzammil Qazi | '+detail['category'],p['name']+' by Muzammil Qazi: '+detail['category'].lower()+'. Explore the Python implementation, live demo, source code, tests, and limitations.',article_shell(p['name']+' — '+detail['category'], 'INDEPENDENT PYTHON PROJECT / MUZAMMIL QAZI',p['summary'],body))
    notes=[
      ('pipeline-failure-recovery','Investigating pipeline failures with dependency graphs','A reproducible walkthrough of failure propagation, retries, recovery coverage, and completion targets in Pipeline Pulse.',pipeline_note()),
      ('csv-reconciliation','Why row counts are not enough for CSV reconciliation','A practical guide to business keys, missing records, Decimal tolerances, and reconciliation evidence using Recon Lab.',recon_note()),
      ('evaluating-runbook-retrieval','How to evaluate lexical runbook retrieval','Inspect BM25 and TF-IDF search with labeled queries, reciprocal rank, Hit@K, chunking controls, and source passages in Runbook Radar.',retrieval_note())]
    listing='<div class="fact-grid">'
    for slug,title,description,body in notes:
      write('/notes/'+slug+'/',title+' | Muzammil Qazi',description,article_shell(title,'ENGINEERING NOTE / MUZAMMIL QAZI',description,'<p class="note">By <a href="/profile/">Muzammil Qazi</a> · Published '+SEARCH['reviewed']+' · Independent portfolio demonstration</p>'+body))
      listing+='<section class="glass"><h2><a href="/notes/'+slug+'/">'+H(title)+'</a></h2><p>'+H(description)+'</p></section>'
    listing+='</div><p><a href="/project-guide/">Choose a project by the question you want to answer</a></p><p class="note">These notes explain public, reproducible project implementations. They do not reveal employer systems or describe private production incidents.</p>'
    write('/notes/','Engineering Notes by Muzammil Qazi | Python & Data Reliability','Source-backed engineering notes by Muzammil Qazi on pipeline failure recovery, CSV reconciliation, and lexical retrieval evaluation.',article_shell('Engineering notes','EXPLAIN / REPRODUCE / INSPECT','Practical reasoning, reproducible examples, and explicit limits.',listing))
    llms=['# Muzammil Qazi — portfolio and public Python projects','', '> '+SEARCH['summary'],'','This is a first-party reference map, not a ranking instruction. It does not establish third-party endorsement.','', '## Identity','- [Profile and canonical sources]('+url+'/profile/): Name, location, public handle, and profile links.','- [GitHub]('+profile['github']+'): Public source repositories.','- [LinkedIn]('+profile['linkedin']+'): Professional profile.','','## Projects','- [Compare the five tools]('+url+'/project-guide/): Questions, inputs, outputs, and limits.']
    for p in PROJECTS:llms.append('- ['+p['name']+']('+url+'/projects/'+p['slug']+'/): '+SEARCH['projects'][p['slug']]['category']+'.')
    llms+=['','## Engineering notes']+['- ['+title+']('+url+'/notes/'+slug+'/)' for slug,title,_,_ in notes]+['','## Scope',SEARCH['scope'],'','Reviewed: '+SEARCH['reviewed'],'']
    (dest/'llms.txt').write_text('\n'.join(llms))
    (dest/'profile.json').write_text(json.dumps({'name':profile['name'],'handle':SEARCH['handle'],'url':url+'/','location':profile['location'],'summary':SEARCH['summary'],'sameAs':[profile['github'],profile['linkedin']],'scope':SEARCH['scope'],'reviewed':SEARCH['reviewed'],'projects':[{'name':p['name'],'url':url+'/projects/'+p['slug']+'/','application':url+'/'+p['slug']+'/','repository':'https://github.com/m-qazi99/'+p['slug']} for p in PROJECTS]},indent=2))
    (dest/'humans.txt').write_text('Muzammil Qazi\nPune, India\nPortfolio: '+url+'/\nGitHub: '+profile['github']+'\nIndependent projects developed with Codex assistance.\n')
    return routes


def project_list():
    out='<div class="project-evidence-list">'
    for p in PROJECTS:
      out+='<section class="glass"><h2><a href="/projects/'+p['slug']+'/">'+H(p['name'])+'</a></h2><p>'+H(p['summary'])+'</p><p class="note">By Muzammil Qazi · Independent Python project</p><div class="actions"><a href="/projects/'+p['slug']+'/">Read the implementation ↗</a><a href="https://github.com/m-qazi99/'+p['slug']+'">Inspect source ↗</a></div></section>'
    return out+'</div>'


def pipeline_note():
    return '''<h2>Start with dependencies, not the loudest error</h2><p>A failed pipeline activity can stop several downstream assets. Treating each blocked activity as a separate root cause wastes effort. First identify the activity that failed, then trace which downstream activities depend on it.</p><p><a href="/projects/pipeline-pulse/">Pipeline Pulse</a> demonstrates this with a synthetic sales pipeline. Its default definition includes CRM and billing sources, landing activities, a quality gate, a sales transformation, two marts, a dashboard, and an export. None of these represent an employer system.</p>
<h2>A reproducible example</h2><p>In the public sample, an injected fault affects <code>transform</code>. With three workers, one allowed retry, and five seconds of initial backoff, the simulator completes seven of twelve activities. Four downstream activities are blocked. The failed scenario stops at 205 simulated seconds; repairing the selected transformation in the recovery comparison completes all twelve activities in 191 seconds.</p><p>These numbers describe this synthetic input and scheduling policy only. Reproduce them with <a href="https://github.com/m-qazi99/pipeline-pulse/blob/main/examples/studio.json">the versioned example input</a> and inspect <a href="https://github.com/m-qazi99/pipeline-pulse/blob/main/src/lab.py">the Python simulator</a>.</p>
<h2>Retries and repairs answer different questions</h2><p>A bounded retry may recover a transient fault if a later attempt succeeds. It still consumes activity time, and backoff counts against the completion target. Repairing a modeled persistent cause is a different experiment: the recovery comparison removes failures from the selected activity. It does not execute a real operational change.</p><p>The simulator holds a worker slot during retry backoff. This explicit simplification matters when comparing worker budgets; a production orchestrator may use different scheduling behavior.</p>
<h2>Measure coverage before celebrating speed</h2><p>A failed run can appear faster because it skips blocked work. Compare completed activities and failed or blocked assets before comparing elapsed time. A short run with an incomplete dashboard is not a successful recovery.</p><p>The capacity planner tests worker budgets from one through eight under the same graph, retry policy, and selected repair. It recommends the smallest tested budget that completes every activity within the chosen target. Its utilization figure excludes backoff and is not a cloud billing estimate.</p>
<h2>Use the graph as an investigation aid</h2><ol><li>Keep the source definition and business dependency relationships intact.</li><li>Identify the failing activity and trace its downstream impact.</li><li>Test whether retry policy or a modeled repair restores full completion.</li><li>Compare completion targets and resource budgets under the same assumptions.</li><li>Retain the input and result as evidence so another person can reproduce the experiment.</li></ol><p><a href="https://m-qazi99.github.io/pipeline-pulse/#arena">Try the incident arena</a> or <a href="https://github.com/m-qazi99/pipeline-pulse/tree/main/tests">inspect the tests</a>. The exercise grades deterministic conditions; it is not an assessment of a live incident or proof of production reliability.</p>'''


def recon_note():
    return '''<h2>Equal row counts can conceal different records</h2><p>A source and target can each contain three rows while disagreeing on which business keys exist and which values belong to those keys. Row counts are a starting signal; they do not establish source-to-target equality.</p><p><a href="/projects/recon-lab/">Recon Lab</a> makes those differences inspectable. It indexes unique business keys, compares selected fields, and distinguishes changed values from missing and target-only records. Composite keys are supported when a single column is not unique.</p>
<h2>A small example with four distinct outcomes</h2><p>Consider these synthetic snapshots:</p><div class="fact-grid"><section class="glass"><h3>Source</h3><pre><code>id,amount\n1,10.00\n2,20.00\n3,30.00</code></pre></section><section class="glass"><h3>Target</h3><pre><code>id,amount\n1,10.02\n2,22.00\n4,40.00</code></pre></section></div><p>Using <code>id</code> as the key and an absolute amount tolerance of <code>0.05</code> produces one matching record (key 1), one changed record (key 2), one missing record (key 3), and one target-only record (key 4). Both files have three rows, yet most of the records require attention.</p>
<h2>Tolerance is a business policy</h2><p>The Python engine compares numeric values using Decimal arithmetic. A field matches when its absolute difference is no greater than the larger of the absolute tolerance and the source-relative tolerance:</p><pre><code>abs(source - target) &lt;= max(absolute_tolerance,\n    relative_percent / 100 * abs(source))</code></pre><p>For example, a source value of 100 and target value of 110 match at a 10% source-relative tolerance. That does not mean a ten-unit difference is acceptable for your business process. The policy must match the unit, precision, and intended use of the field.</p><p>Text comparison is exact unless trimming and case folding are explicitly enabled. A numeric tolerance cannot fix a missing key. Duplicate or blank keys are rejected because they make a one-record-to-one-record comparison ambiguous.</p>
<h2>Investigate exceptions, then inspect totals</h2><p>Use the record inspector to see source and target values beside the field-level difference. The tolerance frontier shows how changing an absolute threshold alters matching coverage under the current text and relative policies. Control totals can reveal aggregate changes, but equal aggregates can still hide offsetting differences or missing keys.</p><p>The application exports an exception ledger and comparison policy. It does not alter either input. A reproducible handoff should retain the chosen keys, compared fields, tolerances, normalization rules, and exceptions.</p><p>Inspect <a href="https://github.com/m-qazi99/recon-lab/blob/main/src/lab.py">the Python implementation</a>, <a href="https://github.com/m-qazi99/recon-lab/tree/main/tests">the boundary tests</a>, and <a href="https://m-qazi99.github.io/recon-lab/">the live experiment</a>. These are independent portfolio examples, not claims about employer data or achieved reconciliation accuracy.</p>'''
