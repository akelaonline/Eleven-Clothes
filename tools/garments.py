from lib import *

def leather_jacket(k):
    d,p=top_path(70,22,245,75,560,120,215,570,205,1010,hemcurve=0)
    s=k.body(d)
    # collar lapels
    s+=k.poly([(CX-70,300),(CX-150,330),(CX-120,470),(CX-20,360)],fill=k.lo)
    s+=k.poly([(CX+70,300),(CX+150,330),(CX+120,470),(CX+20,360)],fill=k.lo)
    # zip asymmetric
    s+=k.line(f'M{CX-15},360 L{CX-35},1010',w=7,op=0.45)
    s+=k.line(f'M{CX-15},360 L{CX-35},1010',w=2,op=0.7,dash='3 9',color='#c9c9c9' if k.dark else '#555')
    # hem band
    s+=k.line(f'M{CX-205},960 L{CX+205},960',w=4)
    # pockets zips
    s+=k.line(f'M{CX-180},760 L{CX-90},775',w=6,op=0.4)
    s+=k.line(f'M{CX+180},760 L{CX+90},775',w=6,op=0.4)
    # cuff zips
    o,i=p['O'],p['I']
    s+=k.line(f'M{o[0]+25},{o[1]-80} L{i[0]-10},{i[1]-95}',w=6,op=0.4)
    s+=k.line(f'M{2*CX-o[0]-25},{o[1]-80} L{2*CX-i[0]+10},{i[1]-95}',w=6,op=0.4)
    # seams
    s+=k.line(f'M{CX-160},480 Q{CX-120},600 {CX-190},760',w=3)
    s+=k.line(f'M{CX+160},480 Q{CX+120},600 {CX+190},760',w=3)
    return s

def puffer(k):
    d,p=top_path(95,14,240,55,540,115,225,560,235,980,hemcurve=0)
    s=k.body(d)
    # quilting bands across body
    for y in range(430,980,110):
        s+=k.line(f'M{CX-232},{y} Q{CX},{y+22} {CX+232},{y}',w=5,op=0.35)
    # sleeve bands
    o=p['O']
    for t in (0.25,0.5,0.75):
        x1=CX-240-55*t; y1=345+540*t
        x2=x1+115*0.99; y2=y1+115*0.1
        s+=k.line(f'M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f}',w=5,op=0.35)
        s+=k.line(f'M{2*CX-x1:.0f},{y1:.0f} L{2*CX-x2:.0f},{y2:.0f}',w=5,op=0.35)
    # high collar
    s+=k.poly([(CX-100,255),(CX+100,255),(CX+108,325),(CX-108,325)],fill=k.lo,w=5)
    s+=k.line(f'M{CX},255 L{CX},980',w=7,op=0.4)
    s+=k.line(f'M{CX-95},300 L{CX+95},300',w=3)
    # pockets
    s+=k.line(f'M{CX-170},780 L{CX-80},800',w=6,op=0.4)
    s+=k.line(f'M{CX+170},780 L{CX+80},800',w=6,op=0.4)
    return s

def coat(k):
    d,p=top_path(80,26,240,60,560,125,240,580,270,1260,hemcurve=0)
    s=k.body(d)
    # lapels
    s+=k.poly([(CX-80,300),(CX-210,350),(CX-150,520),(CX-30,420),(CX-25,330)],fill=k.lo)
    s+=k.poly([(CX+80,300),(CX+210,350),(CX+150,520),(CX+30,420),(CX+25,330)],fill=k.lo)
    s+=k.line(f'M{CX},430 L{CX},1260',w=4)
    for y in (560,720,880):
        s+=k.circ(CX-22,y,13); s+=k.circ(CX+22,y,13)
    # pocket flaps
    s+=k.line(f'M{CX-215},900 L{CX-95},900',w=4)
    s+=k.line(f'M{CX+215},900 L{CX+95},900',w=4)
    # texture
    for y in range(640,1240,60):
        s+=k.line(f'M{CX-250},{y} L{CX-60},{y}',w=2,op=0.08)
        s+=k.line(f'M{CX+60},{y} L{CX+250},{y}',w=2,op=0.08)
    return s

