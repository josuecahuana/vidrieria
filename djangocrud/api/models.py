from django.db import models

# Create your models here.
class Glass(models.Model):
    nombre = models.CharField(max_length=32)
    costo = models.DecimalField(max_digits=7, decimal_places=2)
    tipo = models.CharField(max_length=32, default='None') # Define color y/o tipo. Ej (Catedral rojo)
    descripcion = models.CharField(max_length=100, default='None') 
    largo = models.IntegerField(default=0) # Medido en centimetros
    alto = models.IntegerField(default=0) # Medido en centimetros
    grosor = models.IntegerField(default=0) # Medido en milimetros
    id = models.IntegerField(primary_key=True)
    imagen = models.ImageField(upload_to="vidrios", null=True)