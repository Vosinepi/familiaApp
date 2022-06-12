from django.shortcuts import render
from arbolFamiliarApp.models import Familia, Carga_familia_form


# Create your views here.


def index(request):
    pass
    return render(request, "index.html")


def cargar_familia(request):
    """
    If the request is a POST, then validate the form and save it.
    If the request is not a POST, then create a new form.
    Then render the template with the form.

    :param request: The request object is a Django object that contains metadata about the request sent
    to the server
    :return: The form is being returned.
    """
    if request.method == "POST":
        form = Carga_familia_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Carga_familia_form()

    return render(
        request, "cargar_datos.html", {"carga_familia_form": Carga_familia_form}
    )


def familia(request):

    lista_familia = Familia.objects.all()

    documento = {"lista_familia": lista_familia}

    return render(request, "familia.html", documento)
