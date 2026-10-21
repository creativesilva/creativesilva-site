# -*- coding: utf-8 -*-
# Dia de los Muertos "Honor Someone You Love" assignment: a single bilingual Canvas page.
# Students upload ONE JPG photo of a person they want to honor and remember for the class ofrenda;
# the deliverable is submitted IN Canvas (Mr. Silva downloads it from Canvas). History blurb on the
# tradition + the role of photography ("a photograph is all we have left"). Provided ofrenda header
# image used as the hero. Paste the #top block into a Canvas page via the Copy Canvas HTML button.
import os
from silva_framework import *   # banner, type_card, card, para, steps, note, framed, section_header, DELIVER_ICON, top_wrap, wrap_page, ban_check, SITE

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

HERO=f"{SITE}/assets/images/dia-de-los-muertos/header-v1.jpg"

def cap(text):
    return f'<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">{text}</div>'

def optional_box(es, items):
    # TEAL "optional, not graded" callout (this is an invitation, not a graded deliverable, so it does
    # NOT use the gold deliverables style, which signals a required turn-in).
    title="OPCIONAL &middot; C&Oacute;MO PARTICIPAR" if es else "OPTIONAL &middot; HOW TO TAKE PART"
    lead=("Participar es completamente opcional y no cuenta para calificaci&oacute;n. Si quieres ser parte de nuestra ofrenda de clase, as&iacute; lo haces:" if es
          else "Taking part is completely optional, and it is not graded. If you would like to be part of our class ofrenda, here is how:")
    lis=""
    for b,rest in items:
        lis+=('<div style="margin-bottom:6px;line-height:1.5;"><span style="color:#00b8b8;">&bull;</span> '
              f'<span style="font-size:13pt;color:rgba(255,255,255,0.90);"><strong>{b}</strong> {rest}</span></div>')
    return ('<div style="background:linear-gradient(180deg,rgba(0,184,184,0.12) 0%,rgba(0,184,184,0.03) 100%);border:1px solid rgba(0,184,184,0.35);border-left:6px solid #00b8b8;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(CONTENT_ICON, title, "#00b8b8", "#80e0e0")
      + f'<div style="font-size:13pt;color:#ffffff;margin-bottom:10px;line-height:1.5;">{lead}</div>'
      + f'{lis}</div>')

