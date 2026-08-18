from django.shortcuts import render
from rest_framework import viewstes # importa o viewset a partir da biblioteca restframwwork
from .models import Produto
from .serializers import ProdutosSerializer

# importando metodo para exibir uma pagina home

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Django ! Aplicações Web 2026 - 2 - Aula  02 Loja de Produtos")

    # Cria a classe Produtosviewset responsável por permitir fazer o crude

class ProdutoViewSet(viewstes.ModelViewset):
    queryset + Produto.objects.all().order_by("-id")
    serializer_class = ProdutosSerializer

    
# Create your views here.
