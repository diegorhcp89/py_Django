from django.contrib import admin

# Register your models here.
from .models import Cliente, Categoria, Produto, Fornecedor

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Produto)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'contato', 'nome', 'email', 'telefone')
    search_fields = ('nome', 'e-mail')
