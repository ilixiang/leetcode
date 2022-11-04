#!/usr/bin/python3

from .TreeNode import TreeNode

def generateTrees(n):
    dp = {}
    return generateTreesRecursive(1, n, dp)

def generateTreesRecursive(n1, n2, dp):
    if n1 > n2:
        return [None]

    key = 'f%dt%d'%(n1, n2)
    if key in dp:
        return dp[key]

    if n1 == n2:
        dp[key] = [TreeNode(n1)]
        return dp[key]
    
    rev = []
    for i in range(n1, n2 + 1):
        lefts = generateTreesRecursive(n1, i - 1, dp)
        rights = generateTreesRecursive(i + 1, n2, dp)
        for left in lefts:
            for right in rights:
                rev.append(TreeNode(i, left, right))
    dp[key] = rev
    return rev



