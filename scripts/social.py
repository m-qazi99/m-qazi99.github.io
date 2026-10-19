"""Render the original typographic social card. Requires Pillow."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).resolve().parents[1];im=Image.new('RGB',(1200,630),'#f7f7ef');d=ImageDraw.Draw(im)
def font(size,bold=False,serif=False):return ImageFont.truetype(str(R/'assets'/('editorial.ttf' if serif else 'body-bold.ttf' if bold else 'body.ttf')),size)
d.rectangle((0,0,18,630),fill='#2c4531');d.ellipse((73,55,130,112),fill='#2c4531');d.text((83,68),'mq.',font=font(18,serif=True),fill='#f7f7ef');d.text((150,68),'MUZAMMIL QAZI',font=font(20,True),fill='#2c4531')
d.text((75,175),'Reliable data.',font=font(77),fill='#20271f');d.text((75,270),'Practical AI.',font=font(77),fill='#20271f');d.text((75,371),'Less busywork.',font=font(72,serif=True),fill='#526a39')
d.line((78,508,1120,508),fill='#c9d3ba',width=2);d.text((78,543),'AZURE DATA ENGINEERING / AI WORKFLOW AUTOMATION',font=font(20),fill='#526a39');d.text((930,75),'PUNE, INDIA',font=font(16),fill='#526a39')
for x,y,t in [(915,196,'INGEST'),(915,291,'VALIDATE'),(915,386,'ASSIST')]:
 d.rounded_rectangle((x,y,x+200,y+60),radius=9,outline='#9fac8e',width=2);d.text((x+23,y+19),t,font=font(16),fill='#526a39')
d.line((1015,256,1015,291),fill='#9fac8e',width=2);d.line((1015,351,1015,386),fill='#9fac8e',width=2)
im.save(R/'assets/social-card.png',optimize=True)
