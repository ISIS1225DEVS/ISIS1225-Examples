"""
Copyright 2022, Departamento de sistemas y Computación,
Universidad de Los Andes, Bogotá, Colombia.

Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos

Este módulo contiene un menú de que permite al usuario realizar diferentes
funciones con el ADT List como:
    - Elegir la configuracion del ADT List (ARRAY_LIST o LINKED_LIST)
    - Cargar los elementos a la lista desde un archivo csv
    - Agregar un elemento al inicio, al final o en una posición especifica
    - Eliminar un elemento especifico
    - Eliminar el primero y ultimo elemento de la lista
    - Imprimir la información básica de la lista
    - Leer un pokemon en una posición especifica
    - Imprimir los primeros N elementos recorriendo la lista
    - Imprimir los primeros N elementos creando una sublista
    - Imprimir los elementos de la lista según una secuencia
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
import csv
import gc
import sys
import pprint
import os
import config as cf

# importaciones de modulos DISCLib
from DISClib.ADT import list as lt

# variables globales
# tamaño maximo del buffer de lectura de archivos CSV
SYS_MAX_SIZE_FIELD = sys.maxsize
# tamano recomendado del buffer de lectura de archivos CSV
RECOMENDED_SIZE_FIELD = pow(2, 31) - 1
# frecuencia de impresion de registros
NTH = 200

# chequeando si la configuracion esta activa
assert cf

# =============================================================================
# ================== Funciones para configurar el ADT List ====================
# =============================================================================


def cmp_pokedex_id(mon1, mon2):
    """cmp_pokedex_id compara el numero del pokedex de dos pokemon para
    agregarlo en una lista, sea ARRAY_LIST o LINKED_LIST.

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


# =============================================================================
# =================== Funciones de lectura de archivos CSV ====================
# =============================================================================

def config_buffer(buffer_size=RECOMENDED_SIZE_FIELD):

    """config_buffer configura el tamaño del buffer para la lectura de
    archivos CSV.

    Args:
        buffer_size (int): tamaño del buffer a configurar. Por defecto es
        RECOMENDED_SIZE_FIELD.
    """
    # configurando el buffer de lectura de archivos CSV
    csv.field_size_limit(buffer_size)
    # tomando el nuevo tamaño del buffer
    new_buffer_size = csv.field_size_limit()
    # retornando respuesta al usuario
    return new_buffer_size


def load_data(struct_cfg, folder_name, file_name):
    """load_data carga los datos de un archivo CSV y los devuelve en una
    lista de diccionarios.

    Args:
        struct_cfg (dict): configuracion del ADT List
        folder_name (str): nombre del directorio donde se encuentra el archivo
        file_name (str): nombre del archivo CSV a cargar

    Raises:
        Exception: devuelve un error generico en cualquier otro caso

    Returns:
        ADT list: ADT list de diccionarios con los datos del archivo CSV
    """
    # creando y configurando el ADT list para almacenar los pokemon
    if struct_cfg == 1:
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList("ARRAY_LIST",
                                cmpfunction=cmp_pokedex_id)

    if struct_cfg == 2:
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList("SINGLE_LINKED",
                                cmpfunction=cmp_pokedex_id)

    try:
        # concatenando el nombre del archivo con las carpetas de datos
        pokemon_fpath = os.path.join(cf.data_dir,
                                     folder_name,
                                     file_name)
        print("Archivo ubicado en:", pokemon_fpath)

        # abriendo el archivo CSV
        pokemon_file = open(pokemon_fpath, "r", encoding="utf-8")
        # leyendo el archivo CSV
        pokemon_register = csv.DictReader(pokemon_file, delimiter=",")
        # iterando sobre los registros del archivo CSV
        for pokemon in pokemon_register:
            # agregando el registro al ADT list
            pokemon_lt = add_pokemon(pokemon_lt, pokemon, 1)
        # cerrando el archivo CSV
        pokemon_file.close()
        # retornando la lista de pokemon
        return pokemon_lt
    except Exception as e:
        print(e)
        raise Exception


# =============================================================================
# ================== Funciones para manipular el ADT list =====================
# =============================================================================

