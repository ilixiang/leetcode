#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if root == None:
        return []
    s = [root]
    result = []
    while len(s) != 0:
        node = s.pop()
        result.append(node.val)
        if node.right != None:
            s.append(node.right)
        if node.left != None:
            s.append(node.left)
    return result

print(preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))

