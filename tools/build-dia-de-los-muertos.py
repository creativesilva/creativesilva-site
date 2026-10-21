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

def optional_box(es):
    # The ONE section that states this is optional / ungraded (Chris 2026-10-21: optional should be
    # stated in only one place, no redundant repeats). TEAL callout, no bullets.
    title="OPCIONAL" if es else "OPTIONAL"
    body=("Esto es completamente opcional y no cuenta para calificaci&oacute;n. Es una invitaci&oacute;n a honrar a alguien, no una tarea obligatoria. Participa solo si quieres." if es
          else "This is completely optional, and it is not graded. It is an invitation to honor someone, not a required assignment. Take part only if you want to.")
    return ('<div style="background:linear-gradient(180deg,rgba(0,184,184,0.12) 0%,rgba(0,184,184,0.03) 100%);border:1px solid rgba(0,184,184,0.35);border-left:6px solid #00b8b8;padding:26px 30px;overflow:hidden;margin-bottom:24px;">'
      + section_header(CONTENT_ICON, title, "#00b8b8", "#80e0e0")
      + f'<div style="font-size:13pt;color:#ffffff;line-height:1.6;">{body}</div>'
      + '</div>')

def build():
    # -------- English (#top) --------
    en=banner("D&iacute;a de los Muertos","Honor Someone You Love",
        "Honor someone from your life or your heritage for our class ofrenda.","#espanol","","")
    en+=type_card("overview","D&iacute;a de los Muertos &middot; Studio Exhibit","An Invitation to Honor Someone",
        para("For <strong>D&iacute;a de los Muertos</strong>, the Day of the Dead, our class is building an "
             "<strong>ofrenda</strong> (an altar) in our studio to honor and remember the people we love. You can add to "
             "it by sharing <strong>one photo</strong> of someone you want to honor: an ancestor, a family member, a "
             "friend, or someone from your <strong>heritage</strong>.")
        + para("This is personal and meaningful. The photo you pick will be part of our class ofrenda, so choose someone who matters to you and a photo that shows who they are.")
        + framed(HERO,"A D&iacute;a de los Muertos ofrenda decorated with marigolds, candles, and framed photographs")
        + cap("An ofrenda honors loved ones with marigolds, candles, and their photographs."))
    en+=optional_box(False)
    en+=card("D&iacute;A DE LOS MUERTOS &amp; PHOTOGRAPHY","D&iacute;a de los Muertos &amp; Photography",
        para("<strong>D&iacute;a de los Muertos</strong> is a Mexican tradition celebrated on <strong>November 1 and "
             "2</strong>. It is a time to <strong>honor and remember</strong> the loved ones who have died. It is not a "
             "sad day. It is a warm celebration of their lives and the love we still feel for them.")
        + para("Families build an <strong>ofrenda</strong>, a special altar, and fill it with bright orange "
               "<strong>marigolds</strong>, candles, favorite foods, and <strong>photographs</strong> of the people they "
               "are remembering. Many believe that on these days, the spirits of their loved ones come back to visit.")
        + para("On every ofrenda, the <strong>photograph</strong> is the heart of it. It is how we see their face again, "
               "their smile, and the way they looked at us. For many families, a <strong>photograph is all we have "
               "left</strong> of someone we love. That is why sharing a photo is such a powerful way to honor them: it "
               "keeps them present, and it keeps their story alive."))
    en+=card("HOW TO TAKE PART","How to Take Part",
        para("If you would like to take part, here is how:")
        + steps([
            ("Choose your person:","think of someone you want to honor and remember."),
            ("Bring in a photo:","bring a photo of your person to class so we can add it to the ofrenda. If your photo is only on a phone or a computer, upload it here and Mr. Silva will print it for you."),
        ])
        + para("<strong>Is it a delicate photo or a family heirloom?</strong> If you do not want to risk bringing in the original, you can still take part. Pick whatever works best:")
        + bullets([
            ("Take a picture of it:","photograph it with your <strong>student iPad</strong>, upload it here, and Mr. Silva will reprint it for the ofrenda. Be careful with reflections and glare on the photo so it comes out clean."),
            ("Or have it scanned:","bring it in and Mr. Silva will scan it professionally, then you take the original back home."),
        ])
        + note("This is personal. Honor whoever is meaningful to you. If it feels hard, that is okay. You can always talk to Mr. Silva."))

    # -------- Spanish (#espanol) --------
    es=banner("D&iacute;a de los Muertos","Honra a Alguien que Amas",
        "Honra a alguien de tu vida o de tu herencia para nuestra ofrenda de clase.","#top","","")
    es+=type_card("overview","D&iacute;a de los Muertos &middot; Exhibici&oacute;n del Estudio","Una Invitaci&oacute;n a Honrar a Alguien",
        para("Para el <strong>D&iacute;a de los Muertos</strong>, nuestra clase va a construir una <strong>ofrenda</strong> "
             "(un altar) en nuestro estudio para honrar y recordar a las personas que amamos. Puedes participar "
             "compartiendo <strong>una foto</strong> de alguien que quieres honrar: un antepasado, un familiar, un amigo, o "
             "alguien de tu <strong>herencia</strong>.")
        + para("Esto es algo personal y con significado. La foto que elijas ser&aacute; parte de nuestra ofrenda de clase, as&iacute; que elige a alguien que es importante para ti y una foto que muestre qui&eacute;n es.")
        + framed(HERO,"Una ofrenda de D&iacute;a de los Muertos decorada con cempas&uacute;chil, velas y fotograf&iacute;as")
        + cap("Una ofrenda honra a los seres queridos con cempas&uacute;chil, velas y sus fotograf&iacute;as."))
    es+=optional_box(True)
    es+=card("D&iacute;A DE LOS MUERTOS Y FOTOGRAF&Iacute;A","D&iacute;a de los Muertos y Fotograf&iacute;a",
        para("El <strong>D&iacute;a de los Muertos</strong> es una tradici&oacute;n mexicana que se celebra el <strong>1 y 2 "
             "de noviembre</strong>. Es un tiempo para <strong>honrar y recordar</strong> a los seres queridos que han "
             "fallecido. No es un d&iacute;a triste. Es una celebraci&oacute;n c&aacute;lida de sus vidas y del amor que "
             "todav&iacute;a sentimos por ellos.")
        + para("Las familias construyen una <strong>ofrenda</strong>, un altar especial, y la llenan de "
               "<strong>cempas&uacute;chil</strong> (flores anaranjadas), velas, comidas favoritas y "
               "<strong>fotograf&iacute;as</strong> de las personas que recuerdan. Muchos creen que en estos d&iacute;as, "
               "los esp&iacute;ritus de sus seres queridos regresan a visitarlos.")
        + para("En cada ofrenda, la <strong>fotograf&iacute;a</strong> es el coraz&oacute;n. Es la manera de volver a ver su "
               "rostro, su sonrisa y la forma en que nos miraban. Para muchas familias, una <strong>fotograf&iacute;a es "
               "todo lo que queda</strong> de alguien que aman. Por eso compartir una foto es una manera tan poderosa de "
               "honrarlos: los mantiene presentes y mantiene viva su historia."))
    es+=card("C&Oacute;MO PARTICIPAR","C&oacute;mo Participar",
        para("Si quieres participar, as&iacute; lo haces:")
        + steps([
            ("Elige a tu persona:","piensa en alguien que quieres honrar y recordar."),
            ("Trae una foto:","trae una foto de tu persona a clase para agregarla a la ofrenda. Si tu foto solo est&aacute; en un tel&eacute;fono o una computadora, s&uacute;bela aqu&iacute; y el Sr. Silva la imprimir&aacute; por ti."),
        ])
        + para("<strong>&iquest;Es una foto delicada o una reliquia familiar?</strong> Si no quieres arriesgar la foto original, a&uacute;n puedes participar. Elige lo que funcione mejor:")
        + bullets([
            ("T&oacute;male una foto:","fotograf&iacute;ala con tu <strong>iPad de estudiante</strong>, s&uacute;bela aqu&iacute; y el Sr. Silva la reimprimir&aacute; para la ofrenda. Ten cuidado con los reflejos y el brillo en la foto para que salga limpia."),
            ("O que la escaneen:","tr&aacute;ela y el Sr. Silva la escanear&aacute; de forma profesional, y luego te llevas la original a casa."),
        ])
        + note("Esto es personal. Honra a quien sea importante para ti. Si se siente dif&iacute;cil, est&aacute; bien. Siempre puedes hablar con el Sr. Silva."))

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
