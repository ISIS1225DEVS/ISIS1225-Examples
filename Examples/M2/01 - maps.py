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

import config as cf
import csv
import os
import sys
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
from tabulate import tabulate



def load_data():
  print("==========================================================")
  print("============== ADT Estructure (Map) example =============")
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
  pokemon_list = csv.DictReader(open(pokemon_path,
                                 "r", encoding="utf-8"),
                            delimiter=",")
  print("\n \n +++++++ These are the Pokemon set keys +++++++\n")
  pokemon_keyset = pokemon_list.fieldnames
  i =0
  for key in pokemon_keyset:
    pokeString = f"{i}. {key}"
    i+=1
    print(pokeString)

  poke_key_num = int(input("Seleccione el número de la llave que desea utilizar para cargar los pokemones\n"))
  poke_key = pokemon_list.fieldnames[poke_key_num]
  poke_map = mp.newMap(numelements=801, maptype='PROBING')
  j =0
  for pokemon in pokemon_list:
    mp.put(poke_map,pokemon[poke_key],pokemon)
    j+=1
  print("\nSe encontraron ", j, " pokemones en el set de datos")
  print("Dada la key escogida, el tamaño del mapa es: ", mp.size(poke_map), "\n")
  return poke_map, poke_key


def add_pokemon(poke_map, key):
  key = input(f'Ingresa el {key} del pokemon\n')
  num = input('Ingresa el numero del pokemon\n')
  name = input('Ingresa el nombre del pokemon\n')
  type = input('Ingresa el tipo del pokemon\n')
  generation = input('Ingresa la generacion del pokemon\n')
  hp = input('Ingresa el hp del pokemon\n')
  pokemon_reducido = {'pokedex_num': num, 'name': name,'type': type, 'generation': generation, 'hp': hp} 
  pokemon_reducido[key] = key
  mp.put(poke_map, key, pokemon_reducido)


def remove_pokemon(poke_map, key):
  return mp.remove(poke_map, key)
  

def get_pokemon(poke_map, key):
  return mp.get(poke_map, key)


def print_pokemon_tabulate(pokemon):
  d = dict(pokemon['value'])
  headers1 = ['pokedex_num','name' ,'type1',  'type2', 'generation','abilities' , 'classfication','hp']
  list2 = []
  for i in headers1:
    list2.append(d[i])
  list1 = [headers1,list2]
  print(tabulate(list1,tablefmt='fancy_grid'))


def print_first_n(poke_map, n):
  headers1 = ['pokedex_num','name' ,'type1',  'type2', 'generation','abilities' , 'classfication','hp']
  list_poke = []
  i = 0
  for j in lt.iterator(mp.valueSet(poke_map)):
    d = dict(j)
    value = [d[headers1[0]],d[headers1[1]],d[headers1[2]],d[headers1[3]],d[headers1[4]],d[headers1[5]],d[headers1[6]],d[headers1[7]]]
    if(i<n):
      list_poke.append(value)
    else:
      break
    i+=1
  print(tabulate(list_poke, headers=headers1,tablefmt='fancy_grid'))



def print_map_keys(pokeMap):
  keyset = mp.keySet(pokeMap)
  for poke_key in lt.iterator(keyset):
    print(poke_key)


def printMenu():
  print("Seleccione la opción que desea ejecutar con stack:")
  print("1- Cargar Pokemones en el mapa (A continuación selecciona la llave por la cual deseas cargar los pokemones)")
  print("2- Imprimir las llaves del HashMap")
  print("3- Agregar un Pokemon al HashMap")
  print("4- Eliminar un pokemon dada la Key")
  print("5- Obtener un pokemon dada una key")
  print("6- Imprimir primeros n elementos (sin tener en cuenta una key)")
  print("7- Salir\n")

