"""Small bespoke scientific figures. All example data is illustrative, not measured."""
from pathlib import Path
import json, math, random
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'assets'/'figures'; OUT.mkdir(exist_ok=True)
FONTS=Path('C:/Windows/Fonts')
font=ImageFont.truetype(str(FONTS/'arial.ttf'),10)
small=ImageFont.truetype(str(FONTS/'arial.ttf'),9)
bold=ImageFont.truetype(str(FONTS/'arialbd.ttf'),10)
BG='#edf2f0'; INK='#19333e'; MUTED='#647e86'; BLUE='#287faa'; TEAL='#198277'; ORANGE='#bd6841'; GRID='#cddad9'; WHITE='#ffffff'
notes=json.loads((ROOT/'project-notes.json').read_text())
def text(x,y,s,color=INK,f=font): d.text((x,y),s,fill=color,font=f)
def line(points,color=MUTED,w=1):d.line(points,fill=color,width=w)
def rect(x,y,w,h,fill=None,outline=GRID):d.rectangle((x,y,x+w,y+h),fill=fill,outline=outline)
def circle(x,y,r=3,fill=BLUE,outline=None):d.ellipse((x-r,y-r,x+r,y+r),fill=fill,outline=outline)
def arrow(x,y,xx,yy,color=BLUE):
 line([(x,y),(xx,yy)],color)
 a=math.atan2(yy-y,xx-x)
 d.polygon([(xx,yy),(xx-5*math.cos(a-.5),yy-5*math.sin(a-.5)),(xx-5*math.cos(a+.5),yy-5*math.sin(a+.5))],fill=color)
def doc(x,y,w=28,h=36,marks=3):
 rect(x,y,w,h,WHITE,MUTED)
 for i in range(marks):line([(x+5,y+8+i*7),(x+w-5,y+8+i*7)],GRID)
def cylinder(x,y,w=42,h=40):
 rect(x,y+5,w,h-10,WHITE,MUTED);d.ellipse((x,y,x+w,y+10),fill=BG,outline=MUTED);d.arc((x,y+h-10,x+w,y+h),0,180,fill=MUTED)
def matrix(x,y,cols,rows,step=7,color=BLUE):
 for r in range(rows):
  for c in range(cols):rect(x+c*step,y+r*step,step-2,step-2,color if (r*3+c*5)%7<3 else WHITE,GRID)
def grid(x,y,cols,rows,step=12,blocked=()):
 for r in range(rows):
  for c in range(cols):rect(x+c*step,y+r*step,step-1,step-1,INK if (c,r) in blocked else WHITE,GRID)
def node(x,y,label=None,color=BLUE):
 circle(x,y,4,color)
 if label:text(x+7,y-5,label)
def tree(points,edges):
 for a,b in edges:line([points[a],points[b]],MUTED)
 for x,y in points:circle(x,y,3,TEAL)
