from django.shortcuts import render

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