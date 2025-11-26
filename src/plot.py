import matplotlib.pyplot as plt

def plot_greedy_search_global(estaciones_necesitadas, num_estados_cubiertos, ganancias, estados_cubiertos):
    """
    Grafica:
    - Barras: nuevos estados cubiertos por estación
    - Línea: estados totales cubiertos acumulados
    """
    print("covered states:", estados_cubiertos)
    print("stations needed:", estaciones_necesitadas)
    print("num states covered:", num_estados_cubiertos)
    print("gradients:", ganancias)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Barras: nuevos estados cubiertos
    ax1.bar(estaciones_necesitadas, ganancias, label="Nuevos estados cubiertos")
    ax1.set_ylabel("Nuevos estados")
    ax1.tick_params(axis="y")

    # Línea: cobertura acumulada
    ax2 = ax1.twinx()
    ax2.plot(estaciones_necesitadas, num_estados_cubiertos, marker="o", label="Total acumulado")
    ax2.set_ylabel("Total estados cubiertos")

    # Títulos
    plt.title("Progreso de la cobertura por estación")
    plt.xticks(rotation=45)

    # Leyendas combinadas
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

    fig.tight_layout()
    plt.show()


def plot_greedy_search_local(num_estados_nocubiertos):
    """
    Grafica el resultado de la búsqueda local (estados sin cubrir por iteración)
    """
    print("num states uncovered:", num_estados_nocubiertos)

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(num_estados_nocubiertos)), num_estados_nocubiertos)
    plt.title("Mínimos locales en la búsqueda local")
    plt.xlabel("Iteración")
    plt.ylabel("Estados sin cubrir")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()