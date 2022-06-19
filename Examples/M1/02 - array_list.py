import config as cf
from DISClib.ADT import list as lt


a = lt.newList('SINGLE_LINKED')   #Creacion de una lista vacia con listas sencillamente anlazadas
a = lt.newList('ARRAY_LIST')      #Creacion de una lista vacia con arreglos

#Agregar Elementos
lt.addFirst(a, 'a')               # a = ["a"]
lt.addFirst(a, 'b')               # a = ["b", "a"]
lt.addLast(a, 'c')                # a = ["b", "a", "c"]
lt.insertElement(a, "z", 2)       # a = ["b", "z", "a", "c"]
lt.insertElement(a, "x", 3)       # a = ["b", "z", "x", "a", "c"]
lt.size(a)                        # => 5

#Consultar
elem  = lt.firstElement(a)        # elem = "b"
elem  = lt.lastElement(a)         # elem = "c"
elem  = lt.getElement(a, 3)       # elem = "x"
lt.isEmpty(a)                     # => False                    

#Cambiar un elemento
lt.changeInfo(a, 1, "w")          # a =["w", "z", "x", "a", "c"]

#Eliminar un elemento
lt.removeFirst(a)                 # a = ["z", "x", "a", "c"]
lt.removeLast(a)                  # a = ["z", "x", "a"]
lt.deleteElement(a, 2)            # a = ["z", "a"]


# Recorrer una lista
for n in lt.iterator(a):
  print(n)
  
  
#=================================
# Ejemplos Avanzados
#=================================

def compararElementos(e1, e2):
    if (e1 == e2):
        return 0
    elif (e1 > e2):
        return 1
    return -1


a = lt.newList('ARRAY_LIST', 
    cmpfunction=compararElementos) #Creacion de una lista vacia, los elementos se pueden comparar con cmpfunction (para poder usar lt.isPresent)

lt.addLast(a, 'a')                # a = ["a"]
lt.addLast(a, 'b')                # a = ["a", "b"]
lt.addLast(a, 'c')                # a = ["a", "b", "c"]
lt.addLast(a, 'd')                # a = ["a", "b", "c", "d"]

#Intercambiar dos elementos
lt.exchange(a, 2, 4)              # a = ["a", "d", "c", "b"]
sublista = lt.subList(a, 2, 3)    # sublista = ["d", "c", "b"]


lt.isPresent(a, "z")              # => 0, no esta 
lt.isPresent(a, "a")              # => 1, esta en la posicion 1 
lt.isPresent(a, "d")              # => 2, esta en la posicion 2






