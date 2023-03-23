#!/usr/bin/python3

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif token == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif token == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif token == '/':
            a = stack.pop()
            b = stack.pop()
            quotient = b // a
            if quotient < 0 and b % a != 0:
                quotient += 1
            stack.append(quotient)
        else:
            stack.append(int(token))
    return stack.pop()
