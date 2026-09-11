#!/usr/bin/env python3
# Digital Arts 1A - ANNOUNCEMENT (not an assignment): Cover Decoration Contest winners.
# One celebratory page, bilingual EN/ES, on the silva_framework chrome. Showcases the first-place
# cover (gold) and the honorable mentions (teal), the prize, and the next-contest teaser (orange).
# Treated like a one-page module; listed in the catalog's new per-course "Announcements" section.
import os
from silva_framework import *

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/digarts1/cover-decoration"
ELENA=f"{IMG}/cover-decoration-1st-elena-v1.jpg"
BRYAN=f"{IMG}/cover-decoration-hm-bryan-v1.jpg"
GUADALUPE=f"{IMG}/cover-decoration-hm-guadalupe-v1.jpg"
OUT="digarts1-cover-decoration-winners.html"

GOLD=("#f5b301","rgba(245,179,1,0.12)","rgba(245,179,1,0.35)","#ffd166")
TEAL=("#00b8b8","rgba(0,116,116,0.10)","rgba(0,184,184,0.22)","#80e0e0")
ORANGE=("#FF6B1A","rgba(255,107,26,0.12)","rgba(255,107,26,0.30)","#ffb27c")

def chip(label, c):
    accent,_,_,light=c
    return ('<div style="display:inline-block;background:rgba(0,0,0,0.40);border-left:5px solid '+accent+';padding:9px 18px;margin-bottom:12px;max-width:100%;box-sizing:border-box;">'
      f'<span style="font-family:Arial,sans-serif;font-size:13pt;letter-spacing:0.12em;text-transform:uppercase;color:{light};line-height:1.2;"><strong>{label}</strong></span></div>'
      f'<div style="height:2px;background:{accent};width:60px;margin-bottom:18px;"></div>')

def box(c, inner):
    accent,tint,border,_=c
    return (f'<div style="background:linear-gradient(180deg,{tint} 0%,rgba(0,0,0,0.02) 100%);border:1px solid {border};border-left:6px solid {accent};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">{inner}</div>')

def name(n):
    return f'<div style="font-size:19pt;color:#ffffff;margin:16px 0 2px;"><strong>{n}</strong></div>'

def art(src, alt, cap, c):
    accent,_,_,light=c
    return (f'<div style="background:linear-gradient(135deg,{accent} 0%,rgba(255,255,255,0.06) 100%);padding:3px;margin:8px 0 4px;">'
      f'<img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      f'<div style="font-size:11pt;color:{light};text-align:center;margin:6px 0 2px;opacity:0.9;letter-spacing:0.04em;">{cap}</div>')

def prize(text, c):
    accent,_,_,light=c
    return f'<div style="margin-top:14px;font-size:14pt;color:{light};line-height:1.5;"><strong>{text}</strong></div>'

def side(es):
    banner_html = banner(
        ("Arte Digital 1A &bull; Anuncio" if es else "Digital Arts 1A &bull; Announcement"),
        ("Ganadores del Concurso de Decoraci&oacute;n de Portada" if es else "Cover Decoration Contest Winners"),
        ("&iexcl;Celebrando a nuestros artistas de primer lugar y menci&oacute;n honor&iacute;fica!" if es else "Celebrating our first-place and honorable-mention artists!"),
        ("#top" if es else "#espanol"),
        ("Back to English" if es else "Clic para Espa&ntilde;ol"))
    # intro
    intro = box(TEAL,
        chip(("El Concurso de Decoraci&oacute;n de Portada" if es else "The Cover Decoration Contest"), TEAL)
        + para("&iexcl;Felicidades, artistas! En el proyecto de Decoraci&oacute;n de Portada convirtieron la portada de su cuaderno en arte de verdad. Gracias a todos los que participaron. Estos son los destacados de esta ronda." if es
               else "Congratulations, artists! For the Cover Decoration project you turned your sketchbook cover into real art. Thank you to everyone who entered. Here are this round&rsquo;s standouts."))
    # 1st place
    first = box(GOLD,
        chip(("Primer Lugar" if es else "1st Place"), GOLD)
        + name("Elena Arroyo")
        + art(ELENA,
            ("Portada de cuaderno de primer lugar de Elena Arroyo: dos paneles a l&aacute;piz de color, una escena de naturaleza con criaturas y una escena dram&aacute;tica con una figura enorme sobre un muro y un soldado" if es
             else "Elena Arroyo&rsquo;s first-place sketchbook cover: two colored-pencil panels, a green nature scene with creatures and a dramatic scene with a towering figure over a wall and a soldier"),
            "&ldquo;Do Not Falter&rdquo;", GOLD)
        + prize(("Ganadora de una tarjeta de regalo de $15 de Chick-fil-A." if es else "Winner of a $15 Chick-fil-A gift card."), GOLD))
    # honorable mentions
    hm = box(TEAL,
        chip(("Menci&oacute;n Honor&iacute;fica" if es else "Honorable Mention"), TEAL)
        + name("Bryan Hernandez")
        + art(BRYAN,
            ("Portada de menci&oacute;n honor&iacute;fica de Bryan Hernandez: criaturas aladas blancas sobre un paisaje de monta&ntilde;as, a l&aacute;piz de color" if es
             else "Bryan Hernandez&rsquo;s honorable-mention cover: white winged creatures rising over a mountain landscape, in colored pencil"),
            "Happiness &middot; Hopeful &middot; Inspiring", TEAL)
        + name("Guadalupe Valenzuela")
        + art(GUADALUPE,
            ("Portada de menci&oacute;n honor&iacute;fica de Guadalupe Valenzuela: arte estilo anime con una figura mecha y un personaje de cabello azul" if es
             else "Guadalupe Valenzuela&rsquo;s honorable-mention cover: anime-style art with a mecha figure and a blue-haired character"),
            "Hope &middot; Solitude &middot; Company", TEAL))
    # next contest teaser
    nxt = box(ORANGE,
        chip(("Muy Pronto" if es else "Coming Soon"), ORANGE)
        + para("El siguiente concurso ya viene, con una tarjeta de regalo de $15 de In-N-Out para el ganador. &iquest;No ganaste esta vez? Tienes otra oportunidad muy pronto, as&iacute; que sigue creando arte." if es
               else "The next contest is on its way, with a $15 In-N-Out gift card for the winner. Did not win this time? You have another chance very soon, so keep making art."))
    return banner_html + intro + first + hm + nxt

def build():
    nav_inner=('      <div class="silva-breadcrumb">\n'
        '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
        '        <span class="bc-sep">&rsaquo;</span>\n'
        '        <a href="/curriculum.html" class="bc-hide-sm">Announcements</a>\n'
        '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
        '        <span class="bc-current">Cover Decoration Winners</span>\n'
        '      </div>\n'
        '      <div class="silva-nav-spacer"></div>')
    html=wrap_page("Cover Decoration Contest Winners | Digital Arts 1A | PVHS",
                   nav_inner, top_wrap(side(False), side(True)), "")
    html=ent(html)
    ban_check(html, OUT)
    open(os.path.join(ROOT,"curriculum/shared",OUT),"w",encoding="utf-8").write(html)
    print("wrote", OUT, len(html), "bytes")

build()
