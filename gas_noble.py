# gas_noble.py

gases_nobles = {
    2: "Helio",
    10: "Neón",
    18: "Argón",
    36: "Kriptón",
    54: "Xenón",
    86: "Radón",
    118: "Oganesón"
}

def configuracion_abreviada(Z, calcular_configuracion):

    config_completa = calcular_configuracion(Z).strip()

    gas_base = 0

    for numero in sorted(gases_nobles.keys()):
        if numero < Z:
            gas_base = numero

    if gas_base == 0:
        return config_completa

    simbolo = gases_nobles[gas_base]

    config_gas = calcular_configuracion(gas_base).strip()

    
    config_restante = config_completa.replace(config_gas, "").strip()

    return f"[{simbolo}] {config_restante}"