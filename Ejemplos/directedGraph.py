import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import dfs, bfs, dijsktra, scc
from DISClib.ADT import stack

# Crear grafo:
# {
#   "a": [{'vertexA': 'a', 'vertexB': 'b', 'weight': 1}]
#   "b": []
# }
g = gr.newGraph(datastructure='ADJ_LIST',
    directed=True)

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
gr.outdegree(g, "a")    # => 1
gr.indegree(g, "a")     # => 0

print("=>>", s)
gr.numEdges(g)       # => 1


#Camino de "a" a "b"
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
  
# Strongly Conected components
k = scc.KosarajuSCC(g)
scc.connectedComponents(k)  # => 2
scc.stronglyConnected(k, "a", "b") # => False
scc.stronglyConnected(k, "a", "a") # => False

#Dar el id de la componente de cada vertice
for v in lt.iterator(mp.keySet(k["idscc"])):
  cid = mp.get(k["idscc"], v)["value"]
  print(v, cid) #=> b->1;   a->2
  
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
    directed=True,
    size=10,
    comparefunction=comparefunction)