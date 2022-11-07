#!/usr/bin/python3

def titleToNumber(columnTitle):
    rev = 0
    for c in columnTitle:
        rev = rev * 26 + c.encode()[0] - 65 + 1
    return rev
