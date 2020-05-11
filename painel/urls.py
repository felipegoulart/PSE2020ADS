from django.urls import path
from .views import *

urlpatterns = [
    path('', painel, name='painel'),
    path('adicionar', add_arquivos, name='adicionar'),
    path('delete/<int:id>', deletar, name='deletar'),
    path('dash/<int:id>', dash, name='dash'),
    path('logout', logout_view, name='logout'),
]