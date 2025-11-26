import pytest
from src.greedy_search import buscar_mejor_estacion
from src.greedy_search import busqueda_greedy

@pytest.mark.buscar_mejor_estacion
def test_buscar_mejor_estacion():
    estados_cubiertos = set (["wa", "id"])

    estaciones = {
        "kone": set(["wa", "id", "mt"]),
        "ktwo": set(["or", "nv", "ca"]),
        "kthree": set(["nv", "ut"]),
    }
    
    mejor_estacion, mejor_cobertura = buscar_mejor_estacion(estaciones, estados_cubiertos)
    assert mejor_estacion == "ktwo"
    assert mejor_cobertura == 3

@pytest.mark.buscar_mejor_estacion
def test_buscar_mejor_estacion():
    estados_cubiertos = set()
    estaciones = {
        "kone": set(["wa", "id", "mt"]),
        "ktwo": set(["or", "nv", "ca"]),
        "kthree": set(["nv", "ut"]),
    }

    mejor_estacion, mejor cobertura = buscar_mejor_estacion(estaciones, estados_cubiertos)

    assert mejor_estacion in ["kone", "ktwo"]
    assert mejor_cobertura == 3

@pytest.mark.busqueda_greedy
def test_busqueda_greedy():
    
    estados_necesitados = set(["id","nv","ut","mt","wa","or","ca","az"])
    
    estaciones = {
        "kone": set(["id", "nv", "ut"]),
        "ktwo": set(["wa", "id", "mt"]),
        "kthree": set(["or", "nv", "ca"]),
        "kfour": set(["nv", "ut"]),
        "kfive": set(["ca", "az"]),
    }

    estaciones_necesitadas, numero_estados_cubiertos, ganancias, estados_cubiertos = (
        busqueda_greedy(estaciones, estados_necesitados)
    )

    assert estados_cubiertos == estados_necesitados
    assert set(estaciones_necesitadas) == set(["kone", "ktwo", "kthree", "kfive"])
    assert numero_estados_cubiertos[-1] == len(estados_necesitados)
    assert all(ganancia > 0 for ganancia in ganancias)
    assert ganancias == sorted(ganancias, reverse=True)
    
