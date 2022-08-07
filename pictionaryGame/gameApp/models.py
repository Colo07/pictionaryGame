from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Categoria(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, null=False)
    nombre = models.CharField(null=False, max_length=50)
    listaPalabras = models.TextField(null=False,default='asd')
    
    def __str__(self):
        txt = '{0}'
        return txt.format(self.nombre)
