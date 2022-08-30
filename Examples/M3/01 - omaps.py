import config as cf
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt


# Creacion
mapa = om.newMap(omaptype='RBT')
mapa = om.newMap(omaptype='BST')

om.put(mapa, "k1", 1)               #mapa ={"k1": 1}
om.put(mapa, "k2", 2)               #mapa ={"k1": 1, "k2": 2}
om.put(mapa, "k3", 3)               #mapa ={"k1": 1, "k2": 2, "k3": 3}

val = me.getValue(om.get(mapa, "k1"))   # => 1
val = om.get(mapa, "k1")["value"]       # => 2

om.remove(mapa, "k1")               #mapa ={"k2": 2, "k3": 3}

om.size(mapa)                       # => 2
om.isEmpty(mapa)                    # => False

om.contains(mapa, "k2")             # => True

#Imprimir las llaves y valores en orden
for k in lt.iterator(om.keySet(mapa)):
  print("llave:" + k + ", valor: " + str(om.get(mapa, k)["value"]))
  
#Imprimir los valores
for v in lt.iterator(om.valueSet(mapa)):
  print(v)

#----------------------
# operaciones ordenadas
#----------------------
mapa = om.newMap(omaptype='RBT')
om.put(mapa, "k1", 1)              
om.put(mapa, "k2", 2)              
om.put(mapa, "k3", 3) 
om.put(mapa, "k6", 6) 
#mapa ={"k1": 1, "k2": 2, "k3": 3, , "k6": 3}

om.minKey(mapa)           # => k1
om.maxKey(mapa)           # => k6

om.floor(mapa, "k3")   # => k3
om.floor(mapa, "k4")   # => k3

om.ceiling(mapa, "k4")   # => k6
om.ceiling(mapa, "k6")   # => k6

om.rank(mapa, "k1")      # => 0
om.rank(mapa, "k2")      # => 1
om.rank(mapa, "k3")      # => 2
om.rank(mapa, "k4")      # => 3

om.select(mapa, 0)      # => k1
om.select(mapa, 1)      # => k2
om.select(mapa, 2)      # => k3
om.select(mapa, 3)      # => k6

# Llaves en un rango inclusivo
for k in lt.iterator(om.keys(mapa, "k1", "k4")):
  print(k)  #k1, k2, k3

#----------------------
# Creacion más complicada
#----------------------

def compareKeys(k1, k2):
    if (k1 == k2):
        return 0
    elif (k1 > k2):
        return 1
    else:
        return -1
      
mapa = om.newMap(
    omaptype='RBT', 
    comparefunction=compareKeys #Usando una funcion de comparacion
  )
om.put(mapa, "k1", 1)              
om.put(mapa, "k2", 2)              
om.put(mapa, "k3", 3) 
om.put(mapa, "k6", 6) 





