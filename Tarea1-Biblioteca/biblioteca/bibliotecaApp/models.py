from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50);
    fechaNacimiento = models.DateField();


class Libro(models.Model):
    titulo = models.CharField(max_length=50);
    autor = models.ManyToManyField(Autor);
    fechaPublicacion = models.DateField();

    def __str__(self):
        return self.titulo;
    