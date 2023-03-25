#!/usr/bin/python3

def fractionToDecimal(numerator, denominator):
    integer = numerator // denominator
    remainder = numerator % denominator
    if remainder == 0:
        return str(integer)
    
    positive = (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0)
    numerator = abs(numerator)
    denominator = abs(denominator)
    integer = numerator // denominator
    remainder = numerator % denominator

    decimalParts = []
    indexMap = {}
    index = 0
    while remainder != 0:
        remainderIndex = indexMap.get(remainder, None)
        if remainderIndex != None:
            return ('-' if not positive else '') + str(integer) + '.' + ''.join(decimalParts[:remainderIndex]) + '(' + ''.join(decimalParts[remainderIndex:]) + ')'
        indexMap[remainder] = index
        remainder *= 10
        decimalParts.append(str(remainder // denominator))
        remainder %= denominator
        index += 1
    return ('-' if not positive else '') + str(integer) + '.' + ''.join(decimalParts)
