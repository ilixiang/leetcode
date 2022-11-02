#!/usr/bin/python3

def combinationSum(candidates, target):
    result = []
    tmp = []
    candidates.sort()
    combination(candidates, target, 0, tmp, result)
    return result
    
def combination(candidates, target, index, tmp, result):
    if index >= len(candidates):
        return

    candidate = candidates[index]
    if candidate == target:
        tmp.append(candidate)
        result.append(list(tmp))
        tmp.pop()
        return
    elif candidate < target:
        tmp.append(candidate)
        combination(candidates, target - candidate, index, tmp, result)
        tmp.pop()

        combination(candidates, target, index + 1, tmp, result)
    else:
        return

print(combinationSum([2, 3, 6, 7], 7))

