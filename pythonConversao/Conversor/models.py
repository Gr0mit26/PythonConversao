from django.db import models

# Create your models here.

class Moeda(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.nome