#!/usr/bin/python3

def simplifyPath(path):
    stack = []
    lastIndex = 0
    index = 0
    while index < len(path):
        while index < len(path) and path[index] == '/':
            index = index + 1
        beginIndex = index
        while index < len(path) and path[index] != '/':
            index = index + 1
        endIndex = index
        directory = path[beginIndex: endIndex]
        if directory == '.' or directory == '':
            pass
        elif directory == '..':
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(directory)
    return '/' + '/'.join(stack)

print(simplifyPath('/home/'))
print(simplifyPath('/../'))

