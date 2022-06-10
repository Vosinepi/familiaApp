import datetime
from django import template

register = template.Library()


@register.simple_tag
def edad(pariente):
    año_nacimiento = pariente.fecha_de_nacimiento.year
    return datetime.datetime.today().year - año_nacimiento
