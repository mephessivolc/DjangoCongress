from django.db import models
from django.contrib.auth import get_user_model

from congress.models import Congress

# Create your models here.
Users = get_user_model()

class ColorShirts(models.Model):
    color = models.CharField('Cor', max_length=20)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.color

class SizeShirts(models.Model):
    size = models.CharField('Tamanho', max_length=4)
    description = models.CharField('Descrição', max_length=20)

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'

    def __str__(self):
        return self.size

class TypeShirts(models.Model):
    type_of = models.CharField('Tipo', max_length=20)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.type_of

class Shirts(models.Model):

    congress = models.ForeignKey(Congress, verbose_name='Congresso', on_delete=models.CASCADE)
    size_shirt = models.ForeignKey(SizeShirts, verbose_name='Tamanho da Camisa', on_delete=models.DO_NOTHING)
    type_shirt = models.ForeignKey(TypeShirts, verbose_name='Tipo da Camisa', on_delete=models.DO_NOTHING)
    color_shirt = models.ForeignKey(ColorShirts, verbose_name='Cor da Camisa', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Camisa'
        verbose_name_plural = 'Camisas'

    def __str__(self):
        return "{} [{} - {} ({})]".format(self.congress.username or self.congress, self.size_shirt, self.type_shirt, self.color_shirt)

class RequestShirts(models.Model):

    shirt = models.ForeignKey(Shirts, verbose_name='Camisa', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, verbose_name='Usuario', on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantidade')

    class Meta:
        verbose_name = "Relação de pedido"
        verbose_name_plural = "Relações de Pedidos"


    def __str__(self):
        return "{} - {}".format(self.shirt, self.quantity)
