#EJERCICIO 1
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#EJERCICIO 2
mis_preferidos = ["juegos", "milanesa", "ravioles", "música", "anime"]
penultimo = mis_preferidos[-2]
print("El penúltimo elemento es:", penultimo)

#EJERCICIO 3
palabras = []

palabras.append("dia")
palabras.append("tarde")
palabras.append("noche")

print(palabras)

#EJERCICIO 4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"

animales[3] = "oso"
print(animales)

#EJERCICIO 5
numeros = [1, 2, 3, 4, 5]
numeros.remove(max(numeros))
print(numeros)
#ELIMINA EL ULTIMO NUMERO DE LA LISTA, LUEGO IMPRIME LA LISTA SIN EL ULTIMO NUMERO

#EJERCICIO 6
numeros = list(range(10, 31, 5))

print(numeros[:2])

#EJERCICIO 7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "chevrolet"
autos[2] = "renault"

print(autos)

#EJERCICIO 8
dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

#EJERCICIO 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

compras[1][compras[1].index("fideos")] = "tallarines"

compras[0].remove("pan")

print(compras)

#EJERCICIO 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)