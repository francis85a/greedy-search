import random

estaciones_necesitadas = set(["mt","wa","or","id","nv","ut","ca","az"])

estaciones_añadidas = set(
    ["nm", "tx", "ok", "ks", "co", "ne", "sd", "wy", "nd", "ia","mn", "mo", "ar", "la"]
)

estaciones_necesitadas.update(estaciones_añadidas)

estaciones = {}
estaciones["kone"] = set(["id", "nv", "ut"])
estaciones["ktwo"] = set(["wa", "id", "mt"])
estaciones["kthree"] = set(["or", "nv", "ca"])
estaciones["kfour"] = set(["nv", "ut"])
estaciones["kfive"] = set(["ca", "az"])

estaciones["ksix"] = set(["nm", "tx", "ok"])
estaciones["kseven"] = set(["ok", "ks", "co"])
estaciones["keight"] = set(["ks", "co", "ne"])
estaciones["knine"] = set(["ne", "sd", "wy"])
estaciones["kten"] = set(["nd", "ia"])
estaciones["keleven"] = set(["mn", "mo", "ar"])
estaciones["ktwelve"] = set(["la"])
estaciones["kthirteen"] = set(["mo", "ar"])

def buscar_mejor_estacion(estaciones, estados_cubiertos):
    mejor_estacion = ""
    mejor_cobertura = 0
    for estacion, estados_estacion in estaciones.items():
        nuevos_estados = estados_estacion - estados_cubiertos
        if len(nuevos_estados) > mejor_cobertura:
            mejor_estacion = estacion
            mejor_cobertura = len(nuevos_estados)
    return mejor_estacion, mejor_cobertura

def busqueda_greedy (estaciones, estados_necesitados):
    
    estaciones_copia = estaciones.copy()
    estados_cubiertos = set()
    estaciones_necesitadas = []
    ganancias = []
    numero_estados_cubiertos = []

    while estados_cubiertos < estados_necesitados:
        mejor_estacion, mejor_ganancia = buscar_mejor_estacion(
            estaciones_copia, estados_cubiertos
        )

        if mejor_estacion:
            estados_cubiertos |= estaciones_copia[mejor_estacion]
            estaciones_necesitadas.append(mejor_estacion)
            numero_estados_cubiertos.append(len(estados_cubiertos))
            ganancias.append(mejor_ganancia)
            del estaciones_copia[mejor_estacion]

    return (estaciones_necesitadas, numero_estados_cubiertos, ganancias, estados_cubiertos)


def busqueda_local(estaciones, estados_necesitados):
    NUM_BUSQUEDAS = 40
    MAX_NUM_ESTACIONES = 10
    num_estados_nocubiertos = []

    for _ in range(NUM_BUSQUEDAS):
        estados_cubiertos = set()
        nombres_estaciones = list(estaciones.keys())
        random_estaciones = random.sample(nombres_estaciones, k=MAX_NUM_ESTACIONES)
        for estacion in random_estaciones:
            estados_cubiertos |= (estaciones[estacion])
        num_estados_nocubiertos.append(len(estados_necesitados - estados_cubiertos))
    return num_estados_nocubiertos