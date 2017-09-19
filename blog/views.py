from django.shortcuts import render, redirect
from .models import Publicacion
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm


# Create your views here.
def listar_pub(request):
    pub = Publicacion.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_pub.html',{'pub': pub})

def detalle_pub (request, pk):
    p= get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'p': p})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('postear', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('postear', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
