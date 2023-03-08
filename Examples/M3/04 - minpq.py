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
import csv
import gc
from shutil import ExecError
import sys
import pprint
import os
import config as cf
#importaciones de DISCLib
from DISClib.ADT import list as lt
from DISClib.ADT import minpq as mpq

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
# ================== Funciones para configurar el ADT MinPQ ====================
# =============================================================================

#Funcion que se encarga de visualizar que elementos es mayor
#En el caso que k1 sea mayor a k2 debemos retornar 1
#En el caso que k1 sea igual a k2 debemos retornar 0
#Si no es ninguno de los casos anteriores retornamos -1
def cmpfunction(patient1, patient2):
    hearth_rate = "HR"
    respiratory_rate = "RR"
    systolic_blood_preasure = "SBP"
    diastolic_blood_preasure = "DBP"
    injury="Injury"
    if (patient1[hearth_rate]<patient2[hearth_rate]) or (patient1[respiratory_rate]<patient1[respiratory_rate]):
        return 1
    elif (patient1[systolic_blood_preasure]<patient2[systolic_blood_preasure]) or (patient1[diastolic_blood_preasure]<patient2[diastolic_blood_preasure]):
        return 0
    elif (patient1[injury]<patient2[injury]):
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

def load_data(folder_name, file_name):
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
    pq = mpq.newMinPQ(cmpfunction)

    try:
        # concatenando el nombre del archivo con las carpetas de datos
        triage_fpath = os.path.join(cf.data_dir,
                                     folder_name,
                                     file_name)
        print("Archivo ubicado en:", triage_fpath)

        # abriendo el archivo CSV
        triage_file = open(triage_fpath, "r", encoding="utf-8")
        # leyendo el archivo CSV
        triage_register = csv.DictReader(triage_file, delimiter=",")
        # iterando sobre los registros del archivo CSV
        for triage in triage_register:
            # agregando el registro al ADT list
            mpq.insert(pq, triage)
        # cerrando el archivo CSV
        triage_file.close()
        # retornando la lista de triage
        return pq
    except Exception as e:
        print(e)
        raise Exception

# =============================================================================
# ================== Funciones para manipular el ADT MinPQ =====================
# =============================================================================

#Insertamos elementos en la cola de prioridad
minpq.insert(pq, 2) #pq = [2]
minpq.insert(pq, 1) #pq = [1, 2]
minpq.insert(pq, 4) #pq = [1, 2, 4]
minpq.insert(pq, 3) #pq = [1, 2, 3, 4]

#Retornamos el menor elemento de la lista 
#Se elimina el menor elemento.
minpq.min(pq)     # => 1, no se elimina el minimo
minpq.delMin(pq)  # => 1, se elimina el minimo, pq = [3, 4, 5]

#Se retorna el numero de elementos de la lista
#Indica si la MinPQ esta vacia
minpq.size(pq)    # => 3
minpq.isEmpty(pq) # => False

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
    print("\t1. Cargar pacientes desde el archivo CSV\n",
          "\t¡¡¡IMPORTANTE: ejecutar esta opción antes de cualquier otra!!!")
    print("\t2. Imprimir la información general de la lista de pacientes.")
    print("\t3. Imprimir la información de un paciente.")
    print("\t4. Agregar un nuevo paciente en la cola")
    print("\t5. Atender un paciente.")
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
