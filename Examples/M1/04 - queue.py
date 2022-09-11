
"""
Copyright 2022, Departamento de sistemas y Computación,
Universidad de Los Andes, Bogotá, Colombia.

Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos

Este módulo contiene un menú de que permite al usuario realizar diferentes
funciones con el ADT Sorting como:
    - Elegir la configuracion del ADT List (ARRAY_LIST o LINKED_LIST)
    - Cargar los elementos a la lista desde un archivo CSV
    - Cargar un tipo de pokemon en una cola
    - Imprimir informacion de la lista y la cola
    - Verificar si la cola esta vacia
    - Obtener el tamaño de la cola
    - Obtener el primer elemento de la cola sin eliminarlo
    - Imprimir los N primeros y ultimos elementos de la cola vaciando
      la cola
    - Cambiar la configuracion del ADT List
    - salir del programa
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
import pprint
import csv
import gc
import sys
import os

# importaciones de modulos DISCLib
from DISClib.ADT import list as lt
from DISClib.ADT import queue as q
from DISClib.Algorithms.Sorting import insertionsort as ins

# importaciones para tomar el tiempo de ejecucion
# from Utils.measurements import delta_time, get_time

# variables globales
# tamaño maximo del buffer de lectura de archivos CSV
SYS_MAX_SIZE_FIELD = sys.maxsize
# tamano recomendado del buffer de lectura de archivos CSV
RECOMENDED_SIZE_FIELD = pow(2, 31) - 1
# numero de elementos para imprimir registros
NTH = 200

# llaves generales para el catálogo de pokemon
POKEMON_CTLG_KEYS = [
    "pokemon_lt",       # lista de pokemon
    "pokemon_type_lt",  # lista con los tipos de pokemon unicos
    "search_type_q",    # cola de busqueda de pokemon por tipo
    ]

ADT_LIST_CONFIG = [
    "ARRAY_LIST",       # configuracion de la lista como arreglo
    "SINGLE_LINKED",    # configuracion de la lista como lista enlazada simple
    ]

# lista de llaves relevantes para imprimir
relevant_type_keys = ["type1"]
relevant_pokemon_keys = [
    "name",
    "pokedex_num",
    "sp_attack",
    "sp_defense",
    "speed",
    "type1",
    "type2",
    "weight_kg",
    "abilities",
    "classfication",
    "defense",
    "generation",
    "height_m",
    "hp",
    "is_legendary",
    "japanese_name",
    ]

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


def cmp_pokemon_type(mon1, mon2):
    """cmp_pokemon_type compara el tipo de dos pokemon para agregarlo en una
    lista, sea ARRAY_LIST o LINKED_LIST.

    Args:
        mon1 (dict): primer registro de pokemon a comparar
        mon2 (dict): segundo registro de pokemon a comparar

    Raises:
        Exception: devuelve un error generico en cualquier otro caso

    Returns:
        int: -1 si la comparacion es es menor, 0 si es igual, 1 si es mayor
    """
    # llave de diccionaro para el tipo de pokemon
    type1_key = "type1"
    # en caso de que el pokemon1 sea igual al pokemon2
    if (mon1[type1_key] == mon2[type1_key]):
        # retorna cero 0
        return 0
    # en caso de que el pokemon1 sea mayor al pokemon2
    elif (mon1[type1_key] > mon2[type1_key]):
        # retorna uno 1
        return 1
    # en caso de que el pokemon1 sea menor al pokemon2
    elif (mon1[type1_key] < mon2[type1_key]):
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
        buffer_size (int): tamaño del buffer a configurar
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
        dict: diccionario de ADTs con los datos del archivo CSV
    """
    # estructura de datos general para el calatogo
    # implementada con con diccionario
    pokemon_ctlg = dict()
    pokemon_lt = None
    pokemon_type_lt = None
    pokemon_type_q = None
    # init del calalog de pokemon
    for k in POKEMON_CTLG_KEYS:
        pokemon_ctlg.update({k: None})

    # creando y configurando el ADT list para almacenar los pokemon
    if struct_cfg == 1:
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList(ADT_LIST_CONFIG[0],
                                cmpfunction=cmp_pokedex_id)
        pokemon_type_lt = lt.newList(ADT_LIST_CONFIG[0],
                                     cmpfunction=cmp_pokemon_type)

    if struct_cfg == 2:
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList(ADT_LIST_CONFIG[1],
                                cmpfunction=cmp_pokedex_id)
        pokemon_type_lt = lt.newList(ADT_LIST_CONFIG[1],
                                     cmpfunction=cmp_pokemon_type)

    # creando y configurando el ADT queue vacio para los pokemon segun su tipo
    pokemon_type_q = q.newQueue()
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
            # lista general de pokemon
            add_pokemon(pokemon_lt, pokemon)
            # lista de los tipos unicos de pokemon
            add_pokemon_type(pokemon_type_lt, pokemon)
            # ordenando la lista de pokemon por tipo
            pokemon_lt = sort_pokemon_lt(pokemon_lt,
                                         ins,
                                         cmp_pokemon_by_type_up)
            # ordenando la lista de tipos de pokemon por orden alfabetico
            pokemon_type_lt = sort_pokemon_lt(pokemon_type_lt,
                                              ins,
                                              cmp_pokemon_by_type_up)
        # cerrando el archivo CSV
        pokemon_file.close()
        # agregando los ADTs al diccionario
        # lista general de pokemon
        pokemon_ctlg.update({POKEMON_CTLG_KEYS[0]: pokemon_lt})
        # lista de tipos de pokemon unicos
        pokemon_ctlg.update({POKEMON_CTLG_KEYS[1]: pokemon_type_lt})
        # cola de pokemon segun su tipo
        pokemon_ctlg.update({POKEMON_CTLG_KEYS[2]: pokemon_type_q})
        # retornando el dict catálogo de pokemones
        return pokemon_ctlg
    except Exception as e:
        print(e)
        raise Exception


