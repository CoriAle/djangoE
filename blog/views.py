from django.shortcuts import render

# Create your views here.
def listar_pub(request):
    return render(request, 'blog/listar_pub.html',{})
