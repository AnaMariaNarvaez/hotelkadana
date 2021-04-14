from django.conf.urls import url, include
from Cliente.views import index, Cliente_list, ClienteCreate, Cliente_actualizar, Cliente_eliminar

urlpatterns=[
    url(r'^index', index),
    url(r'^listar', Cliente_list.as_view(), name='Cliente_listar'),
    url(r'^nuevo', ClienteCreate.as_view(), name='cliente_crear'),
    url(r'^editar/(?P<pk>\d+)$', Cliente_actualizar.as_view(), name= 'Cliente_actualizar'),
    url(r'^eliminar/(?P<pk>\d+)$', Cliente_eliminar.as_view(), name= 'Cliente_eliminar'),

]