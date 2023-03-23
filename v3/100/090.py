#!/usr/bin/python3

def subsetsWithDup(nums):
    nums.sort()
    m = len(nums)

    rev = []
    def combination(tmp, start, pos, n):
        if pos == n:
            rev.append(list(tmp))
            return

        i = start
        while i < m - n + pos + 1:
            if i != start and nums[i] == nums[i - 1]:
                i += 1
                continue
            tmp[pos] = nums[i]
            combination(tmp, i + 1, pos + 1, n)
            i += 1

    for i in range(0, len(nums) + 1):
        tmp = [0] * i
        combination(tmp, 0, 0, i)
    return rev
