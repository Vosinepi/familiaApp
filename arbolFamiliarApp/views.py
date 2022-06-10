from cmath import nan
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse
from arbolFamiliarApp.models import Familia, Carga_familia_form


# Create your views here.


def index(request):
    pass
    return render(request, "index.html")


def cargar_familia(request):
    if request.method == "POST":
        form = Carga_familia_form(request.POST)
        if form.is_valid():
            form.save()  # does nothing, just trigger the validation
    else:
        form = Carga_familia_form()

    return render(
        request, "cargar_datos.html", {"carga_familia_form": Carga_familia_form}
    )


def familia(request):

    lista_familia = Familia.objects.all()

    documento = {"lista_familia": lista_familia}

    return render(request, "familia.html", documento)