def title(s):text(9,7,s,INK,bold)
def footer(s='Concept schematic'):text(9,107,s,MUTED,small)
def check(x,y):line([(x,y+4),(x+4,y+8),(x+12,y-3)],TEAL,2)
visuals={}
for name in notes:
 im=Image.new('RGB',(240,120),BG);d=ImageDraw.Draw(im)
 if name=='concept-art-generator':
  title('Reference isolation + human review')
  for i in range(3):
   doc(10+i*7,32-i*4,24,30,2)
  text(10,72,'Style set',f=small)
  arrow(57,46,77,46)
  rect(82,27,45,46,WHITE,MUTED)
  line([(88,62),(98,44),(108,55),(118,37)],BLUE)
  text(87,78,'Draft',f=small)
  circle(151,48,12,WHITE,TEAL);check(145,46)
  arrow(130,48,137,48);arrow(165,48,179,48)
  for r in range(6):
   for c in range(6):rect(183+c*7,27+r*7,7,7,GRID if (r+c)%2 else WHITE,None)
  d.polygon([(188,65),(203,34),(216,65)],fill=TEAL)
  text(180,78,'Alpha final',f=small)
  visuals[name]='Separate style references feed a draft; a human approval gate precedes a transparent image export.'
 elif name=='qwen-image-lora-studio':
  title('Low-rank image-model adaptation')
  matrix(12,34,6,6,7);text(17,80,'W frozen',f=small)
  text(63,48,'+',BLUE,bold)
  matrix(82,34,2,6,7,TEAL);text(83,80,'B',f=small)
  text(103,48,'x',MUTED)
  matrix(119,45,6,2,7,ORANGE);text(137,80,'A',f=small)
  arrow(170,54,189,54)
  rect(195,35,30,35,WHITE,MUTED);d.ellipse((201,40,211,50),fill=ORANGE);d.polygon([(198,66),(209,51),(222,66)],fill=TEAL)
  footer('LoRA: W + BA; train adapters')
  visuals[name]='A frozen weight matrix plus two thin trainable matrices illustrates LoRA adaptation for Qwen image generation.'
 elif name=='FLUX-1-dev':
  title('Quantized LoRA training')
  for i in range(3):
   doc(10+i*9,34+i*4,28,32,2)
  text(9,81,'Image + caption',f=small)
  arrow(62,57,87,57)
  for i in range(4):rect(94+i*15,28,11,11,[INK,MUTED,BLUE,TEAL][i],None)
  text(98,43,'4-bit base',f=small)
  rect(95,61,54,20,None,BLUE);text(102,65,'LoRA',BLUE)
  line([(102,84),(102,92),(152,92),(152,73)],TEAL);arrow(152,73,148,73,TEAL)
  arrow(158,57,177,57)
  doc(184,30,40,47,2);text(185,82,'Adapter',f=small)
  visuals[name]='Captioned images train a small LoRA adapter around a quantized FLUX base model; a feedback arrow denotes training.'
 elif name=='Runeboard':
  title('Hex strategy + action selection')
  for row in range(3):
   for col in range(4):
    x=21+col*18+(row%2)*9;y=36+row*16
    pts=[(x+11*math.cos(math.pi/3*k),y+11*math.sin(math.pi/3*k)) for k in range(6)]
    d.polygon(pts,fill=WHITE,outline=GRID)
  line([(21,36),(39,36),(48,52),(66,52)],BLUE,2);circle(66,52,4,TEAL)
  text(12,87,'Hex state',f=small)
  arrow(94,51,113,51)
  pts=[(158,29),(132,53),(185,53),(121,80),(144,80),(174,80),(197,80)]
  tree(pts,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)])
  text(135,91,'Tasks / actions',f=small)
  visuals[name]='A route on a hex map is paired with hierarchical task decomposition into possible game actions.'
 elif name=='videogamesAI':
  title('Behaviour tree with shared state')
  pts=[(70,31),(35,54),(105,54),(20,80),(50,80),(90,80),(120,80)]
  tree(pts,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)])
  rect(158,29,68,60,INK,INK)
  for i,s in enumerate(['target','position','task']):text(165,35+i*16,s,'#e4eeed',small)
  arrow(111,53,152,53);arrow(152,71,124,80,TEAL)
  text(26,91,'Behaviour tree',f=small);text(168,91,'Blackboard',f=small)
  visuals[name]='A branching behaviour tree reads from and writes to a blackboard of shared game state.'
 elif name=='NazgulsUnleashed':
  title('Territory + character rule changes')
  polygons=[[(12,34),(50,25),(65,51),(41,71),(10,60)],[(50,25),(89,32),(98,63),(65,51)],[(41,71),(65,51),(98,63),(88,91),(43,94)]]
  for i,pts in enumerate(polygons):d.polygon(pts,fill=[WHITE,'#d4e6e0','#d9e4ef'][i],outline=MUTED)
  circle(48,54,4,ORANGE);circle(78,73,4,ORANGE)
  line([(48,54),(78,73)],ORANGE,2)
  text(119,30,'Nazgul domains',f=small)
  for i,s in enumerate(['territories','culture / court','units / rules']):circle(122,51+i*17,2,TEAL);text(130,46+i*17,s,f=small)
  visuals[name]='Adjacent territories and ruler locations accompany the submod’s documented culture, court, unit, and rule changes.'
 elif name=='c':
  title('Dijkstra on a blocked 2D grid')
  grid(10,27,8,6,12,[(3,0),(3,1),(3,2),(3,3),(5,4),(6,4)])
  path=[(16,33),(28,33),(28,45),(28,57),(28,69),(28,81),(40,81),(52,81),(64,81),(64,69),(76,69),(88,69),(100,69)]
  line(path,BLUE,2);circle(16,33,3,TEAL);circle(100,69,3,ORANGE)
  text(127,34,'s: start',TEAL);text(127,53,'t: target',ORANGE);text(127,75,'min path cost',BLUE,small)
  visuals[name]='A highlighted shortest route navigates around blocked cells in a two-dimensional grid.'
 elif name=='mindcraft':
  title('NPC retrieval and memory')
  cylinder(9,28,39,29);text(12,61,'Lore',f=small)
  cylinder(9,75,39,23);text(53,83,'Memory',f=small)
  arrow(54,42,110,58);arrow(92,87,110,70)
  d.ellipse((113,42,156,85),fill=WHITE,outline=BLUE);text(123,57,'LLM',BLUE)
  text(90,25,'persona + mood',f=small);arrow(133,37,133,41,TEAL)
  arrow(161,64,179,64)
  d.rounded_rectangle((183,43,227,77),radius=5,fill=WHITE,outline=MUTED)
  line([(190,54),(220,54)],GRID);line([(190,63),(213,63)],GRID)
  line([(207,80),(207,96),(67,96)],TEAL);arrow(67,96,54,89,TEAL)
  visuals[name]='World lore and character memory supply context to an LLM; personality conditions dialogue and interaction feeds memory.'
 elif name=='toxicity_es_transformers_shap':
  title('Token-level model explanations')
  tokens=['This','news','text','...']
  for i,t in enumerate(tokens):
   rect(12+i*54,29,46,17,['#d2e5e0','#f1d4c5','#c0dce4',WHITE][i],None);text(17+i*54,32,t,f=small)
  text(11,57,'SHAP',MUTED,small);line([(111,52),(111,96)],MUTED)
  for i,(a,b) in enumerate([(111,163),(83,111),(111,139),(98,111)]):rect(a,54+i*11,b-a,6,ORANGE if a==111 else BLUE,None)
  text(18,80,'XLM-R',BLUE,bold)
  footer('Attribution concept; not measured scores')
  visuals[name]='Highlighted text tokens align with signed SHAP attribution bars around a neutral baseline; bars are conceptual, not benchmark results.'
 elif name=='documentqa_back':
  title('Retrieval-augmented document QA')
  for i in range(3):doc(10+i*8,29+i*6,23,29,2)
  arrow(52,52,76,52);matrix(82,29,4,6,6)
  text(80,76,'Index',f=small)
  text(119,27,'Query',TEAL);arrow(137,40,113,50,TEAL)
  arrow(110,60,153,60)
  rect(160,42,65,41,WHITE,BLUE);text(168,47,'Answer',BLUE);line([(168,63),(215,63)],GRID);text(168,69,'[source]',MUTED,small)
  visuals[name]='Document chunks populate a vector index; a question retrieves context for a source-grounded answer.'
 elif name=='documentqa_front':
  title('Document question-answering UI')
  rect(12,26,214,73,WHITE,MUTED);rect(12,26,59,73,'#dce7e7',MUTED)
  text(19,32,'Documents',f=small)
  for i in range(3):doc(20,46+i*15,9,11,0);line([(34,50+i*15),(60,50+i*15)],MUTED)
  d.rounded_rectangle((117,35,216,51),3,fill='#d7e9ed');text(124,38,'Ask a question',f=small)
  rect(81,59,124,18,None,GRID);text(87,64,'Retrieved answer',f=small)
  rect(81,84,133,9,None,BLUE)
  visuals[name]='A compact client interface separates document selection from question entry and returned answers.'
 elif name=='libreCatastro':
  title('Cadastral parcels + spatial search')
  for pts in [[(10,35),(42,27),(49,58),(15,66)],[(42,27),(82,33),(76,65),(49,58)],[(15,66),(49,58),(58,94),(19,96)],[(49,58),(76,65),(94,90),(58,94)]]:d.polygon(pts,fill=WHITE,outline=MUTED)
  for x,y in [(32,45),(60,44),(39,77),(70,79)]:rect(x-4,y-4,8,8,'#9bcbbf',TEAL)
  d.ellipse((21,35,83,91),outline=BLUE,width=2)
  arrow(98,64,121,64);cylinder(131,32,34,45);text(125,84,'Elastic',f=small)
  for x,y in [(191,43),(208,53),(187,74),(218,81)]:circle(x,y,4,ORANGE)
  text(181,89,'Map view',f=small)
  visuals[name]='Property parcels and a spatial query connect cadastral records to an index and geographic visualization.'
 elif name=='TeaNLP-front':
  title('Editable NLP graph canvas')
  rect(10,26,217,73,WHITE,MUTED);rect(10,26,40,73,'#dce7e7',MUTED)
  for i in range(4):rect(18,36+i*13,23,6,None,MUTED)
  for a,b in [((85,48),(135,38)),((85,48),(132,79)),((135,38),(195,58)),((132,79),(195,58))]:line([a,b],BLUE)
  for x,y in [(85,48),(135,38),(132,79),(195,58)]:d.rounded_rectangle((x-14,y-8,x+14,y+8),3,fill='#d3e7e7',outline=TEAL)
  text(74,45,'text',f=small);text(120,76,'tags',f=small)
  visuals[name]='An editor palette and node canvas illustrate the Angular frontend for composing NLP graph workflows.'
 elif name=='TeaNLP':
  title('Linguistic annotations as a graph')
  for x,s in [(18,'The'),(77,'model'),(167,'learns')]:text(x,78,s,INK,bold)
  for x,s in [(20,'DT'),(81,'NN'),(171,'VB')]:text(x,94,s,TEAL,small)
  for x1,x2,top in [(29,91,44),(91,181,28)]:d.arc((x1,top,x2,92),180,360,fill=BLUE,width=2)
  text(44,38,'det',MUTED,small);text(121,22,'subject',MUTED,small)
  circle(29,73,2,BLUE);circle(91,73,2,BLUE);circle(181,73,2,BLUE)
  visuals[name]='A sample sentence carries part-of-speech tags and grammatical links, illustrating structured NLP annotations.'
 elif name=='sparknlp-huggingface-gradio':
  title('Biomedical named-entity recognition')
  text(11,31,'Text:',MUTED,small);text(43,30,'Treatment for diabetes',INK,bold)
  entity_x=43+int(d.textlength('Treatment for ',font=bold))
  entity_w=int(d.textlength('diabetes',font=bold))
  rect(entity_x-2,27,entity_w+4,18,None,TEAL)
  line([(entity_x,49),(entity_x,57),(entity_x+entity_w,57),(entity_x+entity_w,49)],TEAL)
  text(entity_x,59,'DISEASE',TEAL,small)
  for i,s in enumerate(['Tokens','Embeddings','NER']):
   x=12+i*75;rect(x,81,66,16,WHITE,GRID);text(x+5,84,s,f=small)
  visuals[name]='A disease mention is highlighted in biomedical text above the tokenizer, embedding, and named-entity stages.'
 elif name=='medium':
  title('Technical articles + code examples')
  doc(12,28,91,70,0)
  text(21,36,'NLP / APIs',BLUE,bold)
  for yy in [54,61,68,84,91]:line([(21,yy),(94,yy)],GRID)
  rect(119,33,109,60,INK,INK)
  for yy,ss,col in [(40,'POST /predict', '#87c9dc'),(56,'model(text)', '#dfe9e8'),(72,'return entities','#8dc8a8')]:text(126,yy,ss,col,small)
  visuals[name]='An article page sits beside a small serving-code excerpt, representing the repository’s technical writing index.'
 elif name=='anonymizer':
  title('Neural entities + regex redaction')
  text(12,30,'Ana   02/05   a@b.es',INK,bold)
  line([(12,46),(29,46)],TEAL,2);line([(52,46),(90,46)],TEAL,2);line([(112,46),(159,46)],ORANGE,2)
  text(177,32,'NER',TEAL,small);text(177,47,'Regex',ORANGE,small)
  arrow(93,54,93,69)
  for x,w in [(12,26),(52,44),(112,56)]:rect(x,78,w,13,INK,None)
  text(177,80,'Hidden',MUTED,small)
  visuals[name]='Neural recognition identifies names and dates while regex detects an email; the output masks those text spans.'
 elif name=='unsupervised_learning':
  title('Unlabeled structure')
  rng=random.Random(4)
  for cx,cy,col in [(46,57,BLUE),(99,79,TEAL),(127,40,ORANGE)]:
   for _ in range(13):circle(cx+rng.randrange(-13,14),cy+rng.randrange(-12,13),2,col)
  text(167,40,'No labels',f=small);text(167,60,'Discover',f=small);text(167,74,'structure',f=small)
  footer('Teaching topic; illustrative points')
  visuals[name]='Three unlabeled point clouds illustrate the teaching topic of discovering structure; no experiment results are claimed.'
 elif name=='supervised_learning':
  title('Labeled classification')
  line([(19,96),(19,27)],MUTED);line([(19,96),(150,96)],MUTED)
  rng=random.Random(9)
  for i in range(24):
   x=rng.randint(28,140);y=rng.randint(32,88);circle(x,y,2,BLUE if y>.4*x+16 else ORANGE)
  line([(25,26),(148,76)],TEAL,2)
  text(171,40,'x -> y',BLUE,bold);text(171,61,'Class A',BLUE,small);text(171,76,'Class B',ORANGE,small)
  footer('Teaching concept; illustrative data')
  visuals[name]='Labeled points and a separating boundary illustrate supervised classification practice, not measured model performance.'
 elif name=='graph_snippets':
  title('Gremlin JSON to Neo4j graph')
  text(10,30,'{ nodes:',BLUE,bold);text(18,46,'[...],',MUTED);text(18,61,'edges:',BLUE,bold);text(18,77,'[...] }',MUTED)
  arrow(85,58,111,58)
  pts=[(143,36),(188,29),(214,66),(172,88),(134,73)]
  tree(pts,[(0,1),(0,4),(1,2),(2,3),(3,4),(0,3)])
  text(145,97,'Cypher import',f=small)
  visuals[name]='A JSON node-and-edge structure maps into a connected property graph through Cypher imports.'
 elif name=='borme':
  title('Company / person relationships')
  for x,y in [(27,40),(29,80)]:
   circle(x,y-5,5,BLUE);d.arc((x-8,y+1,x+8,y+17),180,360,fill=BLUE,width=2)
  for x,y in [(132,35),(196,61),(125,83)]:
   rect(x-8,y-9,16,18,WHITE,TEAL)
   for xx in [x-4,x+3]:line([(xx,y-5),(xx,y+5)],TEAL)
  for pts in [[(41,41),(122,35)],[(42,46),(185,61)],[(41,81),(114,83)],[(141,36),(186,58)]]:line(pts,MUTED)
  text(11,95,'People',f=small);text(124,99,'Companies',f=small)
  visuals[name]='A bipartite-style network shows people linked to companies, the relationships explored after CSV ingestion.'
 elif name=='news_classifier':
  title('News features / classifier comparison')
  doc(10,28,31,43,3);text(10,80,'News',f=small)
  matrix(63,30,4,6,7);text(56,81,'Features',f=small)
  for yy,s in [(32,'Naive Bayes'),(55,'SVM'),(78,'Random forest')]:
   line([(94,51),(118,yy+5)],MUTED);text(124,yy,s,BLUE,small)
  visuals[name]='News becomes a feature matrix shared by alternative classifiers; no comparative accuracy is fabricated.'
 elif name=='josejuanmartinez':
  title('Profile + professional interests')
  circle(37,43,13,WHITE,BLUE);d.arc((14,57,60,98),180,360,fill=BLUE,width=2)
  for i,s in enumerate(['AI engineering','Game development','NLP / data science']):
   circle(83,35+i*24,3,TEAL);text(94,30+i*24,s,f=small)
  visuals[name]='A profile symbol accompanies the documented areas of professional work.'
 elif name=='josejuanmartinez.github.io':
  title('Repository-driven portfolio')
  rect(12,28,214,69,WHITE,MUTED);line([(12,41),(226,41)],GRID)
  for x in [19,25,31]:circle(x,34,1,BLUE)
  rect(21,49,38,39,'#dce7e7',None)
  for x in [69,118,167]:
   rect(x,50,40,39,None,GRID);line([(x+5,60),(x+34,60)],TEAL,2);line([(x+5,70),(x+34,70)],GRID);line([(x+5,78),(x+28,78)],GRID)
  visuals[name]='A miniature browser contains a personal introduction and a grid of repository cards.'
 elif name=='SoulsRandomizers':
  title('Progression-safe item permutations')
  for i in range(4):
   x=24+i*57;d.polygon([(x,29),(x+5,34),(x,39),(x-5,34)],fill=BLUE)
   rect(x-8,83,16,12,WHITE,TEAL)
  for i,j in enumerate([2,0,3,1]):arrow(24+i*57,43,24+j*57,78,BLUE if i%2 else TEAL)
  text(9,51,'keys',MUTED,small);text(172,99,'locations',MUTED,small)
  visuals[name]='Items are permuted across locations while respecting progression constraints rather than unconstrained shuffling.'
 elif name=='SoulsFormatsNEXT':
  title('Binary format reader / writer')
  for i,s in enumerate(['42 4E 44 33','00 00 00 01','10 00 FF 2A']):text(10,32+i*17,s,BLUE,small)
  arrow(97,43,125,43);arrow(125,75,97,75,TEAL)
  rect(136,27,91,68,WHITE,MUTED);text(144,33,'BND archive',INK,bold)
  for i,s in enumerate(['header','files[]','compression']):text(144,51+i*12,s,MUTED,small)
  visuals[name]='Raw binary bytes map to a structured archive object and back through format readers and writers.'
 elif name=='SoulsIds':
  title('Graph-assisted game ID naming')
  pts=[(25,41),(77,32),(97,73),(40,89)]
  tree(pts,[(0,1),(1,2),(2,3),(0,3)])
  text(12,26,'100',BLUE,small);text(66,18,'201',BLUE,small);text(81,81,'305',BLUE,small)
  arrow(108,57,131,57)
  for i,s in enumerate(['ID -> name','100 : entity','201 : region','305 : item']):text(139,29+i*18,s,INK if i else TEAL,small)
  visuals[name]='Relationships among numeric game IDs help build meaningful names in the modding helper library.'
 elif name=='yet-another-tab-control':
  title('Owner-drawn Windows Forms tabs')
  rect(13,44,211,53,WHITE,MUTED)
  for i,(s,w) in enumerate([('Tab A',59),('Tab B',59),('Tab C',59)]):
   x=13+i*65;d.rounded_rectangle((x,26,x+w,49),4,fill=WHITE if i==1 else '#d6e1e4',outline=BLUE if i==1 else MUTED);text(x+12,33,s,BLUE if i==1 else INK,small)
  line([(21,67),(155,67)],GRID);line([(21,79),(191,79)],GRID)
  visuals[name]='Differently rendered tabs show the selected state above a Windows Forms content panel.'
 elif name=='RealmsInExile':
  title('Total-conversion world model')
  land=[(20,31),(64,25),(75,41),(110,34),(126,56),(109,77),(78,75),(51,97),(28,78),(10,62)]
  d.polygon(land,fill='#d1e3db',outline=TEAL)
  for x,y in [(41,46),(73,56),(100,58),(54,79)]:
   rect(x-3,y-4,6,8,WHITE,INK);circle(x,y+10,1,BLUE)
  text(149,30,'Characters',f=small);text(149,50,'Territories',f=small);text(149,70,'Events',f=small)
  line([(142,24),(136,24),(136,87),(142,87)],MUTED)
  visuals[name]='An abstract game map and connected worldbuilding categories illustrate a total-conversion mod, not a geographic claim.'
 elif name=='making-games-with-ai-course':
  title('Machine learning for games course')
  doc(12,29,67,66,0)
  for i,s in enumerate(['01 Theory','02 Code','03 Practice']):text(19,38+i*19,s,BLUE if i==1 else INK,small)
  grid(113,29,6,5,12,[(1,1),(2,1),(4,3)])
  circle(131,83,4,TEAL);d.polygon([(166,40),(174,44),(166,48)],fill=ORANGE)
  line([(79,64),(105,64)],BLUE)
  visuals[name]='A lesson notebook is paired with a small game environment, reflecting course theory and practical exercises.'
 elif name=='deep-rl-class':
  title('Agent / environment interaction')
  d.ellipse((13,45,64,90),fill=WHITE,outline=BLUE);text(24,61,'Agent',BLUE)
  rect(160,43,69,50,WHITE,TEAL);text(168,59,'Environment',TEAL,small)
  line([(43,42),(43,29),(189,29),(189,39)],BLUE);arrow(189,39,189,43)
  text(96,16,'action',BLUE,small)
  line([(176,94),(176,102),(48,102),(48,94)],TEAL);arrow(48,94,48,90,TEAL)
  text(83,81,'state + reward',TEAL,small)
  visuals[name]='The reinforcement-learning loop sends an action to the environment and returns state and reward to the agent.'
 elif name=='openedgar':
  title('Structured data from SEC filings')
  for i in range(3):doc(10+i*8,29+i*5,39,46,0)
  text(29,52,'10-K',BLUE,bold);arrow(76,60,95,60)
  rect(101,27,74,68,WHITE,MUTED)
  for yy,s in [(33,'company'),(49,'form type'),(65,'filing date'),(81,'sections')]:text(108,yy,s,f=small)
  arrow(181,59,191,59);cylinder(197,37,29,47)
  visuals[name]='SEC filing documents are parsed into structured fields and persisted in a database.'
 else:raise ValueError(name)
 if name not in ['qwen-image-lora-studio','toxicity_es_transformers_shap','unsupervised_learning','supervised_learning']:footer()
 im.save(OUT/(name+'.png'),optimize=True)
 notes[name]['visual_description']=visuals[name]
(ROOT/'project-notes.json').write_text(json.dumps(notes,indent=2),encoding='utf-8')
print(f'Rendered {len(visuals)} bespoke figures at 240 x 120 px.')
