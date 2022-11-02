#!/usr/bin/python3

def romanToInt(s):
    symbols = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
    index = 0
    result = 0
    symbolIndex = 0
    while index < len(s):
        while symbolIndex < len(symbols):
            symbol = symbols[symbolIndex]
            i = 0
            while i < len(symbol[0]) and index + i < len(s) and symbol[0][i] == s[index + i]:
                i = i + 1
            if i == len(symbol[0]):
                index = index + len(symbol[0])
                result = result + symbol[1]
                break
            symbolIndex = symbolIndex + 1
    return result

print(romanToInt('III'))
print(romanToInt('LVIII'))
                    

