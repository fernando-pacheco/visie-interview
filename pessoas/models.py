from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_admissao = models.DateField()
    funcao = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome
