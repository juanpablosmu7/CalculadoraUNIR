def ingresar_calificaciones():
    materias = []
    calificaciones = []

    while True:
        materia = input("\nIntroduce el nombre de la materia: ")

        # Validación de la calificación
        while True:
            try:
                calificacion = float(input("Introduce la calificación (0-10): "))

                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: la calificación debe estar entre 0 y 10.")

            except ValueError:
                print("Error: debes introducir un número.")

        # Guardamos los datos en listas separadas
        materias.append(materia)
        calificaciones.append(calificacion)

        # Preguntamos si desea continuar
        continuar = input("¿Deseas introducir otra materia? (s/n): ").lower()

        if continuar != "s":
            break

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

    # Comprobamos que se haya introducido alguna materia
    if len(materias) == 0:
        print("\nNo se ha introducido ninguna materia.")
        print("Programa finalizado.")
        return

    # Realizamos los cálculos
    promedio = calcular_promedio(calificaciones)

    aprobadas, reprobadas = determinar_estado(calificaciones)

    indice_maximo, indice_minimo = encontrar_extremos(calificaciones)

    # Mostramos el resumen
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