def add_pokemon(pokemon_lt, pokemon, option, *args):
    """add_pokemon agrega un nuevo pokemon al ADT list.

    Args:
        pokemon_lt (ADT List): lista de pokemon
        pokemon (dict): registro de pokemon a agregar
        option (int): opcion para agregar el pokemon, 1 para agregar al
        principio, 2 para agregar al final, 3 para agregar en una posición
        positional args (position, optional): argumento opcional para la opcion
        3, posición en donde se agrega el pokemon

    Raises:
        Exception: error generico en cualquier otro caso
    """
    try:
        # opcion 1 para agregar al principio
        if option == 1:
            lt.addFirst(pokemon_lt, pokemon)
        # opcion 2 para agregar al final
        elif option == 2:
            lt.addLast(pokemon_lt, pokemon)
        # opcion 3 para agregar en una posición especifica
        elif option == 3:
            position = int(args[0])
            lt.insertElement(pokemon_lt, pokemon, position)
        # opcion no valida
        else:
            print("Opción no valida")
        return pokemon_lt
    # error generico
    except Exception as e:
        print("¡Error al agregar el pokemon!")
        raise e


def delete_pokemon(pokemon_lt, option, *args):
    """delete_pokemon borra un pokemon del ADT list.

    Args:
        pokemon_lt (ADT List): lista de pokemon
        option (int): opcion para eliminar el pokemon, 1 para eliminar al
        principio, 2 para eliminar al final, 3 para eliminar en una posición
        positional args (position, optional): argumento opcional para la opcion
        3, posición de la que se elimina el pokemon

    Raises:
        Exception: error generico en cualquier otro caso
    """
    try:
        # opcion 1 para eliminar al principio
        if option == 1:
            lt.removeFirst(pokemon_lt)
        # opcion 2 para eliminar al final
        elif option == 2:
            lt.removeLast(pokemon_lt)
        # opcion 3 para eliminar en una posición especifica
        elif option == 3:
            position = int(args[0])
            lt.deleteElement(pokemon_lt, position)
        # opcion no valida
        else:
            print("Opción no valida")
    # error generico
    except Exception as e:
        print("¡Error al eliminar el pokemon!")
        raise e


def get_lt_info(pokemon_lt):
    """print_info devuelve la informacion de los pokemon en el ADT list.

    Args:
        pokemon_lt (ADT List): lista de pokemon

    Returns:
        list: tamaño del ADT list y si esta vacio o no
    """
    size = lt.size(pokemon_lt)
    is_empty = lt.isEmpty(pokemon_lt)
    return (size, is_empty)


def get_pokemon(pokemon_lt, option, *args):
    """get_pokemon devuelve la informacion de un pokemon en el ADT list.

    Args:
        pokemon_lt (ADT List): lista de pokemon
        option (int): opcion para eliminar el pokemon, 1 para eliminar al
        principio, 2 para eliminar al final, 3 para eliminar en una posición
        positional args (position, optional): argumento opcional para la opcion
        3, posición de la que se elimina el pokemon

    Raises:
        Exception: error generico en cualquier otro caso
    """

    try:
        # opcion 1 para leer al principio
        if option == 1:
            return lt.firstElement(pokemon_lt)
        # opcion 2 para leer al final
        elif option == 2:
            return lt.lastElement(pokemon_lt)
        # opcion 3 para leer en una posición especifica
        elif option == 3:
            position = int(args[0])
            return lt.getElement(pokemon_lt, position)
        # opcion no valida
        else:
            print("Opción no valida")
    # error generico
    except Exception as e:
        print("¡Error al leer el pokemon!")
        raise e


# =============================================================================
# ============= Funciones para imprimir informacion de la lista ===============
# =============================================================================

def print_options(struct_cfg):
    """print_options imprime un menu con las opciones disponibles para el
    usuario y permite elegir una opcion de configuracion del ADT list.

    Args:
        struct_cfg (int): opcion de configuracion del ADT list

    Returns:
        opt_usr (int): la opcion elegida por el usuario
    """
    # imprimir menu de opciones para el usuario
    print("\n++++++++++++++++++++++ MENU PRINCIPAL +++++++++++++++++++++++++")
    # Configuracion del ADT list
    print("\n----- Configuración del ADT List -----")
    # seleccionar ARRAYLIST
    if struct_cfg == 1:
        print("Seleccionó la opción de configuración: ARRAY_LIST.\n")
    # seleccionar LINKEDLIST
    elif struct_cfg == 2:
        print("Seleccionó la opción de configuración: LINKED_LIST.\n")
    # mostrar opciones para el usuario
    print("-----------------------------------------------------\n")
    print("\t1. Cargar pokemon desde el archivo CSV\n",
          "\t¡¡¡IMPORTANTE: ejecutar esta opción antes de cualquier otra!!!")
    print("\t2. Imprimir la información general de la lista de pokemones.")
    print("\t3. Imprimir la información de un pokemon.")
    print("\t4. Agregar un nuevo pokemon en la lista",
          "(al inicio, al final, o en otra posición).")
    print("\t5. Eliminar un pokemon de la lista.",
          "(al inicio, al final, o en otra posición).")
    print("\t6. Imprimir los pokemones de la lista.")
    print("\t7. Imprimir los N pokemones de la lista por iterador.")
    print("\t8. Imprimir los N pokemones de la lista por sublista.")
    print("\t9. Cambiar la configuración del ADT list.")
    print("\t10. Salir.")
    print("\n-----------------------------------------------------")

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    # seleccionar opcion del usuario
    opt_usr = int(input("Seleccione una opción para continuar:"))
    return opt_usr


