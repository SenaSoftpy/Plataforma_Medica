from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index' ),
    path('inicio/', views.inicio, name='index' ),
    path('inicio-medico/', views.medico, name='medico'),
    path('inicio-usuario/', views.usuario, name='usuario'),
]