if __name__ == "__main__":
    while True:
      printMenu()
      option_user=int(input('Seleccione una opción para continuar\n'))
      if option_user == 1:
        poke_map, poke_key = load_data()
      elif option_user == 2:
        print_map_keys(poke_map)
      elif option_user == 3:
        add_pokemon(poke_map, poke_key)
      elif option_user == 4:
        key_to_remove = input('Ingrese la llave del pokemon que desea eliminar\n')
        remove_pokemon(poke_map, key_to_remove)
        print(f'Se eliminó correctamente el pokemon con llave {key_to_remove}, puedes realizar la verificación de esto revisando las llaves del map')
      elif option_user == 5:
        key_to_get = input('Ingrese la llave del pokemon que desea obtener\n')
        if(mp.contains(poke_map,key_to_get)):
          pokemon=get_pokemon(poke_map, key_to_get)
          print(f'El pokemon con llave {key_to_get} es: \n')
          print_pokemon_tabulate(pokemon)
        else:
          print(f'El pokemon con llave {key_to_get} NO existe en tu mapa, ingresa otra llave por favor. \n')

      elif option_user == 6:
        print("El tamaño actual de tu hash map es de: ", mp.size(poke_map), " recuerda que no puedes imprimir más de este número")
        n = int(input('Ingrese el número de pokemones que desea imprimir\n'))
        print_first_n(poke_map,n)
      else:
        sys.out()



""""
# Creacion
mapa = mp.newMap(maptype='CHAINING')
mapa = mp.newMap(maptype='PROBING')

mp.put(mapa, "k1", 1)               #mapa ={"k1": 1}
mp.put(mapa, "k2", 2)               #mapa ={"k1": 1, "k2": 2}
mp.put(mapa, "k3", 3)               #mapa ={"k1": 1, "k2": 2, "k3": 3}

val = me.getValue(mp.get(mapa, "k1"))   # => 1
val = mp.get(mapa, "k1")["value"]       # => 2

mp.remove(mapa, "k1")               #mapa ={"k2": 2, "k3": 3}

mp.size(mapa)                       # => 2
mp.isEmpty(mapa)                    # => False

mp.contains(mapa, "k2")             # => True

#Imprimir las llaves y valores
for k in lt.iterator(mp.keySet(mapa)):
  print("llave:" + k + ", valor: " + str(mp.get(mapa, k)["value"]))
  
#Imprimir los valores
for v in lt.iterator(mp.valueSet(mapa)):
  print(v)


#----------------------
# Creacion más complicada
#----------------------

def compareKeys(k1, entry):
    k2 = me.getKey(entry)
    if (k1 == k2):
        return 0
    elif (k1 > k2):
        return 1
    else:
        return -1

mapa = mp.newMap(
  numelements=5,                #Numero de elementos que se planean guardar, no hay problema si luego son más
  prime=109345121,		            #Un primo, para el hash con MAD
  maptype='CHAINING',             #Tipo de Estructura de datos
  loadfactor=2,                   #Factor de carga maximo. Distinto al factor de carga
  comparefunction=compareKeys     #Funcion para comparar las llaves
  )
#El tamaño del arreglo en "mapa" es un primo > (numelements//loadfactor), en este caso primo > 2, primo == 3

print('size: ', len(mapa["table"]["elements"])) #SOLO para propositos ilustrativos, NO USAR este codigo!!!

mp.put(mapa, "k1", 1)
mp.put(mapa, "k2", 1)
mp.put(mapa, "k3", 1)
mp.put(mapa, "k4", 1)
mp.put(mapa, "k5", 1)
print('size: ', len(mapa["table"]["elements"])) #SOLO para propositos ilustrativos, NO USAR este codigo!!!

mp.put(mapa, "k6", 1) #Causa rehash a una tabla de tamaño primo > 2*size = 7, porque se supera el factor de carga maximo
print('size: ', len(mapa["table"]["elements"])) #SOLO para propositos ilustrativos, NO USAR este codigo!!!

"""



