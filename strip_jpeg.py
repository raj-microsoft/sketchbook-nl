# Remove every optional JPEG application/comment segment; do not touch pixels.
import pathlib
for p in (pathlib.Path(__file__).parent/'photos').glob('*.jpg'):
 d=p.read_bytes();out=bytearray(d[:2]);i=2
 while i<len(d):
  start=i
  assert d[i]==255
  while d[i]==255:i+=1
  m=d[i];i+=1
  if m in [0xda,0xd9]:out.extend(d[start:]);break
  size=int.from_bytes(d[i:i+2],'big');end=i+size
  if not (0xe0<=m<=0xef or m==0xfe):out.extend(d[start:end])
  i=end
 p.write_bytes(out)
 print(p.name,'all APP0–APP15 and COM segments stripped')
