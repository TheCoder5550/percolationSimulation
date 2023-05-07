import sys
import multiprocessing as mp
import numpy as np
import matplotlib.pyplot as plt
import random
from node import Node

sys.setrecursionlimit(4000)

def keepEdge(p):
  return random.random() < p # 0 <= random.random() < 1

def searchNode(node, leftNodesChecked, searchedNodes):
  if node in searchedNodes:
    return False

  if node.x == -(size - 1) // 2:
    leftNodesChecked.append(node)

  if node.x == (size - 1) // 2:
    return True

  searchedNodes.append(node)

  for edge in node.connectedEdges:
    if edge[0] == node:
      if searchNode(edge[1], leftNodesChecked, searchedNodes):
        return True
    elif edge[1] == node:
      if searchNode(edge[0], leftNodesChecked, searchedNodes):
        return True
    else:
      print("Error")

  return False

def generateGrid(nodes, p):
  # Create grid of nodes
  for i in range(size):
    for j in range(size):
      x = i - (size - 1) // 2
      y = j - (size - 1) // 2
      node = Node(x, y)
      nodes.append(node)

  # Connect nodes horizontally
  for i in range(size):
    for j in range(size - 1):
      if keepEdge(p):
        a = nodes[i + j * size]
        b = nodes[i + (j + 1) * size]
        edge = (a, b)

        a.connectedEdges.append(edge)
        b.connectedEdges.append(edge)

  # Connect nodes vertically
  for i in range(size - 1):
    for j in range(size):
      if keepEdge(p):
        a = nodes[i + j * size]
        b = nodes[i + j * size + 1]
        edge = (a, b)

        a.connectedEdges.append(edge)
        b.connectedEdges.append(edge)

def simulate(p):
  nodes = []
  generateGrid(nodes, p)

  # Remove edges - Awefully slow :(
  # for edge in edges[:]:
  #   if not keepEdge():
  #     edge[0].connectedEdges.remove(edge)
  #     edge[1].connectedEdges.remove(edge)
  #     edges.remove(edge)

  leftNodesChecked = []

  for i in range(0, size):
    node = nodes[i]
    searchedNodes = []
    if not (node in leftNodesChecked) and searchNode(node, leftNodesChecked, searchedNodes):
      return True

  return False

def getProbability(p):
  successfullSimulations = 0
  for i in range(iterations):
    # print("Iteration", i + 1)
    if simulate(p):
      successfullSimulations += 1

  print("p =", p, iterations, successfullSimulations, successfullSimulations / iterations)

  return successfullSimulations / iterations

n = 50
pStart = 0.35
pStop = 0.65
pSteps = 100
iterations = 10

size = n * 2 + 1

if __name__ == '__main__':
  P = []
  PROB = []

  step = 0
  for p in np.linspace(pStart, pStop, pSteps):
  # p = 0.2
    print("Step", step + 1)
    prob = getProbability(p)
    P.append(p)
    PROB.append(prob)
    step += 1

  plt.title("n = " + str(n) + ", iters/p = " + str(iterations))
  plt.xlabel("p")
  plt.ylabel("propability that a path from left to right exists")
  plt.plot(P, PROB)
  plt.show()





# # Draw nodes
# X = list(map(lambda n: n.x, nodes))
# Y = list(map(lambda n: n.y, nodes))
# plt.scatter(X, Y)

# # Draw edges
# for edge in edges:
#   X = [ edge[0].x, edge[1].x ]
#   Y = [ edge[0].y, edge[1].y ]
#   plt.plot(X, Y)

# plt.show()