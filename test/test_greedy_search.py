import pytest
from src.greedy_search import *

def test_encontrar_mejor_estacion():
    estados_cubiertos = set (["wa", "id"])

    estaciones = {
        "kone": set(["wa", "id", "mt"]),
        "ktwo": set(["or", "nv", "ca"]),
        "kthree": set(["nv", "ut"]),
    }
    
    mejor_estacion, mejor_covertura = encontrar_mejor_estacion(estaciones, estados_cubiertos)
    assert mejor_estacion == "ktwo"
    assert mejor_covertura == 3