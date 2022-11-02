#!/usr/bin/python3

def lengthOfLastWord(s):
    index = len(s) - 1
    while s[index] == ' ':
        index = index - 1
    end = index
    while s[index] != ' ' and 0 <= index:
        index = index - 1
    begin = index

    return end - begin

print(lengthOfLastWord('Hello World'))
print(lengthOfLastWord('   fly me   to   the moon  '))
print(lengthOfLastWord('a'))

