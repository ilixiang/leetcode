#!/usr/bin/python3

def permuteUnique(nums):
    used = 0
    rev = []
    tmp = [0 for i in range(len(nums))]
    def recursive(n):
        nonlocal used
        if n == len(nums):
            rev.append(list(tmp))
            return

        s = set(nums)
        for i in range(len(nums)):
            if (nums[i] in s) and (used & (1 << i) == 0):
                s.remove(nums[i])
                used |= (1 << i)
                tmp[n] = nums[i]
                recursive(n + 1)
                used &= ~(1 << i)
    
    recursive(0)
    return rev

if __name__ == '__main__':
    print(permuteUnique([1, 1, 2]))