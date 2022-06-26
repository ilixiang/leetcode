#!/usr/bin/python3

def restoreIpAddress(s):
    result = []
    tmp = [None] * 4
    restoreIpAddressRecursive(s, 4, 0, tmp, result)
    return result

def restoreIpAddressRecursive(s, remains, start, tmp, result):
    if remains == 0 and start == len(s):
        result.append('.'.join(tmp))
        return

    if remains == 0 or start == len(s):
        return

    tmp[4 - remains] = s[start]
    restoreIpAddressRecursive(s, remains - 1, start + 1, tmp, result)
    if s[start] != '0':
        if start + 1 < len(s):
            tmp[4 - remains] = s[start: start + 2]
            restoreIpAddressRecursive(s, remains - 1, start + 2, tmp, result)
        if start + 2 < len(s) and int(s[start: start + 3]) <= 255:
            tmp[4 - remains] = s[start: start + 3]
            restoreIpAddressRecursive(s, remains - 1, start + 3, tmp, result)
            
print(restoreIpAddress('25525511135'))
print(restoreIpAddress('0000'))
print(restoreIpAddress('101023'))

