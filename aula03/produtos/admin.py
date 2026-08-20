from django.contrib import admin
from .models import (
    Produto,  # importa a partir do models o produto
    Categoria,
    Cliente,
    Pedido,
    ItemPedido
    )
# Register your models here


# Registrando a categoria no admin

@admin.register(Categoria)

class CategoriaAdmin(admin.Model.Admin):

    list_display = ('id', 'nome')

    # filtro searchfield

    search_fileds = ('nome',)
@admin.register(Produto)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "quantidade", "preco", "categoria", "created_at")
    search_fields = ("nome",)
    list_filter = ("categoria")


# cliente 

