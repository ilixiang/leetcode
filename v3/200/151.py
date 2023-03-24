#!/usr/bin/python3

def reverseWords(s):
    words = s.split(' ')
    words.reverse()
    return ' '.join(filter(lambda x: x != '', words))
