#!/usr/bin/python3

def simplifyPath(path):
    i = 0
    stack = []
    while i < len(path):
        i += 1
        start = i
        while i < len(path) and path[i] != '/':
            i += 1
        if i != start:
            dir = path[start: i]
            if dir == '..' and len(stack) != 0:
                stack.pop()
            elif dir != '.':
                stack.push(dir)
    return '/' + '/'.join(stack)
