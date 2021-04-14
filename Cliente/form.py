from django import forms
from Cliente.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente

        fields = [
            'nombre',
            'apellidos',
            'sexo',
            'edad',
            'telefono',
            'email',
            'domicilio',
            'nacionalidad',

        ]

        labels = {
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'sexo': 'Sexo',
            'edad':'Edad',
            'telefono':'Telefono',
            'email':'Email',
            'domicilio':'Domicilio',
            'nacionalidad':'Nacionalidad',
        }
            

        widgets = {
                'nombre':forms.TextInput(attrs={'class':'form-control'}),
                'apellidos':forms.TextInput(attrs={'class':'form-control'}),
                'sexo':forms.TextInput(attrs={'class':'form-control'}),
                'edad':forms.TextInput(attrs={'class':'form-control'}),
                'telefono':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.TextInput(attrs={'class':'form-control'}),
                'domicilio':forms.TextInput(attrs={'class':'form-control'}),
                'nacionalidad':forms.Select(attrs={'class':'form-control'}),
        }
               

            







        