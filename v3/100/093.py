#!/usr/bin/python3

def restoreIpAddress(s):
    m = len(s)
    tmp = [''] * 4
    rev = []
    def recursive(n, i):
        if n == 4 and i == m:
            rev.append('.'.join(tmp))
            return

        if i == m or n == 4:
            return
        
        tmp[n] = s[i]
        recursive(n + 1, i + 1)

        if i < m - 1 and s[i] != '0':
            tmp[n] = s[i:i + 2]
            recursive(n + 1, i + 2)
        
        if i < m - 2 and (s[i] == '1' or (s[i] == '2' and int(s[i + 1:i + 3]) <= 55)):
            tmp[n] = s[i:i + 3]
            recursive(n + 1, i + 3)
    recursive(0, 0)
    return rev
