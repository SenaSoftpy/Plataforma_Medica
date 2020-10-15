from django.contrib import admin
from .models import *
# Register your models here.

# Configuración del panel
titulo = "Panel de Gestión"
subTitulo = "Proyecto Pravaz"

admin.site.site_header = titulo
admin.site.site_title  = titulo 
admin.site.index_title = subTitulo

admin.site.register(Roles)
admin.site.register(Medicos)
admin.site.register(GruposFamiliares)
admin.site.register(Pacientes)
admin.site.register(Reportes)
admin.site.register(HistoriaMedica)