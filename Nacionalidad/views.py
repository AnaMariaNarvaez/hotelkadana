from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Nacionalidad.models import Nacionalidad
from Nacionalidad.form import NacionalidadForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return HttpResponse ("Index")

    
class Nacionalidad_list(ListView):
    model=Nacionalidad
    template_name='nacionalidad/nacionalidad_list.html'

    
class NacionalidadCreate(CreateView):
   model=Nacionalidad
   form_class= NacionalidadForm 
   template_name= 'Nacionalidad/nacionalidad_form.html'
   success_url= reverse_lazy('nacionalidad_listar')

class Nacionalidad_actualizar(UpdateView):
   model=Nacionalidad
   form_class= NacionalidadForm
   template_name = 'Nacionalidad/nacionalidad_form.html'
   success_url= reverse_lazy('nacionalidad_listar')

class Nacionalidad_eliminar(DeleteView):
   model=Nacionalidad
   form_class= NacionalidadForm
   template_name = 'Nacionalidad/nacionalidad_eliminar.html'
   success_url= reverse_lazy('nacionalidad_listar')