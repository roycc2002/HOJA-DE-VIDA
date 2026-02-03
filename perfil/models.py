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
    
    # --- NUEVOS MODELOS ---

class Formacion(models.Model):
    titulo = models.CharField(max_length=100)  # Ej: Tecnología en TI
    institucion = models.CharField(max_length=100) # Ej: ULEAM
    descripcion = models.TextField(blank=True) # Ej: En curso
    fecha = models.CharField(max_length=50, blank=True) # Ej: 2023 - Presente

    def __str__(self):
        return self.titulo

class Trabajo(models.Model):
    cargo = models.CharField(max_length=100) # Ej: Técnico Automotriz
    empresa = models.CharField(max_length=100) # Ej: Taller X
    descripcion = models.TextField() # Lo que hacías ahí
    fecha = models.CharField(max_length=50) 

    def __str__(self):
        return self.cargo

class ExperienciaGeneral(models.Model):
    tipo = models.CharField(max_length=100) # Ej: Prácticas, Voluntariado
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo