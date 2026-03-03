# grupo_periodo.py

def calcular_periodo(configuracion):

    partes = configuracion.strip().split()
    mayor = 0

    for parte in partes:
        nivel = int(parte[0])  # el número antes de la letra
        if nivel > mayor:
            mayor = nivel

    return mayor


def calcular_grupo(configuracion):

    partes = configuracion.strip().split()
    ultimo = partes[-1]  # último subnivel

    # Ejemplo: "3d8"
    nivel = int(ultimo[0])
    bloque = ultimo[1]
    electrones = int(ultimo[2:])

    # Bloque s
    if bloque == "s":
        return electrones

    # Bloque p
    if bloque == "p":
        return 10 + electrones

    # Bloque d
    if bloque == "d":
        # buscar también el subnivel s del mismo nivel
        electrones_s = 0

        for parte in partes:
            if parte.startswith(f"{nivel}s"):
                electrones_s = int(parte[2:])

        return electrones_s + electrones

    return "Grupo desconocido"