def trench(k):
    d,p=top_path(80,26,240,60,560,125,240,580,262,1210,hemcurve=0)
    s=k.body(d)
    s+=k.poly([(CX-80,300),(CX-205,345),(CX-150,500),(CX-30,420),(CX-25,330)],fill=k.lo)
    s+=k.poly([(CX+80,300),(CX+205,345),(CX+150,500),(CX+30,420),(CX+25,330)],fill=k.lo)
    # belt
    s+=k.poly([(CX-243,760),(CX+243,760),(CX+248,820),(CX-248,820)],fill=k.lo,w=4)
    s+=k.poly([(CX-28,752),(CX+28,752),(CX+28,828),(CX-28,828)],fill=k.hi,w=4)
    s+=k.line(f'M{CX+28},790 L{CX+190},805 L{CX+196},1010',w=26,op=0.0)
    s+=k.poly([(CX+30,820),(CX+80,830),(CX+80,1000),(CX+30,990)],fill=k.lo,w=4)
    # double breasted buttons
    for y in (560,650,880,970,1060):
        s+=k.circ(CX-62,y,12); s+=k.circ(CX+62,y,12)
    s+=k.line(f'M{CX},430 L{CX},750',w=4)
    # epaulettes
    s+=k.poly([(CX-195,332),(CX-110,318),(CX-100,360),(CX-190,378)],fill=k.lo,w=3)
    s+=k.poly([(CX+195,332),(CX+110,318),(CX+100,360),(CX+190,378)],fill=k.lo,w=3)
    # cuff straps
    o=p['O']
    s+=k.line(f'M{o[0]+10},{o[1]-70} L{o[0]+125},{o[1]-60}',w=18,op=0.25)
    s+=k.line(f'M{2*CX-o[0]-10},{o[1]-70} L{2*CX-o[0]-125},{o[1]-60}',w=18,op=0.25)
    return s

def blazer(k):
    d,p=top_path(75,24,235,50,540,115,205,580,215,1060)
    s=k.body(d)
    # inner v opening
    inner=shade(k.c,0.6 if not k.dark else 1.9)
    s+=k.poly([(CX-75,300),(CX+75,300),(CX+8,640),(CX-8,640)],fill=inner,op=0.9,w=3)
    # lapels
    s+=k.poly([(CX-75,300),(CX-190,355),(CX-130,520),(CX-100,470),(CX-175,420),(CX-8,640),(CX-8,640)],fill=k.lo)
    s+=k.poly([(CX+75,300),(CX+190,355),(CX+130,520),(CX+100,470),(CX+175,420),(CX+8,640),(CX+8,640)],fill=k.lo)
    s+=k.circ(CX,700,13)
    s+=k.line(f'M{CX},640 L{CX},1060',w=3,op=0.15)
    # pockets
    s+=k.line(f'M{CX-185},830 L{CX-80},835',w=5)
    s+=k.line(f'M{CX+185},830 L{CX+80},835',w=5)
    s+=k.line(f'M{CX-170},590 Q{CX-140},760 {CX-205},1000',w=3,op=0.15)
    s+=k.line(f'M{CX+170},590 Q{CX+140},760 {CX+205},1000',w=3,op=0.15)
    return s

def hoodie(k):
    d,p=top_path(105,16,255,40,520,125,265,600,265,1020,hemcurve=0)
    s=k.body(d)
    # hood
    s=(k.poly([(CX-130,250),(CX+130,250),(CX+150,320),(CX-150,320)],fill=k.lo,w=5)+s)
    s+=k.body(f'M{CX-105},300 Q{CX},430 {CX+105},300 Q{CX},350 {CX-105},300 Z')
    s+=k.line(f'M{CX-35},400 L{CX-45},560',w=8,op=0.45)
    s+=k.line(f'M{CX+35},400 L{CX+45},560',w=8,op=0.45)
    # kangaroo pocket
    s+=k.poly([(CX-170,780),(CX+170,780),(CX+215,960),(CX-215,960)],fill=k.lo,w=4)
    # rib hem + cuffs
    s+=k.line(f'M{CX-265},990 L{CX+265},990',w=4)
    o,i=p['O'],p['I']
    s+=k.line(f'M{o[0]+3},{o[1]-45} L{i[0]-3},{i[1]-52}',w=4)
    s+=k.line(f'M{2*CX-o[0]-3},{o[1]-45} L{2*CX-i[0]+3},{i[1]-52}',w=4)
    return s

