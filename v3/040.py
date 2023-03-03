#!/usr/bin/python3

def combinationSum2(candidates, target):
    candidates.sort()

    tmp = []
    rev = []
    def recursive(startIndex, target):
        if target == 0:
            rev.append(list(tmp))
            return
        
        if startIndex >= len(candidates) or candidates[startIndex] > target:
            return

        i = startIndex
        while i < len(candidates):
            if i != startIndex and candidates[i] == candidates[i - 1]:
                i += 1
                continue
            
            if candidates[i] > target:
                return
            
            tmp.append(candidates[i])
            recursive(i + 1, target - candidates[i])
            tmp.pop()
            i += 1
    
    recursive(0, target)
    return rev
