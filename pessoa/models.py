from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)