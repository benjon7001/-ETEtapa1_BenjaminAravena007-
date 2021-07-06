from django.shortcuts import render, redirect
from .forms import ColaboradoresForm
from .models import Colaboradores
# Create your views here.

def form(request):
    return render(request, 'formulario.html')
def actl(request):
    return render (request, 'god/actualizar.html')

def form_colaboradores(request):
    if request.method =='POST':
        col=ColaboradoresForm(request.POST)
        if col.is_valid():
            col.save()
            return redirect('formulario')
    else:
        col=ColaboradoresForm()
    return render(request, 'god/formulario.html', {'col': col})

def VerColaboradores(request):
    coll = Colaboradores.objects.all()
    return render(request, 'god/mostrar.html', context={'coll':coll})

def modColaborador(request,id):
    modcol = Colaboradores.objects.get(rut=id)

    datos ={
           'form': ColaboradoresForm(instance=modcol)
    }
    if request.method == 'POST': 
        moddcol = ColaboradoresForm(data=request.POST, instance = modcol)
        if moddcol.is_valid: 
            moddcol.save()          
            return redirect('mostrar') 
    return render(request, 'god/actualizar.html', datos)

def dlColaborador(request,id):
    dl = Colaboradores.objects.get(rut=id)
    dl.delete()
    return redirect('mostrar')