from django.shortcuts import render
from .models import *
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    maqolalar = Maqola.objects.all()
    return render(request, 'blog.html', {'maqolalar':maqolalar})

def maqola(request, son):
    post = Maqola.objects.get(id=son)
    rasmlar = Rasmlar.objects.filter(maqola=post)
    return render(request, 'maqola.html', {'m':post, 'rasmlar':rasmlar})