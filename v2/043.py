#!/usr/bin/python3

def multiply(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    
    tmp = []
    carry = 0
    res = ''
    for n1 in num1:
        if n1 == 0 and res != '':
            res += '0'
            continue
        n1 = int(n1)
        i = len(num2) - 1
        while i >= 0:
            n2 = int(num2[i])
            n = n1 * n2 + carry
            carry = n // 10
            tmp.append(str(n % 10))
        if carry != 0:
            tmp.append(str(carry))
            carry = 0
        tmp.reverse()
        digitProduct = ''.join(tmp)
        tmp.clear()
        res += '0'
        r = len(res) - 1
        p = len(digitProduct) - 1
        while r >= 0 and p >= 0:
            s = int(res[r]) + int(digitProduct[p]) + carry
            tmp.append(str(s % 10))
            carry = s // 10
            r -= 1
            p -= 1
        
        while r >= 0:
            s = int(res[r]) + carry
            tmp.append(str(s % 10))
            carry = s // 10
            r -= 1
        
        while p >= 0:
            s = int(digitProduct[p]) + carry
            tmp.append(str(s % 10))
            carry = s // 10
            p -= 1

        if carry != 0:
            tmp.append(str(carry))
            carry = 0
        
        tmp.reverse()
        res = ''.join(tmp)
        tmp.clear()
    return res
