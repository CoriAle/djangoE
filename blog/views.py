from django.shortcuts import render
from .models import Publicacion
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def listar_pub(request):
    pub = Publicacion.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html',{'pub': pub})

def detalle_pub (request, pk):
    p= get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'p': p})
