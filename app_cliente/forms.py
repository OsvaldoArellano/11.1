from django import forms
from .models import Cliente, Vehiculo


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email', 'rfc', 'direccion', 'foto_cliente']


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['matricula', 'marca', 'modelo', 'anio', 'kilometraje', 'foto_vehiculo']