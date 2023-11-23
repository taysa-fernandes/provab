from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from .models import Aluno,Curso,Cidade
from .forms import AlunoForm
from django.views.generic import CreateView,UpdateView,ListView,TemplateView,DeleteView
from django.urls import reverse_lazy

class AlunoEditar(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/form.html'
    success_url = reverse_lazy('aluno_listar')
    pk_url_kwarg = 'id'
    
# def aluno_editar(request,id):
#     aluno = get_object_or_404(Aluno,id=id)
   
#     if request.method == 'POST':
#         form = AlunoForm(request.POST,instance=aluno)

#         if form.is_valid():
#             form.save()
#             return redirect('aluno_listar')
#     else:
#         form = AlunoForm(instance=aluno)

#     return render(request,'aluno/form.html',{'form':form})

class AlunoDeletar(DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno_listar')
    pk_url_kwarg = 'id'
    
    def get(self, request, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
# def aluno_remover(request, id):
#     aluno = get_object_or_404(Aluno, id=id)
#     aluno.delete()
#     return redirect('aluno_listar') # procure um url com o nome 'lista_aluno'

class AlunoCriar(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/form.html'
    success_url = reverse_lazy('aluno_listar')
    
# def aluno_criar(request):
#     if request.method == 'POST':
#         form = AlunoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = AlunoForm()
#     else:
#         form = AlunoForm()

#     return render(request, "aluno/form.html", {'form': form})

class AlunoListar(ListView):
    model = Aluno
    template_name = 'aluno/alunos.html'
    context_object_name = 'alunos'
    
    
# def aluno_listar(request):
#     alunos = Aluno.objects.all()
#     context ={
#         'alunos':alunos
#     }
#     return render(request, "aluno/alunos.html",context)

class Index(TemplateView):
    template_name = 'aluno/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_alunos'] = Aluno.objects.count()
        context['total_cidades'] = Cidade.objects.count()
        context['total_cursos'] = Curso.objects.count()
        return context
    
# def index(request):
#     total_alunos = Aluno.objects.count()
#     total_cidades = Cidade.objects.count()
#     total_curso = Curso.objects.count()
#     context = {
#         'total_alunos' : total_alunos,
#         'total_cidades' : total_cidades,
#         'total_cursos' : total_curso
#     }
#     return render(request, "aluno/index.html",context)


