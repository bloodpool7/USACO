class Node:
  def __init__(self, key):
    self.key = key
    self.neighbors = []
  def addNeighbor(self, node):
    self.neighbors.append(node)
class Graph:
  def __init__(self):
    self.graph = {}
  def addNode(self, node):
    self.graph[node.key] = node
  def addEdge(self, node1, node2):
    node1.addNeighbor(node2)
    node2.addNeighbor(node1)
f = open("planting.in", "r")
n = int(f.readline())
graph = Graph()
for i in range(n):
  graph.addNode(Node(i+1))
for i in range(n-1):
  x = list(map(int, f.readline().split()))
  graph.addEdge(graph.graph[x[0]], graph.graph[x[1]])
max_neighbor_length = 0
for i in range(1, len(graph.graph)+1):
  if len(graph.graph[i].neighbors) > max_neighbor_length:
    max_neighbor_length = len(graph.graph[i].neighbors)
f = open("planting.out", "w")
f.write(str(max_neighbor_length+1))
