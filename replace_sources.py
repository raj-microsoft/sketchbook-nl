exec(open('fetch_sources.py',encoding='utf8').read().split('places=')[0])
a=json.loads((ROOT/'sources.json').read_text(encoding='utf8'))
for index,name in [(5,'Afsluitdijk 1031.jpg')]:
 q=urllib.parse.urlencode({'action':'query','titles':'File:'+name,'prop':'imageinfo','iiprop':'url|extmetadata','format':'json'})
 info=next(iter(get('https://commons.wikimedia.org/w/api.php?'+q)['query']['pages'].values()))['imageinfo'][0]
 m=info['extmetadata'];clean=lambda k:html.unescape(re.sub('<[^>]+>','',m.get(k,{}).get('value','')))
 a[index].update(file=name,url=info['url'].split('?')[0],source=info['descriptionurl'],author=clean('Artist'),license=clean('LicenseShortName'),licenseUrl=clean('LicenseUrl'),date=clean('DateTimeOriginal'),description=clean('ImageDescription'))
 print(index,a[index],flush=True);time.sleep(5)
(ROOT/'sources.json').write_text(json.dumps(a,indent=2,ensure_ascii=False),encoding='utf8')
