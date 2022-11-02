#!/usr/bin/python3

def fractionToDecimal(numerator, denominator):
    positive = (numerator >= 0 and denominator >= 0) or (numerator <= 0 and denominator <= 0)
    numerator = abs(numerator)
    denominator = abs(denominator)
    intPart = numerator // denominator

    remainderMap = {}
    decimalParts = []
    remainder = numerator % denominator
    if remainder == 0:
        return ('' if positive else '-') + str(intPart)

    decimalIndex = 0
    while remainder != 0 and not remainder in remainderMap:
        remainderMap[remainder] = decimalIndex
        decimalIndex = decimalIndex + 1
        decimalParts.append(remainder * 10 // denominator)
        remainder = (remainder * 10) % denominator
    if remainder == 0:
        return ('' if positive else '-') + str(intPart) + '.' + ''.join(map(lambda x: str(x), decimalParts))
    else:
        recurringIndex = remainderMap[remainder]
        return ('' if positive else '-') + str(intPart) + '.' + ''.join(map(lambda x: str(x), decimalParts[0: recurringIndex])) + '(' + ''.join(map(lambda x: str(x), decimalParts[recurringIndex:])) + ')'

print(fractionToDecimal(4, 7))
print(fractionToDecimal(1, 2))
print(fractionToDecimal(1, 9))
print(fractionToDecimal(1, 99))
print(fractionToDecimal(1, 6))
print(fractionToDecimal(-1, 6))

