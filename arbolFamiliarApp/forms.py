from django.forms import ModelForm
from arbolFamiliarApp.models import Familia

# It creates a form for the Familia model.
class Carga_familia_form(ModelForm):
    class Meta:
        model = Familia
        fields = ["nombre", "apellido", "fecha_de_nacimiento"]
