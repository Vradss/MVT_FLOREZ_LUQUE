from xml.dom import NoModificationAllowedErr
from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Madre 
# Create your views here.

def lista_familiares(request):
    familia = Madre.objects.all()
    if not familia:
        familiar1 = Madre( nombre = "Bertha", apellido = "Luque", edad= 54 , fecha_nac = "1954-02-14")
        familiar1.save()

    return render(request , "familia.html", {"familia": familia})


    

    



    

