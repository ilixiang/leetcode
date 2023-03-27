#!/usr/bin/python3

def hamningWeight(n):
    rev = 0
    for i in range(32):
        rev += (n >> i) & 1
    return rev