def print_lt_info(pokemon_lt):
    """print_lt_info imprime la informacion del ADT list.

    Args:
        pokemon_lt (ADT List): lista de pokemon
    """
    size, is_empty = get_lt_info(pokemon_lt)
    print("\n----- Información del ADT List -----")
    print("Está vacía:", is_empty)
    print("Tipo de ADT List:", pokemon_lt.get("datastructure"))
    print("Tamaño de la lista:", size)
    print("-----------------------------------------------------\n")


def print_load_data(struct_cfg, poke_folder, pokemon_fn):
    """print_load_data imprime la informacion del archivo CSV cargado
    en el ADT list.

    Args:
        struct_cfg (int): opcion de configuracion del ADT list
        poke_folder (str): carpeta donde se encuentra el archivo CSV
        pokemon_fn (str): nombre del archivo CSV

    Returns:
        pokemon_lt (ADT list): lista de pokemon
    """

    print("\n----- Información del archivo CSV -----")
    print("Configuración del ADT List:", struct_cfg)
    print("Carpeta:", poke_folder)
    print("Archivo:", pokemon_fn)
    print("Confgurando buffer para lectura de archivo CSV...")
    cur_limit = config_buffer()
    print("Buffer configurado correctamente.")
    print("tamaño del buffer:", cur_limit)
    print("Cargando archivo CSV...")
    print("Cargando pokemones desde el archivo CSV...")
    pokemon_lt = load_data(struct_cfg, poke_folder, pokemon_fn)
    print("Carga exitosa...")
    print("Lista de tipo:", pokemon_lt.get("datastructure"))
    print("Tamaño de la lista:", lt.size(pokemon_lt), "pokemones")
    print("-----------------------------------------------------\n")
    return pokemon_lt


def print_pokemon(pokemon_lt, option, *args):
    """print_pokemon imprime la informacion del pokemon seleccionado.

    Args:
        pokemon_lt (ADT list): lista de pokemon
        option (int): opcion para eliminar el pokemon, 1 para eliminar al
        principio, 2 para eliminar al final, 3 para eliminar en una posición
        positional args (position, optional): argumento opcional para la opcion
        3, posición de la que se elimina el pokemon
    """
    # imprimir la ipcion elegida por el usuario
    if option == 1:
        print("Imprimiendo el primer pokemon de la lista...")
    elif option == 2:
        print("Imprimiendo el ultimo pokemon de la lista...")
    elif option == 3:
        print("Imprimiendo pokemon en la posición", args[0], "de la lista...")
    else:
        print("Opcion no valida para imprimir el pokemon")
    # imprimir la informacion del pokemon seleccionado
    pokemon = get_pokemon(pokemon_lt, option, *args)
    # utilizando pretty print para imprimir la informacion del pokemon
    print("\n----- Información del pokemon -----")
    # imprimiendo el tipo de dato de la lista
    print("Pokemon data type:", type(pokemon))
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(pokemon)


