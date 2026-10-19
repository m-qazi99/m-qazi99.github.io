"""Generate a concise public resume without unsupported metrics. Requires reportlab."""
import json
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from xml.sax.saxutils import escape
R=Path(__file__).resolve().parents[1];p=json.loads((R/'content/profile.json').read_text())
pdfmetrics.registerFont(TTFont('Body',str(R/'assets/body.ttf')))
pdfmetrics.registerFont(TTFont('Bold',str(R/'assets/body-bold.ttf')))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold')
s=getSampleStyleSheet()
s.add(ParagraphStyle(name='Name',fontName='Bold',fontSize=23,leading=28,textColor=HexColor('#2c4531'),spaceAfter=7))
s.add(ParagraphStyle(name='Sub',fontName='Body',fontSize=9,leading=13,textColor=HexColor('#536445'),spaceAfter=7))
s.add(ParagraphStyle(name='SectionX',fontName='Bold',fontSize=9,leading=13,textColor=HexColor('#2c4531'),spaceBefore=12,spaceAfter=6))
s.add(ParagraphStyle(name='TextX',fontName='Body',fontSize=8.3,leading=12,textColor=HexColor('#30392b'),spaceAfter=5))
s.add(ParagraphStyle(name='RoleX',fontName='Bold',fontSize=8.5,leading=12,spaceBefore=6,spaceAfter=3))
story=[]
def add(text,style='TextX'):story.append(Paragraph(text,s[style]))
add(p['name'],'Name');add('AZURE DATA ENGINEER | AI WORKFLOW AUTOMATION','Sub')
add('Pune, India | <link href="mailto:'+p['email']+'">'+p['email']+'</link><br/><link href="'+p['linkedin']+'">linkedin.com/in/muzammil-1209-qazi</link>','Sub')
story.append(HRFlowable(width='100%',color=HexColor('#becbad'),thickness=.7))
add('PROFILE','SectionX');add('Azure data engineer with enterprise experience at Cognizant spanning data ingestion, transformation, validation, troubleshooting, and operational documentation. Applies AI-assisted workflows to pipeline diagnostics, SQL generation, and knowledge retrieval.')
add('CORE CAPABILITIES','SectionX')
add('Azure Data Factory | ADLS Gen2 | Databricks | Python | PySpark | SQL / T-SQL | ETL / ELT | Data Quality | Reconciliation | Monitoring | Runbooks | Git | Azure DevOps | Streamlit | LLM APIs')
add('EXPERIENCE - COGNIZANT TECHNOLOGY SOLUTIONS, PUNE','SectionX')
for r in p['experience']:
 add(escape(r['role']+' | '+r['dates'].replace('—','-')),'RoleX')
 add(escape(r['focus']))
 add(' '.join(escape(x) for x in r['points']))
add('SELECTED PROJECTS','SectionX')
for project in p['projects']:
 add('<b>'+escape(project['name'])+'</b><br/>'+escape(project['summary']))
add('DEVELOPING SKILLS','SectionX');add(escape(' | '.join(p['learning'])))
add('EDUCATION','SectionX')
for e in p['education']:add(escape((e['degree']+' | '+e['dates']).replace('—','-').replace('·','-'))+'<br/>'+escape(e['school']))
(R/'assets').mkdir(exist_ok=True)
SimpleDocTemplate(str(R/'assets/Muzammil_Qazi_Resume.pdf'),pagesize=(595.28,841.89),rightMargin=43,leftMargin=43,topMargin=35,bottomMargin=30,title='Muzammil Qazi - Public Resume',author='Muzammil Qazi').build(story)
print('Generated concise public resume.')
