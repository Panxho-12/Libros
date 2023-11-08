from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Libros

# Create your views here.

def renderTemplate(request):
    return render(request, 'firstTemplate/templade1.html')

def librosData(request):
    libros = Libros.objects.all()
    data = {'libros' : libros}
    return render(request,'firstTemplate/libros.html',data)


