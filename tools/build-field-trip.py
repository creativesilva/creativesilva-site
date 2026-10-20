# -*- coding: utf-8 -*-
# Field Trip announcement builder: Santa Barbara Museum of Art, Nov 12.
# One bilingual Canvas page per course (Photo 1, Photo 2, Digital Arts 1), styled with the shared
# silva angular framework. Photo courses tour the museum + photo walk the courthouse grounds with
# school cameras; Digital Arts does an art-room activity + the museum tour (no photo walk).
# Paste the #top block into a Canvas page/announcement via the Copy Canvas HTML button.
import os
from silva_framework import *   # banner, type_card, card, para, bullets, note, framed, top_wrap, wrap_page, ban_check, SITE, HICON_*

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

# ---- trip constants ----
FORM="https://forms.gle/vajofWCZ3fUWcPfK6"
SBMA="https://www.sbma.net"
IMGDIR=f"{SITE}/assets/images/field-trips"
MUSEUM=f"{IMGDIR}/sbma-exterior-v1.jpg"
COURTHOUSE=f"{IMGDIR}/sb-courthouse-v1.jpg"

COURSES={
 "photo1":dict(en="Photography 1A", es="Fotograf&iacute;a 1A", photo=True,  hicon=HICON_PHOTO_WALK),
 "photo2":dict(en="Photography 2A", es="Fotograf&iacute;a 2A", photo=True,  hicon=HICON_PHOTO_WALK),
 "da1":   dict(en="Digital Arts 1A",es="Arte Digital 1A",      photo=False, hicon=HICON_DESIGN),
}

# ---- small local helpers (Canvas-safe inline styles) ----
def btn(href,label,primary=True):
    base=("display:inline-block;text-decoration:none;padding:15px 32px;margin:7px;font-family:Arial,sans-serif;"
          "font-size:13pt;letter-spacing:0.05em;text-transform:uppercase;border:2px solid #00b8b8;box-sizing:border-box;")
    skin=("background:#00b8b8;color:#04201f;" if primary else "background:rgba(0,0,0,0.30);color:#a9f2f2;")
    return f'<a href="{href}" target="_blank" rel="noopener" style="{base}{skin}"><strong>{label}</strong></a>'

def btn_row(buttons):
    return '<div style="text-align:center;margin:18px 0 4px;">'+"".join(buttons)+'</div>'

def fact_tile(label,value):
    return ('<div style="flex:1 1 210px;min-width:0;background:rgba(0,116,116,0.14);border:1px solid rgba(0,184,184,0.30);'
      'border-top:3px solid #00b8b8;padding:15px 18px;box-sizing:border-box;">'
      f'<div style="font-size:10pt;letter-spacing:0.13em;text-transform:uppercase;color:#80e0e0;margin-bottom:7px;"><strong>{label}</strong></div>'
      f'<div style="font-size:13.5pt;color:#ffffff;line-height:1.3;"><strong>{value}</strong></div></div>')

def facts_strip(tiles):
    return '<div style="display:flex;flex-wrap:wrap;gap:12px;margin:0 0 22px;">'+"".join(tiles)+'</div>'

def cap(text):
    return f'<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">{text}</div>'

