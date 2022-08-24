"""
TODO _summary_ of this module/file CSV_FREAD
"""
# lib imports
import config as cf
import csv
import os
import sys

# import ADT list
from DISClib.ADT import list as lt

# imports to meassure time and memory
# from Utils.measuremen.ts import *
# checking config
assert cf

# ===============================================
# ===== util function for ADT list example ======
# ===============================================

# El metodo se encarga de revisar los id's de los pokemons en caso de
# que estos sean iguales devuleve cero pero si el primer pokemon tiene 
# un id mayot al del segundo retorna 1.
# En el caso de que el pokemon 2 tenga un id mayor que el primero retorna -1
def cmp_pokedex_id(mon1, mon2):
    """cmp_pokedex_id compara el numero del pokedex de dos pokemon para
    agregarlo en una lista, sea ARRAY_LIST o LINKED_LIST

    Args:
        mon1 (dict): primer registro de pokemon a comparar
        mon2 (dict): segundo registro de pokemon a comparar

    Raises:
        Exception: devuelve un error generico en cualquier otro caso

    Returns:
        int: -1 si la comparacion es es menor, 0 si es igual, 1 si es mayor
    """
    id_key = "pokedex_num"
    if (mon1[id_key] == mon2[id_key]):
        return 0
    elif (mon1[id_key] > mon2[id_key]):
        return 1
    elif (mon1[id_key] < mon2[id_key]):
        return -1
    else:
        raise Exception

#Se debe elegir si deseamos usar numero uno ArrayList o numero dos LinkedList
#Deben seleccionar la numero 1 para que se ejecute la carga de pokemones
def printMenu(estructure):
    if estructure == 1:
        print("Seleccione la opción que desea ejecutar con ArrayList:")
        print("1- Cargar Pokemones (recuerda ejecutar esta opción primero que las anteriores)")
        print("2- Agregar un Pokemon (primera posición, última o en una posición específica")
        print("3- Eliminar un elemento determinado")
        print("4- Eliminar el primero y ultimo elemento")
        print("5- Imprimir la información básica del List")
        print("6- Obtener un elemento en una posición dada")
        print("7- Imprimir primeros n elementos recorriendo el arreglo")
        print("8- Imprimir primeros n elementos creando una sublista")
        print("9- Imprimir pokemones según la secuencia")
        print("10- Salir\n")

    elif estructure == 2:
        print("Seleccione la opción que desea ejecutar con LinkedList:")
        print("1- Cargar Pokemones (recuerda ejecutar esta opción primero que las anteriores)")
        print("2- Agregar un Pokemon (primera posición, última o en una posición específica")
        print("3- Eliminar un elemento determinado")
        print("4- Eliminar el primero y ultimo elemento")
        print("5- Imprimir la información básica del List")
        print("6- Obtener un elemento en una posición dada")
        print("7- Imprimir primeros n elementos recorriendo el arreglo")
        print("8- Imprimir primeros n elementos creando una sublista")
        print("9- Imprimir pokemones según la secuencia")
        print("10- Salir\n")

    return int(input('Seleccione una opción para continuar\n'))


#Realizacion de la carga de datos.
def load_data(estructure):

    if estructure == 1:
        print("==========================================================")
        print("============== ADT List (ARRAY_LIST) example =============")
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
        pokemons = csv.DictReader(open(pokemon_path,
                                       "r", encoding="utf-8"),
                                  delimiter=",")
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList(datastructure="ARRAY_LIST",
                                cmpfunction=cmp_pokedex_id,)        
        # looping through pokemon file
        for mon in pokemons:
            lt.addLast(pokemon_lt, mon)
    if estructure == 2:
        print("==========================================================")
        print("============== ADT List (LINKED_LIST) example =============")
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
        pokemons = csv.DictReader(open(pokemon_path,
                                       "r", encoding="utf-8"),
                                  delimiter=",")
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList('SINGLE_LINKED')   #Creacion de una lista vacia con listas sencillamente anlazadas
        
        # looping through pokemon file
        for mon in pokemons:
            lt.addLast(pokemon_lt, mon)
    return pokemon_lt

# Agregar el pokemon al incio 1 agregar al final 2 o un ligar en especifico oprimir enter
def add_pokemon(list, pokemon, position, option):

    if option == 1:
        lt.addFirst(list, pokemon)
    elif option == 2:
        lt.addLast(list, pokemon)
    else:
        lt.insertElement(list, pokemon, position)


def remove_pokemon(list, position):
    try:
        lt.deleteElement(list, position)
    except Exception as exp:
        print(" ¡Revisa que la posición del elemento que intentas eliminar si exista!")


def remove_first_last_(list):
    lt.removeFirst(list)
    lt.removeLast(list)


def print_info(lista):
    size = lt.size(lista)
    is_empty = lt.isEmpty(lista)
    return (size, is_empty)


def get_element(list, position):
    return lt.getElement(list, position)


def print_by_iterator(list, N):

    if N > lt.size(list):
        print(
            "Estás intentando imprimir más pokemones de los que hay en la lista, ¡Cuidado!")
    else:
        i = 0
        for pokemon in lt.iterator(list):
            if i < N:
                print(pokemon, '\n')
                i = i+1
            else:
                break

#Sublist si deseamos empezar desde el incio debemos poner como primer parametro el 1.
def print_by_sublist(list, N):

    sublist = lt.subList(list, 1, N)
    for pokemon in lt.iterator(sublist):
        print(pokemon, '\n')


def print_by_sequence(list, N):
    i = 0
    for pokemon in lt.iterator(list):
        if i % N == 0.0:
            # printing each N th row
            print("i:", i,
                  "type:", type(pokemon), "\n"
                  "data:", pokemon)
        i = i + 1


