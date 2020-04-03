from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
Users = get_user_model()

class Shirts(models.Model):
    shirt_size = models.CharField('Tamanho da camisa', max_length=3)
    shirt_type = models.CharField('Tipo da camisa', max_length=10)
    color = models.CharField('Cor da Camisa', max_length=15)

    class Meta:
        verbose_name = 'Camisa'
        verbose_name_plural = 'Camisas'

    def __str__(self):
        return self.tshirt_type

class RequestShirts(models.Model):
    shirt = models.ForeignKey(Shirts, verbose_name='Camisa', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, verbose_name='Usuario', on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantidade')

    class Meta:
        verbose_name = "Relação de pedido"
        verbose_name_plural = "Relações de Pedidos"
    

    def __str__(self):
        return "{} - {}".format(self.shirt, self.quantity)
