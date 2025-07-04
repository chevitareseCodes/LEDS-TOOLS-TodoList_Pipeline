from django.contrib import admin
from .models import Usuario,Categoria,Tarefa

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', '_email', 'senha']
    list_display_links = ['id', 'nome', '_email', 'senha']
    search_fields = ['id', 'nome', '_email', 'senha']
    list_per_page = 25
    ordering = ['-id']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ['id', 'nome']
    search_fields = ['id', 'nome']
    list_per_page = 25
    ordering = ['-id']

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descricao', 'data_vencimento']
    list_display_links = ['id', 'titulo', 'descricao', 'data_vencimento']
    search_fields = ['id', 'titulo', 'descricao', 'data_vencimento']
    list_per_page = 25
    ordering = ['-id']

