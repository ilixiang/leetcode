#!/usr/bin/python3

def strStr(haystack, needle):
    lps = [0 for i in range(len(needle) + 1)]

    # initialize lps, index is substring length
    for i in range(2, len(needle) + 1):
        prevLongestPrefix = lps[i - 1]
        if needle[i - 1] == needle[prevLongestPrefix]:
            lps[i] = prevLongestPrefix + 1
        else:
            for length in range(prevLongestPrefix, 0, -1):
                if needle[:length] == needle[i - length:i]:
                    lps[i] = length
                    break
    
    i = j = 0
    while i < len(haystack):
        while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
            i += 1
            j += 1
        if j == len(needle):
            return i - len(needle)
        
        if j == 0:
            i += 1
        else:
            j = lps[j]
    return -1

if __name__ == '__main__':
    assert strStr('sadbutsad', 'sad') == 0
    assert strStr('leetcode', 'leeto') == -1
    assert strStr('aabaaabaaac', 'aabaaac') == 4