def add_pokemon(pokemon_lt, pokemon):
    """add_pokemon agrega un pokemon a la lista de pokemon.

    Args:
        pokemon_lt (ADT list): lista de pokemon
        pokemon (dict): registro de pokemon a agregar

    Returns:
        ADT list: lista de pokemon con el nuevo pokemon agregado
    """
    # agregando el pokemon a la lista
    lt.addLast(pokemon_lt, pokemon)
    return pokemon_lt


def add_pokemon_type(pokemon_type_lt, pokemon):
    """add_pokemon_type agrega un tipo de pokemon a la lista de tipos de
    pokemon si este no existe.

    Args:
        pokemon_type_lt (ADT list): lista de tipos de pokemon
        pokemon (dict): registro de pokemon a agregar

    Returns:
        ADT list: lista de tipos de pokemon con el nuevo tipo de pokemon
    """
    # agregando el tipo de pokemon a la lista
    pokemon_type = dict(type1=pokemon["type1"])
    if isin_pokemon_types(pokemon_type_lt, pokemon_type) is False:
        lt.addLast(pokemon_type_lt, pokemon_type)
    return pokemon_type_lt


def isin_pokemon_types(pokemon_type_lt, pokemon_type):
    """isin_pokemon_types verifica si un tipo de pokemon esta en la lista
    de tipos de pokemon.

    Args:
        pokemon_type_lt (ADT list): lista de tipos de pokemon
        pokemon_type (str): tipo de pokemon a buscar

    Returns:
        bool: True si el tipo de pokemon esta en la lista, False en caso
        contrario
    """
    # buscando el tipo de pokemon en la lista
    isin = False
    if lt.isPresent(pokemon_type_lt, pokemon_type) >= 1:
        isin = True
    # retornando respuesta al usuario
    return isin


# =============================================================================
# ============= Funciones para organizar los datos del ADT List ===============
# =============================================================================

def sort_pokemon_lt(pokemon_lt, sort_algorithm, cmp_function):
    """sort_pokemon_lt ordena la lista de pokemon segun la funcion de
    comparacion dada y el algoritmo de ordenamiento seleccionado.

    Args:
        pokemon_lt (ADT list): lista de pokemon a ordenar
        sort_algorithm (Algoritm): modulo del algoritmo de ordenamiento
        a utilizar
        cmp_function (function): funcion de comparacion seleccionada

    returns:
        ADT list: lista de pokemon ordenada
    """
    # se ordena la lista de pokemon
    # sort_algorithm es una variable vaga que contiene el modulo del algoritmo
    ans = sort_algorithm.sort(pokemon_lt, cmp_function)
    return ans


