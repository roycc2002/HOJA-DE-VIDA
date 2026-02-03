from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# IMPORTANTE: Aquí importamos todos tus modelos (los viejos y los nuevos)
from .models import Certificado, Producto, Formacion, Trabajo, ExperienciaGeneral

def home(request):
    return render(request, 'home.html')

def experiencia(request):
    # Trae los datos de la tabla ExperienciaGeneral
    experiencias = ExperienciaGeneral.objects.all()
    return render(request, 'experiencia.html', {'experiencias': experiencias})

def cursos(request):
    certificados = Certificado.objects.all()
    return render(request, 'cursos.html', {'certificados': certificados})

def academicos(request):
    # Trae los datos de la tabla Formacion
    estudios = Formacion.objects.all()
    return render(request, 'academicos.html', {'estudios': estudios})

def laborales(request):
    # Trae los datos de la tabla Trabajo
    trabajos = Trabajo.objects.all()
    return render(request, 'laborales.html', {'trabajos': trabajos})

def venta_garaje(request):
    productos = Producto.objects.all()
    return render(request, 'venta_garaje.html', {'productos': productos})

def pdf(request):
    # 1. Verificamos qué casillas marcó el usuario en el menú lateral
    # Si marcó el checkbox, la variable será True
    mostrar_perfil = request.GET.get('check_perfil') == 'on'
    mostrar_experiencia = request.GET.get('check_experiencia') == 'on'
    mostrar_formacion = request.GET.get('check_formacion') == 'on'
    mostrar_cursos = request.GET.get('check_cursos') == 'on'
    mostrar_venta = request.GET.get('check_venta') == 'on'

    # 2. Traemos TODA la información de la base de datos
    certificados = Certificado.objects.all()
    productos = Producto.objects.all()
    estudios = Formacion.objects.all()
    trabajos = Trabajo.objects.all()
    experiencias = ExperienciaGeneral.objects.all()

    # 3. Empaquetamos todo en el contexto para enviarlo al HTML del PDF
    context = {
        'mostrar_perfil': mostrar_perfil,
        'mostrar_experiencia': mostrar_experiencia,
        'mostrar_formacion': mostrar_formacion,
        'mostrar_cursos': mostrar_cursos,
        'mostrar_venta': mostrar_venta,
        
        # Datos de la BD
        'certificados': certificados,
        'productos': productos,
        'estudios': estudios,
        'trabajos': trabajos,
        'experiencias': experiencias,
    }

    # 4. Renderizamos el PDF
    template_path = 'cv_pdf.html' # Asegúrate de tener este archivo HTML creado para el diseño del PDF
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    # 'inline' hace que se abra en el navegador, 'attachment' lo descarga directo
    response['Content-Disposition'] = 'inline; filename="mi_hoja_de_vida.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF <pre>' + html + '</pre>')
    
    return response