from django.db import models
from django.contrib.auth.models import User



class Categoria(models.Model):
     categoria = models.CharField(max_length=30)
     ativo = models.BooleanField(default=True)

     class Meta:
          ordering = ('id',)
          verbose_name ='categoria'
          verbose_name_plural = 'categorias'


     def __str__(self):
          return self.categoria

