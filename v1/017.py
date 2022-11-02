#!/usr/bin/python3

def letterCombinations(digits):
    if digits == None or len(digits) == 0:
        return []

    nums = []
    mappings = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    for b in digits.encode('ascii'):
        nums.append(b - 48)

    result = []
    indexStack = [0]
    charStack = [mappings[nums[0]][0]]
    while len(indexStack) != 0:
        if len(indexStack) == len(nums):
            result.append(''.join(charStack))
            while len(indexStack) != 0:
                mappingIndex = indexStack.pop()
                charStack.pop()
                if mappingIndex != len(mappings[nums[len(indexStack)]]) - 1:
                    charStack.append(mappings[nums[len(indexStack)]][mappingIndex + 1])
                    indexStack.append(mappingIndex + 1)
                    break
        else:
            indexStack.append(0)
            charStack.append(mappings[nums[len(indexStack) - 1]][0])
    return result

print(letterCombinations('23'))

