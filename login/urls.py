from django.urls import path
from .views import pag_login, pag_registrar, pag_recuperar_senha

urlpatterns = [
    path('', pag_login, name='login'),
    path('login/', pag_login, name='login'),
    path('registrar/', pag_registrar, name='registrar'),
    path('recuperacao/', pag_recuperar_senha, name='recuperar_senha')
]