if __name__ == "__main__":
    estructure = int(input('Selecciona la estructura que deseas utilizar\n 1. Arraylist\n 2. LinkedList\n'))
    while True:

        option_user= printMenu(estructure)

        if option_user == 1:
            poke_list = load_data(estructure)
            print('¡La operación se realizó con exito!\n')

        elif option_user == 2:
            num = input('Ingresa el numero del pokemon\n')
            name = input('Ingresa el nombre del pokemon\n')
            type = input('Ingresa el tipo del pokemon\n')
            generation = input('Ingresa la generacion del pokemon\n')
            hp = input('Ingresa el hp del pokemon\n')
            option = int(input('Si deseas ingresarlo al incio de la estructura ingresa 1, al final ingresa 2, de lo contrario oprime enter\n'))
            position = lt.size(poke_list)
            if option != 1 and option != 2:
                print(
                    'Recuerda que la posición debe ser entre 0 y el tamaño de la estructura: ', position)
                position = int(
                    input('ingresa la posicion donde quieres guardar tu pokemon\n'))
            pokemon_reducido = {'pokedex_num': num, 'name': name,
                                'type': type, 'generation': generation, 'hp': hp}
            add_pokemon(poke_list, pokemon_reducido, position, option)
            print('¡La operación se realizó con exito!\n')

        elif option_user == 3:
            position = int(
                input('ingresa la posicion tu pokemon que quieres eliminar\n'))
            remove_pokemon(poke_list, position)
            print('¡La operación se realizó con exito!\n')

        elif option_user == 4:
            remove_first_last_(poke_list)
            print('¡La operación se realizó con exito!\n')

        elif option_user == 5:
            res = print_info(poke_list)
            print('El tamaño del arreglo es: ',
                  res[0], ' y el arreglo es vacio: ', res[1])
            print('¡La operación se realizó con exito!\n')

        elif option_user == 6:
            position = int(input('ingresa la posicion tu pokemon que quieres obtener\n'))
            print(get_element(poke_list, position))
            print('¡La operación se realizó con exito!\n')

        elif option_user == 7:
            num = int(input('Ingrese el numero de pokemones que desea imprimir\n'))
            print_by_iterator(poke_list, num)
            print('¡La operación se realizó con exito!\n')

        elif option_user == 8:
            num = int(input('Ingrese el numero de pokemones que desea imprimir\n'))
            print_by_sublist(poke_list, num)
            print('¡La operación se realizó con exito!\n')

        elif option_user == 9:
            num = int(input('Ingrese el la secuenci con la que desea imprimir\n'))
            print_by_sequence(poke_list, num)
            print('¡La operación se realizó con exito!\n')

        else:
            salir = int(input('¿Quieres cambiar de estructura?\n 1. Si\n 2. No\n')) - 1
            if salir:
                sys.exit(0)
            else:
                os.system('cls||clear')
                estructure = int(input('\n\nSelecciona la estructura que deseas utilizar\n 1. Arraylist\n 2. LinkedList\n'))



    # a = lt.newList('SINGLE_LINKED')   #Creacion de una lista vacia con listas sencillamente anlazadas
    # a = lt.newList('ARRAY_LIST')      #Creacion de una lista vacia con arreglos

    # #Agregar Elementos
    # lt.addFirst(a, 'a')               # a = ["a"]
    # lt.addFirst(a, 'b')               # a = ["b", "a"]
    # lt.addLast(a, 'c')                # a = ["b", "a", "c"]
    # lt.insertElement(a, "z", 2)       # a = ["b", "z", "a", "c"]
    # lt.insertElement(a, "x", 3)       # a = ["b", "z", "x", "a", "c"]
    # lt.size(a)                        # => 5

    # #Consultar
    # elem  = lt.firstElement(a)        # elem = "b"
    # elem  = lt.lastElement(a)         # elem = "c"
    # elem  = lt.getElement(a, 3)       # elem = "x"
    # lt.isEmpty(a)                     # => False

    # #Cambiar un elemento
    # lt.changeInfo(a, 1, "w")          # a =["w", "z", "x", "a", "c"]

    # #Eliminar un elemento
    # lt.removeFirst(a)                 # a = ["z", "x", "a", "c"]
    # lt.removeLast(a)                  # a = ["z", "x", "a"]
    # lt.deleteElement(a, 2)            # a = ["z", "a"]

    # # Recorrer una lista
    # for n in lt.iterator(a):
    #   print(n)

    # =================================
    # # Ejemplos Avanzados
    # #=================================

    # def compararElementos(e1, e2):
    #     if (e1 == e2):
    #         return 0
    #     elif (e1 > e2):
    #         return 1
    #     return -1

    # a = lt.newList('ARRAY_LIST',
    #     cmpfunction=compararElementos) #Creacion de una lista vacia, los elementos se pueden comparar con cmpfunction (para poder usar lt.isPresent)

    # lt.addLast(a, 'a')                # a = ["a"]
    # lt.addLast(a, 'b')                # a = ["a", "b"]
    # lt.addLast(a, 'c')                # a = ["a", "b", "c"]
    # lt.addLast(a, 'd')                # a = ["a", "b", "c", "d"]

    # #Intercambiar dos elementos
    # lt.exchange(a, 2, 4)              # a = ["a", "d", "c", "b"]
    # sublista = lt.subList(a, 2, 3)    # sublista = ["d", "c", "b"]

    # lt.isPresent(a, "z")              # => 0, no esta
    # lt.isPresent(a, "a")              # => 1, esta en la posicion 1
    # lt.isPresent(a, "d")              # => 2, esta en la posicion 2