def print_pokemon_lt(pokemon_lt, n_th=NTH):
    """print_pokemon_lt imprime cada n_th elementos los datos de un
    ADT list.

    Args:
        pokemon_lt (ADT List): el ADT list de los pokemon a imprimir
        n_th (int, optional): la frecuencia de impresion de los datos.
        por defecto es NTH.
    """

    # contador de trabajo para imprimir los registros
    i = 0
    # imprimiendo los nombres de las columnas del archivo CSV
    poke_cols = list(lt.firstElement(pokemon_lt).keys())
    print("\n++++++ los campos de la lista de Pokemon son:")
    for col in poke_cols:
        print("\t - '" + str(col) + "'")
    print("\n++++++ los registros de la lista de Pokemon son:")
    print("Imprimiendo cada", str(n_th), "elementos de la lista de Pokemon...")

    # iterando sobre los registros de pokemons en el ADT list
    for pokemon in lt.iterator(pokemon_lt):
        # calculando el modulo del contador de trabajo
        if i % n_th == 0.0:
            # imprimiendo el registro de la n-esima iteracion
            print("\n--------------- Información del pokemon ----------------")
            print("iterator:", i+1, "\n",
                  "type:", type(pokemon), "\n",
                  "data:", "\n")
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(pokemon)
        # incrementando el contador de trabajo
        i = i + 1
    print("++++++ total de registros:", lt.size(pokemon_lt))


def print_lt_by_iterator(pokemon_lt, start_idx, end_idx):
    """print_lt_by_iterator imprime los datos de un ADT list por medio de un
    condicional de iteracion entre un rango de indices.

    Args:
        pokemon_lt (ADT list): lista de pokemon
        start_idx (int): indice inicial del rango de iteracion
        end_idx (int): indicie final del rango de iteracion
    """

    print("Imprimiendo los Pokemon desde la posición",
          start_idx, "hasta la posición", end_idx, "...")

    # iterandor de trabajo para el condicional
    i = 1
    # iterando sobre los registros de pokemons en el ADT list
    for pokemon in lt.iterator(pokemon_lt):
        # condicial para imprimir los registros en el rango de indices
        if i >= start_idx and i <= end_idx:
            # imprimiendo el registro dentro del rango
            print("\n--------------- Información del pokemon ----------------")
            print("iterator:", i, "\n",
                  "type:", type(pokemon), "\n",
                  "data:", "\n")
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(pokemon)
        # incrementando el contador de trabajo
        i = i + 1


def print_lt_by_sublist(pokemon_lt, start_idx, num_elems):

    print("Imprimiendo los", num_elems, "pokemons desde la posición",
          start_idx, "...")

    pokemon_sub_lt = lt.subList(pokemon_lt, start_idx, num_elems)
    i = start_idx
    for pokemon in lt.iterator(pokemon_sub_lt):
        print("\n--------------- Información del pokemon ----------------")
        print("iterator:", i, "\n",
              "type:", type(pokemon), "\n",
              "data:", "\n")
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(pokemon)
        i = i + 1


# =============================================================================
# ===================== variables utiles para el programa =====================
# =============================================================================

cfg_str = "Seleccione el tipo de lista (1. ARRAY_LIST || 2. LINKED_LIST): "
option_str = "(1. Inicio || 2. Final || 3. Otra posición): "
freq_str = "Ingrese la frecuencia para imprimir los pokemon de la lista: "
exit_lt_opt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")

