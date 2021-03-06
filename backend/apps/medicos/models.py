from django.db import models

# Create your models here.


class Especialidade(models.Model):
    especialidade = models.CharField(max_length=150)

    def __str__(self):
        return self.especialidade


class Medico(models.Model):
    crm = models.IntegerField(null=False, unique=True)
    nome = models.CharField(max_length=150, null=False,
                            blank=False, unique=True)
    especialidade = models.ForeignKey(Especialidade, models.CASCADE)
    email = models.EmailField(null=True, blank=True, unique=True)
    telefone = models.IntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.nome
