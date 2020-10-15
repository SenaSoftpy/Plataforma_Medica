from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index' ),
    path('inicio/', views.inicio, name='index' ),
    path('inicio-medico/', views.medico, name='medico'),
    path('inicio-usuario/', views.usuario, name='usuario'),
    path('registro/', views.pagina_registrarse, name= 'registro'),
    path('iniciar-sesion/', views.inicio_sesion, name="inicio"),
    path('cambiar-medico/', views.cambio_medico, name="cambioMedico"),
    path('historia-clinica/', views.historia_clinica, name="historiaClinica"),
    path('solicitud-familiar/', views.grupo_familiar, name="grupoFamiliar"),
]
