#!/usr/bin/python3

def countDigitOne(n):
    rev = 0
    k = 1
    while k <= n:
        rev += n // (10 * k) * k
        remain = n % (10 * k)
        if remain >= k * 2:
            rev += k
        elif remain >= k:
            rev += remain - k + 1
        k *= 10
    return rev

if __name__ == '__main__':
    print(countDigitOne(13))
