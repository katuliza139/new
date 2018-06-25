from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy
from .forms import *
from .models import *
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import login, authenticate
from django.db.models import Q
# Create your views here.
class CrearArticulo(CreateView, LoginRequiredMixin):
    form_class = ArticuloForm
    template_name = 'articulos/form.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        article = form.save(commit=False)
        article.user = self.request.user
        return super(CrearArticulo, self).form_valid(form)

@login_required
def buscar_por_pal(request):
    pal = request.POST['pal']
    artpal = articulo.objects.filter(Q(titulo__icontains=pal) |Q(contenido__icontains=pal))
    return render(request, 'articulos/buscar_por_palabra.html', {'pala': artpal, 'palabra': pal})

@login_required
def buscar_por_categoria(request, catg):
    cates = categoria.objects.get(pk=catg)
    articulos = articulo.objects.filter(categoria=cates,validado=True).order_by("-fecha")
    return render(request, 'articulos/busqueda_por_categoria.html',{'arti':articulos,'categoria':cates})

@login_required
def articulo_validar(request):
    if request.user.is_superuser:
        articulos = articulo.objects.filter(validado=False)
        return render(request, 'articulos/validar_articulo.html', {'validar': articulos})
    else:
        return HttpResponseRedirect(reverse('home'))

@login_required
def validar_articulo(request, artic):
    if request.user.is_superuser:
        val = articulo.objects.get(pk=artic)
        val.validado= True
        val.save()
        Notificaciones.objects.create(titulo= "Articulo nuevo "+val.titulo)
        return HttpResponseRedirect(reverse('articulos_por_validar'))
    else:
        return HttpResponseRedirect(reverse('home'))


class CrearCategoria(CreateView,LoginRequiredMixin):
    form_class= CatForm
    template_name = 'articulos/categoria_form.html'
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        nombre = request.POST["categoria"]
        Notificaciones.objects.create(titulo=str("Se creo la categoria "+nombre))
        return super(CrearCategoria, self).post(request, *args, **kwargs)

@login_required
def articulo_detalle(request, arti):
    artic = articulo.objects.get(pk=arti)
    comentarios = Comentario.objects.filter(articulo=artic).order_by("-fecha")
    if request.method=="POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.fecha = datetime.now()
            comentario.user = request.user
            comentario.articulo = artic
            comentario.save()
            Notificaciones.objects.create(titulo=str("El usuario "+comentario.user.username+" comento el articulo "+comentario.articulo.titulo))
            return HttpResponseRedirect(reverse('articulo_detalle', args={artic.pk}))
    else:
        if artic.validado==False and (request.user.is_superuser or request.user == artic.user):
            return render(request, 'articulos/detalle_articulos.html', {'articulo':artic,'comentarios':comentarios})
        elif artic.validado==True:
            form = ComentarioForm()
            return render(request, 'articulos/detalle_articulos.html', {'form':form, 'articulo':artic,'comentarios':comentarios})
        else:
            return HttpResponseRedirect(reverse('home'))

@login_required
def notificaciones(request):
    noti = Notificaciones.objects.all()
    return render(request, 'articulos/notificaciones.html',{'notif':noti})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.fecha_nac = form.cleaned_data.get('fecha_nac')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm(), SignUpForm()
    return render(request, 'signup.html', {'from': form})
