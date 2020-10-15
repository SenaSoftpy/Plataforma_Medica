from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Roles)
admin.site.register(Medicos)
admin.site.register(GruposFamiliares)
admin.site.register(Pacientes)
admin.site.register(Reportes)
admin.site.register(HistoriaMedica)