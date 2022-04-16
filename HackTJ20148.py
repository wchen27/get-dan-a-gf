from random import randint, random

board = [None] * 16
score = 4
m = 2

def toList(board):
    return [board[:4], board[4:8], board[8:12], board[12:16]]

def toBoard(l):
    return l[0] + l[1] + l[2] + l[3]

def checkSpot(space):
    if board[space] == None:
        return True
    return False

def spawn():
    count = 0
    while count < randint(1, 2):
        space = randint(0, 15)
        if checkSpot(space):
            if random() < 0.9:
                board[space] = 2
            else:
                board[space] = 4
            count += 1

def updateNums():
    temp = 0
    for i in range(16):
        if board[i] != None:
            temp = max(temp, board[i])

def moveLeft(board):
    add = 0
    arr = toList(board)
    for r in range(4):
        for c in range(4):
            if arr[r][c-1] == arr[r][c]:
                arr[r][c-1] *= 2
                arr[r][c] = None
                add += arr[r][c-1]
            if arr[r][c-1] == None:
                arr[r][c-1] = arr[r][c]
                arr[r][c] = None
    return toBoard(arr), add

def moveRight(board):
    arr = toList(board)
    for r in range(4):
        add = 0
        for c in range(4):
            if arr[r][c+1] == 0:
                arr[r][c+1] = arr[r][c]
                arr[r][c] = None
            if arr[r][c+1] == arr[r][c]:
                arr[r][c+1] *= 2
                arr[r][c] = None
                add += arr[r][c+1]
    return toBoard(arr), add

def moveUp(board):
    arr = toList(board)
    add = 0
    for c in range(4):
        for r in range(4):
            if arr[r-1][c] == 0:
                arr[r-1][c] = arr[r][c]
                arr[r][c] = None
            if arr[r-1][c] == arr[r][c]:
                arr[r-1][c] *= 2
                arr[r][c] = None
                add += arr[r-1][c]
    return toBoard(arr), add

def moveDown(board):
    arr = toList(board)
    add = 0
    for c in range(4):
        for r in range(4):
            if arr[r+1][c] == 0:
                arr[r+1][c] = arr[r][c]
                arr[r][c] = None
            if arr[r+1][c] == arr[r][c]:
                arr[r+1][c] *= 2
                arr[r][c] = None
                add += arr[r+1][c]
    return toBoard(arr), add

