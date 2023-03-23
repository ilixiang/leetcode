#!/usr/bin/python3

def simplifyPath(path):
    stack = []
    components = path.split('/')
    for component in components:
        if component == '..':
            if len(stack) != 0:
                stack.pop()
        elif component != '.' and component != '':
            stack.append(component)
    return '/' + '/'.join(stack)
