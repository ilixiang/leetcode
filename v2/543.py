#!/usr/bin/python3

def diameterOfBinaryTree(root):
    def recursive(root):
        if root == None:
            return (-1, -1)
        
        left, right = root.left, root.right
        (leftDiameter, leftRadius) = recursive(left)
        (rightDiameter, rightRadius) = recursive(right)
        return (max(leftDiameter, rightDiameter, 2 + leftRadius + rightRadius), 1 + max(leftRadius, rightRadius))

    return recursive(root)
