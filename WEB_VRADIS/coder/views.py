from xml.dom import NoModificationAllowedErr
from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Madre
# Create your views here.

def lista_familiares(request):
    madre = Madre.objects.all()
    return render(request , "familia.html")


    

