"""
Copyright 2022, Departamento de sistemas y Computación,
Universidad de Los Andes, Bogotá, Colombia.

Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos

Este módulo contiene un menú de que permite al usuario realizar diferentes
funciones con el ADT Sorting como:
    - Elegir la configuracion del ADT Sortin (Iterative_Sorting o Recursive_LISSorting)
    - Cargar los elementos a la lista desde un archivo csv
    - Ordenar ascendentemente los pokemones por numero 
    - Ordenar acendentemente los pokemones por nombre
    - Ordenar descendentemente los pokemones por numero
    - Ordenar descendentemente los pokemones por nombre   
    - Imprimir los primeros N elementos recorriendo la lista
    - Salir del programa
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

# importaciones de librerias
import config as cf
import csv
import gc
import sys
import os

# importaciones de modulos DISCLib
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as me

from DISClib.Algorithms.Sorting import insertionsort

# variables globales
# tamaño maximo del buffer de lectura de archivos CSV
SYS_MAX_SIZE_FIELD = sys.maxsize
# tamano recomendado del buffer de lectura de archivos CSV
CUR_MAX_SIZE_FIELD = pow(2, 31) - 1
# texto de ayuda para el usuario
WARNING_BUFFER_SIZE = """
Recuerde que el tamaño del buffer debe ser menor o igual al tamaño máximo
del buffer en la configuración del sistema. Y que el tamaño del buffer debe
ser lo suficientemente grande para contener todos los registros del archivo.
"""
# frecuencia de impresion de registros
NTH = 200

# chequeando si la configuracion esta activa
assert cf

#Se compara el id de los pokemones para agregarlos en un lista
def cmp_pokedex_id(mon1, mon2):
    """cmp_pokedex_id compara el numero del pokedex de dos pokemon para
    agregarlo en una lista

    Args:
        mon1 (dict): primer registro de pokemon a comparar
        mon2 (dict): segundo registro de pokemon a comparar

    Raises:
        Exception: devuelve un error generico en cualquier otro caso

    Returns:
        int: -1 si la comparacion es es menor, 0 si es igual, 1 si es mayor
    """
    # llave de diccionaro para el numero de pokedex
    id_key = "pokedex_num"
    # en caso de que el pokemon1 sea igual al pokemon2
    if (mon1[id_key] == mon2[id_key]):
        # retorna cero 0
        return 0
    # en caso de que el pokemon1 sea mayor al pokemon2
    elif (mon1[id_key] > mon2[id_key]):
        # retorna uno 1
        return 1
    # en caso de que el pokemon1 sea menor al pokemon2
    elif (mon1[id_key] < mon2[id_key]):
        # retorna uno -1
        return -1
    else:
        raise Exception

#Funcion sort
def sortFunction(sorted_list, cmpfunction):
    me.sort(sorted_list, cmpfunction)
    return sorted_list

#Comparar por numero
def compareElem(pokemonUno, pokemonDos):
    return (float(pokemonUno['pokedex_num']) < float(pokemonDos['pokedex_num']))

#Comparar por el nombre del pokemon
def comparetitle(pokemon1, pokemon2):
    if(pokemon1['name'] != pokemon2['name']):
        return (pokemon1['name'] < pokemon2['name'])
    else:
        return (pokemon1['pokedex_num']<pokemon2['pokedex_num'])

#Comparar por numero
def compareElemDes(pokemonUno, pokemonDos):
    return (float(pokemonUno['pokedex_num']) > float(pokemonDos['pokedex_num']))

#Comparar por el nombre del pokemon
def comparetitleDes(pokemon1, pokemon2):
    if(pokemon1['name'] != pokemon2['name']):
        return (pokemon1['name'] > pokemon2['name'])
    else:
        return (pokemon1['pokedex_num']>pokemon2['pokedex_num'])



# El menu para elegir el tipo de sort que se desea ejecturar
def printMenu(struct_cfg):
    """printMenu _summary_

    Args:
        struct_cfg (_type_): _description_

    Returns:
        _type_: _description_
    """
    if struct_cfg == 1:
        print("Seleccione la opción que desea ejecutar para iterative_sorting:")

    elif struct_cfg == 2:
        print("Seleccione la opción que desea ejecutar para recursive_sorting:")

    print("1- Cargar Pokemones (Ejecuta esta opción primero que las demás).")
    print("2- Organizar los pokemones por el numero del pokemon ascendente.")
    print("3- Organizar los pokemones por el nombre del pokemon ascendente.")
    print("4- Organizar los pokemones por el numero del pokemon descendente.")
    print("5- Organizar los pokemones por el nombre del pokemon descendente.")
    print("6- Imprimir la información básica de la lista.")
    print("7- Imprimir los primeros N Pokemons recorriendo el arreglo")
    print("8- Salir\n")

    return int(input("Seleccione una opción para continuar\n"))


def load_data(struct_cfg, pokemons_file):
    """load_data _summary_

    Args:
        struct_cfg (_type_): _description_

    Returns:
        _type_: _description_
    """
    print("--- Config filepath ---")
    # join pokemon filepath
    pokemon_path = os.path.join(cf.data_dir,
                                pokemons_file)
    # print pokemon filepath
    print("Pokemon filepath:", pokemon_path)
    # reading pokemon file
    print("+++++++ Reading Pokemon file +++++++")
    # dict reader
    pokemons = csv.DictReader(open(pokemon_path,
                                   "r", encoding="utf-8"),
                              delimiter=",")

    pokemon_lt = lt.newList(datastructure="ARRAY_LIST",
                                cmpfunction=cmp_pokedex_id,)

    # looping through pokemon file
    for mon in pokemons:
        lt.addLast(pokemon_lt, mon)

    # return pokemon ADT list
    return pokemon_lt

def print_by_iterator(pokemon_lt, N):

    if N > lt.size(pokemon_lt):
        print(
            "Estás intentando imprimir más pokemones de los que hay en la lista, ¡Cuidado!")
    else:
        i = 0
        for pokemon in lt.iterator(pokemon_lt):
            if i < N:
                print(pokemon, "\n")
                i = i+1
            else:
                break


def print_info(pokemon_lt):
    """print_info _summary_

    Args:
        pokemon_lt (_type_): _description_

    Returns:
        _type_: _description_
    """
    size = lt.size(pokemon_lt)
    is_empty = lt.isEmpty(pokemon_lt)
    return (size, is_empty)


if __name__ == "__main__":

    print("===============================================================")
    print("=========Ejemplos ADT Sort ====================================")
    print("===============================================================\n")
    
    # opciones de estructura de datos IterativeSorting o RecursiveSorting
    io_cfg = "Selecciona el tipo de ordenamiento (1. IterativeSorting || 2. RecursiveSorting):\n"
    sort_cfg = int(input(io_cfg))
    
    # nombre del archivo de datos
    pokemon_fn = "Pokemon-utf8-sample.csv"
    
    # ciclo de menu
    while True:

        # imprimir menu
        option_user = printMenu(sort_cfg)

        if option_user == 1:
            poledex_lt = load_data(sort_cfg, pokemon_fn)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 2:
            sortFunction(poledex_lt, compareElem)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 3:
            sortFunction(poledex_lt, comparetitle)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 4:
            sortFunction(poledex_lt, compareElemDes)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 5:
            sortFunction(poledex_lt, comparetitleDes)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 6:
            res = print_info(poledex_lt)
            print("El tamaño del arreglo es: ",
                  res[0], " y el arreglo es vacio: ", res[1])
            print("¡La operación se realizó con exito!\n")

        elif option_user ==7:
            poke_num = int(input("Ingrese el numero de pokemones que desea imprimir\n"))
            print_by_iterator(poledex_lt, poke_num)
            print("¡La operación se realizó con exito!\n")

        else:
            salir = int(input("¿Quieres cambiar de estructura?\n 1. Si\n 2. No\n")) - 1
            if salir:
                sys.exit(0)
            else:
                os.system("cls||clear")
                #struct_cfg = int(input("\n\nSelecciona el ordenamiento que deseas utilizar\n 1. Iterative Sorting\n 2. Recursive Sorting\n"))