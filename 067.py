#!/usr/bin/python3

def addBinary(a, b):
    index = 0
    aLength = len(a)
    bLength = len(b)
    arr = []
    carry = 0
    while index < aLength or index < bLength:
        aNum = 1 if index < aLength and a[aLength - 1 - index] == '1' else 0
        bNum = 1 if index < bLength and b[bLength - 1 - index] == '1' else 0
        s = aNum + bNum + carry
        carry = s // 2
        arr.append(str(s % 2))
        index = index + 1

    if carry == 1:
        arr.append('1')

    print(arr)
    arr.reverse()
    return ''.join(arr)

print(addBinary('11', '1'))
print(addBinary('1010', '1011'))

