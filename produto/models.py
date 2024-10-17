from django.db import models
from django.contrib.auth.models import User
from fabrica.models import Fabrica



'''
class Ncm(models.Model):
     cod_ncm = models.IntegerField(10)
     nome_ncm = models.CharField(60)

     class Meta:
          ordering = ('id',)

     def __str__(self):
          return self.nome_ncm
'''    
     
     
class Produtos(models.Model):
     choices_unidade = (
        ('UN', 'Unidade'),
        ('PR', 'Par'),
        ('PC', 'Peca'),
        ('MT', 'Metro'),
        ('KG', 'Kilo'),
        ('CX', 'Caixa'),
        ('DZ', 'Duzia'),
        ('RL', 'Rolo'),
        ('PT', 'Pacote'),
        ('CT', 'Cartela'),
        ('G', 'Grama'),
        ('L', 'Litro'),
        ('m3', 'Metro cúbico'),
        ('ml', 'Mililitro')

    )
     descricao = models.CharField(max_length=40)
     data = models.DateTimeField()
     #categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
     unidade = models.CharField(max_length=2, choices=choices_unidade, default='UN')
     fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
     preco = models.DecimalField(max_digits=6, decimal_places=2)
     #ncm = models.ForeignKey(Ncm, on_delete=models.CASCADE)
     reservado = models.CharField(max_length=10)
     mostrar = models.BooleanField(default=True)
     usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)


     class Meta:
       ordering = ('id',)
       verbose_name = 'Produto'
       verbose_name_plural = 'Produtos'


     def __str__(self):
            return self.descricao