#!/usr/bin/python3

def convert(s, numRows):
    if numRows <= 1:
        return s
    repeatCharAmount = 2 * numRows - 2
    loopCount = len(s) // repeatCharAmount + 1
    result = ''
    for rowNum in range(0, numRows):
        for loopNo in range(0, loopCount):
            if loopNo * repeatCharAmount + rowNum < len(s):
                result = result + s[loopNo * repeatCharAmount + rowNum]
            if rowNum != 0 and repeatCharAmount != 2 * rowNum and (loopNo + 1) * repeatCharAmount - rowNum < len(s):
                result = result + s[(loopNo + 1) * repeatCharAmount - rowNum]
    return result

print(convert('PAYPALISHIRING', 3))