def cardigan(k):
    d,p=top_path(120,70,235,55,520,110,225,600,230,1050)
    s=k.body(d)
    inner=shade(k.c,0.55 if not k.dark else 1.8)
    s+=k.poly([(CX-120,300),(CX+120,300),(CX+6,600),(CX-6,600)],fill=inner,op=0.35,w=2)
    s+=k.line(f'M{CX},400 L{CX},1050',w=4,op=0.35)
    for y in range(470,1030,95): s+=k.circ(CX,y,13); 
    # knit ribs
    for x in range(-200,201,25):
        if abs(x)>12: s+=k.line(f'M{CX+x},{660} L{CX+x},{1040}',w=2,op=0.07)
    s+=k.line(f'M{CX-230},1000 L{CX+230},1000',w=4)
    s+=k.poly([(CX-190,780),(CX-90,780),(CX-90,880),(CX-190,880)],fill=k.lo,op=0.85,w=3)
    s+=k.poly([(CX+190,780),(CX+90,780),(CX+90,880),(CX+190,880)],fill=k.lo,op=0.85,w=3)
    return s

def tee(k):
    d,p=top_path(85,32,215,60,170,140,150,620,165,1040,hemcurve=10)
    s=k.body(d)
    s+=k.line(f'M{CX-85},300 Q{CX},{300+74} {CX+85},300',w=12,op=0.18)
    return s

def top_fit(k):
    d,p=top_path(70,20,205,50,520,95,150,620,155,900,hemcurve=0)
    s=k.body(d)
    # mock neck
    s+=k.poly([(CX-75,235),(CX+75,235),(CX+82,305),(CX-82,305)],fill=k.lo,w=5)
    s+=k.line(f'M{CX-78},270 L{CX+78},270',w=3)
    # rib lines
    for x in range(-130,131,26): s+=k.line(f'M{CX+x},330 L{CX+x},890',w=2,op=0.07)
    return s

def blouse(k):
    d,p=top_path(95,70,225,55,520,110,235,610,250,1010,hemcurve=0)
    s=k.body(d)
    s+=k.poly([(CX-95,300),(CX-20,420),(CX,470),(CX+20,420),(CX+95,300),(CX+60,296),(CX,340),(CX-60,296)],fill=k.lo,op=0.9,w=3)
    s+=k.line(f'M{CX},470 L{CX},1010',w=3,op=0.3)
    # satin sheen
    s+=k.line(f'M{CX-160},520 Q{CX-120},760 {CX-210},980',w=22,op=0.14,color='#fff')
    s+=k.line(f'M{CX+110},500 Q{CX+150},740 {CX+200},960',w=14,op=0.10,color='#fff')
    o,i=p['O'],p['I']
    s+=k.line(f'M{o[0]+5},{o[1]-50} L{i[0]-5},{i[1]-58}',w=4)
    s+=k.line(f'M{2*CX-o[0]-5},{o[1]-50} L{2*CX-i[0]+5},{i[1]-58}',w=4)
    return s

def shirt(k):
    d,p=top_path(80,22,245,50,540,115,245,620,255,1080,hemcurve=26)
    s=k.body(d)
    # collar
    s+=k.poly([(CX-80,296),(CX-5,330),(CX-45,392),(CX-135,330)],fill=k.lo,w=4)
    s+=k.poly([(CX+80,296),(CX+5,330),(CX+45,392),(CX+135,330)],fill=k.lo,w=4)
    # placket
    s+=k.line(f'M{CX},335 L{CX},1090',w=3,op=0.35)
    s+=k.line(f'M{CX+38},400 L{CX+38},1085',w=2,op=0.2)
    for y in range(440,1060,90): s+=k.circ(CX+19,y,9)
    # pocket
    s+=k.poly([(CX+80,520),(CX+170,520),(CX+170,610),(CX+125,630),(CX+80,610)],fill=k.lo,op=0.6,w=3)
    o,i=p['O'],p['I']
    s+=k.line(f'M{o[0]+5},{o[1]-60} L{i[0]-5},{i[1]-70}',w=4)
    s+=k.line(f'M{2*CX-o[0]-5},{o[1]-60} L{2*CX-i[0]+5},{i[1]-70}',w=4)
    return s

