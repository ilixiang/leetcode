#!/usr/bin/python3

def intToRoman(num):
    transforms = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    arr = []
    index = 0
    while num != 0 and index < len(transforms):
        quotient = num // transforms[index][0]
        num = num % transforms[index][0]
        arr.extend([transforms[index][1]] * quotient)
        index = index + 1
    return ''.join(arr)

print(intToRoman(3))
print(intToRoman(58))
print(intToRoman(1994))

