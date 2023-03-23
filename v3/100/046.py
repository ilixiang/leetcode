#!/usr/bin/python3

def permute(nums):
    used = 0
    rev = []
    tmp = [0 for i in range(len(nums))]
    def recursive(i):
        if i == len(nums):
            rev.append(list(tmp))
            return

        for j in range(len(nums)):
            nonlocal used
            if used & (1 << j) == 0:
                used |= (1 << j)
                tmp[i] = nums[j]
                recursive(i + 1)
                used &= ~(1 << j)
    
    recursive(0)
    return rev

if __name__ == '__main__':
    print(permute([1,2,3]))
