#!/usr/bin/python3

def diffWaysToCompute(expression):
    symbols = []
    nums = []
    left = right = 0
    while right < len(expression):
        if not expression[right].isdigit():
            symbols.append(expression[right])
            nums.append(int(expression[left:right]))
            left = right + 1
        right += 1
    nums.append(int(expression[left:right]))

    cache = [[None for j in range(len(nums))] for i in range(len(nums))]
    def dp(start, end):
        cachedRev = cache[start][end]
        if cachedRev != None:
            return cachedRev
        
        if start == end:
            cache[start][end] = cachedRev = [nums[start]]
            return cachedRev
        
        cachedRev = []
        for mid in range(start, end):
            leftRevs = dp(start, mid)
            rightRevs = dp(mid + 1, end)
            operator = symbols[mid]
            for left in leftRevs:
                for right in rightRevs:
                    if operator == '+':
                        cachedRev.append(left + right)
                    elif operator == '-':
                        cachedRev.append(left - right)
                    else:
                        cachedRev.append(left * right)
        cache[start][end] = cachedRev
        return cachedRev
    return dp(0, len(nums) - 1)
