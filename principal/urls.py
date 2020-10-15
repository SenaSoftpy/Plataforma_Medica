from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index' ),
    path('inicio/', views.inicio, name='index' ),
    path('inicio-medico/', views.medico, name='medico'),
    path('inicio-usuario/', views.usuario, name='usuario'),
    path('registro/', views.pagina_registrarse, name= 'registro'),
    path('inicio_sesion/', views.inicio_sesion, name="inicio"),
]
