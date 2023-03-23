#!/usr/bin/python3

def isScramble(s1, s2):
    m = len(s1)
    dp = {}
    def isScrambleDp(i, j, x, y):
        key = '%d:%d:%d:%d'%(i, j, x, y)
        rev = dp.get(key, None)
        if rev != None:
            return rev

        m1 = {}
        for k in range(i, j):
            m1[s1[k]] = m1.get(s1[k], 0) + 1
        for k in range(x, y):
            c = m1.get(s2[k], 0)
            if c == 0:
                dp[key] = False
                return False
            m1[s2[k]] = c - 1
        
        if s1[i:j] == s2[x:y]:
            dp[key] = True
            return True
        else:
            for d in range(i + 1, j):
                if (isScrambleDp(i, d, x, x + d - i) and isScrambleDp(d, j, y + d - j, y))\
                    or (isScrambleDp(i, d, y + i - d, y) and isScrambleDp(d, j, x, x + j - d)):
                    dp[key] = True
                    return True
        dp[key] = False
        return False
    return isScrambleDp(0, m, 0, m)
