#!/usr/bin/python3

def addDigits(num):
    def recursive(n):
        if n // 10 == 0:
            return n
        
        nextN = 0
        while n != 0:
            nextN += n % 10
            n //= 10
        return recursive(nextN)
    return recursive(num)
