import config as cf
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt


# Creacion
mapa = mp.newMap(maptype='CHAINING')
mapa = mp.newMap(maptype='PROBING')

mp.put(mapa, "k1", 1)               #mapa ={"k1": 1}
mp.put(mapa, "k2", 2)               #mapa ={"k1": 1, "k2": 2}
mp.put(mapa, "k3", 3)               #mapa ={"k1": 1, "k2": 2, "k3": 3}

val = me.getValue(mp.get(mapa, "k1"))   # => 1
val = mp.get(mapa, "k1")["value"]       # => 2

mp.remove(mapa, "k1")               #mapa ={"k2": 2, "k3": 3}

mp.size(mapa)                       # => 2
mp.isEmpty(mapa)                    # => False

mp.contains(mapa, "k2")             # => True

#Imprimir las llaves y valores
for k in lt.iterator(mp.keySet(mapa)):
  print("llave:" + k + ", valor: " + str(mp.get(mapa, k)["value"]))
  
#Imprimir los valores
for v in lt.iterator(mp.valueSet(mapa)):
  print(v)


#----------------------
# Creacion más complicada
#----------------------

def compareKeys(k1, entry):
    k2 = me.getKey(entry)
    if (k1 == k2):
        return 0
    elif (k1 > k2):
        return 1
    else:
        return -1

mapa = mp.newMap(
  numelements=5,                #Numero de elementos que se planean guardar, no hay problema si luego son más
  prime=109345121,		            #Un primo, para el hash con MAD
  maptype='CHAINING',             #Tipo de Estructura de datos
  loadfactor=2,                   #Factor de carga maximo. Distinto al factor de carga
  comparefunction=compareKeys     #Funcion para comparar las llaves
  )
#El tamaño del arreglo en "mapa" es un primo > (numelements//loadfactor), en este caso primo > 2, primo == 3

print('size: ', len(mapa["table"]["elements"])) #SOLO para propositos ilustrativos, NO USAR este codigo!!!

mp.put(mapa, "k1", 1)
mp.put(mapa, "k2", 1)
mp.put(mapa, "k3", 1)
mp.put(mapa, "k4", 1)
mp.put(mapa, "k5", 1)
print('size: ', len(mapa["table"]["elements"])) #SOLO para propositos ilustrativos, NO USAR este codigo!!!

mp.put(mapa, "k6", 1) #Causa rehash a una tabla de tamaño primo > 2*size = 7, porque se supera el factor de carga maximo
print('size: ', len(mapa["table"]["elements"])) #SOLO para propositos ilustrativos, NO USAR este codigo!!!





