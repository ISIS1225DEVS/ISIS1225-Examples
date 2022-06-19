import config as cf

from DISClib.ADT import list as lt

from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import selectionsort
from DISClib.Algorithms.Sorting import shellsort
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import quicksort

# Crear Lista
elementos = [4, 2, 1, 3]
lista = lt.newList()
for n in elementos:
  lt.addLast(lista, n)


def compareElem(e1, e2):
  return e1 < e2


#Ordenar lista
listaOrdenada = insertionsort.sort(lista, compareElem)
listaOrdenada = selectionsort.sort(lista, compareElem)
listaOrdenada = shellsort.sort(lista, compareElem)
listaOrdenada = mergesort.sort(lista, compareElem)
listaOrdenada = quicksort.sort(lista, compareElem)


for n in lt.iterator(listaOrdenada):
  print(n)

