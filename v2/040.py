#!/usr/bin/python3

def combinationSum2(candidates, target):
    candidates.sort()
    return combinationSum2Recursive(candidates, target, 0)

def combinationSum2Recursive(candidates, target, start):
    if target == 0:
        return [[]]

    if target < 0 or start >= len(candidates):
        return []
    
    res = []
    i = start
    while i < len(candidates):
        if i != start and candidates[i] == candidates[i - 1]:
            i += 1
            continue
        candidate = candidates[i]
        nextCombinations = combinationSum2Recursive(candidates, target - candidate, i + 1)
        for nextCombination in nextCombinations:
            tmp = [candidate]
            tmp.extend(nextCombination)
            res.append(tmp)
        i += 1
    return res


if __name__ == '__main__':
    print(combinationSum2([2,5,2,1,2], 5))
