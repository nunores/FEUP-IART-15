from logic import *
import copy
import random
import time

# Heuristic that considers the amount of adjacent pieces of a given player and the same for the other player, subtracting them
def adjacentHeuristic(pieces, queue):
    queue.appendleft(pieces)
    if (draw(queue)):
        return 0
    myScore = getNumAdjacents(pieces, 1)
    opponentScore = getNumAdjacents(pieces, 2)
    score = myScore - opponentScore
    return score

def adjacentBorderHeuristic(pieces, queue):
    queue.appendleft(pieces)
    if (draw(queue)):
        return 0
    myScore = getNumAdjacents(pieces, 1) + getNumPiecesBorder(pieces, 1)
    opponentScore = getNumAdjacents(pieces, 2) + getNumPiecesBorder(pieces, 2)
    score = myScore - opponentScore
    return score
    
def borderHeuristic(pieces, queue):
    queue.appendleft(pieces)
    if (draw(queue)):
        return 0
    myScore = getNumPiecesBorder(pieces, 1)
    opponentScore = getNumPiecesBorder(pieces, 2)
    score = myScore - opponentScore
    return score


def getNumPiecesBorder(pieces, player):
    num = 0
    if(player == 1):
        for i in range(0, 3):
            if((pieces[i][0] == 1) or (pieces[i][0] == 5)): 
                num += 0.15 #TODO Alterar isto
            if((pieces[i][1] == 1) or (pieces[i][1] == 5)): 
                num += 0.15
    else:
        for i in range(3, 6):
            if((pieces[i][0] == 1) or (pieces[i][0] == 5)): 
                num += 0.15
            if((pieces[i][1] == 1) or (pieces[i][1] == 5)): 
                num += 0.15
    return num
        
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

def choose_move_minimax(pieces, queue, depth, player, heuristic):

    tempPieces = pieces[:]

    (var, pieces) = minimax(pieces, queue, depth, player, None, True, heuristic)
    #print(pieces)
    print(var)
    

    return (pieces, getLastPieceIndex(tempPieces, pieces))

def minimax(possible_move, queue, depth, player, checker, abCuts, heuristic):
    value = None
    pieces = None
    depth -= 1
    if (depth == 0): # Base case
        return (heuristic(possible_move, queue), possible_move)
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
            
            tempQueue = copy.deepcopy(queue)
            tempQueue.appendleft(tempArray)

            if (draw(tempQueue)):
                return (0, tempArray)

            if (gameOver(tempArray, index)):
                if (player == 1):
                    tempScore = 999 + depth
                    return (tempScore, tempArray)
                else:
                    tempScore = -999 - depth
                    return (tempScore, tempArray)

            if(player == 1):
                (tempValue, tempPieces) = minimax(tempArray, tempQueue, depth, 2, value, abCuts, heuristic)
            else:
                (tempValue, tempPieces) = minimax(tempArray, tempQueue, depth, 1, value, abCuts, heuristic)

            # Minimax Backtracking Algorithm

            if (value == None):
                value = tempValue
                pieces = tempArray

            if (player == 1 and tempValue > value):
                value = tempValue
                pieces = tempArray
            elif (abCuts and checker != None and player == 1 and value >= checker):
                return (value, pieces) 
        
            if (player == 2 and tempValue < value):
                value = tempValue
                pieces = tempArray
            elif (abCuts and checker != None and player == 2 and value <= checker):
                return (value, pieces) 

        return (value, pieces)

#start = time.time()

#print(minimax([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)], 6, 1, None, True))

#end = time.time()
#print(end - start)

#root = Node([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)], adjacentHeuristic([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)]))
#root.addChildren(7, 1)
#print(root.getBestMove(1))

  