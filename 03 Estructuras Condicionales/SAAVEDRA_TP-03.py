#EJERCICIO 1
edad=int(input("Por favor, ingresa tu edad: "))

if edad > 18:
    print("Es mayor de edad")

#EJERCICIO 2
nota=float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#EJERCICIO 3
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#EJERCICIO 4 
edad=int(input("Por favor, ingresa tu edad: "))


if edad < 12:
    print("Perteneces a la categoría:Niño/a.")
elif edad >= 12 and edad < 18:
    print("Perteneces a la categoría:Adolescente.")
elif edad >= 18 and edad < 30:
    print("Perteneces a la categoría:Adulto/a joven.")
else:
    print("Perteneces a la categoría:Adulto/a.")

#EJERCICIO 5
contrasena = input("Ingrese su contraseña (entre 8 y 14 caracteres): ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#EJERCICIO 6
import random
from statistics import mode, median, mean

numerosAleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numerosAleatorios)
mediana = median(numerosAleatorios)
media = mean(numerosAleatorios)

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

#EJERCICIO 7
cadena = input("Ingrese una frase o palabra: ")

if cadena[-1].lower() in 'aeiouáéíóú':
    cadena += '!'  

print(cadena)

#EJERCICIO 8
nombre = input("Ingrese su nombre: ")

print("Elija una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra mayúscula")
opcion = input("Ingrese 1, 2 o 3 según lo que desee: ")

if opcion == '1':
    print(nombre.upper())  
elif opcion == '2':
    print(nombre.lower())  
elif opcion == '3':
    print(nombre.title())  
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

#EJERCICIO 9
magnitud=float(input("Ingrese la magnitud del terremoto según la escala de Richter: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#EJERCICIO 10
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("Ingresa el número del mes (1 para enero, 12 para diciembre): "))
dia = int(input("Ingresa el día del mes: "))

def estacion_hemisferio_norte(mes, dia):
    if (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (mes < 6) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (mes < 9) or (mes == 9 and dia <= 20):
        return "Verano"
    else:
        return "Otoño"

def estacion_hemisferio_sur(mes, dia):
    if (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (mes < 6) or (mes == 6 and dia <= 20):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (mes < 9) or (mes == 9 and dia <= 20):
        return "Invierno"
    else:
        return "Primavera"

if hemisferio == "N":
    estacion = estacion_hemisferio_norte(mes, dia)
elif hemisferio == "S":
    estacion = estacion_hemisferio_sur(mes, dia)
else:
    estacion = "Hemisferio no válido"

print(f"Estación actual: {estacion}")
