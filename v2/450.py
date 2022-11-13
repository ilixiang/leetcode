#!/usr/bin/python3

def deleteNode(root, key):
    if root == None:
        return None

    if root.val == key:
        return removeNode(root)

    deletingNode = None
    deletingParent = None
    node = root
    while node:
        left, right = node.left, node.right
        if key < node.val:
            if left != None and left.val == key:
                node.left = removeNode(left)
                break
            else:
                node = left
        else:
            if right != None and right.val == key:
                node.right = removeNode(right)
                break
            else:
                node = right
    return root
    
def removeNode(node):
    if node.left == None:
        return node.right
    if node.right == None:
        return node.left
    
    left = node.left
    predecessor = node.left
    while predecessor.right:
        predecessor = predecessor.right
    predecessor.right = node.right
    return left
    