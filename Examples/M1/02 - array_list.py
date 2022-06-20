"""
TODO _summary_ of this module/file CSV_FREAD
"""
# lib imports
import config as cf
import csv
import os
# import ADT list
from DISClib.ADT import list as lt
# imports to meassure time and memory
# from Utils.measurements import *
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


if __name__ == "__main__":
    # start main()
    print("==========================================================")
    print("============== ADT List (ARRAY_LIST) example =============")
    print("==========================================================\n")

    print("--- Config filepath ---")
    # subfolder name
    file_folder = "Samples"
    pokemon_fn = "Pokemon-utf8-sample.csv"
    # join pokemon file path
    pokemon_path = os.path.join(cf.data_dir,
                                file_folder,
                                pokemon_fn)
    print("Pokemon filepath:", pokemon_path)

    # reading pokemon file
    print("+++++++ Reading Pokemon file +++++++")
    # dict reader
    pokemons = csv.DictReader(open(pokemon_path,
                                   "r", encoding="utf-8"),
                              delimiter=",")
    # row counter
    i = 0
    N = 100

    # config ADT List as ARRAY_LIST
    pokemon_lt = lt.newList(datastructure="ARRAY_LIST",
                            cmpfunction=cmp_pokedex_id,)

    # looping through pokemon file
    for mon in pokemons:
        lt.addFirst(pokemon_lt, mon)
        if i % N == 0.0:
            # printing each N th row
            print("i:", i,
                  "type:", type(mon), "\n"
                  "data:", mon)
        i = i + 1
    lts = lt.size(pokemon_lt)

    print("--- Pokemon list details ---")
    print("Pokemon list size:", lts)
    print("File reader iterator", i)

    print(i, lts)




    # a = lt.newList('SINGLE_LINKED')   #Creacion de una lista vacia con listas sencillamente anlazadas
    # a = lt.newList('ARRAY_LIST')      #Creacion de una lista vacia con arreglos

    # #Agregar Elementos
    # lt.addFirst(a, 'a')               # a = ["a"]
    # lt.addFirst(a, 'b')               # a = ["b", "a"]
    # lt.addLast(a, 'c')                # a = ["b", "a", "c"]
    # lt.insertElement(a, "z", 2)       # a = ["b", "z", "a", "c"]
    # lt.insertElement(a, "x", 3)       # a = ["b", "z", "x", "a", "c"]
    # lt.size(a)                        # => 5

    # #Consultar
    # elem  = lt.firstElement(a)        # elem = "b"
    # elem  = lt.lastElement(a)         # elem = "c"
    # elem  = lt.getElement(a, 3)       # elem = "x"
    # lt.isEmpty(a)                     # => False                    

    # #Cambiar un elemento
    # lt.changeInfo(a, 1, "w")          # a =["w", "z", "x", "a", "c"]

    # #Eliminar un elemento
    # lt.removeFirst(a)                 # a = ["z", "x", "a", "c"]
    # lt.removeLast(a)                  # a = ["z", "x", "a"]
    # lt.deleteElement(a, 2)            # a = ["z", "a"]


    # # Recorrer una lista
    # for n in lt.iterator(a):
    #   print(n)
    
    
    # =================================
    # # Ejemplos Avanzados
    # #=================================

    # def compararElementos(e1, e2):
    #     if (e1 == e2):
    #         return 0
    #     elif (e1 > e2):
    #         return 1
    #     return -1


    # a = lt.newList('ARRAY_LIST', 
    #     cmpfunction=compararElementos) #Creacion de una lista vacia, los elementos se pueden comparar con cmpfunction (para poder usar lt.isPresent)

    # lt.addLast(a, 'a')                # a = ["a"]
    # lt.addLast(a, 'b')                # a = ["a", "b"]
    # lt.addLast(a, 'c')                # a = ["a", "b", "c"]
    # lt.addLast(a, 'd')                # a = ["a", "b", "c", "d"]

    # #Intercambiar dos elementos
    # lt.exchange(a, 2, 4)              # a = ["a", "d", "c", "b"]
    # sublista = lt.subList(a, 2, 3)    # sublista = ["d", "c", "b"]


    # lt.isPresent(a, "z")              # => 0, no esta 
    # lt.isPresent(a, "a")              # => 1, esta en la posicion 1 
    # lt.isPresent(a, "d")              # => 2, esta en la posicion 2






