#------------------------------------
# PRECAUCION!!!:
# Este codigo NO usa el TAD list, es decir no es codigo valido para retos
# Sinembargo, ilustra los pasos que se deberian usar:
#   1) busqueda binaria del indice del elemento mas a la izquierda dentro del rango (bisect_left)
#   2) busqueda binaria del indice del elemento mas a la derecha dentro del rango (bisect_right - 1)
#   3) sublist de los elementos en ese rango
#------------------------------------


from bisect import bisect_left, bisect_right

lista = [
  {
    "id": 1,
    "loud": 2
  },
  {
    "id": 2,
    "loud": 1
  },
  {
    "id": 3,
    "loud": 3
  },
  {
    "id": 4,
    "loud": 2
  }
]


# https://docs.python.org/3/howto/sorting.html
lista.sort(key=lambda x: x["loud"])
listaLoud = [v["loud"] for v in lista]
print(listaLoud)

# https://docs.python.org/3/library/bisect.html
left = bisect_left(listaLoud, 2)
right = bisect_right(listaLoud, 2)

print("Elementos entre 2 y 2")
print(lista[left:right])

#Para implmentar bisect_left y bisect_right mirar:
# https://www.geeksforgeeks.org/find-the-number-of-elements-greater-than-k-in-a-sorted-array/?ref=lbp


