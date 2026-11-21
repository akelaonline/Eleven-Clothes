import math
W,H=1200,1500
CX=600
COLORS={
 'Negro':'#202024','Blanco':'#f5f3ee','Beige':'#d8c6a6','Camel':'#b98a55','Arena':'#d9c5a2',
 'Azul marino':'#20305a','Gris melange':'#a9acb2','Crudo':'#ece3d1','Chocolate':'#5b3b2b',
 'Champagne':'#e4d0ae','Celeste':'#b9d3ea','Nude':'#dcb9a1','Azul clásico':'#4b6c9c',
 'Tostado':'#b27b46','Azul':'#2f5fbf','Bordo':'#6e1f30','Verde':'#2f7d5b','Suela':'#a9713b',
}
def hx(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def tohex(t): return '#%02x%02x%02x'%tuple(max(0,min(255,int(round(v)))) for v in t)
def shade(h,f):
    r=hx(h)
    if f<=1: return tohex([v*f for v in r])
    return tohex([v+(255-v)*(f-1) for v in r])
def lum(h):
    r,g,b=hx(h); return (0.299*r+0.587*g+0.114*b)/255
LAST_SEAM=None
class C:
    def __init__(s,color):
        s.c=color; s.s=shade(color,0.55 if lum(color)>0.3 else 1.9)
        s.dark=lum(color)<0.3
        s.d='#ffffff' if s.dark else '#000000'
        s.dop=0.28 if s.dark else 0.22
        s.hi=shade(color,1.25 if not s.dark else 1.8)
        s.lo=shade(color,0.8)
    def body(s,d,extra=''):
        global LAST_SEAM
        import lib as _l
        seam=''
        if _l.LAST_SEAM:
            for x1,y1,x2,y2 in _l.LAST_SEAM:
                seam+=s.line(f'M{x1:.0f},{y1:.0f} Q{(x1+x2)/2+(8 if x1<CX else -8):.0f},{(y1+y2)/2-30:.0f} {x2:.0f},{y2:.0f}',w=4,op=0.3)
            _l.LAST_SEAM=None
        return (f'<path d="{d}" fill="{s.c}" stroke="{s.s}" stroke-width="5" stroke-linejoin="round" {extra}/>'
                f'<path d="{d}" fill="url(#sh)" stroke="none"/>')+seam
    def line(s,d,w=4,op=None,dash=None,color=None):
        op=s.dop if op is None else op
        col=color or s.d
        da=f' stroke-dasharray="{dash}"' if dash else ''
        return f'<path d="{d}" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{da}/>'
    def poly(s,pts,fill=None,op=1,stroke=None,w=4):
        d='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+' Z'
        return f'<path d="{d}" fill="{fill or s.c}" fill-opacity="{op}" stroke="{stroke or s.s}" stroke-width="{w}" stroke-linejoin="round"/>'
    def circ(s,x,y,r,fill=None,op=1):
        return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill or s.d}" fill-opacity="{op}"/>'
def mirror(pts): return [(2*CX-x,y) for x,y in pts]
def top_path(nw,nd,sw,sx,sl,cw,bw,ay,hw,hy,ny=300,sy=345,hemcurve=0,neckfun=None):
    O=(CX-sw-sx,sy+sl)
    ln=math.hypot(sx,sl); n=(sl/ln,sx/ln)
    I=(O[0]+n[0]*cw,O[1]+n[1]*cw)
    if I[1]>ay:
        bw=min(bw,(CX-I[0])-22)
    A=(CX-bw,ay)
    global LAST_SEAM
    LAST_SEAM=[(CX-sw+8,sy+14,A[0],A[1]),(CX+sw-8,sy+14,2*CX-A[0],A[1])]
    left=[(CX-nw,ny),(CX-sw,sy),O,I,A,(CX-hw,hy)]
    right=mirror(left)[::-1]
    d='M'+f'{left[0][0]},{left[0][1]}'
    for p in left[1:]: d+=f' L{p[0]:.1f},{p[1]:.1f}'
    if hemcurve:
        d+=f' Q{CX},{hy+hemcurve} {right[0][0]:.1f},{right[0][1]:.1f}'
    else:
        d+=f' L{right[0][0]:.1f},{right[0][1]:.1f}'
    for p in right[1:]: d+=f' L{p[0]:.1f},{p[1]:.1f}'
    d+=f' Q{CX},{ny+2*nd} {left[0][0]:.1f},{left[0][1]:.1f} Z'
    return d,dict(O=O,I=I,A=A)
def pants_path(top_w,top_y,hip_w,hip_y,leg_w_top,hem_w,hem_y,gap):
    # left leg + right leg joined at crotch
    # outer left: waist -> hip -> hem outer ; inner: hem inner -> crotch
    tl=(CX-top_w,top_y); hl=(CX-hip_w,hip_y); ho=(CX-hem_w-gap,hem_y); hi=(CX-gap,hem_y)
    cr=(CX,hip_y+ (hem_y-hip_y)*0.18)
    left=[tl,hl,ho,(CX-gap-hem_w+ (hem_w*0.0),hem_y)]
    d=f'M{tl[0]},{tl[1]} L{CX+top_w},{top_y} L{CX+hip_w},{hip_y} L{CX+hem_w+gap},{hem_y} L{CX+gap},{hem_y} L{CX},{cr[1]} L{CX-gap},{hem_y} L{CX-hem_w-gap},{hem_y} L{hl[0]},{hl[1]} Z'
    return d,cr
def svg_wrap(inner,bgtop='#efe9e0',bgbot='#e3dccf',label=True,shadow=(600,1330,330,34)):
    sx,sy,rx,ry=shadow
    lab=''
    if label:
        lab=('<text x="600" y="1442" text-anchor="middle" font-family="DejaVu Sans, sans-serif" '
             'font-size="26" letter-spacing="14" fill="#8a8173" fill-opacity="0.75">ELEVEN CLOTHES</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{bgtop}"/><stop offset="1" stop-color="{bgbot}"/></linearGradient>
<linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0.16"/><stop offset="0.5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.16"/></linearGradient>
<radialGradient id="fl" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#000" stop-opacity="0.22"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<ellipse cx="{sx}" cy="{sy}" rx="{rx}" ry="{ry}" fill="url(#fl)"/>
{inner}
{lab}
</svg>'''
