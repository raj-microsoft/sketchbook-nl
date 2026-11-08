# Original geometries based on visual study; no image tracing or embedding.
def amsterdam():
 b=rect(0,0,600,410,'#b3b09a')+rect(0,0,600,38,'#8eb4c2')+path('M0 50 L600 42 600 63 0 70Z','#607d86')
 # Sweeping canal belt and roofs follow the aerial photograph's concentric structure.
 for r in range(7):
  y=70+r*45
  b+=path(f'M-60 {y+30} Q150 {y+200} 360 {y+55} T680 {y+25}','none','#475a5b',12)
  b+=path(f'M-60 {y+21} Q150 {y+190} 360 {y+46} T680 {y+16}','none','#d2c49f',4)
 for i in range(1500):
  x=random.randint(0,600);y=random.randint(65,410);w=random.randint(7,15);h=random.randint(4,9)
  b+=f'<g transform="translate({x} {y}) rotate({-24 if x>230 else 25})">'+rect(0,0,w,h,random.choice(['#786d59','#b6a183','#d1c5a6','#a18a69']))+path(f'M0 0 L{w/2} -2 L{w} 0','#e4d3ad')+'</g>'
 for x in [125,300,465]:b+=path(f'M{x} 410 L{x-25} 240 {x-16} 140','none','#344c52',9)
 return b

def giethoorn():
 b=rect(0,0,600,410,'#bdd0a2')+path('M0 0 L600 0 600 115 452 119 365 136 282 109 0 145Z','#506442')
 b+=path('M262 120 Q335 153 312 216 L570 410 H75 Q202 286 256 193Z','#9a9d65')
 b+=path('M0 410 L79 410 253 195 268 150 232 166 171 261Z','#d4c398')+path('M600 410 L566 410 360 200 343 153 393 160 458 237Z','#758942')
 b+=poly('35,70 104,63 109,172 44,181','#a99f79')+poly('98,64 146,84 145,168 108,173','#ddd0a4')+poly('21,75 95,8 113,68 100,68 82,34 41,82','#4c4e3e')+poly('95,8 147,74 146,85 113,68','#5f5e4d')
 for x in [54,79,115]:b+=rect(x,103,13,28,'#344e4b')+rect(x,133,13,4,'#ece4c9')
 b+=path('M287 146 Q349 87 416 132 L414 143 Q349 103 291 160Z','#514f37')+path('M284 131 Q348 77 418 115 M285 132 L287 150 M310 111 L310 132 M338 99 L339 117 M367 98 L368 114 M394 105 L395 123 M418 115 L417 138','none','#343f2e',5)
 for x,y,r in [(8,220,65),(87,206,35),(188,142,38),(217,97,30),(483,77,66),(568,60,78)]:
  for z in range(18):b+=f'<ellipse cx="{x+random.randint(-r,r)}" cy="{y+random.randint(-r//2,r//2)}" rx="{r//2}" ry="{r//3}" fill="{random.choice(["#64772d","#81983b","#9aa343","#bbc153"])}"/>'
 b+=path('M478 0 L463 168 M533 0 L511 185 M196 0 L206 122','none','#4e5135',6)
 b+=poly('315,206 334,181 350,198 346,216 328,224','#34474a')+f'<ellipse cx="334" cy="189" rx="6" ry="8" fill="#d5b78b"/>'+rect(329,197,12,15,'#73706a')
 for i in range(19):
  y=228+i*9;b+=path(f'M{300-i*6} {y} Q330 {y+10} {362+i*8} {y}','none','#d0c595',2)
 return b