# =============================================================================
# =========== Funciones de comparacion para organizar el ADT List =============
# =============================================================================

def cmp_pokemon_by_type_up(pokemon1, pokemon2):
    """cmp_pokemon_by_type_up compara ascendentemente dos pokemon por su tipo.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: True si el tipo del pokemon1 es alfabericamente menor que el
        del pokemon2
    """
    return (pokemon1["type1"] < pokemon2["type1"])

# =============================================================================
# =============== Funciones para manipular el ADT list/Queue ==================
# =============================================================================


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


def get_q_info(pokemon_q):
    """print_info devuelve la informacion de los pokemon en el ADT queue.

    Args:
        pokemon_q (ADT Queue): cola de pokemon

    Returns:
        list: tamaño del ADT queue, si esta vacio o no y el primer
        elemento de la cola
    """
    size = q.size(pokemon_q)
    is_empty = q.isEmpty(pokemon_q)
    first = q.peek(pokemon_q)
    return (size, is_empty, first)


def get_pokemon_type(pokemon_type_lt, type_index):
    """get_pokemon_type devuelve el tipo de pokemon en el indice dado.

    Args:
        pokemon_type_lt (ADT List): lista de tipos de pokemon
        type_index (int): indice del tipo de pokemon

    Returns:
        dict: tipo de pokemon
    """
    return lt.getElement(pokemon_type_lt, type_index)


def create_pokemon_q_by_type(pokemon_lt, pokemon_type):
    """create_pokemon_q_by_type crea una cola de pokemon de un tipo dado.

    Args:
        pokemon_lt (ADT list): lista de pokemon
        pokemon_type (dict): tipo de pokemon

    Returns:
        (ADT Queue): cola de pokemon de un tipo dado
    """
    type1_key = "type1"
    pokemon_type_q = q.newQueue()
    for pokemon in lt.iterator(pokemon_lt):
        if pokemon.get(type1_key) == pokemon_type.get(type1_key):
            q.enqueue(pokemon_type_q, pokemon)
    return pokemon_type_q


def dequeue_pokemon(pokemon_q):
    """dequeue_pokemon elimina el primer pokemon de la cola.

    Args:
        pokemon_q (ADT Queue): cola de pokemon

    Returns:
        dict: primer pokemon de la cola
    """
    return q.dequeue(pokemon_q)


def enqueue_pokemon(pokemon_q, pokemon):
    """enqueue_pokemon agrega un pokemon a la cola.

    Args:
        pokemon_q (ADT Queue): cola de pokemon
        pokemon (dict): pokemon a agregar

    Returns:
        ADT Queue: cola de pokemon con el nuevo pokemon
    """
    q.enqueue(pokemon_q, pokemon)
    return pokemon_q


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
          "\t¡¡¡IMPORTANTE: ejecutar esta opción antes que todas!!!")
    print("\t2. Imprimir la información general de la lista de pokemones.")
    print("\t3. Cargar los datos de un tipo de pokemon en una cola (queue).")
    print("\t4. Imprimir la información del catalogo de pokemones.")
    print("\t5. Encolar un pokemon al final de la cola.")
    print("\t6. Desencolar un pokemon al inicio de la cola.")
    print("\t7. Imprimir los N primeros y ultimos pokemones de la cola.")
    print("\t8. Cambiar la configuración del ADT list.")
    print("\t9. Salir.")
    print("\n-----------------------------------------------------")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    # seleccionar opcion del usuario
    opt_usr = int(input("Seleccione una opción para continuar:"))
    return opt_usr


