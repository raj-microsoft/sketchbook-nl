import pathlib,json,urllib.request,subprocess,time
R=pathlib.Path(__file__).parent
sources=json.loads((R/'sources.json').read_text(encoding='utf8'))
(R/'originals').mkdir(exist_ok=True);(R/'photos').mkdir(exist_ok=True)
for i,s in enumerate(sources,1):
 assert s['license'].startswith(('CC BY','CC0','Public domain')),s
 dest=R/'originals'/(f'{i:02}'+pathlib.Path(s['file']).suffix)
 if not dest.exists():
  req=urllib.request.Request(s['url'],headers={'User-Agent':'NetherlandsSketchbook/1.0 (github.com/raj-microsoft/sketchbook-nl)'})
  for attempt in range(4):
   try:
    dest.write_bytes(urllib.request.urlopen(req,timeout=90).read());break
   except urllib.error.HTTPError as e:
    if e.code not in [429,503]:raise
    time.sleep(max(int(e.headers.get('Retry-After','20')),20)*(attempt+1))
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(dest),'-vf',r'scale=if(gte(iw\,ih)\,1600\,-2):if(gte(ih\,iw)\,1600\,-2)','-map_metadata','-1','-fflags','+bitexact','-flags:v','+bitexact','-q:v','3',str(R/'photos'/f'{i:02}.jpg')],check=True)
 print(i,s['place'],dest.stat().st_size,flush=True);time.sleep(2)
