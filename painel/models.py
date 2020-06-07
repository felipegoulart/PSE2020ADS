from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Arquivos(models.Model):
    nome = models.CharField(max_length=20, null= True, blank= True)
    arquivos = models.FileField(upload_to='csv')
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False,  null= True, blank= True)