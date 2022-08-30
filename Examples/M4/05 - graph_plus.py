import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import dfo, cycles
from DISClib.ADT import stack

# Grafo:
# {
#   "a": [{'vertexA': 'a', 'vertexB': 'b', 'weight': 1}]
#   "b": []
# }
g = gr.newGraph(datastructure='ADJ_LIST',
    directed=True)

gr.insertVertex(g, "a")
gr.insertVertex(g, "b")
gr.addEdge(g, "a", "b", 1)

# 1 Verificar que no hay ciclos
search = cycles.DirectedCycle(g)  
cycles.hasCycle(search) #=> Fase

search = dfo.DepthFirstOrder(g)
r = search["reversepost"]
while not stack.isEmpty(r):
  n = stack.pop(r)
  print(n)  #=> a, b

