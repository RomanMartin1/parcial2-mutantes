#Funcion que recorre la matriz en zig zag de izquierda a derecha y de abajo hacia arriba
def diagonalesHaciaDerecha(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    diagonales = []

    for suma_indices in range(filas + columnas - 1):
        if suma_indices % 2 == 0:  
            for fila in range(min(suma_indices, filas - 1), max(0, suma_indices - columnas + 1) - 1, -1):
                columna = columnas - 1 - (suma_indices - fila)
                diagonales.append(matriz[fila][columna])
        else:  
            for fila in range(max(0, suma_indices - columnas + 1), min(suma_indices, filas - 1) + 1):
                columna = columnas - 1 - (suma_indices - fila)
                diagonales.append(matriz[fila][columna])
    return CuatroConsecutivos(diagonales)

#Funcion que recorre la matriz en zig zag de derecha a izquierda y de arriba hacia abajo
def diagonalesHaciaIzquierda(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    diagonales = []

    for suma_indices in range(filas + columnas - 1):
        if suma_indices % 2 == 0:  
            for fila in range(min(suma_indices, filas - 1), max(0, suma_indices - columnas + 1) - 1, -1):
                columna = suma_indices - fila
                diagonales.append(matriz[fila][columna])
        else:  
            for fila in range(max(0, suma_indices - columnas + 1), min(suma_indices, filas - 1) + 1):
                columna = suma_indices - fila
                diagonales.append(matriz[fila][columna])
    return CuatroConsecutivos(diagonales)
#funcion que recorre las filas de una matriz
def recorrerFilas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    recorrido = []
    
    for fila in range(filas):
        for columna in range(columnas):
            recorrido.append(matriz[fila][columna])
    return CuatroConsecutivos(recorrido)

#funcion que rrecorre las columnas de una matriz
def recorrerColumnas(matriz):
    filas = len(matriz)
    recorrido = []
    columnas = len(matriz[0])
    for columna in range(columnas):
        for fila in range(filas):
            recorrido.append(matriz[fila][columna])
    return CuatroConsecutivos(recorrido)

# funcion que detecta si es mutante  

def isMutant(adn):
    
    filas = adn.split(",")
    matriz = [list(fila) for fila in filas]
    for fila in matriz:
        print(fila)
    secuencias = 0
    if diagonalesHaciaIzquierda(matriz):
        secuencias = secuencias + 1
    if diagonalesHaciaDerecha(matriz):
        secuencias = secuencias + 1
    if recorrerFilas(matriz):
        secuencias = secuencias + 1
    if recorrerColumnas(matriz):
        secuencias = secuencias + 1
    if secuencias >=2:
        return True
    else:
        return False
#funcion que nos dice si un elemento se repite mas de 4 veces 
def  CuatroConsecutivos(lista):
    for i in range(len(lista) - 3):
        if lista[i] == lista[i + 1] == lista[i + 2] == lista[i + 3]:
            return True
    return False



#codigo principal

adn= "ATGCGA,CAGTGC,TTTTAT,AGACGG,CCCCTA,TCACTG"


if isMutant(adn):
    print("El ADN ingresado ES MUTANTE")
else:
    print("El ADN ingresado NO es MUTANTE")