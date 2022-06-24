from django.urls import path
from .views import *

urlpatterns = [
    path("familia/", familia, name="familia"),
    path("cargar-datos/", cargar_familia, name="cargar_familia"),
    path("grafico/", grafico, name="grafico"),
    path("eliminar-familiar/<int:id>/", eliminar_familiar, name="eliminar_familiar"),
]
