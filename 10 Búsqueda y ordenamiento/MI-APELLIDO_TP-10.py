# Algoritmos de ordenamiento y búsqueda en Python

# ORDENAMIENTOS

def ordenamiento_burbuja(arr):
    """Ordenamiento burbuja: compara elementos adyacentes y los intercambia si están en el orden incorrecto."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def ordenamiento_insercion(arr):
    """Ordenamiento por inserción: inserta cada elemento en su posición correcta dentro de una lista ordenada."""
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr


def quicksort(arr):
    """Quicksort: divide y conquista, elige un pivote y ordena los elementos menores y mayores a ese pivote."""
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)


def fusionar(izq, der):
    """Fusiona dos listas ordenadas en una sola."""
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# BÚSQUEDAS

def busqueda_lineal(arr, objetivo):
    """Búsqueda lineal: recorre la lista uno por uno hasta encontrar el objetivo."""
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i  # Devuelve la posición
    return -1  # No encontrado

def busqueda_binaria(arr, objetivo):
    """Búsqueda binaria: busca dividiendo a la mitad, requiere lista ordenada."""
    izquierda = 0
    derecha = len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # No encontrado

# EJEMPLO DE USO
if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", datos)
    
    print("Burbuja:", ordenamiento_burbuja(datos.copy()))
    print("Inserción:", ordenamiento_insercion(datos.copy()))
    print("Quicksort:", quicksort(datos.copy()))
   

    ordenada = sorted(datos)  # Para usar búsqueda binaria
    print("\nLista ordenada para búsquedas:", ordenada)

    objetivo = 22
    print(f"Búsqueda lineal de {objetivo}:", busqueda_lineal(ordenada, objetivo))
    print(f"Búsqueda binaria de {objetivo}:", busqueda_binaria(ordenada, objetivo))





# Caso práctico
if __name__ == "__main__":
    print("=== Ordenamiento con Quicksort ===")
    
    # Ingreso simple de datos
    entrada = input("Ingresá números separados por comas: ")
    numeros = [int(x.strip()) for x in entrada.split(",")]

    ordenada = quicksort(numeros)

    print("Lista ordenada:", ordenada)

#Input: 5, 2, 9, 1, 7
#Salida esperada: [1, 2, 5, 7, 9]
Algoritmos de ordenamiento y busqueda.py
4 KB
