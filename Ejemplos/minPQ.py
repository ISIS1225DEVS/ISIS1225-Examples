import config as cf

from DISClib.ADT import list as lt
from DISClib.ADT import minpq

def cmpfunction(k1, k2):
  if k1 > k2:
    return 1
  if k1 == k2:
    return 0
  else:
    return -1

pq = minpq.newMinPQ(cmpfunction)

minpq.insert(pq, 2) #pq = [2]
minpq.insert(pq, 1) #pq = [1, 2]
minpq.insert(pq, 4) #pq = [1, 2, 4]
minpq.insert(pq, 3) #pq = [1, 2, 3, 4]

minpq.min(pq)     # => 1, no se elimina el minimo
minpq.delMin(pq)  # => 1, se elimina el minimo, pq = [3, 4, 5]

minpq.size(pq)    # => 3
minpq.isEmpty(pq) # => False