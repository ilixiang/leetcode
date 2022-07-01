#!/usr/bin/python3

def solve(board):
    bordAdjacent = set()
    maxRow = len(board)
    maxCol = len(board[0])
    for col in range(0, maxCol):
        if board[0][col] == 'O':
            bordAdjacent.add(col)
        if board[maxRow - 1][col] == 'O':
            bordAdjacent.add((maxRow - 1) * maxCol + col)
    for row in range(0, maxRow):
        if board[row][0] == 'O':
            bordAdjacent.add(row * maxCol)
        if board[row][maxCol - 1] == 'O':
            bordAdjacent.add(row * maxCol + maxCol - 1)
    print(bordAdjacent)

    queue = list(bordAdjacent)
    while len(queue) != 0:
        num = queue.pop(0)
        row = num // maxCol
        col = num % maxCol
        if row - 1 >= 0 and board[row - 1][col] == 'O' and not (num - maxCol) in bordAdjacent:
            queue.append(num - maxCol)
            bordAdjacent.add(num - maxCol)
        if col - 1 >= 0 and board[row][col - 1] == 'O' and not (num - 1) in bordAdjacent:
            queue.append(num - 1)
            bordAdjacent.add(num - 1)
        if row + 1 < maxRow and board[row + 1][col] == 'O' and not (num + maxCol) in bordAdjacent:
            queue.append(num + maxCol)
            bordAdjacent.add(num + maxCol)
        if col + 1 < maxCol and board[row][col + 1] == 'O' and not (num + 1) in bordAdjacent:
            queue.append(num + 1)
            bordAdjacent.add(num + 1)

    for row in range(0, maxRow):
        for col in range(0, maxCol):
            if not (row * maxCol + col) in bordAdjacent:
                board[row][col] = 'X'

board =  [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
solve(board)
print(board)

