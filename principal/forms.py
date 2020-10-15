# importamos formularios
from django import forms 
from principal.models import Pacientes

class RegistroPacientes(forms.ModelForm):
    class Meta:
        model  = Pacientes
        # Le decimos los campos que queremos tener 
        fields = ['id_paciente','nombre_paciente', 'apellido_paciente', 'fecha_nacimiento_paciente', 'correo_paciente', 'telefono_paciente', 'medico', 'grupo_familiar', 'clave_paciente']
        widgets = {
            'grupo_familiar': forms.HiddenInput(attrs={
                'value': 1
            }), 
            'medico': forms.HiddenInput(attrs={
                'value': 1
            }), 
            'id_paciente': forms.NumberInput(attrs={
                'placeholder': 'Número de Identificación',
                'autofocus': 'autofocus',
                'class': 'form-control text-center mb-4', }),
            'nombre_paciente': forms.TextInput(attrs={
                'placeholder': 'Nombres',
                'class': 'form-control text-center mb-4', }),
            'apellido_paciente': forms.TextInput(attrs={
                'placeholder': 'Apellidos',
                'class': 'form-control text-center mb-4', }),
            'fecha_nacimiento_paciente': forms.DateInput(attrs={
                'placeholder': 'Fecha de Nacimiento',
                'class': 'form-control text-center mb-4', }),
            'correo_paciente': forms.EmailInput(attrs={
                'placeholder': 'Correo',
                'class': 'form-control text-center mb-4', }),
            'telefono_paciente': forms.NumberInput(attrs={
                'placeholder': 'Telefono',
                'class': 'form-control text-center mb-4', }),
            'clave_paciente': forms.PasswordInput(attrs={
                'placeholder': 'Contraseña',
                'class': 'form-control text-center mb-4', }),
        }