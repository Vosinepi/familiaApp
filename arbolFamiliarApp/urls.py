from django.urls import path
from .views import *

urlpatterns = [
    path("familia/", familia, name="familia"),
    path("cargar-datos/", cargar_familia, name="cargar_familia"),
]
