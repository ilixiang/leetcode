#!/usr/bin/python3

def integerBreak(n):
    caches = [None] * (n + 1)

    def dp(n):
        if n == 1:
            return n
        cache = caches[n]
        if cache != None:
            return cache
        cache = 0
        for i in range(1, n // 2 + 1):
            cache = max(cache, i * (n - i), dp(i) * (n - i),
                        i * dp(n - i), dp(i) * dp(n - i))
        caches[n] = cache
        return cache
    return dp(n)
