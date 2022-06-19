import config as cf
from DISClib.ADT import stack

cola = stack.newStack()  #Crea un stack con listas enlazadas
stack.size(cola)         # => 0
stack.push(cola, "a")    # cola = ["a"]          
stack.push(cola, "b")    # cola = ["a", "b"]
stack.push(cola, "c")    # cola = ["a", "b", "c"]

elem = stack.pop(cola) #elem = "c", cola = ["a", "b"]
elem = stack.pop(cola) #elem = "b", cola = ["a"]
elem = stack.pop(cola) #elem = "a", cola = []


stack.push(cola, "a")    # cola = ["a"]          
stack.push(cola, "b")    # cola = ["a", "b"]
elem  = stack.top(cola)   # elem = "a", cola = ["a", "b"]

# Iterar sobre los elementos de una cola, la cola queda vacia
while not stack.isEmpty(cola):
  n = stack.pop(cola)
  print(n)


