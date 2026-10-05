# CalculadoraUNIR
Calculadora de promedios
# Calculadora de promedios escolares

Este proyecto consiste en una calculadora sencilla de promedios realizada en Python.

El programa permite introducir diferentes materias junto con sus calificaciones y, a partir de esos datos, muestra un pequeño resumen con la información más importante.

## Funcionalidades

La calculadora permite:

- Introducir el nombre de varias materias.
- Introducir una calificación entre 0 y 10 para cada materia.
- Validar que la calificación introducida sea correcta.
- Calcular el promedio general.
- Mostrar qué materias están aprobadas y cuáles están reprobadas.
- Identificar la materia con la nota más alta.
- Identificar la materia con la nota más baja.
- Mostrar un resumen final con todos los resultados.

Para considerar una materia aprobada se utiliza una nota mínima de 5.0.

## Estructura del programa

El programa está dividido en varias funciones para organizar mejor el código:

- `ingresar_calificaciones()`: recoge las materias y sus calificaciones.
- `calcular_promedio()`: calcula la media de todas las notas.
- `determinar_estado()`: separa las materias aprobadas y reprobadas.
- `encontrar_extremos()`: busca la nota más alta y la más baja.
- `main()`: coordina la ejecución del programa y muestra el resumen final.

Las materias y las calificaciones se almacenan en dos listas separadas, utilizando la misma posición para relacionar cada materia con su nota.

## Ejecución

Para ejecutar el programa se puede utilizar el siguiente comando:

```bash
python calculadora_promedios.py