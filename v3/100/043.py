#!/usr/bin/python3

def multiply(num1, num2):

    def a(num1, num2):
        if len(num1) > len(num2):
            num2 = '0' * (len(num1) - len(num2)) + num2
        else:
            num1 = '0' * (len(num2) - len(num1)) + num1

        tmp = []
        i, carry = len(num1) - 1, 0
        while i >= 0:
            s = int(num1[i]) + int(num2[i]) + carry
            carry = s // 10
            tmp.append(str(s % 10))
            i -= 1
        if carry != 0:
            tmp.append(str(carry))

        return ''.join(reversed(tmp))
        
    def m(num, digit):
        if digit == '0':
            return '0'

        tmp = []
        carry, n1, i = 0, int(digit), len(num) - 1
        while i >= 0:
            n2 = int(num[i])
            p = n1 * n2 + carry
            tmp.append(str(p % 10))
            carry = p // 10
            i -= 1
        if carry != 0:
            tmp.append(str(carry))
        return ''.join(reversed(tmp))
        
    
    rev = '0'
    for i in range(len(num1)):
        digit = num1[i]
        rev = a(rev, m(num2, digit) + '0' * (len(num1) - i - 1))
    i = 0
    while i < len(rev) - 1 and rev[i] == '0':
        i += 1

    return rev[i:]

if __name__ == '__main__':
    assert multiply('2', '3') == '6'
    assert multiply('123', '456') == '56088'
