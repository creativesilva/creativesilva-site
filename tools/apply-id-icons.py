#!/usr/bin/env python3
# Assignment identification icons (framework). The first card's eyebrow row becomes a
# space-between flex row: the ORIGINAL eyebrow/title stays on the LEFT, and the assignment
# icon + a short orange description is justified RIGHT (wraps below on narrow screens).
# EN in #top, ES in #espanol. Idempotent (skips pages whose first eyebrow is already an
# <!--IDEYE--> row) and strips any legacy full-width <!--IDCHIP--> bar. Re-run after
# regenerating any builder module.
#
# Icon family (assets/Icons/assignment): overview, your-device, camera-kit, photo-walk,
# reflection. Still needed (no icon yet): editing, contact sheet, research/find, worksheet,
# design/build, sketch.
import os, re
ROOT=os.path.join(os.path.dirname(__file__), "..", "curriculum", "shared")
SITE="https://www.creativesilva.com"
ICO=SITE+"/assets/Icons/assignment"
EYE_SIG='<div style="display:inline-block;background:rgba(0,0,0,0.40);border-left:3px solid #00b8b8;'

DESC={
 "overview":("overview-v2.png","Downloads on This Page","Descargas en Esta P&aacute;gina"),
 "your-device":("your-device.png","Your Own Device Required","Requiere Tu Propio Dispositivo"),
 "camera-kit":("camera-kit.png","Reserve a Camera Kit","Reserva un Equipo de C&aacute;mara"),
 "photo-walk":("photo-walk.png","In-Class Photo Walk","Caminata Fotogr&aacute;fica en Clase"),
 "reflection":("reflection-v2.png","Written Reflection","Reflexi&oacute;n Escrita"),
}
def id_right(kind, es):
    # text first, icon last so the icon sits at the far right edge of the row
    icon,en_d,es_d=DESC[kind]; desc=es_d if es else en_d
    return ('<div style="display:flex;align-items:center;gap:9px;flex:0 0 auto;">'
      f'<span style="font-size:9pt;letter-spacing:0.10em;text-transform:uppercase;color:#ffb27c;line-height:1.25;max-width:180px;text-align:right;"><strong>{desc}</strong></span>'
      f'<img src="{ICO}/{icon}" alt="{desc}" style="width:38px;height:38px;display:block;flex:0 0 auto;" /></div>')

def match_close(h, open_idx):
    j=open_idx+4; depth=1
    while depth>0:
        no=h.find('<div',j); nc=h.find('</div>',j)
        if nc==-1: return None
        if no!=-1 and no<nc: depth+=1; j=no+4
        else:
            depth-=1
            if depth==0: return nc+6
            j=nc+6

def strip_idchip(h):
    while True:
        m=h.find('<!--IDCHIP-->')
        if m==-1: return h
        ds=h.find('<div', m); h=h[:m]+h[match_close(h, ds):]

def strip_ideye(h):
    # unwrap a prior IDEYE flex row back to its original bare eyebrow so the
    # row can be rebuilt with the current layout/icon (keeps the applier idempotent)
    while True:
        m=h.find('<!--IDEYE-->')
        if m==-1: return h
        wrap_open=h.find('<div', m)
        wrap_close=match_close(h, wrap_open)
        i=h.find(EYE_SIG, wrap_open)          # first inner div = original eyebrow
        eb=h[i:h.find('</div>', i)+6]
        h=h[:m]+eb+h[wrap_close:]

def wrap_first_eyebrow(h, frm, kind, es):
    i=h.find(EYE_SIG, frm); assert i!=-1, "eyebrow not found"
    end=h.find('</div>', i)+6
    eb=h[i:end].replace('margin-bottom:12px;','',1)   # move bottom margin to the row
    row=('<!--IDEYE--><div style="display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-bottom:12px;">'
      + eb + id_right(kind,es) + '</div>')
    return h[:i]+row+h[end:]

def apply(fname, kind):
    p=os.path.join(ROOT,fname)
    if not os.path.exists(p): print("  MISSING:", fname); return
    h=open(p,encoding='utf-8').read()
    h=strip_idchip(h)
    h=strip_ideye(h)                          # unwrap any prior row, then rebuild
    esp=h.find('id="espanol"')
    h=wrap_first_eyebrow(h, esp, kind, True)                 # ES first (later in doc)
    h=wrap_first_eyebrow(h, h.find('id="top"'), kind, False) # then EN
    open(p,'w',encoding='utf-8').write(h); print("  id["+kind+"]:", fname)

MAP={
 "digarts1-pictograms-overview.html":"overview",
 "digarts1-color-theory-overview.html":"overview",
 "digarts1-sketchbook-cover-overview.html":"overview",
 "digarts1-sketchbook-cover-step02-submit-reflect.html":"reflection",
 "digarts1-athlete-poster-overview.html":"overview",
 "digarts1-athlete-poster-step03.html":"reflection",
 "photo1-self-portrait-overview.html":"overview",
 "photo1-self-portrait-step01-capture.html":"your-device",
 "photo1-self-portrait-step02-reflection.html":"reflection",
 "photo1-composition-concepts-overview.html":"overview",
 "photo1-composition-concepts-step01-capture.html":"your-device",
 "photo1-composition-concepts-step02-reflection.html":"reflection",
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
