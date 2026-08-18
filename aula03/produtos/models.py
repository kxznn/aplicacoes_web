from django.db import models

# Create your models here.


class Produtos (models. Model): 
    nome = models.CharField(max_length=120) # definindo o tamanho do nome do produto com tamanho maximo de 120 caracteres
    quantidade + models.PositiveIntegerField(default=0) # quantindade de produtos
    preco = models.DecimalField(max_digits=10, decimal_places=2) #definindo a qtde de digitos e casas decimais
    created_at = models.DataTimeField(auto_now_add = True) # registro de tempo automatico quando o prooduto é carregado

# cria a função 

def __str__(self):
    return f"{self.nome} (qtde={self.quantidade})"