#!/usr/bin/python3

def generate(numRows):
    tmp = [1] * numRows
    rev = [None] * numRows
    for i in range(0, numRows):
        for j in range(1, i):
            tmp[i - j] = tmp[i - j] + tmp[i - j - 1]
        rev[i] = tmp[0: i + 1]
    return rev
