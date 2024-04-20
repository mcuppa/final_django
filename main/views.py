from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

