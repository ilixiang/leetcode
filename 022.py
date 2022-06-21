#!/usr/bin/python3

def generateParenthesis(n):
    arr = []
    result = []
    nextParenthesis(arr, n, n, result)
    return result
    
def nextParenthesis(arr, leftRemains, rightRemains, result):
    if leftRemains == 0 and rightRemains == 0:
        result.append(''.join(arr))
        return
    if rightRemains == leftRemains:
        arr.append('(')
        nextParenthesis(arr, leftRemains - 1, rightRemains, result)
        arr.pop()
    else:
        if leftRemains > 0:
            arr.append('(')
            nextParenthesis(arr, leftRemains - 1, rightRemains, result)
            arr.pop()

        if rightRemains > 0:
            arr.append(')')
            nextParenthesis(arr, leftRemains, rightRemains - 1, result)
            arr.pop()

print(generateParenthesis(3))

