import config as cf
from DISClib.ADT import queue

# lib imports
import config as cf
import csv
import os
import sys


def printMenu():
  print("Seleccione la opción que desea ejecutar con Queue:")
  print("1- Cargar Pokemones en la cola (recuerda ejecutar esta opción primero que las anteriores)")
  print("2- Agregar un Pokemon (primera posición, última o en una posición específica")
  print("3- Eliminar un elemento determinado")
  print("4- Obtener el primer elemento de la queue sin eliminarlo")
  print("5- Imprimir primeros n elementos creando una sublista (los elementos son eliminados de la queue)")
  print("6- Imprimir información de la queue")
  print("7- Salir\n")


def load_data():
  print("==========================================================")
  print("============== ADT Estructure (QUEUE)) example =============")
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
  poke_lst = queue.newQueue('SINGLE_LINKED')
  for pokemon in pokemon_list:
    queue.enqueue(poke_lst,pokemon)
  return poke_lst


def add_pokemon(poke_lst, pokemon):
  num = input('Ingresa el numero del pokemon\n')
  name = input('Ingresa el nombre del pokemon\n')
  type = input('Ingresa el tipo del pokemon\n')
  generation = input('Ingresa la generacion del pokemon\n')
  hp = input('Ingresa el hp del pokemon\n')
  pokemon_reducido = {'pokedex_num': num, 'name': name,'type': type, 'generation': generation, 'hp': hp}            
  queue.enqueue(poke_lst,pokemon_reducido)

def remove_pokemon(poke_lst):
  return queue.dequeue(poke_lst)
  
def get_pokemon(poke_lst):
  return queue.peek(poke_lst)

def print_first_n(poke_lst, n):
  i =0
  for j in range(0,n):
    print(queue.dequeue(poke_lst))

def print_queue_info(poke_lst):
  es_vacio = queue.isEmpty(poke_lst)
  tamanio = queue.size(poke_lst)
  return (es_vacio, tamanio)

if __name__ == "__main__":
    while True:
      printMenu()
      option_user=int(input('Seleccione una opción para continuar\n'))
      if option_user == 1:
        poke_lst = load_data()
      elif option_user == 2:
        add_pokemon(poke_lst, pokemon)
      elif option_user == 3:
        pokemon=remove_pokemon(poke_lst)
        print('El pokemon eliminado fue: \n', pokemon)
      elif option_user == 4:
        pokemon=get_pokemon(poke_lst)
        print('El pokemon obtenido (sin eliminarlo de la queue) fue: \n', pokemon)
      elif option_user == 5:
        n = int(input('Ingrese el número de pokemones que desea imprimir\n'))
        print_first_n(poke_lst,n)
      elif option_user == 6:
        info= print_queue_info(poke_lst)
        print('¿La lista es vacia?: \n',info[0],'\n El tamaño de la lista es: \n', info[1])
      else:
        sys.out()