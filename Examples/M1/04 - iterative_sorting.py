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
from DISClib.ADT import list as lt

#importaciones de DISCLib
from DISClib.Algorithms.Sorting import insertionsort

# Crear Lista
elementos = [
  {"a": 1, "b": 2},
  {"a": 2, "b": 4},
  {"a": 2, "b": 3},
  {"a": 1, "b": 1}
]
lista = lt.newList()
for n in elementos:
  lt.addLast(lista, n)


#Ordenar descentemente por "a" y ascendentemente por "b"
def compareElem(e1, e2):
  if e1["a"] != e2["a"]:
    return e1["a"] > e2["a"]
  return e1["b"] < e2["b"]


#Ordenar lista
listaOrdenada = insertionsort.sort(lista, compareElem)

#Se iteran los valores en la lista que tiene como nombre
#listaOrdenada.
for n in lt.iterator(listaOrdenada):
  print(n)

