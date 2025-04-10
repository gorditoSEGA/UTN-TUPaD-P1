#EJERCICIO 1
for i in range(101):
    print(i)

#EJERCICIO 2
numero=input("Por favor, ingresa un número entero: ")

cantidadDigitos=len(numero) if numero[0]!='-' else len(numero) - 1

print(f"El número {numero} tiene {cantidadDigitos} dígitos.")

#EJERCICIO 3
def sumaEntreNumeros(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    
    suma=0
    for i in range(num1+  1, num2):
        suma += i
    
    return suma
try:
    primerNumero=int(input("Ingrese el primer número: "))
    segundoNumero=int(input("Ingrese el segundo número: "))
    
    resultado =sumaEntreNumeros(primerNumero, segundoNumero)
    
    print(f"La suma de los números enteros entre {primerNumero} y {segundoNumero} (excluyendo ambos) es: {resultado}")
except ValueError:
    print("Error: Por favor ingrese números enteros válidos.")

#EJERCICIO 4
total = 0

while True:
    
    numero = int(input("Ingresa un número (0 para detener): "))
    
   
    if numero == 0:
        break
    
    total += numero
print(f"El total acumulado es: {total}")

#EJERCICIO 5
import random
numeroAleatorio=random.randint(0, 9)

intentos=0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    
    intentos += 1
    
    if intento==numeroAleatorio:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Intenta de nuevo.")

#EJERCICIO 6
for i in range(100, -1, -2):
    print(i)

#EJERCICIO 7
numero = int(input("Ingresa un número entero positivo: 4 "))

if numero < 0:
    print("Por favor, ingresa un número positivo.")
else:
    suma = sum(range(numero + 1))
    
    print(f"La suma de los números del 0 a {numero} es: {suma}")

#EJERCICIO 8
pares = 0
impares = 0
positivos = 0
negativos = 0

cantidadNumeros = 100

for _ in range(cantidadNumeros):
    numero = int(input("Ingresa un número entero: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#EJERCICIO 9 
suma=0

cantidadNumeros=100

for _ in range(cantidadNumeros):
    numero = int(input("Ingresa un número entero: "))
    
    suma += numero
media = suma / cantidadNumeros

print(f"La media de los números ingresados es: {media}")

#EJERCICIO 10
numero = input("Ingresa un número: ")


numeroInvertido = numero[::-1]

print(f"El número invertido es: {numeroInvertido}")
