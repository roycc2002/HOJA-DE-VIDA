from django.contrib import admin
from .models import Certificado, Producto, Formacion, Trabajo, ExperienciaGeneral

# Configuraciones visuales
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')

class FormacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'fecha')

class TrabajoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'fecha')

# Registro de modelos
admin.site.register(Certificado, CertificadoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Formacion, FormacionAdmin)
admin.site.register(Trabajo, TrabajoAdmin)
admin.site.register(ExperienciaGeneral)