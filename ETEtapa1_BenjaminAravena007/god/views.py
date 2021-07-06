from django.shortcuts import render, redirect
from .forms import ColaboradoresForm
from .models import Colaboradores
# Create your views here.

def formulario(request):
    return render(request, 'formulario.html')
def actualizar(request):
    return render (request, 'god/actualizar.html')

def form_colaboradores(request):
    if request.method =='POST':
        colab=ColaboradoresForm(request.POST)
        if colab.is_valid():
            colab.save()
            return redirect('formulario')
    else:
        colab=ColaboradoresForm()
    return render(request, 'god/formulario.html', {'colab': colab})

def VerColaboradores(request):
    colabb = Colaboradores.objects.all()
    return render(request, 'god/mostrar.html', context={'colabb':colabb})

def modColaborador(request,id):
    mod = Colaboradores.objects.get(rut=id)

    datos ={
           'form': ColaboradoresForm(instance=mod)
    }
    if request.method == 'POST': 
        modd = ColaboradoresForm(data=request.POST, instance = mod)
        if modd.is_valid: 
            modd.save()          
            return redirect('mostrar') 
    return render(request, 'god/actualizar.html', datos)

def delColaborador(request,id):
    dele = Colaboradores.objects.get(rut=id)
    dele.delete()
    return redirect('mostrar')