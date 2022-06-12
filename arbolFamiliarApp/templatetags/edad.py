import datetime
from django import template

register = template.Library()


@register.simple_tag
def edad(pariente):
    """
    > The function `edad` takes a `pariente` as an argument and returns the difference between the
    current year and the year of the `pariente`'s birth

    :param pariente: the name of the object that will be passed to the function
    :return: The age of the person.
    """
    año_nacimiento = pariente.fecha_de_nacimiento.year
    return datetime.datetime.today().year - año_nacimiento
