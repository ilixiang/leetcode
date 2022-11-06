#!/usr/bin/python3

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors != None else []

def cloneGraph(node):
    if node == None:
        return None

    queue = [node]
    cloneNodes = [None] * 101
    rev = Node(node.val)
    cloneNodes[node.val] = rev
    while len(queue) != 0:
        cur = queue.pop(0)
        curClone = cloneNodes[cur.val]
        neighbors = cur.neighbors
        for neighbor in neighbors:
            if cloneNodes[neighbor.val] == None:
                queue.append(neighbor)
                cloneNodes[neighbor.val] = Node(neighbor.val)
            curClone.neighbors.append(cloneNodes[neighbor.val])
    return rev
