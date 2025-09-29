from django.db import models

class Orden(models.Model):
    numero_orden = models.CharField(max_length=50, unique=True)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    talla_inicio = models.CharField(max_length=10)
    talla_fin = models.CharField(max_length=10)
    total_piezas = models.IntegerField()
    foto_modelo = models.ImageField(upload_to="ordenes/fotos/")
    especificaciones_pdf = models.FileField(upload_to="ordenes/pdfs/")

    def __str__(self):
        return f"Orden {self.numero_orden} - {self.modelo}"