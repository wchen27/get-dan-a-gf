import math
import random
from cmath import inf

POPULATION = 500
CLONES = 50
TOURNEY_SIZE = 50
WIN_PROB = .75
MUTATION_RATE = .8

def numSpaces(board):
    return board.count("0")

def dist(board):
    return (3-board.index(largest(board))%3)**2 + (board.index(largest(board)//4))**2

def largest(board):
    return max(board)

def moveUp(board):
    newBoard = 
    return ()
def moveDown(board):

def moveRight(board):

def moveLeft(board):        

def nextBoards(board):
    boards = []
    boards.append(moveUp(board))
    boards.append(moveDown(board))
    boards.append(moveRight(board))
    boards.append(moveLeft(board))
    return boards

def heuritic(board,strategy,points):
    a,b,c,d = strategy
    score = 0
    score += a*largest(board)
    score += b*numSpaces(board)
    score += c*dist(board)
    score += d*points
    return score

def playGame(strategy):
    board = " "*200
    points = 0
    best = ""
    pointsGained = 0
    while board != "over":
        maxScore = -inf
        for curr in nextBoards(board):
            (currBoard, pointsGained) = curr
            if currBoard == "over":
                continue
            currH = heuristic(currBoard,strategy,pointsGained)
            if currH>maxScore:
                maxScore = currH
                best = currBoard
                bestPoints = pointsGained
        if board == best:
            board = "over"
        else:
            board = best
            points += pointsGained
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


gen = []
g = 0
gen = getPopulation(POPULATION)
while True:
    genDict = printGen(gen,g)
    gen = getNextGen(genDict) 
    g+=1
