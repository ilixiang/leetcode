#!/usr/bin/python3

def titleToNumber(columnTitle):
    rev = 0
    for c in columnTitle:
        rev = rev * 26 + (ord(c) - ord('A') + 1)
    return rev
