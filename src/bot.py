from logic import get_possible_moves, gameOver, playerUpdate, getLastPieceIndex
import random
import time

class Node:
    def __init__(self, state, score):
        self.children = []
        self.state = state
        self.score = score
        

    def getBestMove(self, player):
        if (player == 1):
            max = -10000
            for i in range(len(self.children)):
                (move, min) = self.children[i].getMin()
                if (min > max):
                    moveToPlay = move
                    max = min
                """ elif (min == max and bool(random.randrange(0, 2))):
                    moveToPlay = move
                    max = min """
            return (moveToPlay, max)
        elif (player == 2):
            min = 10000
            for i in range(len(self.children)):
                (move, max) = self.children[i].getMax()
                if (max < min):
                    moveToPlay = move
                    min = max
                """ elif (max == min and bool(random.randrange(0, 2))):
                    moveToPlay = move
                    min = max """
            return (moveToPlay, min)

    def getMax(self):
        max = -10000
        if(len(self.children) == 0):
            return (self.state, self.score)
        for i in range(len(self.children)):
            min = self.children[i].getMin()[1]
            if (min > max):
                moveToPlay = self.state
                max = min
        return (moveToPlay, max)


    def getMin(self):
        min = 10000
        if(len(self.children) == 0):
            return (self.state, self.score)
        for i in range(len(self.children)):
            max = self.children[i].getMax()[1]
            if (max < min):
                moveToPlay = self.state
                min = max
        return (moveToPlay, min)


 
    def addChildren(self, depth, player):
        depth -= 1
        if (depth != 0):
            if (player == 1):
                possible_moves = get_possible_moves(self.state, "black")
            else:
                possible_moves = get_possible_moves(self.state, "white")
            
            for i in range(len(possible_moves)):
                tempArray = self.state[:]
                index = tempArray.index(possible_moves[i][0])
                tempArray[index] = possible_moves[i][1]
                tempScore = adjacentHeuristic(tempArray) # TODO
                if (gameOver(tempArray, index)):
                    if (player == 1):
                        tempScore = 999 + depth
                    else:
                        tempScore = -999 - depth
                    newNode = Node(tempArray, tempScore)
                    self.children.append(newNode)
                else:
                    newNode = Node(tempArray, tempScore)
                    self.children.append(newNode)
                    newNode.addChildren(depth, playerUpdate(player))


    def __eq__(self, node):
        return self.state == node.state

    def printTree(self, spaces):
        for n in range(spaces):
            print("   ", end = "")
        print(self.state + " " + str(self.score))
        #print(str(self.score))
        for i in range(len(self.children)):
            self.children[i].printTree(spaces + 1)

""" 
def generateTree():
    

for possible_moves:
    root.addChildren(possible_move, 3)
"""


# Heuristic that considers the amount of adjacent pieces of a given player and the same for the other player, subtracting them
def adjacentHeuristic(pieces):
    myScore = getNumAdjacents(pieces, 1)
    opponentScore = getNumAdjacents(pieces, 2)
    score = myScore - opponentScore
    return score
        
def getNumAdjacents(pieces, player):
    num = 0
    if(player == 1):
        if(isAdjacent(pieces[0], pieces[1])): 
            num += 1
        if(isAdjacent(pieces[0], pieces[2])): 
            num += 1
        if(isAdjacent(pieces[1], pieces[2])): 
            num += 1
    else:
        if(isAdjacent(pieces[3], pieces[4])): 
            num += 1
        if(isAdjacent(pieces[3], pieces[5])): 
            num += 1
        if(isAdjacent(pieces[4], pieces[5])): 
            num += 1
    return num



def isAdjacent(piece1, piece2):
    # Horizontal
    if ( (piece1[0] - 1 == piece2[0]) and (piece1[1] == piece2[1]) ):
        return True
    if ( (piece1[0] + 1 == piece2[0]) and (piece1[1] == piece2[1]) ):
        return True
    
    # Vertical
    if( (piece1[0] == piece2[0]) and (piece1[1] == piece2[1] - 1) ):
        return True
    if( (piece1[0] == piece2[0]) and (piece1[1] == piece2[1] + 1) ):
        return True

    # Diagonal
    if( (piece1[0] + 1 == piece2[0]) and (piece1[1] + 1 == piece2[1]) ):
        return True
    if( (piece1[0] - 1 == piece2[0]) and (piece1[1] - 1 == piece2[1]) ):
        return True
    if( (piece1[0] + 1 == piece2[0]) and (piece1[1] - 1 == piece2[1]) ):
        return True
    if( (piece1[0] - 1 == piece2[0]) and (piece1[1] + 1 == piece2[1]) ):
        return True
    return False

