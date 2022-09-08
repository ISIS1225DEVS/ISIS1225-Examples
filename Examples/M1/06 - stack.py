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

# lib imports
import config as cf
import csv
import os
import sys


def printMenu():
  print("Seleccione la opción que desea ejecutar con stack:")
  print("1- Cargar Pokemones en la cola (recuerda ejecutar esta opción primero que las anteriores)")
  print("2- Agregar un Pokemon (primera posición, última o en una posición específica")
  print("3- Eliminar un elemento determinado")
  print("4- Obtener el primer elemento de la stack sin eliminarlo")
  print("5- Imprimir primeros n elementos creando una sublista (los elementos son eliminados de la stack)")
  print("6- Imprimir información de la stack")
  print("7- Salir\n")


def load_data():
  print("==========================================================")
  print("============== ADT Estructure (stack)) example =============")
  print("==========================================================\n")
  print("--- Config filepath ---")
  # subfolder name
  pokemon_fn = "Pokemon-utf8-sample.csv"
  # join pokemon file path
  pokemon_path = os.path.join(cf.data_dir,
                          pokemon_fn)
  print("Pokemon filepath:", pokemon_path)        
  # reading pokemon file
  print("+++++++ Reading Pokemon file +++++++")
  # dict reader
  pokemon_list = csv.DictReader(open(pokemon_path,
                                 "r", encoding="utf-8"),
                            delimiter=",")
  poke_lst = stack.newStack('DOUBLE_LINKED')
  for pokemon in pokemon_list:
    stack.push(poke_lst, pokemon)
  return poke_lst


def add_pokemon(poke_lst):
  num = input('Ingresa el numero del pokemon\n')
  name = input('Ingresa el nombre del pokemon\n')
  type = input('Ingresa el tipo del pokemon\n')
  generation = input('Ingresa la generacion del pokemon\n')
  hp = input('Ingresa el hp del pokemon\n')
  pokemon_reducido = {'pokedex_num': num, 'name': name,'type': type, 'generation': generation, 'hp': hp}            
  stack.push(poke_lst,pokemon_reducido)

def remove_pokemon(poke_lst):
  return stack.pop(poke_lst)
  
def get_pokemon(poke_lst):
  return stack.top(poke_lst)

def print_first_n(poke_lst, n):
  for j in range(0,n+1):
    print(stack.pop(poke_lst))

def print_stack_info(poke_lst):
  es_vacio = stack.isEmpty(poke_lst)
  tamanio = stack.size(poke_lst)
  return (es_vacio, tamanio)

if __name__ == "__main__":
    while True:
      printMenu()
      option_user=int(input('Seleccione una opción para continuar\n'))
      if option_user == 1:
        poke_lst = load_data()
      elif option_user == 2:
        add_pokemon(poke_lst, pokemon)
      elif option_user == 3:
        pokemon=remove_pokemon(poke_lst)
        print('El pokemon eliminado fue: \n', pokemon)
      elif option_user == 4:
        pokemon=get_pokemon(poke_lst)
        print('El pokemon que se encuentra en el top de la pila (sin eliminarlo de la stack) fue: \n', pokemon)
      elif option_user == 5:
        n = int(input('Ingrese el número de pokemones que desea imprimir\n'))
        print_first_n(poke_lst,n)
      elif option_user == 6:
        info= print_stack_info(poke_lst)
        print('¿La pila es vacia?: \n',info[0],'\n El tamaño de la pila es: \n', info[1])
      else:
        sys.out()
