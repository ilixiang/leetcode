#!/usr/bin/python3

def myAtoi(s):
    negative = False
    positive = False
    chars = s.encode('ascii')
    result = 0

    startIndex = 0
    while startIndex < len(s) and chars[startIndex] == 32:
        startIndex = startIndex + 1
    if startIndex > len(s) - 1:
        return 0

    maxInt = 2 ** 31 - 1
    minInt = -1 * 2 ** 31
    maxIntQuotient = maxInt // 10
    maxIntRemainder = maxInt % 10
    minIntQuotient = minInt // 10
    minIntRemainder = minInt % 10
    for index in range(startIndex, len(s)):
        c = chars[index]
        if c == 43 and not (positive or negative):
            positive = True
        elif c == 45 and not (positive or negative):
            negative = True
        elif c >= 48 and c <= 57:
            num = c - 48
            if not (positive or negative):
                positive = True
            if positive:
                if maxIntQuotient < result or (maxIntQuotient == result and maxIntRemainder < num):
                    return maxInt
                result = result * 10 + num
            else:
                if minIntQuotient > result - 1 or (minIntQuotient == result - 1 and minIntRemainder > 10 - num):
                    return minInt
                result = result * 10 - c + 48
        else:
            return result
    return result

print(myAtoi('-42'))
print(myAtoi('    -42'))
print(myAtoi('4 2'))
print(myAtoi('-91283472332'))
print(myAtoi('-2147483649'))

