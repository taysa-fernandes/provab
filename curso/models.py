from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    coordenador =  models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.nome 
