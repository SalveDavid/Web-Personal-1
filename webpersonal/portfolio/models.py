from django.db import models


class Project(models.Model):
    tittle = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    link = models.URLField(verbose_name='Dirección Web', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') # Se añadira la hora automaticamente cuando se cree la primera vez
    updated = models.DateTimeField(auto_now=True,  verbose_name='Fecha de edición')   # Se ejecuta cada vez que se actualiza una instancia

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.tittle
