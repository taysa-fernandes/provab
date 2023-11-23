from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome + " - " + self.sigla_estado 

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    coordenador =  models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.nome 

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=150)
    endereco = models.CharField(max_length=250)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

class Client(models.Model):
    nome_client = models.CharField(max_length=250)
    email = models.EmailField()
    telefone = models.CharField(max_length=9)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
