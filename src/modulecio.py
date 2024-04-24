#! /bin/env python3

import time

peliculas = ["La vida de Bryan", "Matrix", "Torrente"]


def instrucciones(tabulacion=False):
    """Print essencial information about Python modules and packages.
    """
    lista_instrucciones = [
        "Un módulo Python es un fichero que contiene código Python",
        "Un paquete Python agrupa varios módulos y submódulos.",
        "Para que un directorio se trasforme en paquete Python, agrégale un \
__init.py__",
        "¡Has difrutado de la tercera versión de este paquete!"
    ]
    espacios = ""

    for instr in lista_instrucciones:
        time.sleep(1)
        print(espacios + instr)
        if tabulacion:
            espacios = espacios + "    "
