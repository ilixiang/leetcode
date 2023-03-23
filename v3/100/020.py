#!/usr/bin/python3

def isValid(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            
            d = stack.pop()
            if (c == ')' and d != '(') or (c == ']' and d != '[') or (c == '}' and d != '{'):
                return False
    return len(stack) == 0
