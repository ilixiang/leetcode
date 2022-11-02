#!/usr/bin/python3

def convertToTitle(columnNumber):
    arr = []
    while columnNumber != 0:
        columnNumber = columnNumber - 1
        num = columnNumber % 26
        arr.append(chr(65 + num))
        columnNumber = columnNumber // 26
    arr.reverse()
    return ''.join(arr)

print(convertToTitle(1))
print(convertToTitle(28))
print(convertToTitle(701))

