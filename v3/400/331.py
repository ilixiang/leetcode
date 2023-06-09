#!/usr/bin/python3

def isValidSerialization(preorder):
    if preorder == '' or preorder == '#':
        return True
    elements = preorder.split(',')
    if elements[0] == '#':
        return False
    idx = 1
    stack = ['L']
    while len(stack) != 0 and idx != len(elements):
        element = elements[idx]
        if element != '#':
            stack.append('L')
        else:
            while len(stack) != 0 and stack[-1] == 'R':
                stack.pop()
            if len(stack) != 0:
                stack.pop()
                stack.append('R')
        idx += 1
    return len(stack) == 0 and idx == len(elements)
