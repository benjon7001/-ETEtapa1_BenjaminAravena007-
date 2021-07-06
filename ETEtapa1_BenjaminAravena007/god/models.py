from django.db import models

# Create your models here.
class Colaboradores(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='rut')
    image = models.ImageField(upload_to='images/', null=True, blank = True)
    nombreComp = models.CharField(max_length=40, verbose_name='Nombre completo')
    telefono = models.CharField(max_length=9, verbose_name='Numero de telefono')
    direccion =  models.CharField(max_length=30, verbose_name='Direccion')
    email = models.CharField(max_length=30, verbose_name='Email')
    contrasenia = models.CharField(max_length=30, verbose_name='Contraseña')
    def __str__(self):
        return(self.nombreComp)