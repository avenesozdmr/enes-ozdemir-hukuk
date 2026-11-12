"""Build published Markdown articles while keeping the original homepage unchanged."""
from pathlib import Path
from datetime import date, datetime
import json, re, shutil, html
import yaml
import markdown

ROOT = Path(__file__).resolve().parent
OUT=ROOT/'dist'
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
for file in ('index.html','enes-ozdemir-portre.jpg'):
    shutil.copy2(ROOT/file,OUT/file)
if (ROOT/'assets').exists(): shutil.copytree(ROOT/'assets',OUT/'assets')
(OUT/'makaleler').mkdir()
items=[]
CSS='''body{margin:0;background:#f6f4ef;color:#26323c;font-family:Arial,sans-serif;line-height:1.85}header{background:#101d2b;color:#fff;padding:23px max(25px,calc((100% - 1000px)/2))}header a{color:#c8a978;text-decoration:none}main{max-width:830px;margin:70px auto;padding:0 25px}h1,h2,h3{font-family:Georgia,serif;color:#101d2b;line-height:1.25}h1{font-size:clamp(34px,5vw,56px)}.meta{color:#98784d;letter-spacing:.06em;font-size:13px}.lead{color:#687782;font-size:19px}.body img{max-width:100%;height:auto}.body a{color:#997546}.body{overflow-wrap:anywhere}.body blockquote{border-left:3px solid #c8a978;margin-left:0;padding-left:20px}footer{background:#101d2b;color:#cbd3d9;padding:35px;text-align:center;font-size:13px}footer a{color:#c8a978}'''
for file in sorted((ROOT/'icerikler').glob('*.md')):
    raw=file.read_text(encoding='utf8')
    if not raw.startswith('---\n'): continue
    try:
        _,front,body=raw.split('---',2)
        meta=yaml.safe_load(front) or {}
    except Exception as exc:
        print('Atlandı:',file.name,exc);continue
    if meta.get('published') is not True:continue
    title=str(meta.get('title','')).strip()
    if not title:continue
    slug=re.sub(r'[^a-z0-9-]','-',file.stem.lower()).strip('-') or 'makale'
    slug=re.sub('-+','-',slug)
    category=str(meta.get('category','Hukuki Makale'))
    summary=str(meta.get('summary',''))
    d=meta.get('date','')
    date_str=d.isoformat() if isinstance(d,(date,datetime)) else str(d)
    image=str(meta.get('image','') or '')
    url=f'makaleler/{slug}.html'
    content=markdown.markdown(body,extensions=['extra','sane_lists'])
    cover=f'<img src="../{html.escape(image.lstrip("/"),quote=True)}" alt="" style="max-width:100%;height:auto">' if image else ''
    page=f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} | Av. Enes ÖZDEMİR</title><meta name="description" content="{html.escape(summary,quote=True)}"><style>{CSS}</style></head><body><header><a href="../index.html#yayinlar">← ÖZDEMİR HUKUK · TÜM YAYINLAR</a></header><main><div class="meta">{html.escape(category)} · {html.escape(date_str)}</div><h1>{html.escape(title)}</h1><p class="lead">{html.escape(summary)}</p>{cover}<article class="body">{content}</article><p style="margin-top:55px;border-top:1px solid #ccc;padding-top:20px"><a href="../index.html#yayinlar">← Tüm yayınlara dön</a></p></main><footer>© Av. Enes ÖZDEMİR · Genel bilgilendirme amaçlıdır, hukuki mütalaa değildir.</footer></body></html>'''
    (OUT/url).write_text(page,encoding='utf8')
    items.append(dict(title=title,category=category,summary=summary,date=date_str,image=image,url=url))
items.sort(key=lambda a:a['date'],reverse=True)
(OUT/'makaleler.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf8')
print(f'{len(items)} yayımlanmış makale oluşturuldu. Çıktı: {OUT}')
