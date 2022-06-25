#!/usr/bin/python3

def combine(n, k):
    arr = []
    result = []
    combineRecursive(n, k, 1, arr, result) 
    return result

def combineRecursive(n, remain, start, arr, result):
    if remain == 0:
        result.append(list(arr))
        return

    for i in range(start, n - remain + 2):
        arr.append(i)
        combineRecursive(n, remain - 1, i + 1, arr, result)
        arr.pop()

print(combine(4, 2))

