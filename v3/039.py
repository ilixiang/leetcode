#!/usr/bin/python3

def combinationSum(candidates, target):
    candidates.sort()

    rev = []
    tmp = []
    def recursive(startIndex, target):
        if target == 0:
            rev.append(list(tmp))
            return
        
        if startIndex >= len(candidates) or candidates[startIndex] > target:
            return
        
        recursive(startIndex + 1, target)

        tmp.append(candidates[startIndex])
        recursive(startIndex, target - candidates[startIndex])
        tmp.pop()
    
    recursive(0, target)
    return rev
