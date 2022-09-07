"""
Copyright 2022, Departamento de sistemas y Computación,
Universidad de Los Andes, Bogotá, Colombia.

Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos

Este módulo contiene un menú de ejemplo para el manejo de archivos CSV,
el cual puede ser modificado para adaptarse al problema particular.
el menú tiene las opciones de configurar el buffer de lectura de archivos CSV,
leer un archivo CSV, mostrar los datos en pantalla, eliminar los datos y salir.

Este es un programa de ejemplo para la clase de Estructura de Datos y
Algoritmos en la Universidad de los Andes (Uniandes) en Bogotá Colombia.

Contribuciones de:
    - Luis Florez - implementación inicial
    - Santiago Arteaga - segunda versión y refactorización del código
    - Daniel Alejandro Angel - implementación de ejemplos y pruebas
    - Melissa Castañeda - implementación de ejemplos y pruebas
    - Jesus Pinchao - implementación de ejemplos y pruebas

###############################################################################
# IMPORTANTE: este código de ejemplo no sigue el patron MVC para simplificar
# su manejo y entendimiento. El código debe ser refactorizado para utilizarse
# en los laboratorios y retos de la clase.
###############################################################################
"""
#importaciones de librerias
import config as cf
#importaciones de DISCLib
from DISClib.ADT import stack

#Crear un stack, e ir agregando a la cola valores
cola = stack.newStack()  #Crea un stack con listas enlazadas
stack.size(cola)         # => 0
stack.push(cola, "a")    # cola = ["a"]          
stack.push(cola, "b")    # cola = ["a", "b"]
stack.push(cola, "c")    # cola = ["a", "b", "c"]

#Eliminar los elementos del stack observar como estos van desapareciendo
#uno a uno del ultimo al primero porque el ultimo que sale es el primero 
#que entra.
elem = stack.pop(cola) #elem = "c", cola = ["a", "b"]
elem = stack.pop(cola) #elem = "b", cola = ["a"]
elem = stack.pop(cola) #elem = "a", cola = []

#Agregar al stack los elementos a y b.
#Devuelve una referencia al elemento superior de la pila.
stack.push(cola, "a")    # cola = ["a"]          
stack.push(cola, "b")    # cola = ["a", "b"]
elem  = stack.top(cola)   # elem = "a", cola = ["a", "b"]

# Iterar sobre los elementos de una cola, la cola queda vacia
while not stack.isEmpty(cola):
  n = stack.pop(cola)
  print(n)


