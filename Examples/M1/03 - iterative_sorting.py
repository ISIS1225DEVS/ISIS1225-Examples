import config as cf

from DISClib.ADT import list as lt

from DISClib.Algorithms.Sorting import insertionsort

# Crear Lista
elementos = [
  {"a": 1, "b": 2},
  {"a": 2, "b": 4},
  {"a": 2, "b": 3},
  {"a": 1, "b": 1}
]
lista = lt.newList()
for n in elementos:
  lt.addLast(lista, n)


#Ordenar descentemente por "a" y ascendentemente por "b"
def compareElem(e1, e2):
  if e1["a"] != e2["a"]:
    return e1["a"] > e2["a"]
  return e1["b"] < e2["b"]


#Ordenar lista
listaOrdenada = insertionsort.sort(lista, compareElem)

for n in lt.iterator(listaOrdenada):
  print(n)

