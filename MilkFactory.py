class Node:
  def __init__(self, key):
    self.key = key
    self.neighbors = []
    self.isVisited = False
  def addNeighbor(self, node):
    self.neighbors.append(node)
class Graph:
  def __init__(self):
    self.graph = {}
  def addNode(self, node):
    self.graph[node.key] = node 
  def addEdge(self, node1, node2):
    node1.addNeighbor(node2) 
  def dfs_iterative(self, vertex):
    output = []
    stack = []
    stack.append(vertex.key)
    while len(stack) != 0:
      currentNode = self.graph[stack[-1]].key
      if self.graph[currentNode].isVisited == False:
        output.append(currentNode)
      self.graph[stack[-1]].isVisited = True
      visitedCount = 0
      for nodes in self.graph[stack[-1]].neighbors:
        if nodes.isVisited == False:
          stack.append(nodes.key)
          break
        else:
          visitedCount += 1
      if visitedCount == len(self.graph[currentNode].neighbors):
        stack.pop()
    return output
  def reset_graph(self):
    for thing in self.graph.values():
        thing.isVisited = False
graph = Graph()
f = open("factory.in")
n = int(f.readline())
counts = {}
for i in range(n):
    graph.addNode(Node(i+1))
    counts[i+1] = 0
for i in range(n-1):
    x = list(map(int, f.readline().split()))
    graph.addEdge(graph.graph[x[0]], graph.graph[x[1]])
outputs = []
for i in range(1, n+1):
    outputs.append(graph.dfs_iterative(graph.graph[i]))
    graph.reset_graph()
for i in range(len(outputs)):
    for j in range(len(outputs[i])):
        counts[outputs[i][j]] += 1
f = open("factory.out", "w")
for i in range(1, len(counts)+1):
    if (counts[i] == n):
        f.write(str(i))
        exit(0)
f.write(str(-1))