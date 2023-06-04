#!/usr/bin/python3

def isAdditiveNumber(num):
    def recursive(left, right, start, idx):
        if idx == len(num):
            return start != 0
        
        s = left + right
        sStr = str(s)
        if not num[idx:].startswith(sStr):
            return False
        return recursive(right, s, start + len(str(left)), idx + len(sStr))

    for i in range(len(num) - 1):
        left = int(num[:i + 1])
        for j in range(i + 1, len(num)):
            right = int(num[i + 1:j + 1])
            if recursive(left, right, 0, j + 1):
                return True
            if num[i + 1] == '0':
                break
        if num[0] == '0':
            break
    return False
