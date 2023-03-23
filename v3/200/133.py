#!/usr/bin/python3

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors

def cloneGraph(node):
    if not node:
        return None

    visited = set()
    nodeCopyMap = {}
    queue = [node]
    while len(queue) != 0:
        curNode = queue.pop(0)
        if curNode.val in visited:
            continue

        curNodeCopy = nodeCopyMap.get(curNode.val, None)
        if not curNodeCopy:
            nodeCopyMap[curNode.val] = curNodeCopy = Node(curNode.val, [])

        for neighbor in curNode.neighbors:
            neighborCopy = nodeCopyMap.get(neighbor.val, None)
            if not neighborCopy:
                nodeCopyMap[neighbor.val] = neighborCopy = Node(neighbor.val, [])
            curNodeCopy.neighbors.append(neighborCopy)
            queue.append(neighbor)
        visited.add(curNode.val)
    return nodeCopyMap[node.val]
            
