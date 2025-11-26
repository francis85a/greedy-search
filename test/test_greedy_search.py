import pytest
from src.greedy_search import *

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