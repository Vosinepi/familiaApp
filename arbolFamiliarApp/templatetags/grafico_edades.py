import matplotlib.pyplot as plt
from django import template
import datetime
from collections import OrderedDict

register = template.Library()


@register.simple_tag
def grafico(familia):
    """
    It takes a list of objects, and returns a dictionary with the number of objects per month.

    :param familia: list of Familiar objects
    :return: A dictionary with the months as keys and the number of family members as values.
    """
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

    parientes = []
    for pariente in ordered_data.values():
        parientes.append(pariente)

    print(parientes)
    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(ordered_data.keys(), ordered_data.values(), color="#1d2c67", width=0.5)

    for i in range(len(parientes)):
        plt.text(
            i,
            (parientes[i] - 0.05),
            round(parientes[i], 1),
            ha="center",
            bbox=dict(facecolor="orange", alpha=0.8),
        )
    plt.xlabel("mes")
    plt.ylabel("familiares")
    plt.title("meses nacimiento")

    plt.savefig("static\img\grafico.png", transparent=True)

    return pariente_x_mes
