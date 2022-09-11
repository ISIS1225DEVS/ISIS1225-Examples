"""
Copyright 2022, Departamento de sistemas y Computación,
Universidad de Los Andes, Bogotá, Colombia.

Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos

Este módulo contiene un menú de ejemplo para el manejo de archivos CSV,
el cual puede ser modificado para adaptarse al problema particular.
el menú tiene las opciones de:

    - Elegir la configuracion del ADT List (ARRAY_LIST o LINKED_LIST)
    - Cargar los elementos a la lista desde un archivo CSV
    - Cargar una clase de pokemon en una pila
    - Imprimir informacion de la lista y la pila
    - Verificar si la pila esta vacia
    - Obtener el tamaño de la pila
    - Obtener el elemento del tope de la pila sin eliminarlo
    - Imprimir los N primeros y ultimos elementos de la pila vaciandola
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
from DISClib.ADT import stack as s
from DISClib.Algorithms.Sorting import quicksort as qus

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
    "pokemon_class_lt",  # lista con la clasificacion de pokemon unicos
    "search_class_s",    # pila de busqueda de pokemon por clase
]

ADT_LIST_CONFIG = [
    "ARRAY_LIST",       # configuracion de la lista como arreglo
    "SINGLE_LINKED",    # configuracion de la lista como lista enlazada simple
]

# lista de llaves relevantes para imprimir
relevant_type_keys = ["classfication"]
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


def cmp_pokemon_class(mon1, mon2):
    """cmp_pokemon_class compara la clase de dos pokemon para agregarlo en una
    lista, sea ARRAY_LIST o LINKED_LIST.

    Args:
        mon1 (dict): primer registro de pokemon a comparar
        mon2 (dict): segundo registro de pokemon a comparar

    Raises:
        Exception: devuelve un error generico en cualquier otro caso

    Returns:
        int: -1 si la comparacion es es menor, 0 si es igual, 1 si es mayor
    """
    # llave de diccionaro para el clasificacion del pokemon
    class_key = "classfication"
    # en caso de que el pokemon1 sea igual al pokemon2
    if (mon1[class_key] == mon2[class_key]):
        # retorna cero 0
        return 0
    # en caso de que el pokemon1 sea mayor al pokemon2
    elif (mon1[class_key] > mon2[class_key]):
        # retorna uno 1
        return 1
    # en caso de que el pokemon1 sea menor al pokemon2
    elif (mon1[class_key] < mon2[class_key]):
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
    pokemon_class_lt = None
    pokemon_class_s = None
    # init del calalog de pokemon
    for k in POKEMON_CTLG_KEYS:
        pokemon_ctlg.update({k: None})

    # creando y configurando el ADT list para almacenar los pokemon
    if struct_cfg == 1:
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList(ADT_LIST_CONFIG[0],
                                cmpfunction=cmp_pokedex_id)
        pokemon_class_lt = lt.newList(ADT_LIST_CONFIG[0],
                                      cmpfunction=cmp_pokemon_class)

    if struct_cfg == 2:
        # config ADT List as ARRAY_LIST
        pokemon_lt = lt.newList(ADT_LIST_CONFIG[1],
                                cmpfunction=cmp_pokedex_id)
        pokemon_class_lt = lt.newList(ADT_LIST_CONFIG[1],
                                      cmpfunction=cmp_pokemon_class)

    # creando y configurando el ADT stack vacio para los pokemon segun su clase
    pokemon_class_s = s.newStack()
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
            add_pokemon_class(pokemon_class_lt, pokemon)
            # ordenando la lista de pokemon por clasificacion
            pokemon_lt = sort_pokemon_lt(pokemon_lt,
                                         qus,
                                         cmp_pokemon_by_class_up)
            # ordenando la lista las clases de pokemon por orden alfabetico
            pokemon_class_lt = sort_pokemon_lt(pokemon_class_lt,
                                               qus,
                                               cmp_pokemon_by_class_up)
        # cerrando el archivo CSV
        pokemon_file.close()
        # agregando los ADTs al diccionario
        # lista general de pokemon
        pokemon_ctlg.update({POKEMON_CTLG_KEYS[0]: pokemon_lt})
        # lista de clasificacion de pokemon unicos
        pokemon_ctlg.update({POKEMON_CTLG_KEYS[1]: pokemon_class_lt})
        # pila de pokemon segun su clasificacion
        pokemon_ctlg.update({POKEMON_CTLG_KEYS[2]: pokemon_class_s})
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


def add_pokemon_class(pokemon_class_lt, pokemon):
    """add_pokemon_class agrega una clase de pokemon a la lista de clasificacion
    de pokemon si este no existe.

    Args:
        pokemon_class_lt (ADT list): lista de clasificacion de pokemon
        pokemon (dict): registro de pokemon a agregar

    Returns:
        ADT list: lista de clases de pokemon con la nueva clasificacion del
        pokemon
    """
    # agregando el clasificacion de pokemon a la lista
    pokemon_class = dict(classfication=pokemon["classfication"])
    if isin_pokemon_classes(pokemon_class_lt, pokemon_class) is False:
        lt.addLast(pokemon_class_lt, pokemon_class)
    return pokemon_class_lt


def isin_pokemon_classes(pokemon_class_lt, pokemon_class):
    """isin_pokemon_classes verifica si la clase de pokemon esta en la
    lista de clasificaciones de pokemon.

    Args:
        pokemon_class_lt (ADT list): lista de clases de pokemon
        pokemon_class (str): clasificacion de pokemon a buscar

    Returns:
        bool: True si la classe de pokemon esta en la lista, False en caso
        contrario
    """
    # buscando la clasificacion de pokemon en la lista
    isin = False
    if lt.isPresent(pokemon_class_lt, pokemon_class) >= 1:
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

def cmp_pokemon_by_class_up(pokemon1, pokemon2):
    """cmp_pokemon_by_class_up compara ascendentemente dos pokemon por su
    clasificacion.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: True si la clase del pokemon1 es alfabericamente menor que el
        del pokemon2
    """
    class_key = "classfication"
    return (pokemon1[class_key] < pokemon2[class_key])


# =============================================================================
# =============== Funciones para manipular el ADT list/Staxk ==================
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


def get_s_info(pokemon_s):
    """get_s_info devuelve la informacion de los pokemon en el ADT stack.

    Args:
        pokemon_s (ADT Stack): pila de pokemones

    Returns:
        list: tamaño del ADT stack, si esta vacio o no y el elemento del
        tope de la pila
    """
    size = s.size(pokemon_s)
    is_empty = s.isEmpty(pokemon_s)
    top = s.top(pokemon_s)
    return (size, is_empty, top)


def get_pokemon_class(pokemon_class_lt, class_index):
    """get_pokemon_class devuelve la clasificacion del pokemon en el
    indice dado.

    Args:
        pokemon_class_lt (ADT List): lista de clases de pokemon
        class_index (int): indice del clasificacion del pokemon

    Returns:
        dict: clasificacion de pokemon
    """
    return lt.getElement(pokemon_class_lt, class_index)


def create_pokemon_s_by_class(pokemon_lt, pokemon_class):
    """create_pokemon_s_by_class crea una pila de pokemones de una
    clasificacion dada.

    Args:
        pokemon_lt (ADT list): lista de pokemon
        pokemon_class (dict): clasificacion de pokemon

    Returns:
        (ADT Stack): pila de pokemones de una dlasificacion dada
    """
    class_key = "classfication"
    pokemon_class_s = s.newStack()
    for pokemon in lt.iterator(pokemon_lt):
        if pokemon.get(class_key) == pokemon_class.get(class_key):
            s.push(pokemon_class_s, pokemon)
    return pokemon_class_s


def push_pokemon(pokemon_s, pokemon):
    """push_pokemon agrega un pokemon a la pila.

    Args:
        pokemon_s (ADT Stack): pila de pokemon
        pokemon (dict): pokemon a agregar

    Returns:
        ADT Stack: pila de pokemon con el nuevo elemento agregado
    """
    s.push(pokemon_s, pokemon)
    return pokemon_s


def pop_pokemon(pokemon_s):
    """pop_pokemon saca un pokemon de la pila.

    Args:
        pokemon_s (ADT Stack): pila de pokemon

    Returns:
        dict: pokemon sacado del tope de la pila
    """
    return s.pop(pokemon_s)


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
    print("\t3. Cargar los datos de las clases de pokemones (stack).")
    print("\t4. Imprimir la información del catalogo de pokemones.")
    print("\t5. apilar un pokemon en el tope de la pila.")
    print("\t6. desapilar un pokemon del tope de la pila.")
    print("\t7. Imprimir los N primeros y ultimos pokemones de la pila.")
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
        # if no hace nada porque stack en DISCLib es DOUBLE_LINKED
        if tk == "search_class_s":
            print("Tamaño de la pila:", s.size(pokemon_ctlg[tk]))
            print("Está vacía?:", s.isEmpty(pokemon_ctlg[tk]))
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
        # if no hace nada porque stack en DISCLib es SINGLE_LINKED
        if tk == "search_type_q":
            size, is_empty, top = get_s_info(pokemon_ctlg[tk])
            print("Está vacía?:", is_empty)
            print("Tamaño de la lista:", size)
            if not is_empty:
                print("Primer elemento en la pila:")
                print_pokemon(top, relevant_pokemon_keys)
            else:
                print("La pila está vacía!!!")

        else:
            size, is_empty = get_lt_info(pokemon_ctlg[tk])
            print("Está vacía?:", is_empty)
            print("Tamaño de la lista:", size)
    print("-----------------------------------------------------\n")


def print_top_stack(pokemon_class_s, relevant_keys):
    """print_top_stack imprime la informacion del elemento tope de la pila.

    Args:
        pokemon_class_s (ADT stack): pila con los pokemones por clase.
        relevant_keys (list): lista de llaves relevantes para imprimir.
    """

    print("++++++ Imprimiendo el tope de la pila...")
    print("-------------------------------------------------------")
    # accediendo al primer elemento de la pila
    peek = s.top(pokemon_class_s)
    # diccionario con la informacion relevante
    relevant_peek = dict()

    # itero sobre las llaves del diccionario
    for key in peek.keys():
        # checkea si la llave es relevante
        if key in relevant_keys:
            relevant_peek.update({key: peek[key]})

    # imprimiendo el primer elemento de la pila con formato
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


def print_nth_stack_pokemon(pokemon_s, relevant_keys, n_th=NTH):
    """print_nth_stack_pokemon imprime cada n_th elementos de la pila.

    Args:
        pokemon_s (ADT stack): pila con los pokemones por clase.
        relevant_keys (list): lista de llaves relevantes para imprimir.
        n_th (int, optional): numero de elementos al principio y final de la
        pila para imprimir. Defaults to NTH.
    """

    print("\n++++++ Imprimiendo los primeros y ultimos",
          str(n_th), "elementos de la pila...")
    # contador de trabajo para imprimir los registros
    i = 0
    # tamaño de la pila
    s_size = s.size(pokemon_s)

    # iterando sobre la pila mientras no este vacia
    while not s.isEmpty(pokemon_s):
        # desencolando el elemento
        data = pop_pokemon(pokemon_s)
        # imprimo los primeros y ultimos n_th elementos
        if (i <= n_th) or (i >= s_size - n_th):
            print("\n-----------------------------------------------------")
            print("indice:", i+1)
            # imprimiendo informacion formateada
            print("data:")
            print_pokemon(data, relevant_keys)
        # incrementando el contador de trabajo
        i = i + 1

    print("Tamano original de la pila:", s_size)
    print("\n++++++ total de elementos desapilados:", i)
    print("La pila está vacía?", s.isEmpty(pokemon_s))
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
    print("================ Ejemplo ADT Stack (Stack/Pila) =================")
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

        # opción 3: cargar los datos de una clase de pokemon en la pila (stack)
        elif opt_usr == 3:
            print("las opciones de clasiificación de pokemon son:")
            # la llave [1] del dict es "pokemon_type_lt"
            pokemon_type_lt = pokemon_ctlg[POKEMON_CTLG_KEYS[1]]
            # imprimir los tipos de pokemon
            print_lt_data(pokemon_type_lt, relevant_type_keys, n_th=1)
            # pedir al usuario el indice de la clase de pokemon
            pokemon_class = input("Ingrese el indice de la clase de pokemon: ")
            # formatear el indice de la clase de pokemon a int
            pokemon_class = int(pokemon_class)
            # extraer la informacion de la clase de pokemon
            pokemon_class = get_pokemon_class(pokemon_type_lt,
                                              pokemon_class)
            # creando la pila de pokemon segun una clase de pokemon
            pokemon_lt = pokemon_ctlg[POKEMON_CTLG_KEYS[0]]
            pokemon_class_s = create_pokemon_s_by_class(pokemon_lt,
                                                        pokemon_class)
            # actualizando el catalogo de pokemon
            pokemon_ctlg[POKEMON_CTLG_KEYS[2]] = pokemon_class_s
            print("Se creo la pila de pokemon con la clase: ", pokemon_class)
            print_top_stack(pokemon_class_s, relevant_pokemon_keys)

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

            # imprimiendo la lista de clases de pokemon
            pokemon_type_lt = pokemon_ctlg[POKEMON_CTLG_KEYS[1]]
            print("\nLeyendo las clases de pokemon...")
            print("Se imprime cada elemento de la lista")
            print_lt_data(pokemon_type_lt,
                          relevant_type_keys,
                          n_th=1)

            # imprimiendo el elemento en el tope de la pila de pokemon
            print("\nLeyendo la pila de tipos de pokemon...")
            pokemon_class_s = pokemon_ctlg[POKEMON_CTLG_KEYS[2]]
            print_top_stack(pokemon_class_s,
                            relevant_pokemon_keys)

        # opción 5: apilar un nuevo pokemon en la pila
        elif opt_usr == 5:
            # pokemon a agregar
            poke_num = input("Ingresa el numero del pokemon: ")
            poke_name = input("Ingresa el nombre del pokemon: ")
            poke_type = input("Ingresa el tipo del pokemon: ")
            poke_class = input("Ingresa la clase del pokemon: ")
            poke_gen = input("Ingresa la generacion del pokemon: ")
            hp = input("Ingresa los HP(Hit Points) del pokemon: ")
            # datos del pokemon a agregar en diccionario
            pokemon_lite = {
                "pokedex_num": poke_num,
                "name": poke_name,
                "type1": poke_type,
                "classfication": poke_class,
                "generation": poke_gen,
                "hp": hp,
            }

            # apilando el pokemon
            print("Apilando el pokemon: ")
            print_pokemon(pokemon_lite, relevant_pokemon_keys)
            pokemon_class_s = pokemon_ctlg[POKEMON_CTLG_KEYS[2]]
            push_pokemon(pokemon_class_s, pokemon_lite)
            new_s_size = s.size(pokemon_class_s)
            print("El nuevo tamaño de la pila es: ", new_s_size)

        # opción 6: desencolar un pokemon al inicio de la pila de pokemones
        elif opt_usr == 6:
            print("Desencolando el primer pokemon de la pila...")
            first = pop_pokemon(pokemon_class_s)
            print_pokemon(first, relevant_pokemon_keys)
            new_s_size = s.size(pokemon_class_s)
            print("El nuevo tamaño de la pila es: ", new_s_size)

        # opción 7: imprimir los N primeros y ultimos pokemones de la pila
        elif opt_usr == 7:
            print("Imprimiendo la pila de los pokemon...")
            print("IMPORTANTE: la pila se vacia al imprimir los elementos!!!")
            nth = input(nth_str)
            nth = int(nth)
            pokemon_class_s = pokemon_ctlg[POKEMON_CTLG_KEYS[2]]
            print_nth_stack_pokemon(pokemon_class_s,
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
