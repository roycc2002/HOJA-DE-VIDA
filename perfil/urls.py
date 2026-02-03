from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('cursos/', views.cursos, name='cursos'),
    path('academicos/', views.academicos, name='academicos'),
    path('laborales/', views.laborales, name='laborales'),
    path('venta-garaje/', views.venta_garaje, name='venta_garaje'),
    path('descargar-pdf/', views.descargar_pdf, name='pdf'),
]