from contextvars import Context
from pipes import Template
from this import d 
from django.http import HttpResponse
from django.template import Template, Context , loader


def familia(request):

    datos = {"Nombres": ["Guido Florez", "Bertha Luque" , "Laurita Florez"], "Relacion" : ["Padre", "Madre", "Hermana"]}
    plantilla = loader.get_template("familia.html")
    
    documento = plantilla.render(datos)
    return HttpResponse(documento)