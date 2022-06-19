import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import dfs, bfs, dijsktra, prim
from DISClib.ADT import stack

# Grafo no dirigido:
# {
#   "a": [{'vertexA': 'a', 'vertexB': 'b', 'weight': 1}]
#   "b": [{'vertexA': 'a', 'vertexB': 'b', 'weight': 1}]
# }
g = gr.newGraph(datastructure='ADJ_LIST',
    directed=False)

gr.insertVertex(g, "a")
gr.insertVertex(g, "b")
gr.addEdge(g, "a", "b", 1)

for n in lt.iterator(gr.adjacents(g, "a")):
  print(n)  # => b

for n in lt.iterator(gr.vertices(g)):
  print(n)  # => a, b
  
for n in lt.iterator(gr.edges(g)):
  print(n)  # => {'vertexA': 'a', 'vertexB': 'b', 'weight': 1}
  
gr.containsVertex(g, "z")   # => True
gr.numVertices(g)       # => 2
gr.degree(g, "a")       # => 1
s = gr.numEdges(g)       # => 1


#Caminos de "a" a "b"
search = dfs.DepthFirstSearch(g, "a")
camino = dfs.pathTo(search, "b")
while not stack.isEmpty(camino):
  n = stack.pop(camino)
  print(n)

search = bfs.BreadhtFisrtSearch(g, "a")
camino = bfs.pathTo(search, "b")
while not stack.isEmpty(camino):
  n = stack.pop(camino)
  print(n)
  
search = dijsktra.Dijkstra(g, "a")
camino = dijsktra.pathTo(search, "b")
while not stack.isEmpty(camino):
  n = stack.pop(camino) 
  print(n)    # => {'vertexA': 'a', 'vertexB': 'b', 'weight': 1}
  

#Imprimir cada vertice del MST
p = prim.PrimMST(g)
prim.weightMST(g, p)   # => 1.0
for n in lt.iterator(p["mst"]):
  print(n)    # => {'vertexA': 'a', 'vertexB': 'b', 'weight': 1}
  
#--------------------------
# Creacion mas compleja del grafo
#--------------------------
  
def comparefunction(v1, v2):
    _v2 = v2['key']
    if (v1 == _v2):
        return 0
    elif (v1 > _v2):
        return 1
    else:
        return -1

g = gr.newGraph(datastructure='ADJ_LIST',
    directed=False,
    size=10,
    comparefunction=comparefunction)