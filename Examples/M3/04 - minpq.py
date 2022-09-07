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
from DISClib.ADT import minpq

#Funcion que se encarga de visualizar que elementos es mayor
#En el caso que k1 sea mayor a k2 debemos retornar 1
#En el caso que k1 sea igual a k2 debemos retornar 0
#Si no es ninguno de los casos anteriores retornamos -1
def cmpfunction(k1, k2):
  if k1 > k2:
    return 1
  if k1 == k2:
    return 0
  else:
    return -1


pq = minpq.newMinPQ(cmpfunction)

#Insertamos elementos en la cola de prioridad
minpq.insert(pq, 2) #pq = [2]
minpq.insert(pq, 1) #pq = [1, 2]
minpq.insert(pq, 4) #pq = [1, 2, 4]
minpq.insert(pq, 3) #pq = [1, 2, 3, 4]

#Retornamos el menor elemento de la lista 
#Se elimina el menor elemento.
minpq.min(pq)     # => 1, no se elimina el minimo
minpq.delMin(pq)  # => 1, se elimina el minimo, pq = [3, 4, 5]

#Se retorna el numero de elementos de la lista
#Indica si la MinPQ esta vacia
minpq.size(pq)    # => 3
minpq.isEmpty(pq) # => False