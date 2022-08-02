from django.shortcuts import render
from django.http import HttpResponse
from coder.models import madre
# Create your views here.

def familiares(request, madre):

    new_var = madre[0].nombre
    return HttpResponse( f"Nombre de la madre {new_var}")

    

