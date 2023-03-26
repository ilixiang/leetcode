#!/usr/bin/python3

def convertToTitle(columnNumber):
    tmp = []
    while columnNumber != 0:
        columnNumber -= 1
        tmp.append(chr(ord('A') + columnNumber % 26))
        columnNumber //= 26
    tmp.reverse()
    return ''.join(tmp)
