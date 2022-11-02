#!/usr/bin/python3

def isValid(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if len(stack) == 0\
                or (c == ')' and stack.pop() != '(')\
                or (c == ']' and stack.pop() != '[')\
                or (c == '}' and stack.pop() != '{'):
                return False
    return len(stack) == 0
