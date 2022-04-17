import math
import random
from cmath import inf
from random import randint

POPULATION = 500
CLONES = 50
TOURNEY_SIZE = 50
WIN_PROB = .75
MUTATION_RATE = .8

def printBoard(board):
    for i in range(4):
        print(board[i*4:i*4+4])

def checkSpot(board,x):
    if board[x] == 0:
        return True
    return False

def spawn(board,n):
    if 0 not in board:
        return board
    count = 0
    while count != n:
        x = randint(0, 15)
        if checkSpot(board,x):
            if random.random() < 0.9:
                board[x]= 2
            else:
                board[x] = 4
            count += 1
    return board

def numSpaces(board):
    return board.count(0)

def dist(board):
    return (3-board.index(largest(board))%3)**5 + (board.index(largest(board))//4)**5

def largest(board):
    return max(board)

def moveUp(board):
    add = 0
    old = board.copy()
    for x in range(16):
        x= 0
    if board != old:
        board = spawn(board,1)
    return (board, add)

def moveDown(board):
    add = 0
    old = board.copy()
    for x in range(16):
        if x+4 <= 15:
            if board[x+4] == 0:
                board[x+4] = board[x]
                board[x] = 0
            if board[x+4] == board[x]:
                board[x+4] *= 2
                board[x] = 0
                add += board[x+4]
    if board != old:
        board = spawn(board,1)
    return (board, add)

def moveRight(board):
    add = 0
    old = board.copy()
    for x in range(16):
        if x%4!=3:
            if board[x+1] == 0:
                board[x+1] = board[x]
                board[x] = 0
            if board[x+1] == board[x]:
                board[x+1] *= 2
                board[x] = 0
                add += board[x+1]
    if board != old:
        board = spawn(board,1)
    return (board, add)


def moveLeft(board):        
    add = 0
    old = board.copy()
    for x in range(16):
        if x-1 >= 0:
            if board[x-1] == 0:
                board[x-1] = board[x]
                board[x] = 0
            if board[x-1] == board[x]:
                board[x-1] *= 2
                board[x] = 0
                add += board[x-1]
    if board != old:
        board = spawn(board,1)
    return (board, add)

def isOver(board):
    temp = board.copy()
    up,b = moveUp(temp)
    down,b = moveDown(temp)
    right,c = moveRight(temp)
    left,d = moveLeft(temp)
    if up == down == right == left == board:
        return True
    if 2048 in board:
        return True
    return False

def nextBoards(board):
    boards = []
    boards.append(moveUp(board))
    boards.append(moveDown(board))
    boards.append(moveRight(board))
    boards.append(moveLeft(board))
    return boards

def heuristic(board,strategy,points):
    a,b,c,d = strategy
    score = 0
    score += a*largest(board)
    score += b*numSpaces(board)
    score += c*dist(board)
    score += d*points
    if 2048 in board:
        score+=100000000000000000
    return score

def newBoard():
    newBoard = []
    for i in range(16):
        newBoard.append(0)
    x = int(random.random()*16)
    newBoard[x] = 2
    while newBoard.count(2)==1:
        y = int(random.random()*4)
        newBoard[y] = 2
    return newBoard

def playGame(strategy):
    board = newBoard()
    points = 0
    best = ""
    pointsGained = 0
    while not isOver(board):
        maxScore = -inf
        for curr in nextBoards(board):
            (currBoard, pointsGained) = curr
            if isOver(currBoard):
                continue
            currH = heuristic(currBoard,strategy,pointsGained)
            if currH>maxScore:
                maxScore = currH
                best = currBoard
                bestPoints = pointsGained
        board = best
        points += bestPoints
    return points

def fitness(strategy):   
    scores = []
    for i in range(5):
        scores.append(playGame(strategy)) 
    return sum(scores)/5

def getPopulation(population):
    pop = []
    for i in range(population):
        a = random.random()*2-1
        b = random.random()*2-1
        c = random.random()*2-1
        d = random.random()*2-1
        pop.append((a,b,c,d))
    return pop

def printGen(gen,g):
    genDict = {}
    n = 1
    total = 0
    for i in range(POPULATION):
        score = fitness(gen[i])
        print("Gen. " + str(g) + ": " + str(n) + " --> " + str(score))
        n+=1
        genDict[gen[i]] = score
        total += score
    genDict = dict(sorted(genDict.items(), key=lambda x: x[1],reverse=True))
    first = list(genDict.keys())[0]
    print("Best stretegy: " + str(first))
    print("Best score: " + str(genDict[first]))
    print("Avg. score: " + str(total/POPULATION))
    return genDict

def getNextGen(genDict):
    nextGen = []
    i = 0
    for gi in genDict.keys():
        nextGen.append(gi)
        i+=1
        if i>CLONES:
            break

    while len(nextGen)<POPULATION:
        #Making tournament
        t1 = random.sample(gen,TOURNEY_SIZE)
        t2 = []
        while len(t2) < TOURNEY_SIZE:
            temp = random.choice(gen)    
            if temp not in t1: t2.append(temp)
        curr1 = {}
        for t in t1:
            curr1[t] = genDict[t]
        curr1 = dict(sorted(curr1.items(), key=lambda x: x[1],reverse=True))

        curr2 = {}
        for t in t2:
            curr2[t] = genDict[t]
        curr2 = dict(sorted(curr2.items(), key=lambda x: x[1],reverse=True))

        winner1 = []
        winner2 = []

        for t in curr1.keys():
            if random.random()<WIN_PROB:
                winner1 = t
                break
            winner1 = t

        for t in curr2.keys():
            if random.random()<WIN_PROB:
                winner2 = t
                break
            winner2 = t

        child = []

        index = int(random.random()*3)+1
        
        for x in range(index):
            child.append(winner1[x])
        
        for x in range(4-index):
            child.append(winner2[x+index])

        if random.random()<MUTATION_RATE:
            child[int(random.random()*3)+1] += random.random()*2

        if child not in nextGen:
            nextGen.append(tuple(child))
    return nextGen

gen = []
# g = 0
# gen = getPopulation(POPULATION)
# while True:
#     genDict = printGen(gen,g)
#     gen = getNextGen(genDict) 
#     g+=1

board = newBoard()
printBoard(board)
while not isOver(board):
    move = input("next move: ")
    if move == "right":
        board,a = moveRight(board)
    if move == "left":
        board,a = moveLeft(board)
    if move == "up":
        board,a = moveUp(board)
    if move == "down":
        board,a = moveDown(board)
    printBoard(board)
