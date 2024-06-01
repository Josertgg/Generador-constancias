from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Solicitar información del usuario
nombres = input("Ingresa tus nombres: ")
apellidos = input("Ingresa tus apellidos: ")
cedula = input("Ingresa tu número de cédula: ")
pnf = input("Ingresa tu Programa Nacional de Formación (PNF): ")
seccion = input("Ingresa tu sección: ")
nucleo = input("Ingresa el núcleo al que perteneces: ")
periodo = input("Ingresa el período académico: ")
turno = input("Ingresa el turno: ")

# Crear un archivo PDF
pdf_filename = "informacion_usuario.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)

# Ajustar márgenes
left_margin = 50
right_margin = 50
top_margin = 700
bottom_margin = 50

# Escribir la información en el PDF
c.setFont("Helvetica", 12)
c.drawString(left_margin +150, top_margin -10, "REPÚBLICA BOLIVARIANA DE VENEZUELA")
c.drawString(left_margin +65, top_margin -25, "MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN UNIVERSITARIA")
c.drawString(left_margin +80, top_margin -40,"UNIVERSIDAD NACIONAL EXPERIMENTAL DE LA GRAN CARACAS")
c.drawString(left_margin +235, top_margin -60, "UNEXCA")

c.drawString(left_margin +180, top_margin -150, "CONSTANCIA DE ESTUDIOS")

ancho_maximo = 400  # Ajusta según tus necesidades

# Divide el texto en párrafos
parrafo1 = (
    f"Quien suscribe, Jefe(E) Ing. Yovany Díaz Coordinación Control de Estudios de la UNIVERSIDAD "
)
parrafo2 = (
    f"NACIONAL EXPERIMENTAL DE LA GRAN CARACAS, hace constar por medio de la presente "
)
parrafo3 = (
    f" que el(la) ciudadano(a) {nombres} {apellidos}, titular de la cédula de identidad "
)
parrafo4 = (
    f" N.º {cedula}, es estudiante activo(a) de esta universidad en el núcleo {nucleo}, cursando  "
 
)
parrafo5 = (f"el período académico {periodo}  del Programa Nacional  de Formación PNF {pnf},")
parrafo6 = (f"sección {seccion}, turno{turno}.")
# Asumiendo que 'c' es tu objeto de lienzo
c.setFont("Helvetica", 12)  # Ajusta el tamaño de fuente según tus necesidades
c.drawString(left_margin, top_margin - 200, parrafo1)
c.drawString(left_margin, top_margin - 220, parrafo2)
c.drawString(left_margin, top_margin - 240, parrafo3)
c.drawString(left_margin, top_margin - 260, parrafo4)
c.drawString(left_margin, top_margin - 280, parrafo5)
c.drawString(left_margin, top_margin - 300, parrafo6)

c.drawString(left_margin +220, top_margin -550, "Atentamente")
c.drawString(left_margin +180, top_margin -600,"_________________________")
c.drawString(left_margin +180, top_margin -620,"JEFE(E) ING. YOVANY DÍAZ")
c.drawString(left_margin +120, top_margin -640,"JEFE(E) COORDINACIÓN CONTROL DE ESTUDIOS")

# Guardar el PDF
c.save()

print(f"Se ha creado el archivo PDF: {pdf_filename}")
