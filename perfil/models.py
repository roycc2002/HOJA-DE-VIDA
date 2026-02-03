from django.db import models

# Modelo para tus diplomas
class Certificado(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='certificados/')

    def __str__(self):
        return self.titulo

# --- NUEVO: Modelo para la Venta de Garaje ---
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Ejemplo: 10.50
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre