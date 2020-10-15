from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegistroPacientes
from .models import Pacientes
# Create your views here.

def inicio(request):


    context = {
        'titulo': 'Inicio'
    }
    return render(request, 'index.html', context)

def medico(request):

    context = {
        'titulo': 'Médico'
    }
    return render(request, 'medico/medico.html', context)

def usuario(request):

    context = {
        'titulo': 'Usuario'
    }
    return render(request, 'usuario/usuario.html', context)
 
def pagina_registrarse(request):

    formulario_registro = RegistroPacientes()

    if request.method == 'POST':
        formulario_registro = RegistroPacientes(request.POST)
        if formulario_registro.is_valid():
            try:  
                formulario_registro.save()
                messages.success(request, 'Te has registrado Correctamente') 
                return redirect('index')  
            except Exception as ex:  
                print(ex)
        else:
            messages.success(request, 'No se efectuo el registro')
    else:  
        formulario_registro = RegistroPacientes()

    context = {
        'titulo': 'Registrarse',
        'formulario_registro': formulario_registro
    }  
    return render(request,'usuario/registro.html',context)  