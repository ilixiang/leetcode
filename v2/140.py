#!/usr/bin/python3

def wordBreak(s, words):
    m = len(s)
    lookup = set(words)
    dp = [None] * m

    def wordBreakDp(i):
        if i == m:
            return [[]]
        
        if dp[i] != None:
            return dp[i]
        
        j = i + 1
        revs = []
        while j <= m:
            word = s[i:j]
            if word in lookup:
                nextRevs = wordBreakDp(j)
                for nextRev in nextRevs:
                    rev = [word]
                    rev.extend(nextRev)
                    revs.append(rev)
            j += 1
        dp[i] = revs
        return revs
    
    revs = wordBreakDp(0)
    return list(map(lambda x: ' '.join(x), revs))

