from fpdf import FPDF
from fpdf.enums import VAlign
from fpdf.fonts import FontFace
from PIL import Image
import json

def seccion(titulo, link=''):
    pdf.ln()
    pdf.set_fill_color(242, 242, 242)
    pdf.rect(0, pdf.get_y() - 1, 216, 10, style="F")
    pdf.set_xy(30, pdf.get_y() + 2)
    pdf.set_font("Bahnschrift", size=14)
    pdf.cell(text='$ cd '+titulo, border=0, align="C")
    if link:
        pdf.set_font("Bahnschrift", size=9)
        pdf.set_x(155)
        pdf.cell(text=link, border=0, align="C", h= pdf.font_size * 1.5, link=link)
    pdf.set_y(pdf.get_y() + 10)

pdf = FPDF(format="Letter")
pdf.add_page()

pdf.add_font("Bahnschrift", fname='fuentes/Bahnschrift-Font-Family/BAHNSCHRIFT.TTF')
pdf.add_font("Bahnschrift", fname='fuentes/Bahnschrift-Font-Family/BAHNSCHRIFT.TTF', style="b")
#Generales
pdf.set_fill_color(242, 242, 242)
pdf.rect(0, 0, 216, 41, style="F")

with pdf.round_clip(x=5, y=3, r=35):
    pdf.image(
        "iconos/foto.png",
        h=37,
        w=37,
        x=4,
        y=2,
    )

with open('datos/generales.json') as json_file:
    dGenerales = json.load(json_file)

pdf.set_fill_color(0,0,0)
#nombre
pdf.set_xy(51,6)
pdf.image("iconos/terminal-solid.svg", w=6)
pdf.set_xy(60,6)
pdf.set_font("Bahnschrift", size=18)
pdf.cell(text=dGenerales['nombre'], border=0, align="C")
pdf.ln(12)

pdf.set_font("Bahnschrift", size=12)
#correo
y = pdf.get_y()
pdf.set_x(52)
pdf.image("iconos/at-solid.svg", w=4)
pdf.set_xy(58, y)
pdf.cell(text=dGenerales['email'], border=0, align="C", link="mailto:"+dGenerales['email'])
#Cedula
pdf.set_xy(123, y-1)
pdf.image("iconos/id-card-solid.svg", w=6)
pdf.set_xy(131, y)
pdf.cell(text="Cédula profesional: "+dGenerales['cedula'], border=0, align="C")
#telefono
y=y+7
pdf.set_xy(52.5, y)
pdf.set_fill_color(0,0,0)
pdf.image("iconos/mobile-screen-solid.svg", w=3)
pdf.set_xy(58, y)
pdf.cell(text=dGenerales['celular'], border=0, align="C", link="tel:"+dGenerales['celular'])
#idiomas
pdf.set_xy(123, y)
pdf.image("iconos/language-solid.svg", w=6)
pdf.set_xy(131, y+0.5)
pdf.cell(text=dGenerales['idiomas'], border=0, align="C")
#cumpleaños
y=y+7
pdf.set_xy(52, y)
pdf.image("iconos/cake-candles-solid.svg", w=4)
pdf.set_xy(58, y+0.5)
pdf.cell(text=dGenerales['cumple'], border=0, align="C")
pdf.ln()

pdf.set_xy(30, 44)
pdf.set_font("Bahnschrift", size=10)
pdf.multi_cell(w=155, text=dGenerales['lema'], border=0, align="J")

seccion('Educación')

with open('datos/educacion.json') as json_file:
    dEducacion = json.load(json_file)
pdf.set_font("Bahnschrift", size=10)

for e in dEducacion:
    pdf.set_x(166)
    pdf.cell(text=e['periodo'], border=0, align="L", h=pdf.font_size+1)
    pdf.set_x(30)
    pdf.multi_cell(w=136, text=e['carrera'], border=0, align="J", h=pdf.font_size+1)
    pdf.set_x(30)
    pdf.multi_cell(w=153, text=e['universidad'], border=0, align="J", h=pdf.font_size+1)
    if e != dEducacion[-1]:
        pdf.ln(3)
seccion('Experiencia')

with open('datos/experiencia.json') as json_file:
    dExperiencia = json.load(json_file)
pdf.set_font("Bahnschrift", size=10)

pdf.set_fill_color(0,0,0)
pdf.set_x(10)
with pdf.table(v_align=VAlign.T, 
                line_height=1 + pdf.font_size,
                text_align="LEFT",
                borders_layout="MINIMAL",
                first_row_as_headings=False) as table:
    row = table.row()
    for e in dExperiencia:
        lista = e['actividades'].split('|')
        n = ''
        for l in lista:
            n += '- '+l+'\n'
        row.cell(e['entidad']+'\n'+e['periodo']+'\n'+e['puesto']+'\n\n'+n[:-1])

seccion('Cursos_Conferencias_y_Actividades_Varias', dGenerales['enlaceCursos'])

pdf.set_x(30)

with open('datos/cursos.json') as json_file:
    dCursos = json.load(json_file)
pdf.set_font("Bahnschrift", size=10)
pdf.set_fill_color(0,0,0)
greyscale = (242, 242, 242)
with pdf.table(width=154, 
                col_widths=(10, 140),
                cell_fill_color=greyscale,
                cell_fill_mode="ROWS",
                v_align=VAlign.T, 
                line_height=pdf.font_size * 1.3,
                text_align="LEFT",
                borders_layout="NONE",
                first_row_as_headings=False) as table:
    for d in dCursos:
        row = table.row()
        row.cell(d['anio'])
        if d['link']:
            row.cell(d['desc']+'  '+d['link'], link=d['link'])
        else:
            row.cell(d['desc'])

seccion('Habilidades_y_Software')

pdf.set_font("Bahnschrift", size=10)
with open('datos/habilidades.json') as json_file:
    dHabilidades = json.load(json_file)

pdf.set_x(30)
pdf.set_fill_color(0,0,0)
ry = pdf.get_y()
rx = pdf.get_x()
maxy = ry
ban = 0
for d in dHabilidades:
    ban += 1
    if ban == 3:
        rx += 51
        pdf.set_xy(rx, ry)
        ban = 1
    else:
        pdf.set_x(rx)

    pdf.cell(text=d['titulo'], border=0, align="L", h=pdf.font_size * 1.9)
    pdf.ln()
    pdf.set_x(rx)

    for x in d['contenido']:
        nx = pdf.get_x()
        ny = pdf.get_y()
        pdf.set_xy(nx, ny + 1)
        if x['svg'] in ['macos.svg', 'curioso.svg', 'persistente.svg']:
            pdf.image("iconos/"+x['svg'], w=2.5)
        elif x['svg'] in ['navicat.svg', 'apache.svg']:
            pdf.image("iconos/"+x['svg'], w=3.5)
        else:
            pdf.image("iconos/"+x['svg'], w=3)
        pdf.set_xy(nx + 5, ny)
        pdf.cell(text=x['desc'], border=0, align="L", h=pdf.font_size * 1.3)
        pdf.ln()
        pdf.set_x(rx)
    
    pdf.ln(2)
    
    if pdf.get_y() > maxy:
        maxy = pdf.get_y()

pdf.set_y(maxy)
seccion('exit')



pdf.output("cv_new.pdf")