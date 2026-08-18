from rest_framework import serializers
from .models import Produtos

# Criando a classe Serializers produtos

class ProdutosSerializer(serializers.MOdelSerializer):
    class Meta: 
        model = Produtos
        fields = ["id", "nome", "quantidade", "preco", "created_at"]