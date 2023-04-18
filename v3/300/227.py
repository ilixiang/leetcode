#!/usr/bin/python3

def calculate(s):
    def resolveTokens(s):
        left = right = 0
        tokens = []
        while right < len(s):
            c = s[right]
            if not c.isdigit():
                if left != right:
                    tokens.append(s[left:right])
                if c != ' ':
                    tokens.append(c)
                left = right + 1
            right += 1
        if left != right:
            tokens.append(s[left:right])
        return tokens
    
    def basicCalculate(numStack, symbolStack):
        symbol = symbolStack.pop()
        num2 = numStack.pop()
        num1 = numStack.pop()
        if symbol == '+':
            numStack.append(num1 + num2)
        elif symbol == '-':
            numStack.append(num1 - num2)
        elif symbol == '*':
            numStack.append(num1 * num2)
        elif symbol == '/':
            numStack.append(num1 // num2)
        else:
            raise SyntaxError
    
    def calculateTokens(tokens):
        symbolStack = []
        numStack = []
        i = 0
        while i < len(tokens):
            print(numStack, symbolStack)
            token = tokens[i]
            if token == '+' or token == '-':
                while len(symbolStack) != 0:
                    basicCalculate(numStack, symbolStack)
                symbolStack.append(token)
            elif token == '*' or token == '/':
                while len(symbolStack) != 0 and (symbolStack[-1] == '*' or symbolStack[-1] == '/'):
                    basicCalculate(numStack, symbolStack)
                symbolStack.append(token)
            else:
                numStack.append(int(token))
            i += 1

        while len(symbolStack) != 0:
            basicCalculate(numStack, symbolStack)

        if len(numStack) != 1:
            raise SyntaxError
        return numStack[0]
    
    tokens = resolveTokens(s)
    return calculateTokens(tokens)
