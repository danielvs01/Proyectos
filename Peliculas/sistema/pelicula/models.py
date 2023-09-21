from django.db import models

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título de película')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen de película')
    descripcion= models.TextField(verbose_name='Descripcion', null=True)

    def __str__(self):
        fila = "Título: " + self.titulo + " Descripción: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()