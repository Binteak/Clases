################# ------- DOCUMENTACION ------- ###############
# Nociones Intermedias Python
# by: Alvaro Ruiz Ramirez 
# Shortcuts: Debug -> Ctrl + Shift + D # Ctrl + F5
# Instalación: Node.js
# Ejecutar en terminal: run
# Instalar en extensiones Code Runner Ctrl+Shift+x
# Ejecutar líneas de codigo con Code Runner: Botón derecho -> Run # Ctrl+Alt+n
# Ejecutar líneas de código con Quokka en terminal: ctrl+alt+n para Run Code
################################################

#-------Hello World en Python
print("Hello, World!")

#-------Iteraciones Indices y Rangos: En python se comienza a iterar en 0

#-------Variables y Tipos de Datos: En Python, puedes declarar variables y asignarles valores sin necesidad de especificar su tipo. Python es un lenguaje de tipado dinámico.
# Ejemplo de variables
x = 10
y = "Hola"
z = 3.14

# Tipos de datos
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

#-------Operadores: Python admite una variedad de operadores para realizar operaciones aritméticas, de comparación, lógicas, etc.
# Operadores aritméticos
a = 10
b = 5
print(a + b)  # Suma
print(a - b)  # Resta
print(a * b)  # Multiplicación
print(a / b)  # División

# Operadores de comparación
print(a == b)  # Igualdad
print(a != b)  # Desigualdad
print(a > b)   # Mayor que
print(a < b)   # Menor que

# Operadores lógicos
x = True
y = False
print(x and y)  # AND lógico
print(x or y)   # OR lógico
print(not x)    # NOT lógico

#-------Condicionales (if, elif, else): Los condicionales se utilizan para ejecutar bloques de código basados en ciertas condiciones.
# Ejemplo de condicional simple (if)
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

# Ejemplo de condicional con bloque else (if-else)
edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejemplo de condicional con múltiples condiciones (if-elif-else)
nota = 75
if nota >= 90:
    print("Tienes una A")
elif nota >= 80:
    print("Tienes una B")
elif nota >= 70:
    print("Tienes una C")
elif nota >= 60:
    print("Tienes una D")
else:
    print("Tienes una F")

# Ejemplo de condicionales anidados
edad = 25
ingresos_mensuales = 3000
deudas = 1000

if edad >= 18:
    print("Eres mayor de edad")
    if ingresos_mensuales > 2000:
        print("Tus ingresos mensuales son suficientes")
        if deudas < 200:
            print("Tienes pocas deudas")
            print("Eres elegible para un préstamo")
        else:
            print("Tienes demasiadas deudas para calificar para un préstamo")
    else:
        print("Tus ingresos mensuales son demasiado bajos para calificar para un préstamo")
else:
    print("Eres menor de edad, no puedes solicitar un préstamo")

# Ejemplo de condicionales anidados con múltiples condiciones. Supongamos que queremos determinar el precio de un producto en función de su categoría y la cantidad comprada.
categoria = "electronica"
cantidad = 10

precio_unitario = 0

if categoria == "alimentos":
    if cantidad <= 10:
        precio_unitario = 2
    elif cantidad <= 20:
        precio_unitario = 1.5
    else:
        precio_unitario = 1
elif categoria == "ropa":
    if cantidad <= 5:
        precio_unitario = 10
    elif cantidad <= 10:
        precio_unitario = 8
    else:
        precio_unitario = 5
elif categoria == "electronica":
    if cantidad <= 5:
        precio_unitario = 100
    elif cantidad <= 10:
        precio_unitario = 90
    else:
        precio_unitario = 80
else:
    print("La categoría no es válida")

# Calcular el precio total
precio_total = precio_unitario * cantidad
print("El precio total es:", precio_total)



#-------Bucles (for, while, do-while): Los bucles se utilizan para repetir bloques de código.

# Bucle for: Itera sobre una secuencia (como una lista, tupla, cadena, etc.) o un rango de números.
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Bucle for con enumeración: Itera sobre una secuencia y proporciona tanto el índice como el elemento.
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

# Bucle for con rango: Itera sobre un rango de números.
for i in range(5):
    print(i)

# Bucle while: Ejecuta un bloque de código mientras se cumpla una condición.
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

# Bucle while con break: Ejecuta un bloque de código mientras se cumpla una condición, pero se puede interrumpir con break.
contador = 0
while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break

# Bucle do-while (emulado): Python no tiene un bucle do-while, pero se puede emular utilizando un bucle while con una condición de salida al principio.
contador = 0
while True:
    print(contador)
    contador += 1
    if contador >= 5:
        break

# Bucle for con break: Se puede usar para salir del bucle antes de que se complete su iteración normal.
for i in range(10):
    print(i)
    if i == 5:
        break

