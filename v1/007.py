#!/usr/bin/python3

def reverse(x):
    maxInt = 2 ** 31
    minInt = -1 * 2 ** 31 - 1
    quotient = x if x > 0 else -1 * x
    remainders = []
    while quotient != 0:
        remainders.append(quotient % 10)
        quotient = quotient // 10

    result = 0
    for i in range(0, len(remainders)):
        if (maxInt - remainders[i]) // 10 < result:
            return 0
        result = result * 10 + remainders[i]

    return result if x > 0 else -1 * result

print(reverse(321))
print(reverse(-321))