def body_suit(k):
    d=(f'M{CX-190},300 L{CX-120},300 L{CX-110},395 Q{CX},420 {CX+110},395 L{CX+120},300 L{CX+190},300 '
       f'L{CX+170},640 Q{CX+175},760 {CX+120},880 L{CX+60},960 Q{CX},985 {CX-60},960 L{CX-120},880 Q{CX-175},760 {CX-170},640 Z')
    s=k.body(d)
    s+=k.line(f'M{CX-115},398 Q{CX},425 {CX+115},398',w=10,op=0.2)
    s+=k.line(f'M{CX-165},640 Q{CX-140},760 {CX-110},860',w=3,op=0.15)
    s+=k.line(f'M{CX+165},640 Q{CX+140},760 {CX+110},860',w=3,op=0.15)
    return s

def tank(k):
    d=(f'M{CX-170},260 L{CX-110},260 L{CX-100},370 Q{CX},430 {CX+100},370 L{CX+110},260 L{CX+170},260 '
       f'L{CX+165},520 Q{CX+175},640 {CX+190},1010 Q{CX},1040 {CX-190},1010 Q{CX-175},640 {CX-165},520 Z')
    s=k.body(d)
    for x in range(-150,151,24):
        s+=k.line(f'M{CX+x},470 L{CX+x*1.04},1010',w=2,op=0.09)
    s+=k.line(f'M{CX-100},370 Q{CX},430 {CX+100},370',w=8,op=0.2)
    return s

def jeans(k):
    d,cr=pants_path(175,300,200,420,0,125,1250,12)
    s=k.body(d)
    s+=k.poly([(CX-175,300),(CX+175,300),(CX+178,345),(CX-178,345)],fill=k.lo,w=3)
    s+=k.line(f'M{CX},345 L{CX},{cr[1]-60}',w=3)
    s+=k.line(f'M{CX},345 Q{CX-30},420 {CX-10},480',w=3,dash='10 8')
    s+=k.line(f'M{CX-170},350 Q{CX-120},440 {CX-60},370',w=3,dash='10 8')
    s+=k.line(f'M{CX+170},350 Q{CX+120},440 {CX+60},370',w=3,dash='10 8')
    s+=k.line(f'M{CX-190},700 L{CX-170},1230',w=2,op=0.12)
    s+=k.line(f'M{CX-130+12},1210 L{CX-12-0},1210',w=3,dash='10 8')
    s+=k.line(f'M{CX+12},1210 L{CX+130-12},1210',w=3,dash='10 8')
    s+=k.circ(CX,322,10,fill=k.hi,op=1)
    return s

def trousers(k):
    d,cr=pants_path(175,300,215,430,0,135,1250,14)
    s=k.body(d)
    s+=k.poly([(CX-175,300),(CX+175,300),(CX+178,340),(CX-178,340)],fill=k.lo,w=3)
    for x in (-130,-50,50,130): s+=k.poly([(CX+x-10,296),(CX+x+10,296),(CX+x+10,350),(CX+x-10,350)],fill=k.c,w=2)
    s+=k.line(f'M{CX},340 L{CX},{cr[1]-70}',w=3)
    # pleats
    s+=k.line(f'M{CX-70},345 L{CX-75},470',w=3,op=0.3)
    s+=k.line(f'M{CX+70},345 L{CX+75},470',w=3,op=0.3)
    # crease lines
    s+=k.line(f'M{CX-120},470 L{CX-125},1245',w=3,op=0.22)
    s+=k.line(f'M{CX+120},470 L{CX+125},1245',w=3,op=0.22)
    s+=k.line(f'M{CX-195},420 L{CX-190},480',w=5,op=0.2)
    return s

