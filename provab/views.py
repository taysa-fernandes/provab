from django.urls import reverse_lazy
from .models import Hospedagem
from .forms import HospedagemForm
from django.views.generic import CreateView,UpdateView,ListView,TemplateView,DeleteView

class HospedagemEditar(UpdateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = 'provab/form.html'
    success_url = reverse_lazy('hospedagem_listar')
    pk_url_kwarg = 'id'
    
class HospedagemDeletar(DeleteView):
    model = Hospedagem
    success_url = reverse_lazy('hospedagem_listar')
    pk_url_kwarg = 'id'
    
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
class HospedagemCriar(CreateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = 'provab/form.html'
    success_url = reverse_lazy('hospedagem_listar')
    
class HospedagemListar(ListView):
    model = Hospedagem
    template_name = 'provab/hospedagens.html'
    context_object_name = 'hospedagens'