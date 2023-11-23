from django.contrib import admin
from .models import Cidade,Client,Reserva,Funcionario,Dvd

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display=('nome','sigla_estado')
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display=('nome','email','telefone','cidade')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display=('data_reserva','data_entrega','valor','client','funcionario','dvd')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display=('nome','cpf','email')

@admin.register(Dvd)
class DvdAdmin(admin.ModelAdmin):
    list_display=('titulo','text','valor')