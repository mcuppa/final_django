from django.shortcuts import render
from posts.models import *

# Create your views here.
def articles(request):
    articulos = Post.objects.all()
    return render(request, 'articles.html',{'articulos':articulos})