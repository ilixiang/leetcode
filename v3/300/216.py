#!/usr/bin/python3

def conbinationSumDp(k, n):
    cache = {}
    END_REV = [[]]
    EMPTY_REV = []

    def dp(start, pos, target):
        cachedRev = cache.get((start, pos, target), None)
        if cachedRev != None:
            return cachedRev
        
        if target == 0 and pos == k:
            return END_REV
        if pos >= k:
            return EMPTY_REV

        cachedRev = []
        for num in range(start, min(target + 1, 11 - k + pos)):
            for nextRev in dp(num + 1, pos + 1, target - num):
                cachedRev.append([num] + nextRev)
        cache[(start, pos, target)] = cachedRev
        return cachedRev
    return dp(1, 0, n)

def combinationSumRecursive(k, n):
    rev = []
    tmp = [0] * k
    def dfs(start, pos, target):
        if target == 0 and pos == k:
            rev.append(list(tmp))
            return
        
        if pos >= k:
            return
        
        for num in range(start, min(target + 1, 11 - k + pos)):
            tmp[pos] = num
            dfs(num + 1, pos + 1, target - num)
    dfs(1, 0, n)
    return rev
