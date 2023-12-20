from fpdf import FPDF
from PIL import Image

pdf = FPDF(format="Letter")
pdf.add_page()

pdf.add_font("Bahnschrift", fname='fuentes/Bahnschrift-Font-Family/BAHNSCHRIFT.TTF')
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

pdf.set_fill_color(0,0,0)
#nombre
pdf.set_xy(51,6)
pdf.image("iconos/terminal-solid.svg", w=6)
pdf.set_xy(60,6)
pdf.set_font("Bahnschrift", size=18)
pdf.cell(text="Jesús Alfredo Bravo Méndez", border=0, align="C")
pdf.ln(12)
#correo
y = pdf.get_y()
pdf.set_x(52)
pdf.image("iconos/at-solid.svg", w=4)
pdf.set_xy(58, y)
pdf.set_font("Bahnschrift", size=12)
pdf.cell(text="isc.alfredobravo@gmail.com", border=0, align="C")

pdf.set_xy(123, y-1)
pdf.image("iconos/id-card-solid.svg", w=6)
pdf.set_xy(131, y)
pdf.cell(text="Cédula profesional: 13282553", border=0, align="C")

pdf.set_x(52)
pdf.image("iconos/at-solid.svg", w=4)


pdf.output("cv_new.pdf")