#!/usr/bin/python3

from TreeNode import TreeNode

def generateTrees(n):
    def generate(left, right):
        if left > right:
            return None
        
        rev = []
        for i in range(left, right + 1):
            leftTrees = generate(left, i - 1)
            rightTrees = generate(i + 1, right)
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    rev.append(TreeNode(i, leftTree, rightTree))
        return rev

    return generate(1, n)