# Bucle for con continue: Se puede usar para pasar a la siguiente iteración del bucle sin ejecutar el resto del código en el bloque.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Bucle for con else: El bloque else se ejecuta después de que el bucle haya recorrido todos los elementos de la secuencia o rango.
for i in range(3):
    print(i)
else:
    print("Fin del bucle")

# Bucle while con else: El bloque else se ejecuta después de que la condición del bucle se vuelva falsa.
contador = 0
while contador < 3:
    print(contador)
    contador += 1
else:
    print("Fin del bucle")


# Bucle for para construir una estructura JSON:
import json

# Inicializamos una lista vacía para almacenar datos
datos = []

# Iteramos sobre un rango de números y agregamos elementos a la lista en forma de diccionarios
for i in range(3):
    nombre = input("Ingrese un nombre: ")
    edad = int(input("Ingrese la edad: "))
    ciudad = input("Ingrese la ciudad: ")

    # Creamos un diccionario con los datos ingresados
    persona = {"nombre": nombre, "edad": edad, "ciudad": ciudad}

    # Agregamos el diccionario a la lista de datos
    datos.append(persona)

# Convertimos la lista de datos a formato JSON
json_data = json.dumps(datos, indent=4)

# Imprimimos la estructura JSON
print(json_data)



#-------Funciones: Las funciones son bloques de código reutilizables que se utilizan para realizar tareas específicas.
# Definición de una función
def saludar(nombre):
    """
    Esta función saluda a la persona proporcionada.
    :param nombre: Nombre de la persona.
    """
    print("Hola,", nombre)

# Llamada a la función
saludar("Juan")

# Funciones más usadas:
# - print(): Imprime un mensaje en la consola.
# - len(): Devuelve la longitud de un objeto iterable.
# - range(): Crea una secuencia de números.
# - input(): Solicita una entrada al usuario.
# - str(): Convierte un objeto a una cadena.
# - int(): Convierte un objeto a un entero.
# - float(): Convierte un objeto a un número de punto flotante.
# - list(): Crea una lista a partir de un objeto iterable.
# - dict(): Crea un diccionario.
# - max(): Devuelve el elemento más grande en un iterable.
# - min(): Devuelve el elemento más pequeño en un iterable.
# - sum(): Devuelve la suma de los elementos en un iterable.

#-------Imports y Módulos: Los módulos son archivos de Python que contienen funciones y variables. Puedes importarlos en tu programa para usar su funcionalidad.
# Ejemplo de importación
import math
print(math.sqrt(16))  # Raíz cuadrada

# Importar solo una función específica
from random import randint
print(randint(1, 100))  # Número aleatorio entre 1 y 100



#-------Comprensión de listas y diccionarios: La comprensión de listas y diccionarios es una forma concisa de crear y manipular listas y diccionarios en Python.
# Ejemplo de comprensión de lista
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros]
print(cuadrados)

# Ejemplo de comprensión de diccionario
pares = {x: x ** 2 for x in numeros if x % 2 == 0}
print(pares)

#-------Manejo de archivos: Puedes abrir, leer, escribir y cerrar archivos en Python utilizando las funciones open(), read(), write(), close(), etc.
# Ejemplo de manejo de archivos
with open("archivo.txt", "w") as archivo:
    archivo.write("¡Hola, mundo!")

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)



#-------Imports de librerías
import pandas as pd #Me carga una librería
import re

#-------Creación de Dataframes
df = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Carlos'],
    'Edad': [25, 30, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']
})

#-------Lectura y Escritura de archivos.
#Ejemplo de creación de un archivo Excel:
# Escribimos el DataFrame en un archivo Excel
df.to_excel('datos.xlsx', index=False)
datos_leidos = pd.read_excel('datos.xlsx') # Leemos los datos del archivo Excel
print(datos_leidos) # Imprimimos los datos leídos

#-------Expresiones regulares: Las expresiones regulares son patrones utilizados para buscar y manipular texto en cadenas de caracteres.
# Ejemplo de uso de expresiones regulares
import re
texto = "La lluvia en Sevilla es una maravilla."
patron = r"\bS\w+"
coincidencias = re.findall(patron, texto)
print(coincidencias)



#-------Clases y cómo hacer un import:
# Ejemplo de una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase
persona = Persona("Juan", 30)
persona.saludar()



#-------Decoradores: Los decoradores son funciones que modifican o envuelven otras funciones para agregar funcionalidades adicionales.
# Ejemplo de decorador
def decorador(funcion):
    def wrapper():
        print("Antes de llamar a la función.")
        funcion()
        print("Después de llamar a la función.")
    return wrapper

@decorador
def saludar():
    print("Hola, mundo!")

saludar()


