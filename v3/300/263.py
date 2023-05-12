#!/usr/bin/python3

def isUgly(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 == 0:
            n //= n
            continue

        if n % 3 == 0:
            n //= 3
            continue
    
        if n % 5 == 0:
            n //= 5
            continue
        
        return False
    return True
