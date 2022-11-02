#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    tuples = sumNumbersRecursive(root)
    result = 0
    for t in tuples:
        result = result + t[0]
    return result

def sumNumbersRecursive(root):
    if root.left == None and root.right == None:
        return [(root.val, 1)]

    result = []
    if root.left != None:
        lefts = sumNumbersRecursive(root.left)
        print(lefts)
        for (val, exponent) in lefts:
            result.append((root.val * (10 ** exponent) + val, exponent + 1))
    if root.right != None:
        rights = sumNumbersRecursive(root.right)
        print(rights)
        for (val, exponent) in rights:
            result.append((root.val * (10 ** exponent) + val, exponent + 1))
    return result

print(sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))

