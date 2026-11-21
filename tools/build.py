import sys,os,subprocess,unicodedata
sys.path.insert(0,'/home/claude/gen')
from lib import *
from garments import GARMENTS
from products import PRODUCTS
OUT='/home/claude/eleven-clothes/products'
os.makedirs(OUT,exist_ok=True)
only=sys.argv[1:] 
def slugc(c): return unicodedata.normalize('NFKD',c.lower()).encode('ascii','ignore').decode().replace(' ','-')
n=0
for pid,slug,g,cols,alt in PRODUCTS:
    if only and slug not in only: continue
    for col in cols:
        k=C(COLORS[col])
        inner=GARMENTS[g](k)
        # background tone adapts: light garments -> slightly darker bg
        bt,bb=('#e8e1d6','#d9d0c1') if lum(COLORS[col])>0.7 else ('#efe9e0','#e3dccf')
        # auto-fit: render garment alone to get bbox
        import tempfile
        tmp=svg_wrap(inner,'none','none',label=False,shadow=(0,0,0,0)).replace('<rect width="1200" height="1500" fill="url(#bg)"/>','')
        tf=tempfile.mktemp(suffix='.svg'); open(tf,'w').write(tmp)
        tp=tf.replace('.svg','.png')
        subprocess.run(['rsvg-convert','-w','1200','-h','1500',tf,'-o',tp],check=True)
        bbox=subprocess.run(['convert',tp,'-trim','-format','%w %h %X %Y','info:'],capture_output=True,text=True).stdout.split()
        os.remove(tf); os.remove(tp)
        bw_,bh_=int(bbox[0]),int(bbox[1]); bx=int(bbox[2].replace('+','')); by=int(bbox[3].replace('+',''))
        tw,th=820,1020
        sc=min(tw/bw_,th/bh_,1.7)
        cxb=bx+bw_/2; cyb=by+bh_/2
        tcx,tcy=600,760
        inner=f'<g transform="translate({tcx-cxb*sc:.1f},{tcy-cyb*sc:.1f}) scale({sc:.4f})">'+inner+'</g>'
        shy=tcy+bh_*sc/2+18
        svg=svg_wrap(inner,bt,bb,shadow=(600,shy,min(bw_*sc*0.5,380),30))
        base=f'{OUT}/{slug}-{slugc(col)}'
        open(base+'.svg','w').write(svg)
        subprocess.run(['rsvg-convert','-w','1000','-h','1250',base+'.svg','-o',base+'.png'],check=True)
        subprocess.run(['convert',base+'.png','-quality','88',base+'.jpg'],check=True)
        os.remove(base+'.png'); os.remove(base+'.svg')
        n+=1
print('generated',n)
