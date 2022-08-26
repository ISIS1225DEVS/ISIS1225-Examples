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

# importaciones de librerias
import csv
import gc
import sys
import config as cf
import os

<<<<<<< HEAD
#load pokemon file, reading, looping through the fie
def load_data(N):

        print("\n--- Joining filepath ---")
        # subfolder name
        pokemon_fn = "Pokemon-utf8-sample.csv"
        # join pokemon file path
        pokemon_path = os.path.join(cf.data_dir,
                                pokemon_fn)
        print("Pokemon filepath:", pokemon_path)    
        # reading pokemon file
        print("+++++++ Reading Pokemon file with csv.DictReader +++++++")
        pokemon_file = open(pokemon_path, "r", encoding="utf-8")
        # reader
        pokemons = csv.reader(pokemon_file, delimiter=",")
        # row counter
        i = 0
        pocket_cols = list()
        pokemon_list_values = list()

        # looping through pokemon file
        for mon in pokemons:
            if i == 0:
                # getting pokemon columns
                pocket_cols = mon
            elif i != 0:
                if i%N == 0:
                    pokemon_list_values.append(mon)
            i = i + 1

        # pokemon file details
        print("\n--- Pokemon csv details ---")
        print("Pokemon file size:", i)
        print("Pokemon columns:\n", pocket_cols)
        print("////////////////////////////////////////////////////////////////////////////////////////")
        print("////////////////////////////////////////////////////////////////////////////////////////")

        # close pokemon file
        pokemon_file.close()
        return (pocket_cols,pokemon_list_values)

def print_results(titulos, valores, N):
    i=0
    list_result = list()
    for x in range(0,N):
        pokemon = "" 
        for z in range(0, len(titulos)):
            pokemon +=titulos[z]+ ": "+ valores[x][z]+" "
            list_result.append(pokemon)
        print(pokemon,"\n")

#Method main
if __name__ == "__main__":
    # start main()
    print("==========================================================")
    print("================== csv readfile example ==================")
    print("==========================================================\n")

    print("--- Config ---")
    # OS max field size
    SYS_MAX_SIZE_FIELD = sys.maxsize
    print("OS MAX FIELD SIZE:", SYS_MAX_SIZE_FIELD)

    # current example max field size
    # Higher than OS max field size generates an error!!!
    CUR_MAX_SIZE_FIELD = pow(2, 31) - 1
    print("CURRENT MAX FIELD SIZE:", CUR_MAX_SIZE_FIELD)

    # config field size
    csv.field_size_limit(CUR_MAX_SIZE_FIELD)

    # row counter

    secuencia_a_imprimir = int(input("ingresa la secuencia con la que deseas imprimir los pokemones"))
    pokemon_lists = load_data(secuencia_a_imprimir)
    datos_a_imprimir = int(input("ingresa la cantidad de pokemones que deseas imprimir"))

    print_results(pokemon_lists[0], pokemon_lists[1], datos_a_imprimir)

    
=======
# importaciones de modulos DISCLib
from DISClib.ADT import list as lt

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


# =============================================================================
# ================== Funciones para configurar el ADT List ====================
# =============================================================================

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


# =============================================================================
# =================== Funciones de lectura de archivos CSV ====================
# =============================================================================

def config_buffer(buffer_size):
    """config_buffer configura el tamaño del buffer para la lectura de
    archivos CSV

    Args:
        buffer_size (int): tamaño del buffer a configurar
    """
    # configurando el buffer de lectura de archivos CSV
    csv.field_size_limit(buffer_size)
    # tomando el nuevo tamaño del buffer
    new_buffer_size = csv.field_size_limit()
    # retornando respuesta al usuario
    return new_buffer_size


def load_data(folder_name, file_name):
    """load_data carga los datos de un archivo CSV y los devuelve en una
    lista de diccionarios

    Args:
        file_name (str): nombre del archivo CSV a cargar

    Raises:
        Exception: devuelve un error generico en cualquier otro caso

    Returns:
        list: ADT list de diccionarios con los datos del archivo CSV
    """

    # creando y configurando el ADT list para almacenar los pokemon
    pokemon_lt = lt.newList("ARRAY_LIST", cmpfunction=cmp_pokedex_id)

    try:
        # concatenando el nombre del archivo con las carpetas de datos
        pokemon_fpath = os.path.join(cf.data_dir,
                                     folder_name,
                                     pokemon_fn)
        # print("Pokemon filepath:", pokemon_fpath)

        # abriendo el archivo CSV
        pokemon_file = open(pokemon_fpath, "r", encoding="utf-8")
        # leyendo el archivo CSV
        pokemons = csv.DictReader(pokemon_file, delimiter=",")
        # iterando sobre los registros del archivo CSV
        for mon in pokemons:
            # agregando el registro al ADT list
            lt.addFirst(pokemon_lt, mon)
        # cerrando el archivo CSV
        pokemon_file.close()
        # retornando la lista de pokemon
        return pokemon_lt
    except Exception as e:
        print(e)
        raise Exception


