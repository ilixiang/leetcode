#!/usr/bin/python3

def lengthOfLastWord(s):
    i = len(s) - 1
    rev = 0
    while i >= 0 and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        i -= 1
        rev += 1
    return rev
