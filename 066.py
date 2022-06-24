#!/usr/bin/python3

def plusOne(digits):
    length = len(digits)
    index = length - 1
    carry = 1
    while index >= 0 and carry == 1:
        s = digits[index] + carry
        digits[index] = s % 10
        carry = s // 10
        index = index - 1
    print(carry)
    if carry == 1:
        digits.insert(0, 1)
    return digits

print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9]))

