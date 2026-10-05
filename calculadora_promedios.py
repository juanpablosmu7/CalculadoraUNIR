def ingresar_calificaciones():
    materias = []
    calificaciones = []

    while True:
        continuar = input("\n¿Deseas introducir una materia? (s/n): ").lower()

        if continuar != "s":
            break

        materia = input("Introduce el nombre de la materia: ")

        while True:
            try:
                calificacion = float(input("Introduce la calificación (0-10): "))

                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: la calificación debe estar entre 0 y 10.")

            except ValueError:
                print("Error: debes introducir un número.")

        materias.append(materia)
        calificaciones.append(calificacion)

    return materias, calificaciones


def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio


def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []

    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    indice_maximo = 0
    indice_minimo = 0

    for i in range(1, len(calificaciones)):
        if calificaciones[i] > calificaciones[indice_maximo]:
            indice_maximo = i

        if calificaciones[i] < calificaciones[indice_minimo]:
            indice_minimo = i

    return indice_maximo, indice_minimo


def main():
    print("=== CALCULADORA DE PROMEDIOS ESCOLARES ===")

    materias, calificaciones = ingresar_calificaciones()

    # Caso especial: no se ha introducido ninguna materia
    if len(materias) == 0:
        print("\nNo se ha introducido ninguna materia.")
        print("Programa finalizado.")
        return

    promedio = calcular_promedio(calificaciones)

    aprobadas, reprobadas = determinar_estado(calificaciones)

    indice_maximo, indice_minimo = encontrar_extremos(calificaciones)

    print("\n========== RESUMEN FINAL ==========")

    print("\nMaterias y calificaciones:")

    for i in range(len(materias)):
        print(f"{materias[i]}: {calificaciones[i]:.2f}")

    print(f"\nPromedio general: {promedio:.2f}")

    print("\nMaterias aprobadas:")

    if len(aprobadas) > 0:
        for i in aprobadas:
            print(f"- {materias[i]}: {calificaciones[i]:.2f}")
    else:
        print("No hay materias aprobadas.")

    print("\nMaterias reprobadas:")

    if len(reprobadas) > 0:
        for i in reprobadas:
            print(f"- {materias[i]}: {calificaciones[i]:.2f}")
    else:
        print("No hay materias reprobadas.")

    print(
        f"\nMejor calificación: "
        f"{materias[indice_maximo]} - {calificaciones[indice_maximo]:.2f}"
    )

    print(
        f"Peor calificación: "
        f"{materias[indice_minimo]} - {calificaciones[indice_minimo]:.2f}"
    )

    print("\nGracias por utilizar la calculadora. ¡Hasta pronto!")


if __name__ == "__main__":
    main()