from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'perfiles/anahi/assets/CV_Anahi_Ramirez_2026_PUBLICO.pdf'
font='/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV',font+'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB',font+'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB')
W,H=595.276,841.89
c=canvas.Canvas(str(OUT),pagesize=(W,H))
c.setTitle('Anahí Guadalupe Ramírez Patiño - CV público 2026')
c.setAuthor('Anahí Guadalupe Ramírez Patiño')
ink='#382c32'; wine='#7d354b'; muted='#574950'
c.setFillColor(colors.HexColor('#fcf9f6'));c.rect(0,H-128,W,128,fill=1,stroke=0)
c.setFillColor(colors.HexColor(wine));c.roundRect(39,H-79,43,43,12,fill=1,stroke=0)
c.setFont('DVB',15);c.setFillColor(colors.white);c.drawString(47,H-63,'AR')
c.setFillColor(colors.HexColor(ink));c.setFont('DVB',16.2);c.drawString(98,H-52,'ANAHÍ GUADALUPE')
c.drawString(98,H-73,'RAMÍREZ PATIÑO')
c.setFont('DV',8.7);c.setFillColor(colors.HexColor(wine));c.drawString(40,H-103,'INGENIERA EN GESTIÓN EMPRESARIAL | ADMINISTRACIÓN Y FACTURACIÓN')
y=H-150
style=ParagraphStyle('body',fontName='DV',fontSize=9,leading=13,textColor=colors.HexColor(muted),spaceAfter=0)
bold=ParagraphStyle('bold',parent=style,fontName='DVB',textColor=colors.HexColor(ink))
def para(text,st=style,gap=6,indent=0):
 global y
 p=Paragraph(text,st);_,h=p.wrap(W-80-indent,1000);p.drawOn(c,40+indent,y-h);y-=h+gap
def heading(text):
 global y
 y-=9;c.setStrokeColor(colors.HexColor('#e5d6d9'));c.line(40,y-16,W-40,y-16)
 c.setFont('DVB',9);c.setFillColor(colors.HexColor(wine));c.drawString(40,y,text.upper());y-=27
def bullet(text):para('• '+text,gap=3,indent=3)
heading('Perfil profesional')
para('Ingeniera en Gestión Empresarial titulada, con más de dos años de experiencia en administración, facturación CFDI 4.0, complementos de pago, cuentas por cobrar y atención a clientes. Experiencia en cotizaciones, control documental, reportes y apoyo en inventarios. Formación en Cadena de Suministro y uso de Excel para organizar información.')
heading('Experiencia profesional')
para('Tecnicentro Rudi de Tequila | Auxiliar administrativa',bold,3)
para('Septiembre de 2024 - actualidad',gap=6)
for t in ['Elaboración y revisión de facturas CFDI 4.0 y seguimiento a incidencias de facturación.','Complementos de pago y seguimiento a cuentas por cobrar y actividades de cobranza.','Carga de facturas y documentación en portales empresariales de clientes y seguimiento a su recepción.','Preparación de cotizaciones y presupuestos conforme a requerimientos de clientes.','Apoyo en inventarios, organización de información y reportes administrativos.','Atención a clientes y seguimiento a sus solicitudes.']:bullet(t)
heading('Formación académica')
para('Ingeniería en Gestión Empresarial | Generación 2019-2023',bold,3)
para('Tecnológico Superior de Jalisco, Campus Tequila. Título obtenido; cédula profesional en trámite.',gap=5)
para('<b>Especialidad en Cadena de Suministro</b> | Agosto - diciembre de 2023.<br/>Integrada al plan académico de la carrera. Constancia.',gap=3)
heading('Conocimientos y herramientas')
para('<b>Administración:</b> CFDI 4.0, complementos de pago, portales de clientes, cuentas por cobrar, cobranza, cotizaciones, presupuestos, reportes y control documental.',gap=4)
para('<b>Excel y herramientas:</b> fórmulas, tablas y organización de información; conocimientos básicos de dashboards. Microsoft Office y Canva.',gap=4)
para('<b>Inventarios y procesos:</b> apoyo en inventarios, análisis de rotación, fundamentos de stock mínimo y máximo, Kanban y conocimientos básicos de indicadores KPI.',gap=3)
heading('Proyecto académico')
para('Propuesta de mejora de procesos e inventarios mediante Kanban | PRISA',bold,3)
para('Agosto - diciembre de 2023. Análisis de ventas y rotación, propuesta de stock mínimo y máximo e identificación de posibles cuellos de botella. Desarrollo teórico y actividades prácticas iniciales; sin implementación completa.',gap=3)
heading('Competencias y formación complementaria')
para('Organización y atención al detalle · Pensamiento analítico · Comunicación · Trabajo en equipo · Adaptabilidad.',gap=4)
para('Cursos: Emprendimiento Social (marzo de 2022) y Modelo de Emprendimiento (septiembre de 2022).',gap=2)
assert y>48, f'Contenido fuera del margen: {y}'
c.setStrokeColor(colors.HexColor('#e5d6d9'));c.line(40,39,W-40,39)
c.setFont('DV',7);c.setFillColor(colors.HexColor(muted));c.drawString(40,26,'CV público · Octubre de 2026 · Sin datos personales de contacto')
c.setFillColor(colors.HexColor(wine));c.drawRightString(W-40,26,'Consultar portafolio ↗')
c.linkURL('https://descobt-stack.github.io/Equipo-Dinamita-Alfa-Lobo-Buena-Onda/perfiles/anahi/index.html',(W-150,20,W-40,36),relative=0)
c.showPage();c.save();print(f'{OUT} · margen inferior {y:.1f} pt')
