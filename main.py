from src.greedy_search import (
    busqueda_greedy,
    busqueda_local,
    estaciones,
    estaciones_necesitadas,
)
import src.plot as plot


def main():
    buscar_estado = busqueda_greedy(estaciones.copy(), estaciones_necesitadas)
    plot.plot_busqueda_greedy(*buscar_estado)

    num_estados_nocubiertos = busqueda_local(estaciones.copy(), estaciones_necesitadas)
    plot.plot_busqueda_local(num_estados_nocubiertos)
