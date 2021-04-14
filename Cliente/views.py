from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse

from Cliente.models import Cliente
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from Cliente.form import ClienteForm


from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return HttpResponse("Soy la pagina de HotelKadana")

 
# def Cliente_view(request):
#       if request.method =='POST':
#          form = ClienteForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('Cliente:index')
#       else:
#            form=ClienteForm()
#        return render(request, 'Cliente/cliente_form.html',{'form':form})

# def Cliente_list(request):
#    cliente=Cliente.objects.all()
#    contexto={"Cliente": cliente}
#    return render(request, "cliente/cliente_list.html", contexto)

class ClienteCreate(CreateView):
   model=Cliente
   form_class= ClienteForm 
   template_name= 'cliente/cliente_form.html'
   success_url= reverse_lazy('Cliente_listar')

class Cliente_list(ListView):
   model=Cliente
   template_name='cliente/cliente_list.html'

class Cliente_actualizar(UpdateView):
   model=Cliente
   form_class= ClienteForm
   template_name = 'cliente/cliente_form.html'
   success_url= reverse_lazy('Cliente_listar')

class Cliente_eliminar(DeleteView):
   model=Cliente
   form_class= ClienteForm
   template_name = 'cliente/cliente_eliminar.html'
   success_url= reverse_lazy('Cliente_listar')





