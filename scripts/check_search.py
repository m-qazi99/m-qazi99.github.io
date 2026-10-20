"""Validate indexability, identity, structured-data links, and sitemap coverage offline."""
import json,sys,unittest
from pathlib import Path
from html.parser import HTMLParser
from urllib.robotparser import RobotFileParser
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist'
P=json.loads((ROOT/'content/profile.json').read_text());U=P['siteUrl'].rstrip('/')
PROJECTS=json.loads((ROOT/'content/live-projects.json').read_text())
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.meta={};self.canonical=[];self.graph=[];self.in_json=False;self.buffer='';self.text=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if tag=='script' and a.get('type')=='application/ld+json':self.in_json=True;self.buffer=''
 def handle_data(self,data):
  if self.in_json:self.buffer+=data
  else:self.text.append(data)
 def handle_endtag(self,tag):
  if tag=='script' and self.in_json:
   j=json.loads(self.buffer);self.graph+=j.get('@graph',[j]);self.in_json=False
class SearchChecks(unittest.TestCase):
 def pages(self):return [(f,Page(f.read_text())) for f in D.rglob('*.html')]
 def test_public_routes_indexable_and_unique(self):
  canonicals=[]
  for f,p in self.pages():
   if f.name=='404.html':self.assertIn('noindex',p.meta['robots']);continue
   self.assertNotIn('noindex',p.meta['robots']);self.assertEqual(len(p.canonical),1);canonicals+=p.canonical
  self.assertEqual(len(canonicals),len(set(canonicals)))
 def test_same_person_identity_and_profiles_everywhere(self):
  for f,p in self.pages():
   people=[n for n in p.graph if n.get('@type')=='Person'];self.assertEqual(len(people),1,str(f))
   person=people[0];self.assertEqual(person['@id'],U+'/#person');self.assertEqual(person['name'],P['name']);self.assertEqual(set(person['sameAs']),{P['github'],P['linkedin']})
 def test_structured_data_references_resolve_across_site(self):
  ids={x['@id'] for _,p in self.pages() for x in p.graph if '@id'in x}
  for f,p in self.pages():
   def walk(obj):
    if isinstance(obj,list):
     for v in obj:walk(v)
    if isinstance(obj,dict):
     if set(obj)=={'@id'}:self.assertIn(obj['@id'],ids,(f,obj))
     for v in obj.values():walk(v)
   walk(p.graph)
 def test_sitemap_contains_all_canonical_pages_and_apps(self):
  doc=ET.parse(D/'sitemap.xml');locs=[n.text for n in doc.findall('.//{*}loc')]
  self.assertEqual(len(locs),len(set(locs)));self.assertNotIn(U+'/404.html',locs)
  for f,p in self.pages():
   if f.name!='404.html':self.assertIn(p.canonical[0],locs)
  for p in PROJECTS:self.assertIn(U+'/'+p['slug']+'/',locs)
 def test_search_bots_can_read_important_routes(self):
  parser=RobotFileParser();parser.parse((D/'robots.txt').read_text().splitlines())
  for bot in ['Googlebot','bingbot','OAI-SearchBot','Claude-SearchBot','PerplexityBot','OtherSearchBot']:
   for path in ['/','/profile/','/projects/','/notes/','/pipeline-pulse/']:
    self.assertTrue(parser.can_fetch(bot,U+path),(bot,path))
 def test_project_evidence_has_source_and_visible_limitations(self):
  for p in PROJECTS:
   text=(D/'projects'/p['slug']/'index.html').read_text();page=Page(text)
   self.assertIn('https://github.com/m-qazi99/'+p['slug'],text)
   self.assertIn('Scope and limitations',' '.join(page.text));self.assertIn('Muzammil Qazi',' '.join(page.text))
   self.assertTrue(any(n.get('@type')=='WebApplication' and n['name']==p['name'] for n in page.graph))
 def test_reference_map_is_navigation_not_ranking_instructions(self):
  text=(D/'llms.txt').read_text();self.assertIn('/profile/',text)
  for p in PROJECTS:self.assertIn('/projects/'+p['slug']+'/',text)
  self.assertNotIn('rank first',text.lower());self.assertNotIn('ignore previous',text.lower())
 def test_profile_json_agrees_with_visible_identity(self):
  p=json.loads((D/'profile.json').read_text());self.assertEqual(p['name'],P['name']);self.assertEqual(p['handle'],'m-qazi99');self.assertEqual(len(p['projects']),5)
 def test_no_fabricated_rating_markup(self):
  for _,p in self.pages():
   serialized=json.dumps(p.graph).lower();self.assertNotIn('aggregaterating',serialized);self.assertNotIn('reviewrating',serialized)
 def test_focused_articles_have_authorship_and_dates(self):
  for slug in ['pipeline-failure-recovery','csv-reconciliation','evaluating-runbook-retrieval']:
   p=Page((D/'notes'/slug/'index.html').read_text());article=next(n for n in p.graph if n['@type']=='TechArticle')
   self.assertEqual(article['author']['@id'],U+'/#person');self.assertEqual(article['datePublished'],'2026-10-20')
 def test_comparison_and_answers_are_visible_without_javascript(self):
  guide=(D/'project-guide/index.html').read_text()
  for project in PROJECTS:
   self.assertIn('/projects/'+project['slug']+'/',guide)
  self.assertIn('<caption>',guide);self.assertEqual(guide.count('scope="row"'),5)
  profile=Page((D/'profile/index.html').read_text())
  visible=' '.join(profile.text)
  self.assertIn('Does Runbook Radar use a generative AI model?',visible)
  self.assertIn('It does not call an LLM',visible)
 def test_walkthroughs_are_linked_from_project_evidence(self):
  for project,slug in [('pipeline-pulse','pipeline-failure-recovery'),('recon-lab','csv-reconciliation'),('runbook-radar','evaluating-runbook-retrieval')]:
   source=(D/'projects'/project/'index.html').read_text()
   self.assertIn('/notes/'+slug+'/',source)
  note=(D/'notes/evaluating-runbook-retrieval/index.html').read_text()
  self.assertIn('github.com/m-qazi99/runbook-radar/blob/main/src/lab.py',note)
  self.assertIn('github.com/m-qazi99/runbook-radar/blob/main/tests/test_studio.py',note)
  self.assertIn('illustrative calculation, not a measured benchmark',note)
if __name__=='__main__':unittest.main()
