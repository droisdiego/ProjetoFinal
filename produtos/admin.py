from django.contrib import admin
from produtos.models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','marca','preco','imagem','descricao')

# Register your models here.
