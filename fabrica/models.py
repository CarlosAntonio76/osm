from django.db import models


class Fabrica(models.Model):
     nome_fabrica = models.CharField(max_length=40)
     cnpj_fabrica = models.CharField(max_length=18)
     ie_fabrica = models.CharField(max_length=12)
     cep_fabrica = models.CharField(max_length=10)
     endereco_fabrica = models.CharField(max_length=30)
     numero = models.IntegerField(4)
     complemento = models.CharField(max_length=8)
     bairro_fabrica = models.CharField(max_length=30)
     cidade_fabrica = models.CharField(max_length=30)
     telefone_fabrica = models.CharField(max_length=12)
     email_fabrica = models.EmailField()

     class Meta:
          ordering = ('id',)
          verbose_name = 'fabrica'
          verbose_name_plural ='fabricas'


     def __str__(self):
          return self.nome_fabrica
