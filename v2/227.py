#!/usr/bin/python3

def calculate(s):
    stack = []
    suffixExp = []

    left = right = 0
    while right < len(s):
        if s[right] == ' ':
            right += 1
            continue
        left = right

        # operand
        while right < len(s) and s[right].isnumeric():
            right += 1
        if right != left:
            suffixExp.append(s[left:right])
            continue

        # '('
        if s[right] == '(':
            stack.append('(')
            right += 1
            continue

        if s[right] == '+' or s[right] == '-':
            while len(stack) != 0 and stack[-1] != '(':
                suffixExp.append(stack.pop())
            stack.append(s[right])
            right += 1
            continue
        if s[right] == '*' or s[right] == '/':
            while len(stack) != 0 and (stack[-1] != '+' and stack[-1] != '-'):
                suffixExp.append(stack.pop())
            stack.append(s[right])
            right += 1
            continue
            
        if s[right] == ')':
            operator = stack.pop()
            while operator != '(':
                suffixExp.append(operator)
                operator = stack.pop()
            right += 1
            continue
    while len(stack) != 0:
        suffixExp.append(stack.pop())
    print(suffixExp)
    
    for token in suffixExp:
        if token.isnumeric():
            stack.append(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                stack.append(operand2 + operand1)
            elif token == '-':
                stack.append(operand2 - operand1)
            elif token == '*':
                stack.append(operand2 * operand1)
            else:
                stack.append(operand2 // operand1)
    
    return stack[0]

if __name__ == '__main__':
    print(calculate('14/3*2'))
