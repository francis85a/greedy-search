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
    estados_necesitados = []
    ganancias = []
    numero_estados_cubiertos = []

    while estados_cubiertos < estados_necesitados:
        mejor_cobertura, mejor_estacion = buscar_mejor_estacion(
            estaciones_copia, estados_cubiertos
        )

        if mejor_estacion:
            estados_cubiertos |= estaciones_copia[mejor_estacion]
            estados_necesitados.append(mejor_estacion)
            numero_estados_cubiertos.append(len(estados_cubiertos))
            ganancias.append(mejor_cobertura)
            del estaciones_copia[mejor_estacion]

    return (estados_necesitados, numero_estados_cubiertos, ganancias, estados_cubiertos)

