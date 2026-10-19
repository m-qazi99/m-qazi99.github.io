"""Check generated routes, local links, metadata, structured data and downloadable assets."""
import json, re, zipfile
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist'
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.h1=0;self.titles=0;self.metas={};self.canonical=[];self.json=False;self.structured=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id'in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.titles+=1
  if tag=='meta':self.metas[a.get('name',a.get('property',''))]=a.get('content')
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  for attr in ['href','src']:
   if attr in a:self.links.append(a[attr])
  if tag=='script' and a.get('type')=='application/ld+json':self.json=True
 def handle_data(self,data):
  if self.json:self.structured.append(json.loads(data))
 def handle_endtag(self,tag):
  if tag=='script':self.json=False
pages={}
for f in D.rglob('*.html'):
 p=Parser();p.feed(f.read_text());pages[f]=p
 assert p.h1==1 and p.titles==1,(f,'heading/title')
 assert len(p.ids)==len(set(p.ids)),(f,'duplicate id')
 for key in ['description','robots','og:title','og:description','og:image','og:url','twitter:card']:assert p.metas.get(key),(f,key)
 assert len(p.canonical)==1 and p.structured,(f,'canonical or schema')
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(D/u.path.lstrip('/')) if u.path.startswith('/') else (f.parent/u.path)
  if target.is_dir():target=target/'index.html'
  if not u.path:target=f
  assert target.is_file(),(f,link,'missing target')
  if u.fragment:
   q=Parser();q.feed(target.read_text());assert unquote(u.fragment)in q.ids,(f,link,'missing anchor')
assert (D/'Muzammil_Qazi_Resume.pdf').read_bytes().startswith(b'%PDF-')
assert (D/'assets/social-card.png').read_bytes().startswith(b'\x89PNG')
with zipfile.ZipFile(D/'portfolio-source.zip')as z:assert z.testzip()is None
ElementTree.parse(D/'sitemap.xml')
assert 'Disallow: /'in (D/'robots.txt').read_text() or 'Allow: /'in (D/'robots.txt').read_text()
print(f'PASS: {len(pages)} pages; internal routes, anchors, unique H1s, metadata, structured data, PDF, PNG, sitemap and source ZIP.')
