import pathlib,struct,json,subprocess
root=pathlib.Path(__file__).parent
report=[]
for p in sorted((root/'photos').glob('*.jpg')):
 data=p.read_bytes();assert data[:2]==b'\xff\xd8';i=2;markers=[]
 while i<len(data):
  assert data[i]==255
  while data[i]==255:i+=1
  marker=data[i];i+=1
  if marker in [0xda,0xd9]:break
  length=int.from_bytes(data[i:i+2],'big');payload=data[i+2:i+length]
  if marker==0xfe or 0xe0<=marker<=0xef:markers.append(hex(marker))
  i+=length
 assert not markers,(p.name,markers)
 v=json.loads(subprocess.check_output(['ffprobe','-v','quiet','-show_streams','-of','json',str(p)]))['streams'][0]
 assert max(v['width'],v['height'])==1600
 report.append({'file':p.name,'width':v['width'],'height':v['height'],'metadata':'No EXIF, XMP, IPTC, ICC, comments or GPS; no application/comment segments; JPEG coding structure only'})
print(json.dumps(report,indent=2));(root/'.impeccable'/'photo-check.json').write_text(json.dumps(report,indent=2))
