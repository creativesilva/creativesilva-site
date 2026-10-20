# -*- coding: utf-8 -*-
# Field Trip INTEREST announcement builder: Santa Barbara Museum of Art, Nov 12.
# One bilingual Canvas page per course (Photo 1, Photo 2, Digital Arts 1), styled with the shared
# silva angular framework. This is a LIMITED-SPACE privilege: students fill out an INTEREST form and
# the teacher selects by GPA/grades + good standing. Caps: 25 photography, 25 art, 10 digital arts
# (60 total). If selected it is an all-day trip (bus 8:30am, miss 1st-7th, teacher permission, make-up
# work). Photo courses tour the museum + photo walk the courthouse grounds with school cameras;
# Digital Arts does an art-room activity + the museum tour (no photo walk).
# Paste the #top block into a Canvas page/announcement via the Copy Canvas HTML button.
import os
from silva_framework import *   # banner, type_card, card, para, bullets, note, float_right, top_wrap, wrap_page, ban_check, SITE, HICON_*

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
 "photo1":dict(en="Photography 1A", es="Fotograf&iacute;a 1A", photo=True,  hicon=HICON_PHOTO_WALK, prog_en="photography", prog_es="fotograf&iacute;a", spots=25),
 "photo2":dict(en="Photography 2A", es="Fotograf&iacute;a 2A", photo=True,  hicon=HICON_PHOTO_WALK, prog_en="photography", prog_es="fotograf&iacute;a", spots=25),
 "da1":   dict(en="Digital Arts 1A",es="Arte Digital 1A",      photo=False, hicon=HICON_DESIGN,      prog_en="digital arts",prog_es="arte digital", spots=10),
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

