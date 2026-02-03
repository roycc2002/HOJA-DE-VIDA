import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .models import Certificado, Producto

# --- TUS VISTAS NORMALES ---
def home(request):
    return render(request, "home.html")

def experiencia(request):
    return render(request, "experiencia.html")

def cursos(request):
    certificados = Certificado.objects.all()
    return render(request, "cursos.html", {"certificados": certificados})

def academicos(request):
    return render(request, "academicos.html")

def laborales(request):
    return render(request, "laborales.html")

def venta_garaje(request):
    return render(request, 'venta_garaje.html')

# --- GENERADOR DE PDF "A LA CARTA" ---
def descargar_pdf(request):
    # 1. Verificamos qué casillas marcó el usuario.
    # Si llega algo en request.GET, usamos eso. Si no, activamos todo por defecto.
    if request.GET:
        ver_perfil = request.GET.get('check_perfil')
        ver_experiencia = request.GET.get('check_experiencia')
        ver_formacion = request.GET.get('check_formacion')
        ver_cursos = request.GET.get('check_cursos')
        ver_venta = request.GET.get('check_venta')
    else:
        # Si alguien entra directo al link sin formulario, mostramos todo
        ver_perfil = 'on'
        ver_experiencia = 'on'
        ver_formacion = 'on'
        ver_cursos = 'on'
        ver_venta = 'on'

    # 2. Buscamos datos en la BD solo si el usuario pidió esas secciones
    certificados = Certificado.objects.all() if ver_cursos else None
    productos = Producto.objects.all() if ver_venta else None
    
    # 3. Empaquetamos todo para enviarlo al HTML
    data = {
        'ver_perfil': ver_perfil,
        'ver_experiencia': ver_experiencia,
        'ver_formacion': ver_formacion,
        'certificados': certificados, 
        'productos': productos
    }
    
    template = get_template('cv_pdf.html')
    html = template.render(data)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Hoja_Vida_Juan_Roy.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)

    if pisa_status.err:
       return HttpResponse('Error al generar PDF: <pre>' + html + '</pre>')
    return response

# --- FUNCIÓN DE IMÁGENES (No tocar) ---
def link_callback(uri, rel):
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        s_url = settings.STATIC_URL 
        s_path = uri.replace(s_url, "") 
        path = finders.find(s_path)
        if not path:
             path = os.path.join(settings.STATIC_ROOT, s_path)
    else:
        path = uri

    if not os.path.isfile(path):
        print("ERROR PDF: No se encuentra la imagen en: " + str(path))
        return None 
    return path