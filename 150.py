#!/usr/bin/python3

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            subtrahend = stack.pop()
            minuend = stack.pop()
            stack.append(minuend - subtrahend)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            divisor = stack.pop()
            dividend = stack.pop()
            positive = (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0)
            stack.append((1 if positive else -1) * (abs(dividend) // abs(divisor)))
        else:
            stack.append(int(token))
    return stack.pop()

print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

