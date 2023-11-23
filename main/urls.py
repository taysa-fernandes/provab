"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aluno import views
from prova.views import dvd_criar,dvd_editar,dvd_listar,dvd_remover
from provab.views import HospedagemCriar,HospedagemDeletar,HospedagemEditar,HospedagemListar

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.Index.as_view(),name='index'),
    path('aluno/',views.AlunoCriar.as_view(),name='aluno_criar'),
    path('aluno/editar/<int:id>/',views.AlunoEditar.as_view(), name='aluno_editar'),
    path('aluno/remover/<int:id>/',views.AlunoDeletar.as_view(),name='aluno_remover'),
    path('aluno/listar',views.AlunoListar.as_view(),name='aluno_listar'),
    path('dvd/',dvd_criar, name='dvd_criar'),
    path('dvd/editar/<int:id>/',dvd_editar, name='dvd_editar'),
    path('dvd/listar',dvd_listar, name='dvd_listar'),
    path('dvd/remover/<int:id>/',dvd_remover,name='dvd_remover'),
    path('hospedagem/',HospedagemCriar.as_view(), name='hospedagem_criar'),
    path('hospedagem/editar/<int:id>/',HospedagemEditar.as_view(), name = 'hospedagem_editar'),
    path('hospedagem/remover/<int:id>/',HospedagemDeletar.as_view(), name= 'hospedagem_remover'),
    path('hospedagem/listar', HospedagemListar.as_view(), name= 'hospedagem_listar'),
]



