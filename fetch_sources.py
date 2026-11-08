import urllib.request,urllib.parse,json,time,pathlib,re,html
ROOT=pathlib.Path(__file__).parent
UA={'User-Agent':'NetherlandsSketchbook/1.0 (educational art; github.com/raj-microsoft/sketchbook-nl)'}
def get(url):
 for attempt in range(4):
  try: return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=45))
  except urllib.error.HTTPError as e:
   if e.code not in [429,503]: raise
   time.sleep(max(int(e.headers.get('Retry-After','15')),15)*(attempt+1))
places=['Kinderdijk','Canals of Amsterdam','Giethoorn','Hoorn','Keukenhof','Afsluitdijk','Delft','Zaanse Schans']
results=[]
for place in places:
 q=urllib.parse.urlencode({'action':'query','titles':place,'prop':'pageimages','format':'json','piprop':'name'})
 p=next(iter(get('https://en.wikipedia.org/w/api.php?'+q)['query']['pages'].values()))
 name=p.get('pageimage'); print(place,name,flush=True)
 if not name: continue
 q=urllib.parse.urlencode({'action':'query','titles':'File:'+name,'prop':'imageinfo','iiprop':'url|extmetadata','format':'json'})
 info=next(iter(get('https://commons.wikimedia.org/w/api.php?'+q)['query']['pages'].values()))['imageinfo'][0]
 m=info['extmetadata']; clean=lambda k:html.unescape(re.sub('<[^>]+>','',m.get(k,{}).get('value','')))
 item={'place':place,'file':name,'url':info['url'].split('?')[0],'source':info['descriptionurl'],'author':clean('Artist'),'license':clean('LicenseShortName'),'licenseUrl':clean('LicenseUrl'),'date':clean('DateTimeOriginal'),'description':clean('ImageDescription')}
 results.append(item);print(item,flush=True);(ROOT/'sources.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf8');time.sleep(5)
(ROOT/'sources.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf8')