def jogger(k):
    d,cr=pants_path(175,300,215,420,0,105,1200,16)
    s=k.body(d)
    s+=k.poly([(CX-175,300),(CX+175,300),(CX+178,360),(CX-178,360)],fill=k.lo,w=3)
    s+=k.line(f'M{CX-25},350 L{CX-35},470',w=7,op=0.4)
    s+=k.line(f'M{CX+25},350 L{CX+35},470',w=7,op=0.4)
    # cuffs
    s+=k.poly([(CX-142,1150),(CX-17,1150),(CX-17,1210),(CX-142,1210)],fill=k.lo,w=3)
    s+=k.poly([(CX+17,1150),(CX+142,1150),(CX+142,1210),(CX+17,1210)],fill=k.lo,w=3)
    s+=k.line(f'M{CX-215},470 Q{CX-190},560 {CX-190},640',w=4,op=0.15)
    s+=k.line(f'M{CX+215},470 Q{CX+190},560 {CX+190},640',w=4,op=0.15)
    return s

def skirt(k):
    d=(f'M{CX-165},330 L{CX+165},330 L{CX+330},1230 Q{CX},1270 {CX-330},1230 Z')
    s=k.body(d)
    s+=k.poly([(CX-165,300),(CX+165,300),(CX+167,355),(CX-167,355)],fill=k.lo,w=4)
    for i in range(-7,8):
        x0=CX+i*22; x1=CX+i*45
        s+=k.line(f'M{x0},355 Q{(x0+x1)/2},800 {x1},1245',w=3,op=0.2 if i%2 else 0.1)
    return s

def shorts(k):
    d,cr=pants_path(175,300,205,400,0,170,850,14)
    s=k.body(d)
    s+=k.poly([(CX-175,300),(CX+175,300),(CX+178,345),(CX-178,345)],fill=k.lo,w=3)
    for x in (-130,-50,50,130): s+=k.poly([(CX+x-10,296),(CX+x+10,296),(CX+x+10,350),(CX+x-10,350)],fill=k.c,w=2)
    s+=k.line(f'M{CX},345 L{CX},{cr[1]-40}',w=3)
    s+=k.line(f'M{CX-70},345 L{CX-75},440',w=3,op=0.3)
    s+=k.line(f'M{CX+70},345 L{CX+75},440',w=3,op=0.3)
    s+=k.circ(CX+1,322,9,fill=k.hi)
    return s

def leggings(k):
    d,cr=pants_path(150,300,160,420,0,80,1280,8)
    s=k.body(d)
    s+=k.poly([(CX-150,300),(CX+150,300),(CX+153,380),(CX-153,380)],fill=k.lo,w=3)
    s+=k.line(f'M{CX-155},430 L{CX-140},1270',w=8,op=0.2)
    s+=k.line(f'M{CX+155},430 L{CX+140},1270',w=8,op=0.2)
    s+=k.line(f'M{CX},380 L{CX},{cr[1]-40}',w=3,op=0.18)
    return s

def dress_satin(k):
    d=(f'M{CX-95},210 L{CX-75},210 L{CX-60},330 Q{CX},470 {CX+60},330 L{CX+75},210 L{CX+95},210 '
       f'L{CX+105},330 Q{CX+135},470 {CX+120},560 L{CX+230},1150 Q{CX},1200 {CX-230},1150 L{CX-120},560 Q{CX-135},470 {CX-105},330 Z')
    s=k.body(d)
    s+=k.line(f'M{CX-100},330 Q{CX},520 {CX+100},330',w=5,op=0.25)
    s+=k.line(f'M{CX-120},560 Q{CX},610 {CX+120},560',w=5,op=0.18)
    s+=k.line(f'M{CX-90},660 Q{CX-140},900 {CX-180},1130',w=26,op=0.14,color='#fff')
    s+=k.line(f'M{CX+60},640 Q{CX+110},900 {CX+150},1140',w=18,op=0.10,color='#fff')
    s+=k.line(f'M{CX-30},640 Q{CX-45},900 {CX-60},1170',w=3,op=0.12)
    return s

