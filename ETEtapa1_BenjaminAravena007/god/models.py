from django.db import models

# Create your models here.
class Colaboradores(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='rut')
    image = models.ImageField(upload_to='images/', null=True, blank = True)
    nomComp = models.CharField(max_length=40, verbose_name='Nombre')
    email = models.CharField(max_length=30, verbose_name='Email')
    direccion =  models.CharField(max_length=30, verbose_name='Direccion')
    telefono = models.CharField(max_length=9, verbose_name='Numero telefono')
    contrasenia = models.CharField(max_length=30, verbose_name='Contraseña')
    def __str__(self):
        return(self.nomComp)