def hoorn():
 b=rect(0,0,600,410,'#74a6cb')+rect(0,282,600,128,'#899a91')+rect(0,266,600,20,'#a8a28b')
 for x in range(0,390,38):
  h=random.randint(50,87);b+=rect(x,267-h,34,h,random.choice(['#9b795c','#b9ac86','#785e4c']))+poly(f'{x-3},{267-h} {x+17},{248-h} {x+37},{267-h}','#5a6668')
  for yy in range(270-h,253,17):b+=rect(x+7,yy,6,9,'#d9d4b8')+rect(x+22,yy,6,9,'#45585b')
 b+=poly('373,259 379,186 415,172 456,189 463,263','#d3c7a6')+poly('378,189 413,117 457,190','#556574')+poly('391,183 412,138 443,185','#81919a')+rect(409,94,12,54,'#c9b57e')+poly('405,97 415,69 424,97','#6c7270')+path('M415 74 V29','none','#b8a25c',2)
 for x in [387,404,421,440]:
  for y in [202,229]:b+=rect(x,y,7,10,'#566069')
 b+=rect(415,246,13,17,'#566069')
 for x in [52,93,131,197,251,492,539,580]:b+=path(f'M{x} 270 V{random.randint(172,220)}','none','#5b6965',2)
 b+=path('M26 285 L255 288 242 310 55 310Z','#3d535e')+path('M37 281 L255 285 257 293 39 291Z','#e7dfbc')+rect(104,261,116,22,'#d0c8b3')+rect(117,267,30,10,'#6b858b')+rect(156,267,40,10,'#6b858b')
 b+=path('M454 287 L600 315 M458 301 L600 330 M472 283 V317 M507 291 V327 M545 301 V338 M582 311 V350','none','#d1c9a9',3)
 for i in range(35):
  x=random.randint(0,600);y=random.randint(320,410);b+=path(f'M{x} {y} h{random.randint(8,50)}','none','#b6b9a2',2)
 return b

def keukenhof():
 b=rect(0,0,600,410,'#c3d1c9')+path('M0 149 L600 150 600 410 0 410Z','#8a8864')
 # Pond shape opens toward the foreground, flowers hug its banks.
 b+=path('M240 176 Q304 159 358 183 L600 410 H0 Q147 323 240 176Z','#aab4a0')+path('M0 410 L0 215 Q144 224 238 175 L242 188 Q146 263 70 410Z','#788f44')+path('M600 410 L600 192 357 177 356 191 510 278Z','#7b8b45')
 for i in range(65):
  x=random.randint(0,600);y=random.randint(85,180);r=random.randint(12,35)
  b+=f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*1.3}" fill="{random.choice(["#839346","#a3a455","#697c47","#bbc176"])}"/>'
 for x,y in [(34,224),(89,217),(166,191),(426,188),(501,196),(571,201)]:b+=path(f'M{x} {y} L{x-4} 41 M{x-3} 110 l-24 -35 M{x-3} 91 l23 -27','none','#6c6850',3)
 for i in range(300):
  x=random.randint(0,600);y=random.randint(189,276)
  if x<220-(y-189)*1.8 or x>367+(y-189)*2:
   b+=f'<ellipse cx="{x}" cy="{y}" rx="{random.randint(2,5)}" ry="2" fill="{random.choice(["#b23f34","#d76f33","#d7b64c","#e5cd77","#aa4869"])}"/>'
 for i in range(48):
  x=random.randint(120,490);y=random.randint(260,410);b+=path(f'M{x} {y} h{random.randint(10,38)}','none',random.choice(['#cbd2b9','#798b71','#e1dfbe']),3)
 b+=path('M248 188 L269 247 277 316 M347 190 L378 254 400 344','none','#757e59',13)
 return b

def afsluitdijk():
 b=rect(0,0,600,410,'#becfd5')+rect(0,138,600,272,'#9bafb4')+path('M0 84 Q171 65 600 74','none','#d4dddd',16)
 b+=poly('0,305 368,142 387,142 99,410 0,410','#909c6a')+poly('75,410 383,142 395,142 446,410','#858888')+poly('446,410 395,142 402,142 474,410','#b4ac96')+poly('474,410 402,142 405,142 506,410','#747c74')
 b+=path('M113 410 L385 142 M292 410 L390 142 M439 410 L397 142','none','#d5d1b9',3)+path('M50 410 L379 142','none','#c4c0ad',5)
 for x,y,s in [(304,373,1),(342,314,.8),(283,288,.7),(368,260,.55),(359,222,.38),(379,190,.25),(211,341,.7),(390,171,.2)]:
  b+=f'<g transform="translate({x} {y}) scale({s})">'+poly('-10,-4 8,-9 15,8 -4,14','#354b5b')+poly('-8,-4 7,-8 10,-1 -5,5','#aebfc2')+path('M-3 15 L12 10','none','#d8cbb1',3)+'</g>'
 for i in range(6):
  y=220+i*37;x=389+(y-142)*.33;b+=path(f'M{x} {y} v-10','none','#d9d1b9',2)
 b+=path('M493 410 L451 263','none','#d9ddcf',3)+poly('453,266 492,283 484,302 455,288','#e7e3ce')+path('M460 270 L487 294 M456 282 L482 297','none','#4a78a0',5)
 for x,y in [(462,277),(474,286),(484,290)]:b+=f'<ellipse cx="{x}" cy="{y}" rx="3" ry="2" fill="#ae5148"/>'
 return b

