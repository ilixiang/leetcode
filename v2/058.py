#!/usr/bin/python3

def lengthOfLastWord(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    endIndex = i

    while i >= 0 and s[i] != ' ':
        i -= 1
    return endIndex - i
