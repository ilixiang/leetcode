#!/usr/bin/python3

def decodeString(s):

    def recursive(sIndex):
        left = sIndex
        right = sIndex
        
        tmp = []
        while right < len(s) and s[right] != ']':
            left = right
            while right < len(s) and s[right].isalpha():
                right += 1
            tmp.append(s[left:right])
            if right == len(s) or s[right] == ']':
                break

            left = right
            while right < len(s) and s[right].isnumeric():
                right += 1
            number = int(s[left:right])
            # s[right] == '['
            (nestedStr, nextIndex) = recursive(right + 1)
            for i in range(0, number):
                tmp.append(nestedStr)
            right = nextIndex + 1
        return (''.join(tmp), right)
    return recursive(0)[0]
