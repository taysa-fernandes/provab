from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
class Quarto(models.Model):
    apartamento = models.IntegerField()
    valor = models.FloatField()
    
    
class Hospedagem(models.Model):
    data_entrada = models.DateField()
    data_saida = models.DateField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto,on_delete=models.CASCADE)

class Consumo(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    valor = models.FloatField()
    hospedagem = models.ForeignKey(Hospedagem,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
