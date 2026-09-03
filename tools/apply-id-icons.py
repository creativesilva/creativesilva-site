#!/usr/bin/env python3
# Assignment identification icons (framework). Inserts a small orange "assignment type"
# chip (icon + label, EN in #top, ES in #espanol) right after the banner on every active
# module page. Idempotent (skips pages that already have the <!--IDCHIP--> marker), so it
# is safe to re-run, and MUST be re-run after regenerating any builder module (a fresh
# build has no chip). Icons live in assets/Icons/assignment/.
#
# Icon family so far: overview, your-device (homework, own phone/tablet), camera-kit
# (project needing a camera kit checkout), photo-walk (camera kit during class), reflection.
# Still needed (no icon yet): editing, contact sheet, research/find, worksheet, design/build, sketch.
import os
ROOT=os.path.join(os.path.dirname(__file__), "..", "curriculum", "shared")
SITE="https://www.creativesilva.com"
ICO=SITE+"/assets/Icons/assignment"
BSIG='<div style="background:linear-gradient(135deg,#000000 0%,#003838 40%,#007474 100%)'

LABELS={
 "overview":("overview.png","Overview","Resumen"),
 "your-device":("your-device.png","Capture on Your Device","Captura en Tu Dispositivo"),
 "camera-kit":("camera-kit.png","Camera Kit Project","Proyecto con Equipo de C&aacute;mara"),
 "photo-walk":("photo-walk.png","Photo Walk","Caminata Fotogr&aacute;fica"),
 "reflection":("reflection.png","Reflection","Reflexi&oacute;n"),
}
def chip(kind, es):
    icon,en_lab,es_lab=LABELS[kind]
    kicker="Tipo de Tarea" if es else "Assignment Type"
    lab=es_lab if es else en_lab
    return ('<!--IDCHIP--><div style="display:flex;align-items:center;gap:14px;margin:0 0 22px;padding:11px 16px;'
      'background:rgba(255,107,26,0.08);border:1px solid rgba(255,107,26,0.28);border-left:4px solid #FF6B1A;">'
      f'<img src="{ICO}/{icon}" alt="{lab}" style="width:50px;height:50px;display:block;flex:0 0 auto;" />'
      f'<div><div style="font-size:9pt;letter-spacing:0.2em;text-transform:uppercase;color:#ffb27c;margin-bottom:2px;"><strong>{kicker}</strong></div>'
      f'<div style="font-size:15pt;color:#ffffff;"><strong>{lab}</strong></div></div></div>')

def after_banner(h, frm):
    bi=h.find(BSIG, frm); assert bi!=-1, "banner not found"
    j=bi+4; depth=1
    while depth>0:
        no=h.find('<div',j); nc=h.find('</div>',j); assert nc!=-1
        if no!=-1 and no<nc: depth+=1; j=no+4
        else:
            depth-=1
            if depth==0: return nc+6
            j=nc+6

def apply(fname, kind):
    p=os.path.join(ROOT,fname)
    if not os.path.exists(p): print("  MISSING:", fname); return
    h=open(p,encoding='utf-8').read()
    if '<!--IDCHIP-->' in h: print("  ok (already):", fname); return
    esp=h.find('id="espanol"')
    ins_es=after_banner(h, esp); h=h[:ins_es]+chip(kind,True)+h[ins_es:]
    ins_en=after_banner(h, h.find('id="top"')); h=h[:ins_en]+chip(kind,False)+h[ins_en:]
    open(p,'w',encoding='utf-8').write(h); print("  chip["+kind+"]:", fname)

# Every active module page that HAS an icon type. Pages absent here have no icon yet.
MAP={
 # Digital Arts 1A
 "digarts1-pictograms-overview.html":"overview",
 "digarts1-color-theory-overview.html":"overview",
 "digarts1-sketchbook-cover-overview.html":"overview",
 "digarts1-sketchbook-cover-step02-submit-reflect.html":"reflection",
 "digarts1-athlete-poster-overview.html":"overview",
 "digarts1-athlete-poster-step03.html":"reflection",
 # Photography 1A
 "photo1-self-portrait-overview.html":"overview",
 "photo1-self-portrait-step01-capture.html":"your-device",
 "photo1-self-portrait-step02-reflection.html":"reflection",
 "photo1-composition-concepts-overview.html":"overview",
 "photo1-composition-concepts-step01-capture.html":"your-device",
 "photo1-composition-concepts-step02-reflection.html":"reflection",
 # Photography 2A
 "photo2-composition-overview.html":"overview",
 "photo2-composition-step01-photowalk.html":"photo-walk",
 "photo2-composition-step03-reflection.html":"reflection",
 "photo2-ocf-overview.html":"overview",
 "photo2-ocf-step02-photowalk.html":"photo-walk",
 "photo2-ocf-step03-reflection.html":"reflection",
 "photo2-studio-session-overview.html":"overview",
 "photo2-studio-session-step01-capture.html":"camera-kit",
 "photo2-studio-session-step03-reflection.html":"reflection",
}
for f,k in MAP.items(): apply(f,k)
print("total mapped:", len(MAP))
