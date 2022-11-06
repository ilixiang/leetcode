#!/usr/bin/python3

def sumNumbers(root):
    def sumNumbersRecursive(root):
        val, left, right = root.val, root.left, root.right
        if left == None and right == None:
            return [(val, 1)]
        
        revs = []
        if left != None:
            leftRevs = sumNumbersRecursive(root.left)
            for leftRev in leftRevs:
                (leftVal, leftWeight) = leftRev
                curWeight = leftWeight * 10
                revs.append((val * curWeight + leftVal, curWeight))

        if right != None:
            rightRevs = sumNumbersRecursive(root.right)
            for rightRev in rightRevs:
                (rightVal, rightWeight) = rightRev
                curWeight = rightWeight * 10
                revs.append((val * curWeight + rightVal, curWeight))
        return revs
    
    rootRecursiveRevs = sumNumbersRecursive(root)
    rev = 0
    for rootRecursiveRev in rootRecursiveRevs:
        rev += rootRecursiveRev[0]
    return rev
    