def dress_knit(k):
    d,p=top_path(85,40,190,40,560,95,160,700,185,1170,hemcurve=14)
    s=k.body(d)
    s+=k.line(f'M{CX-85},300 Q{CX},{300+80} {CX+85},300',w=12,op=0.18)
    for x in range(-150,151,22): s+=k.line(f'M{CX+x},700 L{CX+x*1.05},1165',w=2,op=0.09)
    for x in range(-110,111,22): s+=k.line(f'M{CX+x},420 L{CX+x},700',w=2,op=0.09)
    s+=k.line(f'M{CX-185},1140 L{CX+185},1140',w=4)
    return s

def jumpsuit(k):
    d=(f'M{CX-75},230 L{CX-55},230 L{CX-30},340 L{CX},400 L{CX+30},340 L{CX+55},230 L{CX+75},230 '
       f'L{CX+100},330 Q{CX+135},420 {CX+115},560 L{CX+265},1270 L{CX+30},1270 L{CX},720 L{CX-30},1270 L{CX-265},1270 '
       f'L{CX-115},560 Q{CX-135},420 {CX-100},330 Z')
    s=k.body(d)
    s+=k.line(f'M{CX-30},340 L{CX},400 L{CX+30},340',w=5,op=0.3)
    s+=k.poly([(CX-125,540),(CX+125,540),(CX+128,605),(CX-128,605)],fill=k.lo,w=4)
    s+=k.poly([(CX-24,530),(CX+24,530),(CX+24,615),(CX-24,615)],fill=k.hi,w=3)
    s+=k.line(f'M{CX-130},620 L{CX-200},1250',w=3,op=0.15)
    s+=k.line(f'M{CX+130},620 L{CX+200},1250',w=3,op=0.15)
    return s

def sneaker(k):
    s=''
    body=('M300,1050 L305,850 Q310,800 360,795 L440,800 Q470,835 505,835 L565,772 Q650,755 705,820 Q790,885 885,922 Q955,950 958,1022 L958,1050 Z')
    s+=k.body(body)
    s+='<rect x="282" y="1040" width="688" height="78" rx="34" fill="#faf9f5" stroke="#bdb6a8" stroke-width="5"/>'
    s+='<path d="M296,1078 L956,1078" stroke="#bdb6a8" stroke-width="4" fill="none"/>'
    s+=k.line('M780,905 Q850,940 860,1040',w=4,op=0.25)
    s+=k.poly([(300,880),(345,860),(420,1030),(300,1035)],fill=k.lo,op=0.9,w=3)
    for (x,y) in [(585,800),(630,820),(675,845),(725,872),(775,895)]:
        s+=k.line(f'M{x-26},{y-6} L{x+22},{y+22}',w=8,op=0.45)
    s+=k.poly([(440,800),(500,832),(560,775),(520,740)],fill=k.lo,w=4)
    return s