def build():
    # -------- English (#top) --------
    en=banner("D&iacute;a de los Muertos","Honor Someone You Love",
        "Optional: honor someone from your life or your heritage for our class ofrenda.","#espanol","","")
    en+=type_card("overview","D&iacute;a de los Muertos &middot; Studio Exhibit","An Invitation to Honor Someone",
        para("For <strong>D&iacute;a de los Muertos</strong>, the Day of the Dead, our class is building an "
             "<strong>ofrenda</strong> (an altar) in our studio to honor and remember the people we love. If you would "
             "like, you can add to it by sharing <strong>one photo</strong> of someone you want to honor: an ancestor, a "
             "family member, a friend, or someone from your <strong>heritage</strong>.")
        + note("<strong>This is completely optional, and it is not graded.</strong> It is an invitation to take part, not a required assignment. Take part only if you want to.")
        + para("If you choose to share, this is personal and meaningful. The photo you pick will be part of our class ofrenda, so choose someone who matters to you and a photo that shows who they are.")
        + framed(HERO,"A D&iacute;a de los Muertos ofrenda decorated with marigolds, candles, and framed photographs")
        + cap("An ofrenda honors loved ones with marigolds, candles, and their photographs."))
    en+=optional_box(False,[
        ("One photo (JPG):","if you choose to take part, upload one clear <strong>JPG</strong> image of the person you are honoring here."),
    ])
    en+=card("ABOUT THE TRADITION","What Is D&iacute;a de los Muertos?",
        para("<strong>D&iacute;a de los Muertos</strong> is a Mexican tradition celebrated on <strong>November 1 and "
             "2</strong>. It is a time to <strong>honor and remember</strong> the loved ones who have died. It is not a "
             "sad day. It is a warm celebration of their lives and the love we still feel for them.")
        + para("Families build an <strong>ofrenda</strong>, a special altar, and fill it with bright orange "
               "<strong>marigolds</strong>, candles, favorite foods, and <strong>photographs</strong> of the people they "
               "are remembering. Many believe that on these days, the spirits of their loved ones come back to visit."))
    en+=card("WHY PHOTOGRAPHS MATTER","A Photo Keeps Them With Us",
        para("On every ofrenda, the <strong>photograph</strong> is the heart of it. It is how we see their face again, "
             "their smile, and the way they looked at us.")
        + para("For many families, a <strong>photograph is all we have left</strong> of someone we love. That is why "
               "sharing a photo is such a powerful way to honor them. It keeps them present, and it keeps their story alive."))
    en+=card("HOW TO TAKE PART","If You Want to Share a Photo",
        para("Taking part is optional. If you would like to share a photo, here is how.")
        + steps([
            ("Choose your person:","think of someone you want to honor and remember."),
            ("Find a photo:","look for a photo that shows who they are. A clear photo of their face works best. If your photo is a printed picture, take a photo of it with your <strong>student iPad</strong> to scan it, then save it."),
            ("Save it as a JPG:","make sure your image is a <strong>JPG</strong> file."),
            ("Upload it here:","if you want to take part, upload your JPG to this Canvas assignment."),
        ])
        + note("This is personal, and it is optional. Honor whoever is meaningful to you, and only if you want to. If it feels hard, that is okay. You can always talk to Mr. Silva."))

    # -------- Spanish (#espanol) --------
    es=banner("D&iacute;a de los Muertos","Honra a Alguien que Amas",
        "Opcional: honra a alguien de tu vida o de tu herencia para nuestra ofrenda de clase.","#top","","")
    es+=type_card("overview","D&iacute;a de los Muertos &middot; Exhibici&oacute;n del Estudio","Una Invitaci&oacute;n a Honrar a Alguien",
        para("Para el <strong>D&iacute;a de los Muertos</strong>, nuestra clase va a construir una <strong>ofrenda</strong> "
             "(un altar) en nuestro estudio para honrar y recordar a las personas que amamos. Si quieres, puedes participar "
             "compartiendo <strong>una foto</strong> de alguien que quieres honrar: un antepasado, un familiar, un amigo, o "
             "alguien de tu <strong>herencia</strong>.")
        + note("<strong>Esto es completamente opcional y no cuenta para calificaci&oacute;n.</strong> Es una invitaci&oacute;n a participar, no una tarea obligatoria. Participa solo si quieres.")
        + para("Si decides compartir, esto es algo personal y con significado. La foto que elijas ser&aacute; parte de nuestra ofrenda de clase, as&iacute; que elige a alguien que es importante para ti y una foto que muestre qui&eacute;n es.")
        + framed(HERO,"Una ofrenda de D&iacute;a de los Muertos decorada con cempas&uacute;chil, velas y fotograf&iacute;as")
        + cap("Una ofrenda honra a los seres queridos con cempas&uacute;chil, velas y sus fotograf&iacute;as."))
    es+=optional_box(True,[
        ("Una foto (JPG):","si decides participar, sube una imagen <strong>JPG</strong> clara de la persona que est&aacute;s honrando aqu&iacute;."),
    ])
    es+=card("SOBRE LA TRADICI&Oacute;N","&iquest;Qu&eacute; es el D&iacute;a de los Muertos?",
        para("El <strong>D&iacute;a de los Muertos</strong> es una tradici&oacute;n mexicana que se celebra el <strong>1 y 2 "
             "de noviembre</strong>. Es un tiempo para <strong>honrar y recordar</strong> a los seres queridos que han "
             "fallecido. No es un d&iacute;a triste. Es una celebraci&oacute;n c&aacute;lida de sus vidas y del amor que "
             "todav&iacute;a sentimos por ellos.")
        + para("Las familias construyen una <strong>ofrenda</strong>, un altar especial, y la llenan de "
               "<strong>cempas&uacute;chil</strong> (flores anaranjadas), velas, comidas favoritas y "
               "<strong>fotograf&iacute;as</strong> de las personas que recuerdan. Muchos creen que en estos d&iacute;as, "
               "los esp&iacute;ritus de sus seres queridos regresan a visitarlos."))
    es+=card("POR QU&Eacute; IMPORTAN LAS FOTOGRAF&Iacute;AS","Una Foto los Mantiene con Nosotros",
        para("En cada ofrenda, la <strong>fotograf&iacute;a</strong> es el coraz&oacute;n. Es la manera de volver a ver su "
             "rostro, su sonrisa y la forma en que nos miraban.")
        + para("Para muchas familias, una <strong>fotograf&iacute;a es todo lo que queda</strong> de alguien que aman. Por "
               "eso compartir una foto es una manera tan poderosa de honrarlos. Los mantiene presentes y mantiene viva su historia."))
    es+=card("C&Oacute;MO PARTICIPAR","Si Quieres Compartir una Foto",
        para("Participar es opcional. Si quieres compartir una foto, as&iacute; lo haces.")
        + steps([
            ("Elige a tu persona:","piensa en alguien que quieres honrar y recordar."),
            ("Busca una foto:","busca una foto que muestre qui&eacute;n es. Una foto clara de su rostro funciona mejor. Si tu foto es una foto impresa, t&oacute;male una foto con tu <strong>iPad de estudiante</strong> para escanearla, y gu&aacute;rdala."),
            ("Gu&aacute;rdala como JPG:","aseg&uacute;rate de que tu imagen sea un archivo <strong>JPG</strong>."),
            ("S&uacute;bela aqu&iacute;:","si quieres participar, sube tu JPG a esta tarea de Canvas."),
        ])
        + note("Esto es personal y es opcional. Honra a quien sea importante para ti, y solo si quieres. Si se siente dif&iacute;cil, est&aacute; bien. Siempre puedes hablar con el Sr. Silva."))

    nav_inner=('      <div class="silva-breadcrumb">\n'
        '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
        '        <span class="bc-sep">&rsaquo;</span>\n'
        '        <span class="bc-current">D&iacute;a de los Muertos</span>\n'
        '      </div>\n'
        '      <div class="silva-nav-spacer"></div>')

    return wrap_page("D&iacute;a de los Muertos: Honor Someone You Love | PVHS",
        nav_inner, top_wrap(en,es), "")

if __name__=="__main__":
    html=ent(build())
    fname="dia-de-los-muertos-honor-photo.html"
    ban_check(html,fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote",fname,len(html),"bytes")
