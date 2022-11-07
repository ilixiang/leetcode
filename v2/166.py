#!/usr/bin/python3

def fractionToDecimal(numerator, denominator):
    negative = (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0)
    numerator, denominator = abs(numerator), abs(denominator)
    integerPart = numerator // denominator

    numerator %= denominator
    if numerator == 0:
        return ('-' if negative else '') + str(integerPart)
    tmp = []
    if negative:
        tmp.append('-')
    tmp.append(str(integerPart))
    tmp.append('.')
    numeratorMap = {}
    decimalIndex = len(tmp)
    while numerator != 0 and not numerator in numeratorMap:
        numeratorMap[numerator] = decimalIndex
        numerator *= 10
        tmp.append(str(numerator // denominator))
        numerator %= denominator
        decimalIndex += 1
    
    if numerator == 0:
        return ''.join(tmp)
    
    cycleStartIndex = numeratorMap[numerator]
    return ''.join(tmp[:cycleStartIndex]) + '(' + ''.join(tmp[cycleStartIndex:]) + ')'