# ========================= PAGE =========================
def build(course):
    c=COURSES[course]; photo=c["photo"]
    fname=f"{course}-field-trip-sbma.html"

    # -------- English (#top) --------
    if photo:
        sub_en="A museum tour and a camera photo walk. Thursday, November 12."
        what_en="Museum tour + photo walk"
        lead_en=(para("On <strong>Thursday, November 12</strong>, our class is going on a field trip to the "
            "<strong>Santa Barbara Museum of Art</strong>. First we will tour the museum with a guide and see "
            "real art up close. Then we will take a <strong>photo walk</strong> with our school cameras in the "
            "beautiful grounds of the <strong>Santa Barbara County Courthouse</strong>, right nearby."))
        plan_en=bullets([
            ("Tour the museum:","walk through the galleries with a guide and see real works of art up close."),
            ("Photo walk at the courthouse:","take a school camera into the courthouse gardens and grounds and make your own photos of the light, the arches, and the views."),
            ("Work like an artist:","look for great light, strong shapes, and small details, just like we practice in class."),
        ])
        plan_extra_en=framed(COURTHOUSE,"The Santa Barbara County Courthouse grounds")+cap("The Santa Barbara County Courthouse grounds, where we will take our photo walk.")
    else:
        sub_en="Make art in the museum, then tour the galleries. Thursday, November 12."
        what_en="Art activity + museum tour"
        lead_en=(para("On <strong>Thursday, November 12</strong>, our class is going on a field trip to the "
            "<strong>Santa Barbara Museum of Art</strong>. We will make art together in the museum&#x2019;s own "
            "<strong>art room</strong>, and then take a <strong>guided tour</strong> of the museum to see real art up close."))
        plan_en=bullets([
            ("Make art in the art room:","join a hands-on art activity in the museum&#x2019;s own art room."),
            ("Tour the museum:","walk through the galleries with a guide and see real works of art up close."),
            ("Get inspired:","find ideas, styles, and colors you can bring back to your own digital art."),
        ])
        plan_extra_en=""

    en=banner(f"{c['en']} &bull; Field Trip","Santa Barbara Museum of Art",sub_en,"#espanol","",c["hicon"])
    en+=type_card("overview","Field Trip &middot; November 12","We Are Going on a Field Trip!",
        lead_en + framed(MUSEUM,"The Santa Barbara Museum of Art") + cap("The Santa Barbara Museum of Art."))
    en+=facts_strip([
        fact_tile("When","Thursday, November 12"),
        fact_tile("Where","Santa Barbara Museum of Art"),
        fact_tile("What","" + what_en),
    ])
    en+=card("THE PLAN","What We Will Do", plan_en + plan_extra_en)
    en+=card("COME WITH US","Say Yes and Come Along",
        para("Do you want to come? Here is how. First, ask your parent or guardian for permission. Then fill out the "
             "form below so Mr. Silva knows you are coming. Fill it out as soon as you can so we can save your spot.")
        + btn_row([btn(FORM,"Fill Out the Form",True), btn(SBMA,"See the Museum",False)])
        + note("The <strong>Fill Out the Form</strong> button opens the permission and sign-up form. The <strong>See the Museum</strong> button opens the museum website, sbma.net, so you can look around before we go."))

    # -------- Spanish (#espanol) --------
    if photo:
        sub_es="Un recorrido por el museo y una caminata fotogr&aacute;fica. Jueves, 12 de noviembre."
        what_es="Recorrido + caminata fotogr&aacute;fica"
        lead_es=(para("El <strong>jueves 12 de noviembre</strong>, nuestra clase va de excursi&oacute;n al "
            "<strong>Museo de Arte de Santa B&aacute;rbara</strong>. Primero vamos a recorrer el museo con un gu&iacute;a "
            "y ver arte real de cerca. Luego vamos a hacer una <strong>caminata fotogr&aacute;fica</strong> con las "
            "c&aacute;maras de la escuela en los hermosos jardines del <strong>Palacio de Justicia del Condado de Santa "
            "B&aacute;rbara</strong>, que est&aacute; muy cerca."))
        plan_es=bullets([
            ("Recorrer el museo:","camina por las galer&iacute;as con un gu&iacute;a y ve obras de arte reales de cerca."),
            ("Caminata fotogr&aacute;fica en el palacio de justicia:","lleva una c&aacute;mara de la escuela a los jardines del palacio de justicia y toma tus propias fotos de la luz, los arcos y las vistas."),
            ("Trabajar como artista:","busca buena luz, formas fuertes y peque&ntilde;os detalles, como practicamos en clase."),
        ])
        plan_extra_es=framed(COURTHOUSE,"Los jardines del Palacio de Justicia del Condado de Santa B&aacute;rbara")+cap("Los jardines del Palacio de Justicia del Condado de Santa B&aacute;rbara, donde haremos nuestra caminata fotogr&aacute;fica.")
    else:
        sub_es="Haz arte en el museo y luego recorre las galer&iacute;as. Jueves, 12 de noviembre."
        what_es="Actividad de arte + recorrido"
        lead_es=(para("El <strong>jueves 12 de noviembre</strong>, nuestra clase va de excursi&oacute;n al "
            "<strong>Museo de Arte de Santa B&aacute;rbara</strong>. Vamos a hacer arte juntos en el "
            "<strong>sal&oacute;n de arte</strong> del museo, y luego vamos a hacer un <strong>recorrido guiado</strong> "
            "del museo para ver arte real de cerca."))
        plan_es=bullets([
            ("Hacer arte en el sal&oacute;n de arte:","participa en una actividad de arte pr&aacute;ctica en el sal&oacute;n de arte del museo."),
            ("Recorrer el museo:","camina por las galer&iacute;as con un gu&iacute;a y ve obras de arte reales de cerca."),
            ("Inspirarte:","encuentra ideas, estilos y colores que puedes usar en tu propio arte digital."),
        ])
        plan_extra_es=""

    es=banner(f"{c['es']} &bull; Excursi&oacute;n","Museo de Arte de Santa B&aacute;rbara",sub_es,"#top","",c["hicon"])
    es+=type_card("overview","Excursi&oacute;n &middot; 12 de noviembre","&iexcl;Vamos de Excursi&oacute;n!",
        lead_es + framed(MUSEUM,"El Museo de Arte de Santa B&aacute;rbara") + cap("El Museo de Arte de Santa B&aacute;rbara."))
    es+=facts_strip([
        fact_tile("Cu&aacute;ndo","Jueves, 12 de noviembre"),
        fact_tile("D&oacute;nde","Museo de Arte de Santa B&aacute;rbara"),
        fact_tile("Qu&eacute;","" + what_es),
    ])
    es+=card("EL PLAN","Qu&eacute; Vamos a Hacer", plan_es + plan_extra_es)
    es+=card("VEN CON NOSOTROS","Di que S&iacute; y Ven con Nosotros",
        para("&iquest;Quieres venir? As&iacute; es como. Primero, pide permiso a tu padre, madre o tutor. Luego llena el "
             "formulario de abajo para que el Sr. Silva sepa que vas a ir. Ll&eacute;nalo lo antes posible para apartar tu lugar.")
        + btn_row([btn(FORM,"Llenar el Formulario",True), btn(SBMA,"Ver el Museo",False)])
        + note("El bot&oacute;n <strong>Llenar el Formulario</strong> abre el formulario de permiso e inscripci&oacute;n. El bot&oacute;n <strong>Ver el Museo</strong> abre el sitio del museo, sbma.net, para que lo conozcas antes de ir."))

    # -------- nav (breadcrumb only, no step dots) --------
    nav_inner=('      <div class="silva-breadcrumb">\n'
        '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
        '        <span class="bc-sep">&rsaquo;</span>\n'
        f'        <span class="bc-current">{c["en"]} Field Trip</span>\n'
        '      </div>\n'
        '      <div class="silva-nav-spacer"></div>')

    return wrap_page(f"Field Trip: Santa Barbara Museum of Art | {c['en']} | PVHS",
        nav_inner, top_wrap(en,es), "")

if __name__=="__main__":
    for course in ("photo1","photo2","da1"):
        html=ent(build(course))
        fname=f"{course}-field-trip-sbma.html"
        ban_check(html,fname)
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote",fname,len(html),"bytes")
