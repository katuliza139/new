from arts.models import *

def categorias(request):
    cate = categoria.objects.all()
    return {'cat': cate}

def notifica(request):
    nott = Notificaciones.objects.all().order_by('-id')[:5]
    return {'nott': nott}