# =============================================================================
# ============ Funciones para desplegar informacion del archivo ===============
# =============================================================================

def print_options():
    """
    print_options imprime un menu de opciones para

    Returns:
        int: la opcion elegida por el usuario
    """
    print("\n++++++++++++++++++++++ MENU PRINCIPAL +++++++++++++++++++++++++")
    print("\t1. configurar el buffer de lectura para archivos CSV.")
    print("\t2. leer un archivo CSV y cargarlo en un ADT list.")
    print("\t3. mostrar los datos en el ADT List.")
    print("\t4. eliminar los datos del ADT List.")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    opt_usr = int(input("Seleccione una opción para continuar:"))
    return opt_usr


def print_pokemon_lt(lt_pokemon, n_th=NTH):

    # contador de trabajo para imprimir los registros
    i = 0
    # imprimiendo los nombres de las columnas del archivo CSV
    poke_cols = list(lt.firstElement(lt_pokemon).keys())
    print("\n++++++ los campos de la lista de Pokemon son:")
    for col in poke_cols:
        print("\t - '" + str(col) + "'")
    print("\n0++++++ los registros de la lista de Pokemon son:")
    print("imprimiendo cada " + str(n_th) + " veces la lista de Pokemon...\n")

    # iterando sobre los registros de pokemons en el ADT list
    for mon in lt.iterator(lt_pokemon):
        # calculando el modulo del contador de trabajo
        if i % n_th == 0.0:
            # imprimiendo el registro de la n-esima vez
            print("-------------------------------------------------------")
            print("i:", i,
                  "type:", type(mon), "\n"
                  "data:", mon, "\n")
        # incrementando el contador de trabajo
        i = i + 1
    
    print("++++++ total de registros:", lt.size(lt_pokemon))


# main del ejercicio
if __name__ == "__main__":
    """
    main del modulo CSV_FREAD para ejecutar el programa, tiene un menu
    con las siguientes opciones:
    1) configurar el buffer de lectura de archivos CSV
    2) cargar los datos de un archivo CSV
    3) mostrar los datos de cargados en la lista desde el archivo CSV
    4) eliminar datos de la lista
    """

    # titulo del programa
    print("===============================================================")
    print("=============== Ejemplo para leer archivo CSV =================")
    print("===============================================================")

    # variables de configuracion
    poke_folder = "Pokemons"
    pokemon_fn = "Pokemon-utf8-sample.csv"
    pokemon_lt = None
    working = True

    # ciclo del menu
    while working:

        # imprimir opciones del menu
        opt_usr = print_options()

        # opciones del menu
        # opcion 1: configurar el buffer de lectura de archivos CSV
        if opt_usr == 1:
            cur_limit = csv.field_size_limit()
            print("\nEl tamaño actual del buffer es:", cur_limit, "bytes")
            print("El tamaño máximo del buffer es:", SYS_MAX_SIZE_FIELD)
            print("El tamaño recomendado del buffer es:", CUR_MAX_SIZE_FIELD)
            input_str = "Ingrese el tamaño del buffer a configurar: "
            buffer_size = int(input(input_str))
            new_buffer_size = config_buffer(buffer_size)
            print("El tamaño del buffer ahora es:", new_buffer_size)
            print(WARNING_BUFFER_SIZE)
            print("¡La operación fue exitosa!\n")

        # opcion 2: cargar los datos de un archivo CSV
        elif opt_usr == 2:
            print("\nCargando los datos del archivo CSV...")
            print("\tArchivo:", pokemon_fn)
            pokemon_lt = load_data(poke_folder, pokemon_fn)
            print("la lista tiene", lt.size(pokemon_lt), "pokemons")
            print("¡La operación fue exitosa!\n")

        # opcion 3: mostrar los datos del ADT List
        elif opt_usr == 3:
            print("\nLa frecuencia de impresion es de", NTH, "registros")
            input_str = "Seleccione la frecuencia de impresion: "
            n_th = int(input(input_str))
            print_pokemon_lt(pokemon_lt, n_th)
            print("¡La operación fue exitosa!\n")

        # opcion 4: eliminar los datos del ADT List
        elif opt_usr == 4:
            print("\nEliminando los pokemon del ADT List...")
            pokemon_lt = None
            print("Se eliminaron los datos del ADT List")
            dsize = gc.collect()
            print("¡La operación fue exitosa!\n")

        # finalizar el programa
        else:
            # confirmar salida del programa
            end_str = "¿desea salir del programa? (s/n): "
            opt_usr = input(end_str)
            # diferentes opciones de salida
            if opt_usr in ("s", "S", "1", True, "true", "True", "si", "Si"):
                working = False
    # fin del programa
    sys.exit(0)
>>>>>>> 17a88af (01 example documentation and refactor)
