from django.shortcuts import render

# Create your views here.

def inicio(request):


    context = {
        'titulo': 'Inicio'
    }
    return render(request, 'inicio.html', context)

def medico(request)

    context = {
        'titulo': 'Médico'
    }
    return render(request, 'inicio.html', context)

def usuario(request)

    context = {
        'titulo': 'Usuario'
    }
    return render(request, 'inicio.html', context)