from django.shortcuts import render,get_object_or_404,redirect
from .models import Dvd
from .forms import DvdForm

def dvd_editar(request,id):
    dvd = get_object_or_404(Dvd,id=id)
   
    if request.method == 'POST':
        form = DvdForm(request.POST,instance=dvd)

        if form.is_valid():
            form.save()
            return redirect('dvd_listar')
    else:
        form = DvdForm(instance=dvd)

    return render(request,'prova/form.html',{'form':form})

def dvd_remover(request, id):
    dvd = get_object_or_404(Dvd, id=id)
    dvd.delete()
    return redirect('dvd_listar')

def dvd_criar(request):
    if request.method == 'POST':
        form = DvdForm(request.POST)
        if form.is_valid():
            form.save()
            form = DvdForm()
        return redirect('dvd_listar')
    else:
        form = DvdForm()

    return render(request, "prova/form.html", {'form': form})

def dvd_listar(request):
    dvds = Dvd.objects.all()
    context ={
        'dvds': dvds
    }
    return render(request, "prova/dvds.html",context)

