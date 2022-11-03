#!/usr/bin/python3

def generateParenthesis(n):
    finished = []
    tmp = []
    generateParenthesisRecursive(finished, n, n, tmp)
    return finished

def generateParenthesisRecursive(finished, left, right, tmp):
    if right == 0:
        finished.append(''.join(tmp))
        return
    
    if left < right:
        tmp.append(')')
        generateParenthesisRecursive(finished, left, right - 1, tmp)
        tmp.pop()
    
    if left > 0:
        tmp.append('(')
        generateParenthesisRecursive(finished, left - 1, right, tmp)
        tmp.pop()

