#!/usr/bin/python3

def remoeKdigits(num, k):
    digits = [int(c) for c in num]

    deque = []
    rev = 0
    for i in range(0, len(digits)):
        digit = digits[i]
        while len(deque) != 0 and digits[deque[-1]] > digit:
            deque.pop()
        deque.append(i)
        if i >= k:
            rev = rev * 10 + digits[deque.pop(0)]
    
    return str(rev)
