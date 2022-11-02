#!/usr/bin/python3

def isValid(s):
    if len(s) % 2 == 1:
        return False
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif c == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        else:
            if len(stack) == 0 or stack.pop() != '{':
                return False
    return len(stack) == 0

print(isValid('()'))

