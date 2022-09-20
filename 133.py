#!/usr/bin/python3

def cloneGraph(node):
    if node == None:
        return None
    visited = set([node.val])
    cloneNodeMap = {}
    queue = [node]
    while len(queue) != 0:
        cur = queue.pop(0)
        if not cur.val in cloneNodeMap:
            cloneNodeMap[cur.val] = Node(val, [])
        cloneCur = cloneNodeMap[cur.val]
        for neighbor in cur.neighbors:
            if not neighbor.val in cloneNodeMap:
                cloneNodeMap[neighbor.val] = Node(neighbor.val, [])
            cloneCur.neighbor.append(cloneNodeMap[neighbor.val])
            if not neighbor.val in visited:
                queue.append(neighbor)
                visited.add(neighbor.val)
    return cloneNodeMap[node.val]

