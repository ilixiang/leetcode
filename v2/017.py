#!/usr/bin/python3

def letterCombinations(digits):
    letters = [\
        [], [], ['a', 'b', 'c'], ['d', 'e', 'f'],\
        ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],\
        ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']\
    ]

    tmps = list(letters[int(digits[0])])
    res = []
    for i in range(1, len(digits)):
        for letter in letters[int(digits[i])]:
            for tmp in tmps:
                res.append(tmp + letter)
        res, tmps = tmps, res
        res.clear()
    return tmps