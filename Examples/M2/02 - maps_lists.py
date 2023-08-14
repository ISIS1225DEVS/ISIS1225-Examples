"""
Copyright 2022, Departamento de sistemas y Computación,
Universidad de Los Andes, Bogotá, Colombia.

Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos

Este módulo contiene un menú de que permite al usuario realizar diferentes
funciones con el ADT Sorting como:
    - Elegir la configuracion del ADT Map (CHAINING o PROBING).
    - Cargar todos los pokemon al mapa/índice desde un archivo CSV.
    - Imprimir los detalles del índice de pokemon.
    - imprimir la lista de llaves en el índice de pokemon.
    - imprimir la lista de valores en el índice de pokemon.
    - Agregar un nuevo pokemon al índice.
    - Eliminar un pokemon existente del índice
    - Leer la informacion de un pokemon dentro del índice.
    - Salir del programa.

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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
# import config as cf
# import csv
# import os
# import sys

# from DISClib.ADT import list as lt
# from tabulate import tabulate

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
# ================== Funciones para configurar el ADT Map ====================
# =============================================================================


def cmp_pokedex_id(id_mon1, me_mon2):
    """cmp_pokedex_id compara el numero del pokedex de dos pokemon para
    agregarlo en un mapa/índice, sea CHAINING o PROBING.

    Args:
        id_mon1 (int): id del primer registro del pokemon a comparar
        mon2 (mapentry): registro k:v del segundo pokemon a comparar

    Raises:
        Exception: devuelve un error generico en cualquier otro caso

    Returns:
        int: -1 si la comparacion es es menor, 0 si es igual, 1 si es mayor
    """

    # obtengo el id del pokemon2 del registro k:v
    id_mon2 = me.getKey(me_mon2)
    if (int(id_mon1) == int(id_mon2)):
        # retorna cero 0
        return 0
    # en caso de que el pokemon1 sea mayor al pokemon2
    elif (int(id_mon1) > int(id_mon2)):
        # retorna uno 1
        return 1
    # en caso de que el pokemon1 sea menor al pokemon2
    elif (int(id_mon1) < int(id_mon2)):
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
    """load_data carga los datos de un archivo CSV y los devuelve en un
    índice de diccionarios.

    Args:
        struct_cfg (dict): configuracion del ADT Map
        folder_name (str): nombre del directorio donde se encuentra el archivo
        file_name (str): nombre del archivo CSV a cargar

    Raises:
        Exception: devuelve un error generico en cualquier otro caso

    Returns:
        ADT Map: ADT Map de diccionarios con los datos del archivo CSV
    """
    # creando y configurando el ADT Map para almacenar los pokemon
    if struct_cfg == 1:
        # config ADT Map as CHAINING
        pokemon_mp = mp.newMap(1000,
                               maptype="CHAINING",
                               loadfactor=4.0,
                               cmpfunction=cmp_pokedex_id)

    if struct_cfg == 2:
        # config ADT Map as PROBING
        pokemon_mp = mp.newMap(1000,
                               maptype="PROBING",
                               loadfactor=0.5,
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
            # convirtiendo el numero de pokedex a entero
            pokemon.update({"pokedex_num": int(pokemon["pokedex_num"])})
            # agregando el registro al ADT Map
            pokemon_mp = put_pokemon(pokemon_mp, pokemon)
        # cerrando el archivo CSV
        pokemon_file.close()
        # retornando la índice de pokemon
        return pokemon_mp
    except Exception as e:
        print(e)
        raise Exception


# =============================================================================
# ================== Funciones para manipular el ADT Map =====================
# =============================================================================

def put_pokemon(pokemon_mp, pokemon):
    """put_pokemon agrega un nuevo pokemon al ADT Map.

    Args:
        pokemon_mp (ADT Map): índice de pokemon
        pokemon (dict): registro de pokemon a agregar

    Raises:
        Exception: error generico en cualquier otro caso
    """
    try:
        # agregando el pokemon al índice
        mp.put(pokemon_mp, pokemon["pokedex_num"], pokemon)
        return pokemon_mp
    # error generico
    except Exception as e:
        print("¡Error al agregar el pokemon!")
        raise e


def remove_pokemon(pokemon_mp, poke_key):
    """remove_pokemon borra un pokemon del ADT Map.

    Args:
        pokemon_mp (ADT Map): índice de pokemon
        poke_key (str): llave del pokemon a eliminar

    Raises:
        Exception: error generico en cualquier otro caso
    """
    try:
        # eliminando el pokemon del índice
        mp.remove(pokemon_mp, poke_key)
        return pokemon_mp

    # error generico
    except Exception as e:
        print("¡Error al eliminar el pokemon!")
        raise e


def get_mp_info(pokemon_mp):
    """get_mp_info devuelve la informacion de los pokemon en el ADT Map.

    Args:
        pokemon_mp (ADT Map): índice de pokemon

    Returns:
        list: tamaño del ADT Map y si esta vacio o no
    """
    size = mp.size(pokemon_mp)
    is_empty = mp.isEmpty(pokemon_mp)
    return (size, is_empty)


def get_pokemon(pokemon_mp, poke_key):
    """get_pokemon devuelve la informacion de un pokemon en el ADT Map.

    Args:
        pokemon_mp (ADT Map): índice de pokemon
        poke_key (str): llave del pokemon a buscar

    return:
        poke_entry (mapentry): elemento (pareja llave-valor) con el
        pokemon encontrado

    Raises:
        Exception: error generico en cualquier otro caso
    """

    try:
        # leyendo el pokemon en el índice
        poke_entry = mp.get(pokemon_mp, poke_key)
        return poke_entry
    # error generico
    except Exception as e:
        print("¡Error al leer el pokemon!")
        raise e


# =============================================================================
# ============= Funciones para imprimir informacion del índice  ===============
# =============================================================================

def print_options(struct_cfg):
    """print_options imprime un menu con las opciones disponibles para el
    usuario y permite elegir una opcion de configuracion del ADT Map.

    Args:
        struct_cfg (int): opcion de configuracion del ADT Map

    Returns:
        opt_usr (int): la opcion elegida por el usuario
    """
    # imprimir menu de opciones para el usuario
    print("\n++++++++++++++++++++++ MENU PRINCIPAL +++++++++++++++++++++++++")
    # Configuracion del ADT Map
    print("\n----- Configuración del ADT Map -----")
    # seleccionar ARRAYLIST
    if struct_cfg == 1:
        print("Seleccionó la opción de configuración: CHAINING.\n")
    # seleccionar LINKEDLIST
    elif struct_cfg == 2:
        print("Seleccionó la opción de configuración: PROBING.\n")
    # mostrar opciones para el usuario
    print("-----------------------------------------------------\n")
    print("\t1. Cargar pokemon desde el archivo CSV\n",
          "\t¡¡¡IMPORTANTE: ejecutar esta opción antes de cualquier otra!!!")
    print("\t2. Imprimir la información general del índice de pokemones.")
    print("\t3. Imprimir la información de un pokemon.")
    print("\t4. Agregar un nuevo pokemon al índice.")
    print("\t5. Eliminar un pokemon del índice.")
    print("\t6. Imprimir la lista de llaves del índice de pokemon.")
    print("\t7. Imprimir la lista de valores del índice de pokemon.")
    print("\t8. Cambiar la configuración del ADT Map.")
    print("\t9. Salir.")
    print("\n-----------------------------------------------------")

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    # seleccionar opcion del usuario
    opt_usr = int(input("Seleccione una opción para continuar:"))
    return opt_usr


def print_mp_info(pokemon_mp):
    """print_mp_info imprime la informacion del ADT Map.

    Args:
        pokemon_mp (ADT Map): mapa de pokemon
    """
    size, is_empty = get_mp_info(pokemon_mp)
    print("\n----- Información del ADT Map -----")
    print("Está vacía:", is_empty)
    print("Tipo de ADT Map:", pokemon_mp.get("datastructure"))
    print("Tamaño del mapa:", size)
    print("-----------------------------------------------------\n")


def print_load_data(struct_cfg, poke_folder, pokemon_fn):
    """print_load_data imprime la informacion del archivo CSV cargado
    en el ADT Map.

    Args:
        struct_cfg (int): opcion de configuracion del ADT Map
        poke_folder (str): carpeta donde se encuentra el archivo CSV
        pokemon_fn (str): nombre del archivo CSV

    Returns:
        pokemon_mp (ADT Map): mapa de pokemon
    """

    print("\n----- Información del archivo CSV -----")
    print("Configuración del ADT Map:", struct_cfg)
    print("Carpeta:", poke_folder)
    print("Archivo:", pokemon_fn)
    print("Confgurando buffer para lectura de archivo CSV...")
    cur_limit = config_buffer()
    print("Buffer configurado correctamente.")
    print("tamaño del buffer:", cur_limit)
    print("Cargando archivo CSV...")
    print("Cargando pokemones desde el archivo CSV...")
    pokemon_mp = load_data(struct_cfg, poke_folder, pokemon_fn)
    print("Carga exitosa...")
    print("mapa de tipo:", pokemon_mp.get("datastructure"))
    print("Tamaño de la mapa:", lt.size(pokemon_mp), "pokemones")
    print("-----------------------------------------------------\n")
    return pokemon_mp


def print_pokemon(pokemon_mp, poke_key):
    """print_pokemon imprime la informacion del pokemon seleccionado.

    Args:
        pokemon_mp (ADT Map): lista de pokemon
        poke_key (str): llave del pokemon a buscar
    """
    # obteniendo el elemento llave-valor del pokemon seleccionado
    poke_entry = get_pokemon(pokemon_mp, poke_key)
    # obteniendo la informacion del pokemon
    pokemon = me.getValue(poke_entry)
    # utilizando pretty print para imprimir la informacion del pokemon
    print("\n----- Información del pokemon -----")
    # imprimiendo el tipo de dato de la lista
    print("Pokemon data type:", type(pokemon))
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(pokemon)


def print_pokemon_mp_keys(pokemon_mp, n_th=NTH):
    """print_pokemon_mp_keys imprime cada n_th elementos los datos de
    las llaves de un ADT Map.

    Args:
        pokemon_mp (ADT Map): el ADT Map de los pokemon a imprimir
        n_th (int, optional): la frecuencia de impresion de los datos.
        por defecto es NTH.
    """

    # contador de trabajo para imprimir los registros
    i = 0
    # obteniendo las llaves del índice de pokemon
    pokemon_keys = mp.keySet(pokemon_mp)
    # obteniendo la primera llave del índice de pokemon
    poke_key = lt.firstElement(pokemon_keys)
    # reconociiendo el tipo de dato de la llave
    print("\nLas llaves del índice de Pokemon son de tipo:", type(poke_key))
    print("\n++++++ los registros de la lista de Pokemon son:")
    print("Imprimiendo cada", str(n_th), "elementos de la lista de Pokemon...")

    # iterando sobre las llaves de pokemons en el ADT Map
    for poke_key in lt.iterator(pokemon_keys):
        # calculando el modulo del contador de trabajo
        if i % n_th == 0.0:
            # imprimiendo el registro de la n-esima iteracion
            print("\n-------- Información de la llave del pokemon --------")
            print("iterator:", i+1, "\n",
                  "type:", type(poke_key), "\n",
                  "data:", "\n")
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(poke_key)
        # incrementando el contador de trabajo
        i = i + 1
    print("++++++ total de llaves en el índice:", lt.size(pokemon_keys))


def print_pokemon_mp_values(pokemon_mp, n_th=NTH):
    """print_pokemon_mp_keys imprime cada n_th elementos los valores de
    las llaves de un ADT Map.

    Args:
        pokemon_mp (ADT Map): el ADT Map de los pokemon a imprimir
        n_th (int, optional): la frecuencia de impresion de los datos.
        por defecto es NTH.
    """

    # contador de trabajo para imprimir los registros
    i = 0
    # obteniendo los valores del índice de pokemon
    pokemon_values = mp.valueSet(pokemon_mp)

    # imprimiendo los nombres de las columnas de los valores del índice
    poke_cols = list(lt.firstElement(pokemon_values).keys())
    print("\n++++++ los campos del valor del índice de Pokemon son:")
    for col in poke_cols:
        print("\t - '" + str(col) + "'")
    print("\n++++++ los registros de los valores del índice de Pokemon son:")
    print("Imprimiendo cada", str(n_th), "elementos de la lista de Pokemon...")

    # iterando sobre los valores de pokemons en el ADT list
    for pokemon in lt.iterator(pokemon_values):
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
    print("++++++ total de valores en el índice:", lt.size(pokemon_values))


# =============================================================================
# ===================== variables utiles para el programa =====================
# =============================================================================

cfg_str = "Seleccione el tipo de mapa (1. CHAINING || 2. PROBING): "
option_str = "(1. Inicio || 2. Final || 3. Otra posición): "
freq_str = "Ingrese la frecuencia para imprimir los pokemon del mapa: "
exit_lt_opt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")

# main del ejercicio
if __name__ == "__main__":

    print("===============================================================")
    print("============== Ejemplo ADT Map (CHAINING/PROBING) =============")
    print("===============================================================")

    # opciones de estructura de datos ARRAY_LIST o SINGLE_LINKED
    struct_cfg = int(input(cfg_str))

    # variables de configuracion
    poke_folder = "Samples"
    pokemon_fn = "Pokemon-utf8-sample.csv"
    pokemon_mp = None
    working = True

    # llave con la que se configura el ADT Map
    key_opt = "('pokedex_num'): "

    # ciclo del menu
    while working:

        # imprimir opciones del menu
        opt_usr = print_options(struct_cfg)

        # opciones del menu
        # opción 1: cargar pokemon desde archivo CSV
        if opt_usr == 1:
            pokemon_mp = print_load_data(struct_cfg, poke_folder, pokemon_fn)

        # opción 2: leer la información general del mapa de pokemones
        elif opt_usr == 2:
            print_mp_info(pokemon_mp)

        # opción 3: leer la información de un pokemon
        elif opt_usr == 3:
            # seleccionar la llave del pokemon a leer
            key_str = "Ingrese la llave del pokemon a leer " + key_opt
            poke_key = int(input(key_str))
            print_pokemon(pokemon_mp, poke_key)

        # opción 4: agregar un nuevo pokemon en el mapa
        elif opt_usr == 4:
            # pokemon a agregar
            poke_num = input("Ingresa el numero (llave) del pokemon: ")
            poke_name = input("Ingresa el nombre del pokemon: ")
            poke_type = input("Ingresa el tipo del pokemon: ")
            poke_gen = input("Ingresa la generacion del pokemon: ")
            hp = input("Ingresa los HP(Hit Points) del pokemon: ")
            # datos del pokemon a agregar en diccionario
            pokemon_lite = {
                "pokedex_num": int(poke_num),
                "name": poke_name,
                "type1": poke_type,
                "generation": poke_gen,
                "hp": hp,
            }

            # agregando nuevo pokemon al mapa
            pokemon_mp = put_pokemon(pokemon_mp,
                                     pokemon_lite)

        # opción 5: eliminar un pokemon del mapa
        elif opt_usr == 5:
            # seleccionando la llave del pokemon para eliminar
            delete_str = "Ingrese la llave del pokemon a eliminar " + key_opt
            poke_key = int(input(delete_str))
            pokemon_mp = remove_pokemon(pokemon_mp,
                                        poke_key)

        # opción 6: imprimir las llaves de los pokemon con cierta frecuencia
        elif opt_usr == 6:
            # frecuencia de impresion de las llaves de pokemon
            # formateo a int para evitar errores
            n_th = int(input(freq_str))
            print_pokemon_mp_keys(pokemon_mp, n_th)

        # opción 7: imprimir los pokemones de la mapa por secuencia
        elif opt_usr == 7:
            # frecuencia de impresion de las llaves de pokemon
            # formateo a int para evitar errores
            n_th = int(input(freq_str))
            print_pokemon_mp_values(pokemon_mp, n_th)

        # opción 8: cambiar la configuración del ADT Map
        elif opt_usr == 8:
            # opciones de estructura de datos ARRAY_LIST o SINGLE_LINKED
            print("\n----- Configuración del ADT Map -----")
            struct_cfg = int(input(cfg_str))
            pokemon_mp = None
            print("Configuración del mapa cambiada correctamente.")
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
