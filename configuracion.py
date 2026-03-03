subniveles = [
    ("1s", 2),
    ("2s", 2),
    ("2p", 6),
    ("3s", 2),
    ("3p", 6),
    ("4s", 2),
    ("3d", 10),
    ("4p", 6),
    ("5s", 2),
    ("4d", 10),
    ("5p", 6),
    ("6s", 2),
    ("4f", 14),
    ("5d", 10),
    ("6p", 6),
    ("7s", 2),
    ("5f", 14),
    ("6d", 10),
    ("7p", 6)
]

def calcular_configuracion(Z):

    electrones = Z
    configuracion = ""

    for subnivel, capacidad in subniveles:

        if electrones > 0:

            if electrones >= capacidad:
                configuracion += f"{subnivel}{capacidad} "
                electrones -= capacidad
            else:
                configuracion += f"{subnivel}{electrones} "
                electrones = 0

    return configuracion