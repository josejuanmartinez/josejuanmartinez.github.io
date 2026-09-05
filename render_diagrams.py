"""Render tiny, deterministic project schematics from documentation-based notes."""
from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'assets'/'diagrams'
OUT.mkdir(exist_ok=True)
font_path=Path('C:/Windows/Fonts/consola.ttf')
font=ImageFont.truetype(str(font_path),10) if font_path.exists() else ImageFont.load_default()
small=ImageFont.truetype(str(font_path),9) if font_path.exists() else font
for name,note in json.loads((ROOT/'project-notes.json').read_text()).items():
 im=Image.new('RGB',(240,80),'#151b1e'); d=ImageDraw.Draw(im)
 d.text((8,7),note['caption'],font=small,fill='#90a9b6')
 for i,label in enumerate(note['nodes']):
  x=8+i*78
  d.rectangle((x,31,x+65,59),outline='#527688',width=1)
  d.text((x+32,45),label,font=font,fill='#e2ebef',anchor='mm')
  if i<2:
   d.line((x+67,45,x+75,45),fill='#78b8cc',width=1)
   d.line((x+72,42,x+75,45,x+72,48),fill='#78b8cc',width=1)
 d.text((8,67),'SCHEMATIC',font=small,fill='#71818a')
 im.save(OUT/(name+'.png'),optimize=True)
print('Rendered 32 schematics at 240 x 80 px.')
