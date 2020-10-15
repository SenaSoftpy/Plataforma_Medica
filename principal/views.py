from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout #  son necesarios para el inicio de sesion
from django.contrib.auth.forms import AuthenticationForm


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

def inicio_sesion(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario') # recogemos el dato que nos llega en el name de los campos del formulario
        clave_paciente = request.POST.get('clave') 

        # paciente = authenticate(request, nombre_paciente=usuario, clave_paciente=contrasena)

        # print(clave)
        # if contrasena == clave:
        #     print("La clave")

        # if paciente is not None:
        #     login(request, paciente) #esto nos crea la sesion de usuario. Le pasamos el request y el usuario que queremos identificar
        #     return redirect('usuario')
        # else:
        #     messages.warning(request, 'Credenciales incorrectas')

    context = {
        'title': 'Iniciar Sesión'
    }
    return render(request, 'usuario/inicio_sesion.html', context)