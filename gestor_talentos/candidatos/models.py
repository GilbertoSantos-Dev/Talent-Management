from django.db import models

class Candidato(models.Model):
    STATUS_LIST = [
        ('disponivel', 'disponivel'),
        ('indisponivel', 'indisponivel'),   
    ]

    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    escolaridade = models.CharField(max_length=100)
    habilidades = models.CharField(max_length=100)
    status = models.CharField(max_length=100,choices=STATUS_LIST,default='disponivel')
    data_atualizacao = models.DateField()

    def __str__(self):
        return self.nome
