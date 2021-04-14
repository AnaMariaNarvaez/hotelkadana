from django import forms
from Nacionalidad.models import Nacionalidad

class NacionalidadForm(forms.ModelForm):
    class Meta:
        model= Nacionalidad

        
        fields = [
            'Pais',
            'Provincia',
            'Codigo',
        ]

        labels = {
            'Pais':'Pais',
            'Provincia':'Provincia',
            'Codigo': 'Codigo',
        }
        

        widgets = {
                'Pais':forms.TextInput(attrs={'class':'form-control'}),
                'Provincia':forms.TextInput(attrs={'class':'form-control'}),
                'Codigo':forms.TextInput(attrs={'class':'form-control'}),
        }




