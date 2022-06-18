import matplotlib.pyplot as plt
from django import template
import datetime
from collections import OrderedDict

register = template.Library()


@register.simple_tag
def grafico(familia):
    pariente_x_mes = dict()

    for familiar in familia:
        pariente_x_mes[
            (
                datetime.datetime.strptime(
                    str(familiar.fecha_de_nacimiento.month), "%m"
                )
            ).strftime("%b")
        ] = (
            pariente_x_mes.get(
                (
                    datetime.datetime.strptime(
                        str(familiar.fecha_de_nacimiento.month), "%m"
                    )
                ).strftime("%b"),
                0,
            )
            + 1
        )
    ordered_data = OrderedDict(
        sorted(
            pariente_x_mes.items(), key=lambda x: datetime.datetime.strptime(x[0], "%b")
        )
    )
    print(pariente_x_mes)
    print(ordered_data)
    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(ordered_data.keys(), ordered_data.values(), color="#1d2c67", width=0.5)

    plt.xlabel("mes")
    plt.ylabel("familiares")
    plt.title("meses nacimiento")

    plt.savefig("static\img\grafico.png", transparent=True)

    return pariente_x_mes
