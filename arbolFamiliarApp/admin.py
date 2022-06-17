from django.contrib import admin
from arbolFamiliarApp.models import Familia

# Register your models here.


class FamiliaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "fecha_de_nacimiento",
    )
    search_fields = ("nombre", "apellido")


admin.site.register(Familia, FamiliaAdmin)
