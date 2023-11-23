from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome + " - " + self.sigla_estado 
    
class Client(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    telefone = models.CharField(max_length=9)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome

class Dvd(models.Model):
    titulo = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    valor = models.FloatField()
    
    def __str__(self):
        return self.titulo
    
class Reserva(models.Model):
    data_reserva = models.DateField()
    data_entrega = models.DateField()
    valor =  models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    funcionario =  models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    dvd = models.ForeignKey(Dvd,on_delete=models.CASCADE)
    


