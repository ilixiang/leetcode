#!/usr/bin/python3

def isHappy(n):
    calced = set()
    def recursive(n):
        if n == 1:
            return True
        if n in calced:
            return False
        
        calced.add(n)
        nn = 0
        while n != 0:
            nn += (n % 10) ** 2
            n //= 10
        return recursive(nn)
    return recursive(n)
        