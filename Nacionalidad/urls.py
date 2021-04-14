from django.conf.urls import url, include 
from Nacionalidad.views import index, Nacionalidad_list, NacionalidadCreate, Nacionalidad_actualizar, Nacionalidad_eliminar


urlpatterns= [
    url(r'^$', index),
    url(r'^listar$',  Nacionalidad_list.as_view(), name='nacionalidad_listar'),
    url(r'^nuevo', NacionalidadCreate.as_view(), name='nacionalidad_crear'),
    url(r'^editar/(?P<pk>\d+)$', Nacionalidad_actualizar.as_view(), name= 'nacionalidad_actualizar'),
    url(r'^eliminar/(?P<pk>\d+)$', Nacionalidad_eliminar.as_view(), name= 'nacionalidad_eliminar'),
]