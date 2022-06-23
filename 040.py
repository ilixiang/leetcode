#!/usr/bin/python3

def combinationSum2(candidates, target):
    candidates.sort()
    tmp = []
    result = []
    combination2(candidates, target, 0, tmp, result)
    return result

def combination2(candidates, target, index, tmp, result):
    if index >= len(candidates):
        return

    candidate = candidates[index]
    if candidate > target:
        return
    elif candidate == target:
        tmp.append(candidate)
        result.append(list(tmp))
        tmp.pop()
    else:
        tmp.append(candidate)
        combination2(candidates, target - candidate, index + 1, tmp, result)
        tmp.pop()
        index = index + 1
        while index < len(candidates) and candidates[index] == candidates[index - 1]:
            index = index + 1
        if index < len(candidates):
            combination2(candidates, target, index, tmp, result)

print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

