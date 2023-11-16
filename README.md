## Parcial 2 - Programacion 1 . UTN Mendoza
 Roman Martin /Legajo: 50639 /Mail: roman.martin@alumnos.frm.utn.edu.ar 

# Descripción del Programa
El programa analiza secuencias de ADN para determinar si una persona es mutante o no.
Mediante una matriz que representa el ADN, en la cual busca secuencias consecutivas
de cuatro elementos en todas las direcciones( filas , columnas y diagonales)

# Resolucion del Problema 
Para poder realizar esto, el programa define funciones que sirven para recorrer la matriz 
en distintas direcciones 

* *diagonalesHaciaDerecha(matriz)* esta funcion recorre las diagonales desde la esquina inferior izquierda 
hacia la superior derecha buscando secuencias consecutivas 

* *diagonalesHaciaIzquierda(matriz)* esta funcion recorre las diagonales desde la esquina superior izquierda 
hacia la esquina inferior derecha buscando secuencias consecutivas 

* *recorrerFilas(matriz)* Examina cada fila de la matriz en busca de secuencias consecutivas.

* *recorrerColumnas(matriz)* Explora cada columna de la matriz para identificar secuencias consecutivas.

* *CuatroConsecutivos(lista)* Esta funcion ayuda a las anteriores a identificar si hay secuencias de 
cuatro elementos repetidos y cuenta cuantas secuencias hay 

* *isMutant(cadena)* Función principal que convierte la cadena de ADN en una matriz y utiliza las funciones 
anteriores para contar el número total de secuencias consecutivas encontradas.

si el numero total de secuencias es igual o mayor a 2 la funcion devuelve "True"(es mutante)
caso contrario devuelve "False" (no es mutante)

* *Codigo principal* Solicita al usuario una matriz que represente un ADN y luego por medio de
la funcion isMutant determina si es mutante o no 

## Como ejecutar el programa 
* Tener python Instalado en el sistema 
* clonar el repositorio con el comando : git clone https://github.com/RomanMartin1/parcial2-mutantes.git
* Ejecutar el archivo python mutantes.py
* Ingresa una matriz válida separando las filas con comas (,)
* El programa determina si es mutante o no 
* Tenes la opcion elegir ingresar otro ADN o salir del programa.

*NOTA* Aqui tienes un caso mutante: #ATGCGA,CAGTGC,TTATGT,AGAAGG,CCCCTA,TCACTG
       y un caso no mutante: #TTGCGA,AAGTGC,TTATTT,AGATGG,GCGTCA,TCACTG
       Esto te servira para realizar tus pruebas 