# ========================= PAGE =========================
def build(course):
    c=COURSES[course]; photo=c["photo"]; spots=c["spots"]
    fname=f"{course}-field-trip-sbma.html"

    # ---------------- English (#top) ----------------
    if photo:
        sub_en="A special Visual Arts trip with limited space. Thursday, November 12."
        do_en="we will tour the museum and then take a <strong>photo walk</strong> with our school cameras in the beautiful grounds of the <strong>Santa Barbara County Courthouse</strong> nearby"
        plan_en=bullets([
            ("Tour the museum:","walk through the galleries with a guide and see real works of art up close."),
            ("Photo walk at the courthouse:","take a school camera into the courthouse gardens and grounds and make your own photos of the light, the arches, and the views."),
            ("Work like an artist:","look for great light, strong shapes, and small details, just like we practice in class."),
        ])
        plan_extra_en=float_right(COURTHOUSE,"The Santa Barbara County Courthouse grounds","The Santa Barbara County Courthouse grounds, where we will take our photo walk.")
    else:
        sub_en="A special Visual Arts trip with limited space. Thursday, November 12."
        do_en="we will make art together in the museum&#x2019;s own <strong>art room</strong> and then take a <strong>guided tour</strong> of the museum"
        plan_en=bullets([
            ("Make art in the art room:","join a hands-on art activity in the museum&#x2019;s own art room."),
            ("Tour the museum:","walk through the galleries with a guide and see real works of art up close."),
            ("Get inspired:","find ideas, styles, and colors you can bring back to your own digital art."),
        ])
        plan_extra_en=""

    en=banner(f"{c['en']} &bull; Field Trip","Santa Barbara Museum of Art",sub_en,"#espanol","",c["hicon"])
    en+=type_card("overview","Field Trip &middot; November 12","A Special Chance to Go",
        para("Our Visual Arts classes have a special chance to take a field trip to the <strong>Santa Barbara Museum "
             "of Art</strong> on <strong>Thursday, November 12</strong>. This is a <strong>privilege</strong>, and space "
             "is limited. Not everyone can go.")
        + para(f"If you are chosen, {do_en}.")
        + para("To be considered, fill out the short <strong>interest form</strong> below. Filling it out is <strong>not a "
               "promise</strong> that you will go. Your teacher will let you know if you are selected.")
        + float_right(MUSEUM,"The Santa Barbara Museum of Art","The Santa Barbara Museum of Art."))
    en+=facts_strip([
        fact_tile("When","Thursday, Nov 12 &middot; All day"),
        fact_tile("Where","Santa Barbara Museum of Art"),
        fact_tile("Spots",f"{spots} {c['prog_en']} students"),
    ])
    en+=card("THE PLAN","What We Will Do", plan_en + plan_extra_en)
    en+=card("WHO GETS TO GO","How Students Are Chosen",
        para(f"Only <strong>{spots} {c['prog_en']} students</strong> can be chosen for this trip. Space is limited, so not "
             "everyone who signs up will go.")
        + bullets([
            ("Good grades:","you are chosen based on your <strong>GPA and grades</strong>, so keep them strong."),
            ("Stay locked in:","you need to be caught up and doing your work, in good standing in all your classes."),
            ("First come, first served:","spots fill up fast, so fill out the interest form early."),
        ])
        + note("This is an <strong>interest form</strong>, not a sign-up. It does not promise you a spot. Your teacher will tell you if you are selected to attend."))
    en+=card("IF YOU ARE CHOSEN","What to Know About the Day",
        bullets([
            ("All-day trip:","the bus leaves at <strong>8:30 am</strong>. You will miss <strong>1st through 7th period</strong>."),
            ("Permission from every teacher:","you must get <strong>signed permission from all of your teachers</strong> before you go."),
            ("Make up your work:","you are responsible for making up any work you miss that day."),
        ]))
    en+=card("SHOW YOUR INTEREST","Fill Out the Interest Form",
        para("Ready? Fill out the short interest form below. Make sure your grades are in good shape first.")
        + para("The form will ask for your <strong>name</strong>, <strong>student ID</strong>, your <strong>class and "
               "period</strong>, your <strong>GPA</strong>, and a <strong>screen capture (a photo) of your Aeries grades</strong>. "
               "Have your Aeries grades ready before you start.")
        + btn_row([btn(FORM,"Fill Out the Interest Form",True), btn(SBMA,"See the Museum",False)])
        + note("Filling out this form is <strong>not a guarantee</strong>. Your teacher will let you know if you are selected to go."))

    # ---------------- Spanish (#espanol) ----------------
    if photo:
        sub_es="Un viaje especial de Artes Visuales con espacio limitado. Jueves, 12 de noviembre."
        do_es="vamos a recorrer el museo y luego haremos una <strong>caminata fotogr&aacute;fica</strong> con las c&aacute;maras de la escuela en los hermosos jardines del <strong>Palacio de Justicia del Condado de Santa B&aacute;rbara</strong>, que est&aacute; cerca"
        plan_es=bullets([
            ("Recorrer el museo:","camina por las galer&iacute;as con un gu&iacute;a y ve obras de arte reales de cerca."),
            ("Caminata fotogr&aacute;fica en el palacio de justicia:","lleva una c&aacute;mara de la escuela a los jardines del palacio de justicia y toma tus propias fotos de la luz, los arcos y las vistas."),
            ("Trabajar como artista:","busca buena luz, formas fuertes y peque&ntilde;os detalles, como practicamos en clase."),
        ])
        plan_extra_es=float_right(COURTHOUSE,"Los jardines del Palacio de Justicia del Condado de Santa B&aacute;rbara","Los jardines del Palacio de Justicia del Condado de Santa B&aacute;rbara, donde haremos nuestra caminata fotogr&aacute;fica.")
    else:
        sub_es="Un viaje especial de Artes Visuales con espacio limitado. Jueves, 12 de noviembre."
        do_es="vamos a hacer arte juntos en el <strong>sal&oacute;n de arte</strong> del museo y luego haremos un <strong>recorrido guiado</strong> del museo"
        plan_es=bullets([
            ("Hacer arte en el sal&oacute;n de arte:","participa en una actividad de arte pr&aacute;ctica en el sal&oacute;n de arte del museo."),
            ("Recorrer el museo:","camina por las galer&iacute;as con un gu&iacute;a y ve obras de arte reales de cerca."),
            ("Inspirarte:","encuentra ideas, estilos y colores que puedes usar en tu propio arte digital."),
        ])
        plan_extra_es=""

    es=banner(f"{c['es']} &bull; Excursi&oacute;n","Museo de Arte de Santa B&aacute;rbara",sub_es,"#top","",c["hicon"])
    es+=type_card("overview","Excursi&oacute;n &middot; 12 de noviembre","Una Oportunidad Especial",
        para("Nuestras clases de Artes Visuales tienen una oportunidad especial de ir de excursi&oacute;n al <strong>Museo "
             "de Arte de Santa B&aacute;rbara</strong> el <strong>jueves 12 de noviembre</strong>. Esto es un "
             "<strong>privilegio</strong> y el espacio es limitado. No todos pueden ir.")
        + para(f"Si te eligen, {do_es}.")
        + para("Para que te consideren, llena el breve <strong>formulario de inter&eacute;s</strong> de abajo. Llenarlo "
               "<strong>no es una promesa</strong> de que ir&aacute;s. Tu maestro te avisar&aacute; si te eligen.")
        + float_right(MUSEUM,"El Museo de Arte de Santa B&aacute;rbara","El Museo de Arte de Santa B&aacute;rbara."))
    es+=facts_strip([
        fact_tile("Cu&aacute;ndo","Jueves, 12 de nov &middot; Todo el d&iacute;a"),
        fact_tile("D&oacute;nde","Museo de Arte de Santa B&aacute;rbara"),
        fact_tile("Lugares",f"{spots} estudiantes de {c['prog_es']}"),
    ])
    es+=card("EL PLAN","Qu&eacute; Vamos a Hacer", plan_es + plan_extra_es)
    es+=card("QUI&Eacute;N PUEDE IR","C&oacute;mo se Eligen los Estudiantes",
        para(f"Solo se pueden elegir <strong>{spots} estudiantes de {c['prog_es']}</strong> para esta excursi&oacute;n. El "
             "espacio es limitado, as&iacute; que no todos los que se inscriban podr&aacute;n ir.")
        + bullets([
            ("Buenas calificaciones:","te eligen seg&uacute;n tu <strong>GPA y tus calificaciones</strong>, as&iacute; que mantenlas altas."),
            ("Mantente al corriente:","necesitas estar al d&iacute;a y haciendo tu trabajo, en buen estado en todas tus clases."),
            ("Primero en llegar, primero en servir:","los lugares se llenan r&aacute;pido, as&iacute; que llena el formulario pronto."),
        ])
        + note("Este es un <strong>formulario de inter&eacute;s</strong>, no una inscripci&oacute;n. No te asegura un lugar. Tu maestro te dir&aacute; si te eligen para asistir."))
    es+=card("SI TE ELIGEN","Lo Que Debes Saber del D&iacute;a",
        bullets([
            ("Excursi&oacute;n de todo el d&iacute;a:","el autob&uacute;s sale a las <strong>8:30 am</strong>. Vas a faltar de la <strong>1ra a la 7ma clase</strong>."),
            ("Permiso de cada maestro:","debes conseguir el <strong>permiso firmado de todos tus maestros</strong> antes de ir."),
            ("Repon tu trabajo:","eres responsable de reponer cualquier trabajo que pierdas ese d&iacute;a."),
        ]))
    es+=card("MUESTRA TU INTER&Eacute;S","Llena el Formulario de Inter&eacute;s",
        para("&iquest;Todo listo? Llena el breve formulario de inter&eacute;s de abajo. Primero aseg&uacute;rate de que tus calificaciones est&eacute;n bien.")
        + para("El formulario te pedir&aacute; tu <strong>nombre</strong>, tu <strong>n&uacute;mero de estudiante</strong>, tu "
               "<strong>clase y per&iacute;odo</strong>, tu <strong>GPA</strong> y una <strong>captura de pantalla (una foto) de "
               "tus calificaciones de Aeries</strong>. Ten listas tus calificaciones de Aeries antes de empezar.")
        + btn_row([btn(FORM,"Llenar el Formulario de Inter&eacute;s",True), btn(SBMA,"Ver el Museo",False)])
        + note("Llenar este formulario <strong>no es una garant&iacute;a</strong>. Tu maestro te avisar&aacute; si te eligen para ir."))

    # ---------------- nav (breadcrumb only, no step dots) ----------------
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