def print_load_data(struct_cfg, poke_folder, pokemon_fn):
    """print_load_data imprime la informacion del archivo CSV cargado
    en el ADT list.

    Args:
        struct_cfg (int): opcion de configuracion del ADT list
        poke_folder (str): carpeta donde se encuentra el archivo CSV
        pokemon_fn (str): nombre del archivo CSV

    Returns:
        pokemon_ctlg (dict): diccionrio donde los valores de las llaves
        son los ADT de pokemon
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
    pokemon_ctlg = load_data(struct_cfg, poke_folder, pokemon_fn)
    print("Carga exitosa...\n")
    print("Catalogo de tipo:", type(pokemon_ctlg))
    print("llaves del catálogo:", list(pokemon_ctlg.keys()))
    print("\n--- Tamaño de las llaves en el catálogo ---")

    # iterando sobre las llaves del catalogo
    for tk in pokemon_ctlg.keys():
        # reconociendo el tipo del ADT en la llave
        t_adt_type = pokemon_ctlg[tk].get("datastructure")
        # imprimiento el tipo de ADT y el tamaño de la llave
        print("Tipo de ADT:", t_adt_type)
        # if no hace nada porque queue en DISCLib es SINGLE_LINKED
        if tk == "search_type_q":
            print("Tamaño de la cola:", q.size(pokemon_ctlg[tk]))
            print("Está vacía?:", q.isEmpty(pokemon_ctlg[tk]))
        else:
            print("Tamaño de la lista:", lt.size(pokemon_ctlg[tk]))
            print("Está vacía?:", lt.isEmpty(pokemon_ctlg[tk]))
    print("-----------------------------------------------------\n")
    return pokemon_ctlg


def print_lt_data(work_lt, relevant_keys, n_th=NTH):
    """print_lt_data imprime cada n_th elementos los datos de un ADT list.

    Args:
        work_lt (ADT List): el ADT list con los elementos a imprimir.
        relevant_keys (list): lista de llaves relevantes para imprimir.
        n_th (in, optional): la frecuencia de impresion de los datos.
        por defecto es NTH.
    """

    # contador de trabajo para imprimir los registros
    i = 0
    # imprimiendo los nombres de las columnas del archivo CSV
    print("\n++++++ los campos relevantes para la lista son:")
    for col in relevant_keys:
        print("\t - '" + str(col) + "'")
    print("\n++++++ los registros de la lista son:")
    print("Imprimiendo cada", str(n_th), "elementos de la lista...")

    # iterando sobre los registros de pokemons en el ADT list
    for data in lt.iterator(work_lt):
        # calculando el modulo del contador de trabajo
        if i % n_th == 0.0:
            # imprimiendo el registro de la n-esima vez
            print("\n---------------------------------------------------")
            print("indice:", i+1)
            # itero sobre las llaves relevantes
            # diccionario de trabajo
            pp_dict = dict()
            for key in data.keys():
                # reviso si la llave es relevante
                if key in relevant_keys:
                    # imprimo la llave y el valor
                    pp_dict.update({key: data[key]})
            # imprimiendo informacion formateada
            pp = pprint.PrettyPrinter(indent=4)
            print("data:")
            pp.pprint(pp_dict)
        # incrementando el contador de trabajo
        i = i + 1
    print("\n++++++ total de registros:", lt.size(work_lt))


def print_ctlg_info(pokemon_ctlg):
    """print_ctlg_info imprime la informacion del catálogo con los ADTs.

    Args:
        pokemon_ctlg (dict): diccionario donde los valores de sus llaves son
        los ADTs de los pokemon
    """

    print("----------------- Información del catálogo -----------------")

    print("Catalogo de tipo:", type(pokemon_ctlg))
    print("llaves del catálogo:", list(pokemon_ctlg.keys()))
    print("\n--- Tamaño de las llaves en el catálogo ---")

    # iterando sobre las llaves del catalogo
    for tk in pokemon_ctlg.keys():
        # reconociendo el tipo del ADT en la llave
        t_adt_type = pokemon_ctlg[tk].get("datastructure")
        # imprimiento el tipo de ADT y el tamaño de la llave
        print("\n----- Información del ADT -----")
        print("Tipo de ADT:", t_adt_type)
        # if no hace nada porque queue en DISCLib es SINGLE_LINKED
        if tk == "search_type_q":
            size, is_empty, first = get_q_info(pokemon_ctlg[tk])
            print("Está vacía?:", is_empty)
            print("Tamaño de la lista:", size)
            if not is_empty:
                print("Primer elemento en la cola:")
                print_pokemon(first, relevant_pokemon_keys)
            else:
                print("La cola está vacía!!!")

        else:
            size, is_empty = get_lt_info(pokemon_ctlg[tk])
            print("Está vacía?:", is_empty)
            print("Tamaño de la lista:", size)
    print("-----------------------------------------------------\n")


def print_peek_queue(pokemon_type_q, relevant_keys):
    """print_peek_queue imprime la informacion del primer elemento de la cola.

    Args:
        pokemon_type_q (ADT queue): cola con los pokemones por tipo.
        relevant_keys (list): lista de llaves relevantes para imprimir.
    """

    print("++++++ Imprimiendo el primer elemento de la cola...")
    print("-------------------------------------------------------")
    # accediendo al primer elemento de la cola
    peek = q.peek(pokemon_type_q)
    # diccionario con la informacion relevante
    relevant_peek = dict()

    # itero sobre las llaves del diccionario
    for key in peek.keys():
        # checkea si la llave es relevante
        if key in relevant_keys:
            relevant_peek.update({key: peek[key]})

    # imprimiendo el primer elemento de la cola con formato
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(relevant_peek)
    print("-----------------------------------------------------\n")


def print_pokemon(pokemon, relevant_keys):
    """print_pokemon imprime la informacion de un pokemon.

    Args:
        pokemon (dict): diccionario con la informacion del pokemon.
        relevant_keys (list): lista de llaves relevantes para imprimir.
    """

    print("-----------------------------------------------------")
    # diccionario con la informacion relevante
    relevant_pokemon = dict()

    # itero sobre las llaves del diccionario
    for key in pokemon.keys():
        # checkea si la llave es relevante
        if key in relevant_keys:
            relevant_pokemon.update({key: pokemon[key]})

    # imprimiendo el elemento con el formato adecuado
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(relevant_pokemon)


def print_nth_queue_pokemon(pokemon_q, relevant_keys, n_th=NTH):
    """print_nth_queue_pokemon imprime cada n_th elementos de la cola.

    Args:
        pokemon_q (ADT queue): cola con los pokemones por tipo.
        relevant_keys (list): lista de llaves relevantes para imprimir.
        n_th (int, optional): numero de elementos al principio y final de la
        cola para imprimir. Defaults to NTH.
    """

    print("\n++++++ Imprimiendo los primeros y ultimos",
          str(n_th), "elementos de la cola...")
    # contador de trabajo para imprimir los registros
    i = 0
    # tamaño de la cola
    q_size = q.size(pokemon_q)

    # iterando sobre la cola mientras no este vacia
    while not q.isEmpty(pokemon_q):
        # desencolando el elemento
        data = dequeue_pokemon(pokemon_q)
        # imprimo los primeros y ultimos n_th elementos
        if (i <= n_th) or (i >= q_size - n_th):
            print("\n-----------------------------------------------------")
            print("indice:", i+1)
            # imprimiendo informacion formateada
            print("data:")
            print_pokemon(data, relevant_keys)
        # incrementando el contador de trabajo
        i = i + 1

    print("Tamano original de la cola:", q_size)
    print("\n++++++ total de elementos desencolados:", i)
    print("La cola está vacía?", q.isEmpty(pokemon_q))
    print("-----------------------------------------------------\n")


# =============================================================================
# ===================== variables utiles para el programa =====================
# =============================================================================

cfg_str = "Seleccione el tipo de lista (1. ARRAY_LIST || 2. LINKED_LIST): "
nth_str = "Ingrese los n primeros y últimos elementos a mostrar: "
exit_lt_opt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")

# main del ejercicio
if __name__ == "__main__":

    print("=================================================================")
    print("================ Ejemplo ADT Queue (Queue/Cola) =================")
    print("=================================================================")

    # opciones de estructura de datos ARRAY_LIST o SINGLE_LINKED
    struct_cfg = int(input(cfg_str))

    # variables de configuracion
    poke_folder = "Samples"
    pokemon_fn = "Pokemon-utf8-sample.csv"
    working = True

    # catalogo con la informacion de los pokemon
    pokemon_ctlg = None

    # ciclo del menu
    while working:

        # imprimir opciones del menu
        opt_usr = print_options(struct_cfg)

        # opciones del menu
        # opción 1: cargar pokemon desde archivo CSV
        if opt_usr == 1:
            pokemon_ctlg = print_load_data(struct_cfg, poke_folder, pokemon_fn)

        # opción 2: leer la información general del catalogo de pokemones
        elif opt_usr == 2:
            print_ctlg_info(pokemon_ctlg)

        # opción 3: cargar los datos de un tipo de pokemon en una cola (queue)
        elif opt_usr == 3:
            print("las opciones de tipo de pokemon son:")
            # la llave [1] del dict es "pokemon_type_lt"
            pokemon_type_lt = pokemon_ctlg[POKEMON_CTLG_KEYS[1]]
            # imprimir los tipos de pokemon
            print_lt_data(pokemon_type_lt, relevant_type_keys, n_th=1)
            # pedir al usuario el indice del tipo de pokemon
            pokemon_type = input("Ingrese el indice del tipo de pokemon: ")
            # formatear el indice del tipo de pokemon a int
            pokemon_type = int(pokemon_type)
            # extraer la informacion del tipo de pokemon
            pokemon_type = get_pokemon_type(pokemon_type_lt, pokemon_type)
            # creando la cola de pokemon segun un tipo de pokemon
            pokemon_lt = pokemon_ctlg[POKEMON_CTLG_KEYS[0]]
            pokemon_type_q = create_pokemon_q_by_type(pokemon_lt, pokemon_type)
            # actualizando el catalogo de pokemon
            pokemon_ctlg[POKEMON_CTLG_KEYS[2]] = pokemon_type_q
            print("Se creo la cola de pokemon con el tipo: ", pokemon_type)
            print_peek_queue(pokemon_type_q, relevant_pokemon_keys)

        # opción 4: imprimir los detalles del catalogo de pokemones
        elif opt_usr == 4:
            # imprimiendo detalles del catalogo de pokemon
            print("++++++ Imprimiento detalles del catalogo de pokemones...")
            print("\nLeyendo la lista de pokemon...")
            # imprimiendo la lista total de pokemon
            polemon_lt = pokemon_ctlg[POKEMON_CTLG_KEYS[0]]
            print("se imprime cada", NTH, "elementos de la lista")
            print_lt_data(pokemon_lt,
                          relevant_pokemon_keys,
                          n_th=NTH)

            # imprimiendo la lista de tipos de pokemon
            pokemon_type_lt = pokemon_ctlg[POKEMON_CTLG_KEYS[1]]
            print("\nLeyendo los tipos de pokemon...")
            print("Se imprime cada elemento de la lista")
            print_lt_data(pokemon_type_lt,
                          relevant_type_keys,
                          n_th=1)

            # imprimiendo el primer elemento de la cola de pokemon
            print("\nLeyendo la cola de tipos de pokemon...")
            pokemon_type_q = pokemon_ctlg[POKEMON_CTLG_KEYS[2]]
            print_peek_queue(pokemon_type_q,
                             relevant_pokemon_keys)

        # opción 5: encolar un pokemon al final de la cola de pokemones
        elif opt_usr == 5:
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

            # encolando el pokemon
            print("Encolando el pokemon: ")
            print_pokemon(pokemon_lite, relevant_pokemon_keys)
            pokemon_type_q = pokemon_ctlg[POKEMON_CTLG_KEYS[2]]
            enqueue_pokemon(pokemon_type_q, pokemon_lite)
            new_q_size = q.size(pokemon_type_q)
            print("El nuevo tamaño de la cola es: ", new_q_size)

        # opción 6: desencolar un pokemon al inicio de la cola de pokemones
        elif opt_usr == 6:
            print("Desencolando el primer pokemon de la cola...")
            first = dequeue_pokemon(pokemon_type_q)
            print_pokemon(first, relevant_pokemon_keys)
            new_q_size = q.size(pokemon_type_q)
            print("El nuevo tamaño de la cola es: ", new_q_size)

        # opción 7: imprimir los N primeros y ultimos pokemones de la cola
        elif opt_usr == 7:
            # TODO implementar la funcion print_nth_queue_pokemon()
            print("Imprimiendo la cola de los pokemon...")
            print("IMPORTANTE: la cola se vacia al imprimir los elementos!!!")
            nth = input(nth_str)
            nth = int(nth)
            pokemon_type_q = pokemon_ctlg[POKEMON_CTLG_KEYS[2]]
            print_nth_queue_pokemon(pokemon_type_q,
                                    relevant_pokemon_keys,
                                    n_th=nth)

        # opción 8: cambiar la configuración del ADT list
        elif opt_usr == 8:
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
