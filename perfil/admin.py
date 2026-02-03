from django.contrib import admin
from .models import Certificado, Producto  # Importamos ambos

admin.site.register(Certificado)
admin.site.register(Producto)