"""
Copyright 2022, Departamento de sistemas y Computación,
Universidad de Los Andes, Bogotá, Colombia.

Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos

Este módulo contiene un menú de que permite al usuario realizar diferentes
funciones con el ADT Sorting como:
    - Elegir la configuracion del ADT List (ARRAY_LIST o LINKED_LIST)
    - Cargar los elementos a la lista desde un archivo CSV
    - Elegir el algoritmo de ordenamiento (selection_sort, insertion_sort,
        shell_sort, merge_sort, quick_sort)
    - Elegir los criterios de ordenamiento (ascendente o descendente), y
        las propiedades pokedex_num, name, type1, classification y generation
    - ordenar los elementos de la lista
    - Imprimir los N primeros y ultimos elementos recorriendo la lista
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
import pprint
import csv
import gc
import sys
import os

# importaciones de modulos DISCLib
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.Algorithms.Sorting import mergesort as mes
from DISClib.Algorithms.Sorting import quicksort as qus

# importaciones para tomar el tiempo de ejecucion
# from Utils.measurements import delta_time, get_time

# variables globales
# tamaño maximo del buffer de lectura de archivos CSV
SYS_MAX_SIZE_FIELD = sys.maxsize
# tamano recomendado del buffer de lectura de archivos CSV
RECOMENDED_SIZE_FIELD = pow(2, 31) - 1
# numero de elementos para imprimir registros
NTH = 5

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
            pokemon_lt = add_pokemon(pokemon_lt, pokemon)
        # cerrando el archivo CSV
        pokemon_file.close()
        # retornando la lista de pokemon
        return pokemon_lt
    except Exception as e:
        print(e)
        raise Exception


def add_pokemon(pokemon_lt, pokemon):
    """add_pokemon agrega un nuevo pokemon a la lista de pokemon

    Args:
        pokemon_lt (ADT list): lista DISCLib de pokemon
        pokemon (dict): nuevo pokemon a agregar

    Returns:
        ADT list: lista de pokemon con el nuevo pokemon agregado
    """
    lt.addFirst(pokemon_lt, pokemon)
    return pokemon_lt


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
    print("\t3. Seleccionar el algoritmo para ordenar los pokemones.\n",
          "\t(Selection, Insertion, Shell, Merge o Quick)")
    print("\t4. Seleccionar el criterio para ordenar los pokemones\n",
          "\t (Nombre, Tipo, numero del pokedex)", "asendente o descendente.")
    print("\t5. Ordenar la lista de pokemones.")
    print("\t6. Imprimir los N primeros y ultimos pokemones de la lista.")
    print("\t7. Cambiar la configuración del ADT list.")
    print("\t8. Salir.")
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


def print_select_sort(algo_opt):
    print("\n----- Selección del algoritmo de ordenamiento -----")
    print("Algoritmo seleccionado:", algo_opt)
    config = select_sort_algorithm(algo_opt)
    slctd_algo = config[0]
    str_sort = config[1]
    print("Configuración del algoritmo:\n\t", str_sort)
    return slctd_algo


def print_select_cmp(sort_opt, criteria_opt):
    print("\n----- Selección de los criterios de ordenamiento -----")
    print("Orden seleccionado:", sort_opt)
    print("Criterio seleccionado:", criteria_opt)
    config = select_sort_criteria(sort_opt, criteria_opt)
    sort_criterion = config[0]
    str_sort = config[1]
    print("Configuración de la función de comparación:\n\t", str_sort)
    return sort_criterion


def print_pokemon_lt(pokemon_lt, n_th=NTH):
    """print_pokemon_lt imprime los primeros n_th y ultimos n_th elementos
    de la lista de pokemones en el ADT list

    Args:
        pokemon_lt (ADT List): el ADT list de los pokemon a imprimir
        n_th (int, optional): la cantidad de elementos a imprimir al principio
        y al final. Por defecto es NTH
    """

    # contador de trabajo para imprimir los registros
    i = 0
    # imprimiendo los nombres de las columnas del archivo CSV
    poke_cols = list(lt.firstElement(pokemon_lt).keys())
    print("\n++++++ los campos de la lista de Pokemon son:")
    for col in poke_cols:
        print("\t - '" + str(col) + "'")

    print("\n++++++ los primeros", n_th, "pokemones son:")

    # iterando sobre los registros de pokemons en el ADT list
    for pokemon in lt.iterator(pokemon_lt):
        # calculando el modulo del contador de trabajo
        if i < n_th or (i >= lt.size(pokemon_lt) - n_th):
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

# =============================================================================
# ================== Funciones para manipular el ADT list =====================
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


# =============================================================================
# ============= Funciones para organizar los datos del ADT List ===============
# =============================================================================

def select_sort_algorithm(algo_opt):
    """select_sort_algorithm permite seleccionar el algoritmo de ordenamiento
    para la lista de pokemon.

    Args:
        algo_opt (int): opcion de algoritmo de ordenamiento, las opciones son:
            1: Selection Sort
            2: Insertion Sort
            3: Shell Sort
            4: Merge Sort
            5: Quick Sort

    Returns:
        list: slctd_algo (sort) la instancia del ordenamiento y
        algo_ans (str) el texto que describe la configuracion del ordenamiento
    """

    # respuestas por defecto
    slctd_algo = None
    algo_ans = None

    # selecciona el algoritmo de ordenamiento
    # opcion 1: Selection Sort
    if algo_opt == 1:
        slctd_algo = ses
        algo_ans = "Seleccionó la configuración - Selection Sort"

    # opcion 2: Insertion Sort
    elif algo_opt == 2:
        slctd_algo = ins
        algo_ans = "Seleccionó la configuración - Insertion Sort"

    # opcion 3: Shell Sort
    elif algo_opt == 3:
        slctd_algo = shs
        algo_ans = "Seleccionó la configuración - Shell Sort"

    # opcion 4: Merge Sort
    elif algo_opt == 4:
        slctd_algo = mes
        algo_ans = "Seleccionó la configuración - Merge Sort"

    # opcion 5: Quick Sort
    elif algo_opt == 5:
        slctd_algo = qus
        algo_ans = "Seleccionó la configuración - Quick Sort"

    # respuesta final: algoritmo de ordenamiento y texto de configuracion
    return slctd_algo, algo_ans


def select_sort_criteria(sort_opt, criteria_opt):
    """select_sort_criteria selecciona la funcion de comparacion para
    organizar los datos del ADT list.

    Args:
        sort_opt (int): opcion de ordenamiento, las opciones son:
            1: ascendente
            2: descendente
        criteria_opt (int): opcion del para la funcion especifica del criterio
        de comparacio, las opciones son:
            1: por numero de pokemon
            2: por nombre
            3: por tipo
            4: por generarion y clasificacion

    Returns:
        sort_crit: funcion con el criterio de ordenamiento seleccionado
        crit_ans (str) el texto que describe la configuracion del ordenamiento
    """
    sort_crit = None
    crit_ans = None

    # selecciona el orden
    # opcion 1: ascendente
    if sort_opt == 1:
        # selecciona el criterio
        # opcion 1: comparar por numero de pokemon
        if criteria_opt == 1:
            sort_crit = sort_crit_by_number_up
            crit_ans = "Orden ascendente por número del pokemon."
        # opcion 2: comparar por nombre de pokemon
        elif criteria_opt == 2:
            sort_crit = sort_crit_by_name_up
            crit_ans = "Orden ascendente por nombre del pokemon."
        # opcion 3: comparar por tipo de pokemon
        elif criteria_opt == 3:
            sort_crit = sort_crit_by_type_up
            crit_ans = "Orden ascendente por tipo del pokemon."
        # opcion 4: comparar por clasificacion y generacion de pokemon
        elif criteria_opt == 4:
            sort_crit = sort_crit_by_genclass_up
            crit_ans = "Orden ascendente por clase y generación del pokemon."

    # opcion 2: descendente
    elif sort_opt == 2:
        # selecciona el criterio
        # opcion 1: comparar por numero de pokemon
        if criteria_opt == 1:
            sort_crit = sort_crit_by_number_down
            crit_ans = "Orden descendente por número del pokemon."
        # opcion 2: comparar por nombre de pokemon
        elif criteria_opt == 2:
            sort_crit = sort_crit_by_name_down
            crit_ans = "Orden descendente por nombre del pokemon."
        # opcion 3: comparar por tipo de pokemon
        elif criteria_opt == 3:
            sort_crit = sort_crit_by_type_down
            crit_ans = "Orden descendente por tipo del pokemon."
        elif criteria_opt == 4:
            sort_crit = sort_crit_by_genclass_up
            crit_ans = "Orden descendente por clase y generación del pokemon."

    return sort_crit, crit_ans


def sort_pokemon_lt(pokemon_lt, sort_algorithm, sort_crit):
    """sort_pokemon_lt ordena la lista de pokemon segun la funcion de
    comparacion dada y el algoritmo de ordenamiento seleccionado.

    Args:
        pokemon_lt (ADT list): lista de pokemon a ordenar
        sort_algorithm (Algoritm): modulo del algoritmo de ordenamiento
        a utilizar
        sort_crit (function): funcion de comparacion seleccionada

    returns:
        ADT list: lista de pokemon ordenada
    """
    # se ordena la lista de pokemon
    # sort_algorithm es una variable vaga que contiene el modulo del algoritmo
    ans = sort_algorithm.sort(pokemon_lt, sort_crit)
    return ans


# =============================================================================
# =========== Funciones de comparacion para organizar el ADT List =============
# =============================================================================

def sort_crit_by_number_up(pokemon1, pokemon2):
    """sort_crit_by_number_up compara ascendentemente dos pokemon por su
    numero en el pokedex.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: True si el numero de pokedex del pokemon1 es menor que el del
        pokemon2
    """
    ans = (pokemon1["pokedex_num"] < pokemon2["pokedex_num"])
    return ans


def sort_crit_by_name_up(pokemon1, pokemon2):
    """sort_crit_by_name_up compara ascendentemente dos pokemon por su
    nombre.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: True si el nombre del pokemon1 es alfabericamente menor que el
        del pokemon2
    """
    ans = (pokemon1['name'] < pokemon2['name'])
    return ans


def sort_crit_by_type_up(pokemon1, pokemon2):
    """sort_crit_by_type_up compara ascendentemente dos pokemon por su
    tipo.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: True si el tipo del pokemon1 es alfabericamente menor que el
        del pokemon2
    """
    ans = (pokemon1['type1'] < pokemon2['type1'])
    return ans


def sort_crit_by_genclass_up(pokemon1, pokemon2):
    """sort_crit_by_genclass_up compara ascendentemente dos pokemon por
    su generacion y clasificacion.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: True si la generacion del pokemon1 es menor que la del pokemon2.
        si son iguales, compara por clasificacion.
    """
    if pokemon1['generation'] == pokemon2['generation']:
        ans = (pokemon1['classfication'] < pokemon2['classfication'])
        return ans
    else:
        ans = (pokemon1['generation'] < pokemon2['generation'])
        return ans


def sort_crit_by_number_down(pokemon1, pokemon2):
    """sort_crit_by_number_down compara descendentemente dos pokemon por
    su numero en el pokedex.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: True si el numero de pokedex del pokemon1 es mayor que el del
        pokemon2
    """
    ans = (pokemon1["pokedex_num"] > pokemon2["pokedex_num"])
    return ans


def sort_crit_by_name_down(pokemon1, pokemon2):
    """sort_crit_by_name_down compara descendentemente dos pokemon por
    su nombre.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: True si el nombre del pokemon1 es alfabericamente mayor que el
        del pokemon2
    """
    ans = (pokemon1['name'] > pokemon2['name'])
    return ans


def sort_crit_by_type_down(pokemon1, pokemon2):
    """sort_crit_by_type_down compara descendentemente dos pokemon por
    su tipo.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: true si el tipo del pokemon1 es alfabericamente mayor que el
        del pokemon2
    """
    ans = (pokemon1['type1'] > pokemon2['type1'])
    return ans


def sort_crit_by_genclass_down(pokemon1, pokemon2):
    """sort_crit_by_genclass_down compara descendentemente dos pokemon
    por su generacion y clasificacion.

    Args:
        pokemon1 (dict): primer pokemon a comparar
        pokemon2 (dict): segundo pokemon a comparar

    Returns:
        bool: True si la generacion del pokemon1 es mayor que la del pokemon2.
        si son iguales, compara por clasificacion.
    """
    if pokemon1['generation'] == pokemon2['generation']:
        ans = (pokemon1['classfication'] > pokemon2['classfication'])
        return ans
    else:
        ans = (pokemon1['generation'] > pokemon2['generation'])
        return ans


# =============================================================================
# ===================== variables utiles para el programa =====================
# =============================================================================

cfg_str = "Seleccione el tipo de lista (1. ARRAY_LIST || 2. LINKED_LIST): "
option_str = "(1. Inicio || 2. Final || 3. Otra posición): "
algo_str = """Seleccione el algoritmo de ordenamiento
                (1. Selection Sort ||
                 2. Insertion Sort ||
                 3. Shell Sort ||
                 4. Merge Sort ||
                 5. Quick Sort): """
sort_str = """Seleccione el tipo de ordenamiento
            (1. Ascendente || 2. Descendente): """
crit_str = """Seleccione el criterio de comparación
                (1. Numero ||
                 2. Nombre ||
                 3. Tipo ||
                 4. Generación y Clasificación): """

nth_str = "Ingrese los n primeros y últimos elementos a mostrar: "
exit_lt_opt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")

# main del ejercicio
if __name__ == "__main__":

    print("=================================================================")
    print("== Ejemplo Sorting (Selection, Insertion, Shell, Merge, Quick) ==")
    print("=================================================================")

    # opciones de estructura de datos ARRAY_LIST o SINGLE_LINKED
    struct_cfg = int(input(cfg_str))

    # variables de configuracion
    poke_folder = "Samples"
    pokemon_fn = "Pokemon-utf8-sample.csv"
    pokemon_lt = None
    slctd_algo = None
    cmp_func = None
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

        # opción 3: seleccionar el algoritmo de ordenamiento
        elif opt_usr == 3:
            print("\n----- Seleccione el algoritmo de ordenamiento: -----")
            algo_opt = input(algo_str)
            algo_opt = int(algo_opt)
            slctd_algo = print_select_sort(algo_opt)

        # opción 4: seleccionar el criterio de ordenamiento
        elif opt_usr == 4:
            print("\n----- Seleccione los criterios de ordenamiento: -----")
            sort_opt = input(sort_str)
            sort_opt = int(sort_opt)
            criteria_opt = input(crit_str)
            criteria_opt = int(criteria_opt)
            cmp_func = print_select_cmp(sort_opt, criteria_opt)

        # opción 5: ordenar la lista de pokemones
        elif opt_usr == 5:
            print("\n----- Ordenando la lista de pokemones -----")
            pokemon_lt = sort_pokemon_lt(pokemon_lt, slctd_algo, cmp_func)

        # opción 6: imprimir los primeros y ultimos N Pokemons de la lista
        elif opt_usr == 6:
            print("\n---- Imprimiendo los primeros y ultimos N Pokemons ----")
            n_th = int(input(nth_str))
            print_pokemon_lt(pokemon_lt, n_th)

        # opción 7: cambiar la configuración del ADT list
        elif opt_usr == 7:
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
