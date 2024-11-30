from django.urls import path
from . import views


urlpatterns = [
    path('ativo/', views.listagem_ativo, name='ativo'),
    path('nao_ativo/', views.listagem_nao_ativo, name='nao_ativo'),
]
