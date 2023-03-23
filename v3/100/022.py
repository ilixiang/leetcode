#!/usr/bin/python3

def generateParenthesis(n):
    tmp = []
    rev = []
    def generate(left, right):
        if right == 0:
            rev.append(''.join(tmp))
            return

        if left == right or left != 0:
            tmp.append('(')
            generate(left - 1, right)
            tmp.pop()
            
        if left != right:
            tmp.append(')')
            generate(left, right - 1)
            tmp.pop()
        
    generate(n, n)
    return rev