# main del ejercicio
if __name__ == "__main__":

    print("===============================================================")
    print("========= Ejemplo ADT List (ARRAY_LIST/SINGLE_LINKED) =========")
    print("===============================================================")

    # opciones de estructura de datos ARRAY_LIST o SINGLE_LINKED
    struct_cfg = int(input(cfg_str))

    # variables de configuracion
    poke_folder = "Samples"
    pokemon_fn = "Pokemon-utf8-sample.csv"
    pokemon_lt = None
    working = True

    # ciclo del menu
    while working:

        # imprimir opciones del menu
        opt_usr = print_options(struct_cfg)

        # opciones del menu
        # opción 1: cargar pokemon desde archivo CSV
        if opt_usr == 1:
            pokemon_lt = print_load_data(struct_cfg, poke_folder, pokemon_fn)

        # opción 2: leer la información general de la lista de pokemones
        elif opt_usr == 2:
            print_lt_info(pokemon_lt)

        # opción 3: leer la información de un pokemon
        elif opt_usr == 3:
            # seleccionar como leer el pokemon
            read_str = "Ingrese como leer al pokemon " + option_str
            io_opt = int(input(read_str))
            # si se selecciona la opcion 1 o 2, se lee el primer o ultimo
            if io_opt in (1, 2):
                print_pokemon(pokemon_lt, io_opt)
            # si se selecciona la opcion 3, se lee el pokemon en la posición
            if io_opt == 3:
                # seleccionando la posición del pokemon a leer
                pos_str = "Ingrese la posición del pokemon a leer: "
                position = int(input(pos_str))
                print_pokemon(pokemon_lt, io_opt, position)

        # opción 4: agregar un nuevo pokemon en la lista
        elif opt_usr == 4:
            # pokemon a agregar
            poke_num = input("Ingresa el numero del pokemon: ")
            poke_name = input("Ingresa el nombre del pokemon: ")
            poke_type = input("Ingresa el tipo del pokemon: ")
            poke_gen = input("Ingresa la generacion del pokemon: ")
            hp = input("Ingresa los HP(Hit Points) del pokemon: ")
            # datos del pokemon a agregar en diccionario
            pokemon_lite = {
                "pokedex_num": poke_num,
                "name": poke_name,
                "type1": poke_type,
                "generation": poke_gen,
                "hp": hp,
                }
            # seleccionar como agregar el pokemon
            read_str = "Ingrese como agregar al pokemon " + option_str
            io_opt = int(input(read_str))
            # si se selecciona la opcion 1 o 2, se agrega el primer o ultimo
            if io_opt in (1, 2):
                pokemon_lt = add_pokemon(pokemon_lt,
                                         pokemon_lite,
                                         io_opt)
            # si se selecciona la opcion 3, se agrega el pokemon en la posición
            if io_opt == 3:
                # seleccionando la posición del pokemon a agregar
                pos_str = "Ingrese la posición del pokemon a agregar: "
                position = int(input(pos_str))
                pokemon_lt = add_pokemon(pokemon_lt,
                                         pokemon_lite,
                                         io_opt,
                                         position)

        # opción 5: eliminar un pokemon de la lista
        elif opt_usr == 5:
            # seleccionar como eliminar el pokemon
            delete_str = "Ingrese como eliminar al pokemon " + option_str
            io_opt = int(input(delete_str))
            # si se selecciona la opcion 1 o 2, se elimina el primer o ultimo
            if io_opt in (1, 2):
                delete_pokemon(pokemon_lt,
                               io_opt)
            # si selecciona la opcion 3, se elimina el pokemon en la posición
            if io_opt == 3:
                # seleccionando la posición del pokemon para eliminar
                pos_str = "Ingrese la posición del pokemon para eliminar: "
                position = int(input(pos_str))
                delete_pokemon(pokemon_lt,
                               io_opt,
                               position)

        # opción 6: imprimir los pokemon de la lista con cierta frecuencia
        elif opt_usr == 6:
            # frecuencia de impresion de los pokemones
            # formateo a int para evitar errores
            n_th = int(input(freq_str))
            print_pokemon_lt(pokemon_lt, n_th)

        # opción 7: imprimir los pokemones de la lista por secuencia
        elif opt_usr == 7:
            start_str = "Ingrese la posición inicial de la secuencia: "
            end_str = "Ingrese la posición final de la secuencia: "
            start_idx = int(input(start_str))
            end_idx = int(input(end_str))
            print("Imprimiendo los pokemones de la lista por secuencia...")
            print_lt_by_iterator(pokemon_lt, start_idx, end_idx)

        # opción 8: imprimir los N pokemones de la lista por sublista
        elif opt_usr == 8:
            start_str = "Ingrese la posición inicial de la secuencia: "
            num_elems_str = "Ingrese el numero de elementos de la sublista: "
            start_idx = int(input(start_str))
            num_elems = int(input(num_elems_str))
            print("Imprimiendo los pokemones de la lista por sublista...")
            print_lt_by_sublist(pokemon_lt, start_idx, num_elems)

        # opción 9: cambiar la configuración del ADT list
        elif opt_usr == 9:
            # opciones de estructura de datos ARRAY_LIST o SINGLE_LINKED
            print("\n----- Configuración del ADT List -----")
            struct_cfg = int(input(cfg_str))
            pokemon_lt = None
            print("Configuración de la lista cambiada correctamente.")
            print("¡¡¡IMPORTANTE: Vuelva a ejecutar la opción 1!!!")
            # limpieza de memoria
            gc.collect()

        # finalizar el programa
        else:
            # confirmar salida del programa
            end_str = "¿desea salir del programa? (s/n): "
            opt_usr = input(end_str)
            # diferentes opciones de salida
            if opt_usr in exit_lt_opt:
                working = False
                print("\nGracias por utilizar el programa.")
        # mensaje de exito de la operacion
        print("¡La operación fue exitosa!\n")
    # fin del programa
    sys.exit(0)
