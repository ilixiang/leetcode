#!/usr/bin/python3

def reverseBits(n):
    result = 0
    for i in range(0, 16):
        print('BIT %d => %d'%(i, ((1 << i) & n) >> i))
        result = result | (((1 << i) & n) << (31 - i - i))
        print('BIT %d => %d'%(31 - i, ((1 << (31 - i)) & n) >> (31 - i)))
        result = result | (((1 << (31 - i)) & n) >> (31 - i - i))
    return result

print(reverseBits(43261596))

