"""
TODO _summary_ of this module/file ADT List
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


def printMenu(struct_cfg):
    """printMenu _summary_

    Args:
        struct_cfg (_type_): _description_

    Returns:
        _type_: _description_
    """
    if struct_cfg == 1:
        print("Seleccione la opción que desea ejecutar para ARRAY_LIST:")

    elif struct_cfg == 2:
        print("Seleccione la opción que desea ejecutar para LINKED_LIST:")

    print("1- Cargar Pokemones (Ejecuta esta opción primero que las demás).")
    print("2- Agregar un Pokemon (al inicio, al final, o en una posición).")
    print("3- Eliminar un Pokemon especifico.")
    print("4- Eliminar el primero y ultimo Pokemon.")
    print("5- Imprimir la información básica de la lista.")
    print("6- Leer un Pokemon en una posición especifica.")
    print("7- Imprimir los primeros N Pokemons recorriendo el arreglo")
    print("8- Imprimir los primeros N Pokemons creando una sublista")
    print("9- Imprimir los Pokemons según la secuencia")
    print("10- Salir\n")

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

    if struct_cfg == 1:
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList(datastructure="ARRAY_LIST",
                                cmpfunction=cmp_pokedex_id,)

    if struct_cfg == 2:
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList("SINGLE_LINKED",
                                cmpfunction=cmp_pokedex_id,)

    # looping through pokemon file
    for mon in pokemons:
        lt.addLast(pokemon_lt, mon)

    # return pokemon ADT list
    return pokemon_lt


def add_pokemon(pokemon_lt, pokemon, position, option):
    """add_pokemon _summary_

    Args:
        pokemon_lt (_type_): _description_
        pokemon (_type_): _description_
        position (_type_): _description_
        option (_type_): _description_
    """

    if option == 1:
        # adding pokemon to the beginning of the list
        lt.addFirst(pokemon_lt, pokemon)
    elif option == 2:
        # adding pokemon to the end of the list
        lt.addLast(pokemon_lt, pokemon)
    else:
        # adding pokemon to the position of the list
        lt.insertElement(pokemon_lt, pokemon, position)


def remove_pokemon(pokemon_lt, position):
    try:
        lt.deleteElement(pokemon_lt, position)
    except Exception as exp:
        print(" ¡Revisa que la posición del elemento que intentas eliminar si exista!")


def remove_first_last_pokemon(pokemon_lt):
    """remove_first_last_pokemon _summary_

    Args:
        pokemon_lt (_type_): _description_
    """
    lt.removeFirst(pokemon_lt)
    lt.removeLast(pokemon_lt)


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


def get_element(pokemon_lt, position):
    """get_element _summary_

    Args:
        pokemon_lt (_type_): _description_
        position (_type_): _description_

    Returns:
        _type_: _description_
    """
    return lt.getElement(pokemon_lt, position)


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


def print_by_sublist(pokemon_lt, N):

    sublist = lt.subList(pokemon_lt, 1, N)
    for pokemon in lt.iterator(sublist):
        print(pokemon, "\n")


def print_by_sequence(pokemon_lt, N):
    i = 0
    for pokemon in lt.iterator(pokemon_lt):
        if i % N == 0.0:
            # printing each N th row
            print("i:", i,
                  "type:", type(pokemon), "\n"
                  "data:", pokemon)
        i = i + 1


if __name__ == "__main__":

    print("===============================================================")
    print("========= Ejemplo ADT List (ARRAY_LIST/SINGLE_LINKED) =========")
    print("===============================================================\n")
    
    # opciones de estructura de datos ARRAY_LIST o SINGLE_LINKED
    io_cfg = "Selecciona el tipo de lista (1. ArrayList || 2. LinkedList):\n"
    struct_cfg = int(input(io_cfg))
    
    # nombre del archivo de datos
    pokemon_fn = "Pokemon-utf8-sample.csv"
    
    # ciclo de menu
    while True:

        # imprimir menu
        option_user = printMenu(struct_cfg)

        if option_user == 1:
            poledex_lt = load_data(struct_cfg, pokemon_fn)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 2:
            poke_num = input("Ingresa el numero del pokemon\n")
            poke_name = input("Ingresa el nombre del pokemon\n")
            poke_type = input("Ingresa el tipo del pokemon\n")
            poke_gen = input("Ingresa la generacion del pokemon\n")
            hp = input("Ingresa el hp del pokemon\n")
            option = int(input("Si deseas ingresarlo al incio de la estructura ingresa 1, al final ingresa 2, de lo contrario oprime enter\n"))
            position = lt.size(poledex_lt)
            if option != 1 and option != 2:
                print(
                    "Recuerda que la posición debe ser entre 0 y el tamaño de la estructura: ", position)
                position = int(
                    input("ingresa la posicion donde quieres guardar tu pokemon\n"))

            pokemon_lite = {
                "pokedex_num": poke_num,
                "name": poke_name,
                "type": poke_type,
                "generation": poke_gen,
                "hp": hp}
            
            add_pokemon(poledex_lt, pokemon_lite, position, option)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 3:
            position = int(
                input("ingresa la posicion del pokemon que quieres eliminar\n"))
            remove_pokemon(poledex_lt, position)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 4:
            remove_first_last_pokemon(poledex_lt)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 5:
            res = print_info(poledex_lt)
            print("El tamaño del arreglo es: ",
                  res[0], " y el arreglo es vacio: ", res[1])
            print("¡La operación se realizó con exito!\n")

        elif option_user == 6:
            position = int(input("ingresa la posicion tu pokemon que quieres obtener\n"))
            print(get_element(poledex_lt, position))
            print("¡La operación se realizó con exito!\n")

        elif option_user == 7:
            poke_num = int(input("Ingrese el numero de pokemones que desea imprimir\n"))
            print_by_iterator(poledex_lt, poke_num)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 8:
            poke_num = int(input("Ingrese el numero de pokemones que desea imprimir\n"))
            print_by_sublist(poledex_lt, poke_num)
            print("¡La operación se realizó con exito!\n")

        elif option_user == 9:
            poke_num = int(input("Ingrese el la secuenci con la que desea imprimir\n"))
            print_by_sequence(poledex_lt, poke_num)
            print("¡La operación se realizó con exito!\n")

        else:
            salir = int(input("¿Quieres cambiar de estructura?\n 1. Si\n 2. No\n")) - 1
            if salir:
                sys.exit(0)
            else:
                os.system("cls||clear")
                struct_cfg = int(input("\n\nSelecciona la estructura que deseas utilizar\n 1. Arraylist\n 2. LinkedList\n"))

