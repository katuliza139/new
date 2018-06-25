from django.conf.urls import url
from django.urls import include, path,re_path
from django.views import *
from django import forms

urlpatterns = [
    re_path(r'^articulo/crear/', CrearArticulo.as_view(), name="articulo"),
    re_path(r'^articulo/(?P<arti>\d+)$',articulo_detalle,name="articulo_detalle"),
    re_path(r'^articulo/palabra/$',buscar_por_pal, name="palabra_busqueda"),
    re_path(r'^articulo/validar/(?P<artic>\d+)$',validar_articulo,name="articulo_validado"),
    re_path(r'^articulo/busqueda/(?P<catg>\d+)$',buscar_por_categoria,name="buscar_por_categoria"),
    re_path(r'^articulo/validar/$',articulo_validar, name="articulos_por_validar"),
    re_path(r'^categoria/crear/$',CrearCategoria.as_view(),name="crear_categoria"),
    re_path(r'^signup/$', usuarios.signup, name='signup'),
    re_path(r'^articulo/notificaciones/$', notificaciones,name="notificaciones")

]