def choose_move_adjacent(pieces, player):

    #root = Node(pieces, 0) ################################################################
    
    if (player == 1):
        possible_moves = get_possible_moves(pieces, "black")
        score = -4 # Worse possible score
        indexMove = 0

        for i in range(len(possible_moves)):
            tempArray = pieces[:] # Copy by value
            index = tempArray.index(possible_moves[i][0])
            tempArray[index] = possible_moves[i][1]
            tempScore = adjacentHeuristic(tempArray)
            if (tempScore > score):
                score = tempScore
                indexMove = i
            if (gameOver(tempArray, index)): # Best possible score
                score = tempScore
                indexMove = i
                break
        pieces[pieces.index(possible_moves[indexMove][0])] = possible_moves[indexMove][1]
    else:
        possible_moves = get_possible_moves(pieces, "white")
        score = 4 # Worse possible score
        indexMove = 0

        for i in range(len(possible_moves)):
            tempArray = pieces[:]
            index = tempArray.index(possible_moves[i][0])
            tempArray[index] = possible_moves[i][1]
            tempScore = adjacentHeuristic(tempArray)
            if (tempScore < score):
                score = tempScore
                indexMove = i
            if (gameOver(tempArray, index)): # Best possible score
                score = tempScore
                indexMove = i
                break
        pieces[pieces.index(possible_moves[indexMove][0])] = possible_moves[indexMove][1]

    print(score)
    return pieces.index(possible_moves[indexMove][1])

def choose_move_minimax(pieces, depth, heuristic, player):

    tempPieces = pieces[:]

    root = Node(pieces, heuristic(pieces))
    #print(root)
    root.addChildren(depth, player)

    (pieces, var) = root.getBestMove(player)
    print(var)
    

    return (pieces, getLastPieceIndex(tempPieces, pieces))

def minimax(possible_move, depth, player, checker, abCuts):
    value = None
    pieces = None
    depth -= 1
    if (depth == 0): # Base case
        return (adjacentHeuristic(possible_move), possible_move)
    else:
        if (player == 1):
            possible_moves = get_possible_moves(possible_move, "black")
        else:
            possible_moves = get_possible_moves(possible_move, "white")


        for i in range(len(possible_moves)):

            # Setup
            tempArray = possible_move[:]
            index = tempArray.index(possible_moves[i][0])
            tempArray[index] = possible_moves[i][1]

            if (gameOver(tempArray, index)):
                if (player == 1):
                    tempScore = 999 + depth
                    return (tempScore, tempArray)
                else:
                    tempScore = -999 - depth
                    return (tempScore, tempArray)

            if(player == 1):
                (tempValue, tempPieces) = minimax(tempArray, depth, 2, value, abCuts)
            else:
                (tempValue, tempPieces) = minimax(tempArray, depth, 1, value, abCuts)

            # Minimax Backtracking Algorithm

            if (value == None):
                #print("New Node")
                value = tempValue
                pieces = tempArray

            if (player == 1 and tempValue > value):
                value = tempValue
                pieces = tempArray
                #print(player, depth, value, pieces)           
            elif (abCuts and checker != None and player == 1 and value >= checker):
                return (value, pieces) 
        
            if (player == 2 and tempValue < value):
                value = tempValue
                pieces = tempArray
                #print(player, depth, value, pieces)     
            elif (abCuts and checker != None and player == 2 and value <= checker):
                return (value, pieces) 

        return (value, pieces)

#start = time.time()

print(minimax([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)], 6, 1, None, True))

#end = time.time()
#print(end - start)

#root = Node([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)], adjacentHeuristic([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)]))
#root.addChildren(7, 1)
#print(root.getBestMove(1))

  