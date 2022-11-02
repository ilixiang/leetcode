#!usr/bin/python3

def singleNumber(nums):
    rev = 0
    signBits = 0
    for i in range(0, 32):
        tmp = 0
        for num in nums:
            if num < 0:
                signBits += 1
                num = -num
            tmp += (num >> i) & 1
        rev = rev | ((tmp % 3) << i)
    return rev if (signBits % 3) == 0 else -rev

print(singleNumber([2, 2, 3, 2]))
print(singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))

