#!/usr/bin/python3

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            addend = stack.pop()
            augend = stack.pop()
            stack.append(augend + addend)
        elif token == '-':
            subtrahend = stack.pop()
            minuend = stack.pop()
            stack.append(minuend - subtrahend)
        elif token == '*':
            multiplier = stack.pop()
            multiplicant = stack.pop()
            stack.append(multiplicant * multiplier)
        elif token == '/':
            divisor = stack.pop()
            divident = stack.pop()
            if (divisor > 0 and divident < 0) or (divisor < 0 and divident > 0):
                quotient = divident // divisor
                if divident % divisor != 0:
                    quotient += 1
                stack.append(quotient)
            else:
                stack.append(divident // divisor)
        else:
            stack.append(int(token))
    return stack.pop()

