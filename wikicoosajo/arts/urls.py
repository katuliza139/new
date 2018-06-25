from django.conf.urls import url
from django.urls import include, path,re_path
from django.views import *
from django import forms

urlpatterns = [
    url(r'^articulo/crear/$', CrearArticulo.as_view(), name="articulo"),
    url(r'^articulo/(?P<arti>\d+)$',articulo_detalle,name="articulo_detalle"),
    url(r'^articulo/palabra/$',buscar_por_pal, name="palabra_busqueda"),
    url(r'^articulo/validar/(?P<artic>\d+)$',validar_articulo,name="articulo_validado"),
    url(r'^articulo/busqueda/(?P<catg>\d+)$',buscar_por_categoria,name="buscar_por_categoria"),
    url(r'^articulo/validar/$',articulo_validar, name="articulos_por_validar"),
    url(r'^categoria/crear/$',CrearCategoria.as_view(),name="crear_categoria"),
    url(r'^signup/$', usuarios.signup, name='signup'),
    url(r'^articulo/notificaciones/$', notificaciones,name="notificaciones")

]
