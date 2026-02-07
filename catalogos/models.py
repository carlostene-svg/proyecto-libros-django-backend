from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    biografia = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='autores/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50, blank=True, null=True)
    resumen = models.TextField(blank=True)
    portada = models.ImageField(upload_to='libros/', blank=True, null=True)

    def __str__(self):
        return self.titulo