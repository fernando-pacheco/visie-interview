from django.urls import path
from . import views

urlpatterns = [
    path('listar_pessoas/', views.listar_pessoas, name='listar_pessoas'),
    path('adicionar_pessoas/', views.adicionar_pessoas, name='adicionar_pessoas'),
    path('atualizar_pessoas/<int:pessoa_id>', views.atualizar_pessoas, name='atualizar_pessoas'),
    path('editar_pessoas/', views.editar_pessoas, name='editar_pessoas'),
    path('deletar_pessoas/<int:pessoa_id>', views.deletar_pessoas, name='deletar_pessoas'),
    path('home/', views.home, name='home'),
]
