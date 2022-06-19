#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    if root == None:
        return []
    s = [root]
    result = []
    while len(s) != 0:
        node = s.pop()
        result.append(node.val)
        if node.left != None:
            s.append(node.left)
        if node.right != None:
            s.append(node.right)
    left = 0
    right = len(result) - 1
    while left < right:
        tmp = result[left]
        result[left] = result[right]
        result[right] = tmp
        left = left + 1
        right = right - 1
    return result

print(postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))

