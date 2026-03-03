from elementos import elementos
from configuracion import calcular_configuracion
from gas_noble import configuracion_abreviada
from grupo_periodo import calcular_periodo, calcular_grupo


Z = 0

try:
    Z = int(input("Ingresa el número atómico (1-118): "))
except ValueError:
    print("Error: Debes ingresar un número entero.")


if 1 <= Z <= 118:
    nombre = elementos[Z]
    config = calcular_configuracion(Z)
    config_abrev = configuracion_abreviada(Z, calcular_configuracion)
    periodo = calcular_periodo(config)
    grupo = calcular_grupo(config)

    print("Elemento:", nombre)
    print("Configuración electrónica:", config)
    print("Configuración abreviada:", config_abrev)
    print("Periodo:", periodo)
    print("Grupo:", grupo)
else:
    print("Error: Número atómico fuera de rango (1-118).")