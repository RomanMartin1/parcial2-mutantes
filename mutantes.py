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

def isMutant(cadena):
    adn =cadena.upper()
    filas = adn.split(",")
    matriz = [list(fila) for fila in filas]
    
    secuencias = 0
    secuencias = secuencias + diagonalesHaciaIzquierda(matriz)
    secuencias = secuencias + diagonalesHaciaDerecha(matriz)
    secuencias = secuencias +recorrerFilas(matriz)
    secuencias = secuencias +recorrerColumnas(matriz)  
    if secuencias >=2:
        return True
    else:
        return False
#funcion que nos dice si un elemento se repite mas de 4 veces 
def  CuatroConsecutivos(lista):
    contador = 0 
    for i in range(len(lista) - 3):
        if lista[i] == lista[i + 1] == lista[i + 2] == lista[i + 3]:
            contador = contador + 1 
    return contador



#codigo principal

salida = False
while(salida == False):
    adn = str(input("ingrese una matriz que contenga un ADN \n(separando las filas con coma ',')    :"))
    if isMutant(adn):
        print("El ADN ingresado ES MUTANTE")
    else:
        print("El ADN ingresado NO es MUTANTE")
    print()
    valida = False
    while(valida == False):
        ingreso =input("Si desea ingresar otro ADN Presione (1) \nPara salir presione(2): ")
        print()
        if ingreso == "1":
            salida = False
            valida = True
        elif ingreso == "2":
            salida = True
            valida = True
        else:
            print("ERROR: Ingrese un valor valido(1 o 2)")
            print("-------------------------------------")
            valida = False