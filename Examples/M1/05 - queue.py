import config as cf
from DISClib.ADT import queue

cola = queue.newQueue()     #Crea una cola con listas enlazadas
queue.size(cola)            # => 0
queue.enqueue(cola, "a")    # cola = ["a"]          
queue.enqueue(cola, "b")    # cola = ["a", "b"]
queue.enqueue(cola, "c")    # cola = ["a", "b", "c"]

elem = queue.dequeue(cola) #elem = "a", cola = ["b", "c"]
elem = queue.dequeue(cola) #elem = "b", cola = ["c"]
elem = queue.dequeue(cola) #elem = "c", cola = []


queue.enqueue(cola, "a")    # cola = ["a"]          
queue.enqueue(cola, "b")    # cola = ["a", "b"]
elem  = queue.peek(cola)    # elem = "a", cola = ["a", "b"]

# Iterar sobre los elementos de una cola, la cola queda vacia
while not queue.isEmpty(cola):
  n = queue.dequeue(cola)
  print(n)


