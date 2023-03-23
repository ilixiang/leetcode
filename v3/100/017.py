#!/usr/bin/python3

def letterCombinations(digits):
    if len(digits) == 0:
        return ''
    
    m = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'],\
         ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],\
         ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    
    def recursive(i, prevs):
        if i == len(digits):
            return prevs

        rev = []
        for prev in prevs:
            for c in m[int(digits[i])]:
                rev.append(prev + c)
        return recursive(i + 1, rev)
    return recursive(0, [''])
