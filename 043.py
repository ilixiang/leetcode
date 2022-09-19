#!/usr/bin/python3

def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'

    singleDigitProducts = [None] * 10
    singleDigitProducts[0] = '0'
    rev = '0'
    for i in range(len(num1) - 1, -1, -1):
        c = num1[i]
        intC = int(c)
        if singleDigitProducts[intC] == None:
            singleDigitProducts[intC] = multiplyWithSingleDigit(c, num2)
        tmp = singleDigitProducts[intC]
        rev = add(rev, tmp + '0' * (len(num1) - 1 - i))
    return rev

def multiplyWithSingleDigit(c, num):
    carry = 0
    rev = ''
    for i in range(len(num) - 1, -1, -1):
        tmp = int(c) * int(num[i]) + carry
        carry = tmp // 10
        rev = str(tmp % 10) + rev
    if carry != 0:
        rev = str(carry) + rev
    return rev

def add(num1, num2):
    carry = 0
    i1 = len(num1) - 1
    i2 = len(num2) - 1
    rev = ''
    while i1 >= 0 and i2 >= 0:
        c1 = num1[i1]
        c2 = num2[i2]
        tmp = int(c1) + int(c2) + carry
        carry = tmp // 10
        rev = str(tmp % 10) + rev
        i1 = i1 - 1
        i2 = i2 - 1

    while i1 >= 0:
         c1 = num1[i1]
         tmp = int(c1) + carry
         carry = tmp // 10
         rev = str(tmp % 10) + rev
         i1 = i1 - 1

    while i2 >= 0:
         c2 = num2[i2]
         tmp = int(c2) + carry
         carry = tmp // 10
         rev = str(tmp % 10) + rev
         i2 = i2 - 1

    if carry != 0:
        rev = str(carry) + rev
    return rev

print(multiply('2', '3'))
print(multiply('123', '456'))