def delft():
 b=rect(0,0,600,410,'#adbfc2')+rect(0,35,600,375,'#849b86')
 # Hundreds of discrete roofs retain the density of the view without tracing it.
 for row in range(14):
  y=50+row*28
  for col in range(17):
   x=col*38+random.randint(-13,10);w=random.randint(24,41);h=random.randint(14,24)
   b+=poly(f'{x},{y} {x+w},{y+3} {x+w},{y+h+8} {x},{y+h+3}',random.choice(['#d0c6ae','#c1bba8','#8b8b7d']))+poly(f'{x-3},{y} {x+w//2},{y-10} {x+w+3},{y+3} {x+w//2},{y+10}',random.choice(['#b96c48','#9d5c43','#c18456','#7c7b70']))
   if row>5:b+=rect(x+6,y+11,5,7,'#45616b')+rect(x+18,y+12,5,7,'#45616b')
 b+=path('M142 410 L255 274 298 170','none','#668788',18)+path('M150 410 L263 274 305 172','none','#d3c9b0',3)
 b+=poly('273,147 318,127 414,164 410,205 318,180 274,193','#9a9c92')+poly('269,147 317,109 416,159 410,169 318,132 274,157','#536c77')+poly('279,146 304,139 304,192 280,196','#b6b2a1')+poly('295,139 310,135 310,90 297,90','#737e79')+poly('292,92 305,40 314,91','#425963')+path('M305 42 V18','none','#536765',2)
 for y in [99,115,131]:b+=rect(299,y,6,10,'#d4c7a5')
 for x in [328,347,366,385]:b+=path(f'M{x} 159 v29','none','#536875',6)
 return b

def zaanse():
 b=rect(0,0,600,410,'#9bbdcc')+path('M0 232 L600 215 600 410 0 410Z','#96a352')+path('M0 315 L600 258 600 281 0 345Z','#668a86')+path('M0 350 L600 287 600 302 0 373Z','#bbc082')+path('M0 388 L600 322 600 410 0 410Z','#486a4b')
 b+=path('M22 40 Q44 22 77 42 T130 48 M251 71 Q286 50 322 70 M409 37 Q445 16 487 36','none','#e2e5d4',15)
 for x,y,s in [(95,239,.5),(200,232,.62)]:b+=mill(x,y,s)
 b+=poly('284,231 329,231 321,165 295,165','#568760')+poly('290,167 324,167 317,151 298,151','#3f6754')+rect(283,217,47,10,'#d3d5b4')+rect(292,228,27,19,'#769862')+path('M308 171 L310 89 M308 171 L390 176 M308 171 L306 252 M308 171 L231 166','none','#d2d5a5',4)+path('M310 90 L319 90 317 164 M390 176 V184 L318 179 M306 252 H298 L299 181 M231 166 V158 L298 161','none','#5b8056',4)
 for x,w in [(399,55),(467,68)]:
  b+=rect(x,216,w,40,'#4e7057')+poly(f'{x-4},216 {x+12},190 {x+w-4},190 {x+w+4},216','#b7814c')+path(f'M{x} 216 h{w} M{x+w} 216 v40','none','#d5d5ad',3)+rect(x+13,229,12,16,'#c3ccab')+rect(x+w-22,231,10,25,'#35594c')
 for i in range(100):
  x=random.randint(0,600);y=random.randint(350,410);b+=path(f'M{x} {y} l{random.randint(-4,4)} -{random.randint(8,28)}','none',random.choice(['#6e8746','#3c5a45','#93a157']),2)
 return b
SCENES={1:amsterdam,2:giethoorn,3:hoorn,4:keukenhof,5:afsluitdijk,6:delft,7:zaanse}
