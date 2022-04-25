#!/usr/bin/python3

def lengthOfLongestSubstring(s):
    if not s:
        return 0

    begin = 0
    end = 1
    maxLen = 1
    while end != len(s):
        c = s[end]
        print(s[begin: end] + ' => ' + c)
        existedIndex = s[begin: end].find(c)
        if existedIndex != -1:
            tmpLen = end - begin
            maxLen = tmpLen if tmpLen > maxLen else maxLen
            begin = begin + existedIndex + 1
        end = end + 1
    tmpLen = end - begin
    maxLen = tmpLen if tmpLen > maxLen else maxLen
    return maxLen

print(lengthOfLongestSubstring('abcabcbb'))

