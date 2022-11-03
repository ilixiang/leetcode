#!/usr/bin/python3

def combinationSum(candidates, target):
    return combinationSumRecursive(candidates, target, 0)

def combinationSumRecursive(candidates, target, start):
    if target < 2:
        return []
    res = []
    for i in range(start, len(candidates)):
        candidate = candidates[i]
        nextCombinations = combinationSumRecursive(candidates, target - candidate, i)
        for nextCombination in nextCombinations:
            tmp = [candidate]
            tmp.extend(nextCombination)
            res.append(tmp)
    return res


