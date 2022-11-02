#!/usr/bin/python3

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n):
    dp = [None] * (n + 2)
    for i in range(0, n + 2):
        dp[i] = [None] * (n + 2)
    return generateTreesDp(1, n + 1, dp)

def generateTreesDp(left, right, dp):
    if dp[left][right] != None:
        return dp[left][right]

    if left == right:
        dp[left][right] = [None]
    else:
        val = left
        trees = []
        while val < right:
            leftTrees = generateTreesDp(left, val, dp)
            rightTrees = generateTreesDp(val + 1, right, dp)
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    trees.append(TreeNode(val, leftTree, rightTree))
            val = val + 1
        dp[left][right] = trees
    return dp[left][right]

print(len(generateTrees(3)))