def sandal(k):
    sole='#8a6a4c' if lum(k.c)<0.55 else '#a98466'
    sk='#5c4631'
    s=f'<path d="M270,1090 Q268,1135 325,1140 L850,1140 Q965,1140 975,1105 Q960,1072 895,1068 L330,1058 Q275,1058 270,1090 Z" fill="{sole}" stroke="{sk}" stroke-width="5" stroke-linejoin="round"/>'
    s+=f'<path d="M280,1140 L450,1140 L440,1300 L290,1300 Z" fill="{sole}" stroke="{sk}" stroke-width="5" stroke-linejoin="round"/>'
    def strap(d,w=40):
        return (f'<path d="{d}" fill="none" stroke="{k.s}" stroke-width="{w+8}" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="{d}" fill="none" stroke="{k.c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
    s+=strap('M330,1062 Q300,860 420,800 L560,780')
    s+=strap('M560,780 Q650,800 720,1062')
    s+=strap('M880,1068 Q850,960 770,965')
    s+=k.circ(430,810,12,fill=k.hi)
    return s

def boot(k):
    body=('M390,380 L640,380 L650,760 Q700,800 840,850 Q930,890 935,980 L935,1080 L350,1080 L350,980 Q390,900 390,820 Z')
    s=k.body(body)
    s+=k.poly([(330,1080),(960,1080),(960,1150),(330,1150)],fill=shade('#2b2622',1.0),w=4)
    s+=k.poly([(330,1150),(470,1150),(470,1290),(330,1290)],fill=shade('#2b2622',1.0),w=4)
    s+=k.line('M395,430 L640,430',w=3,op=0.2)
    s+=k.line('M640,400 L650,760',w=4,op=0.2)
    s+=k.line('M420,900 Q500,940 520,1060',w=3,op=0.2)
    s+=k.poly([(580,420),(630,420),(630,520),(580,520)],fill=k.lo,w=3)
    return s

def sandal(k):
    sole='#8a6a4c' if lum(k.c)<0.55 else '#a98466'
    s=f'<path d="M280,1100 Q270,1140 330,1150 L850,1150 Q960,1150 970,1120 Q950,1090 880,1085 L330,1070 Q285,1070 280,1100 Z" fill="{sole}" stroke="#5c4631" stroke-width="5" stroke-linejoin="round"/>'
    s+=f'<path d="M800,1150 L930,1150 L930,1290 L800,1290 Z" fill="{sole}" stroke="#5c4631" stroke-width="5" stroke-linejoin="round"/>'
    s+=k.body('M470,1060 Q520,900 640,880 Q700,880 740,900 L720,960 Q640,940 600,1010 L620,1075 Z')
    s+=k.body('M700,930 Q790,940 850,1070 L800,1078 Q750,990 690,980 Z')
    s+=k.body('M860,880 L900,880 L915,1090 L860,1085 Z')
    s+=k.circ(880,990,12,fill=k.hi)
    return s

def bra(k,ox=0,oy=0,sc=1.0):
    def T(x,y): return (CX+(x-CX)*sc+ox, 300+(y-300)*sc+oy)
    def P(pts): return [T(x,y) for x,y in pts]
    s=''
    # halter cords
    for sg in (-1,1):
        a=T(CX+sg*45,420); b=T(CX+sg*8,140)
        s+=f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="{k.s}" stroke-width="{16*sc:.1f}" stroke-linecap="round"/>'
        s+=f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="{k.c}" stroke-width="{10*sc:.1f}" stroke-linecap="round"/>'
        a=T(CX+sg*235,420); b=T(CX+sg*330,470)
        s+=f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="{k.s}" stroke-width="{16*sc:.1f}" stroke-linecap="round"/>'
        s+=f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="{k.c}" stroke-width="{10*sc:.1f}" stroke-linecap="round"/>'
    for sg in (-1,1):
        p=P([(CX+sg*38,410),(CX+sg*240,420),(CX+sg*150,640)])
        d=f'M{p[0][0]:.1f},{p[0][1]:.1f} Q{(p[0][0]+p[1][0])/2:.1f},{p[0][1]-18*sc:.1f} {p[1][0]:.1f},{p[1][1]:.1f} Q{p[1][0]+(p[2][0]-p[1][0])*0.3:.1f},{p[2][1]-10*sc:.1f} {p[2][0]:.1f},{p[2][1]:.1f} Q{p[0][0]+sg*8*sc:.1f},{(p[0][1]+p[2][1])/2:.1f} {p[0][0]:.1f},{p[0][1]:.1f} Z'
        s+=k.body(d)
        # lace scallop edge
        for t in range(7):
            x,y=T(CX+sg*(58+t*25),428+t*4)
            s+=k.circ(x,y,8*sc,op=0.22)
        for t in range(4):
            x,y=T(CX+sg*(90+t*30),500+t*28)
            s+=k.circ(x,y,6*sc,op=0.12)
    return s

def panty(k,ox=0,oy=0,sc=1.0):
    def T(x,y): return (CX+(x-CX)*sc+ox, 300+(y-300)*sc+oy)
    def q(x,y): return f'{T(x,y)[0]:.1f},{T(x,y)[1]:.1f}'
    d=(f'M{q(CX-210,350)} L{q(CX+210,350)} L{q(CX+215,430)} Q{q(CX+190,600)} {q(CX+70,690)} Q{q(CX,740)} {q(CX-70,690)} '
       f'Q{q(CX-190,600)} {q(CX-215,430)} Z')
    s=k.body(d)
    a=T(CX-210,372);b=T(CX+210,372)
    s+=k.line(f'M{a[0]},{a[1]} L{b[0]},{b[1]}',w=4,op=0.25)
    return s

def bra_solo(k):
    return bra(k,0,260,1.35)

def panty_solo(k):
    return panty(k,0,300,1.4)

def lingerie_set(k):
    return bra(k,0,-10,0.85)+panty(k,0,420,0.8)

def bikini(k):
    s=bra(k,0,-30,0.85)
    # tie ends
    s+=panty(k,0,430,0.85)
    return s

def belt(k):
    dark=shade(k.c,0.75)
    s=f'<ellipse cx="{CX}" cy="780" rx="330" ry="250" fill="none" stroke="{k.s}" stroke-width="92" />'
    s+=f'<ellipse cx="{CX}" cy="780" rx="330" ry="250" fill="none" stroke="{k.c}" stroke-width="80" />'
    s+=f'<ellipse cx="{CX}" cy="780" rx="330" ry="250" fill="none" stroke="url(#sh)" stroke-width="80" />'
    s+=f'<ellipse cx="{CX}" cy="780" rx="330" ry="250" fill="none" stroke="{k.d}" stroke-opacity="0.35" stroke-width="3" stroke-dasharray="14 12" transform="translate(0,-34)"/>'
    # buckle
    s+='<rect x="'+str(CX+220)+'" y="410" width="150" height="130" rx="14" fill="none" stroke="#b9ab8a" stroke-width="16"/>'
    s+='<rect x="'+str(CX+290)+'" y="430" width="12" height="90" fill="#b9ab8a"/>'
    # holes
    for i in range(5): s+=k.circ(CX-170+i*70,990 if i not in (0,4) else 990,10,op=0.4)
    return s

def bag(k):
    body=('M330,640 L870,640 L920,1130 Q925,1190 870,1190 L330,1190 Q275,1190 280,1130 Z')
    s=''
    # strap
    s+=f'<path d="M345,650 Q300,260 600,250 Q900,260 855,650" fill="none" stroke="{k.s}" stroke-width="40" stroke-linecap="round"/>'
    s+=f'<path d="M345,650 Q300,260 600,250 Q900,260 855,650" fill="none" stroke="{k.lo}" stroke-width="30" stroke-linecap="round"/>'
    s+=k.body(body)
    flap='M300,640 L900,640 L880,820 Q600,900 320,820 Z'
    s+=k.body(flap)
    s+=k.line('M320,860 Q600,940 880,860',w=3,dash='10 8')
    s+=k.poly([(570,810),(630,810),(630,890),(570,890)],fill=k.hi,w=4)
    s+=k.circ(600,850,10,fill=k.s)
    s+=k.line('M345,1150 L855,1150',w=3,dash='10 8')
    return s

GARMENTS={
 'leather_jacket':leather_jacket,'puffer':puffer,'coat':coat,'trench':trench,'blazer':blazer,
 'hoodie':hoodie,'cardigan':cardigan,'tee':tee,'top_fit':top_fit,'blouse':blouse,'shirt':shirt,
 'body_suit':body_suit,'tank':tank,'jeans':jeans,'trousers':trousers,'jogger':jogger,'skirt':skirt,
 'shorts':shorts,'leggings':leggings,'dress_satin':dress_satin,'dress_knit':dress_knit,'jumpsuit':jumpsuit,
 'sneaker':sneaker,'boot':boot,'sandal':sandal,'bra':bra_solo,'panty':panty_solo,'lingerie_set':lingerie_set,
 'bikini':bikini,'belt':belt,'bag':bag,
}
