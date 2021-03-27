from logic import possible_moves_black, possible_moves_white, gameOver, playerUpdate

class Node:
    def __init__(self, state, score):
        self.children = []
        self.state = state
        self.score = score

    def getMax(self):
        print("GetMax")

    def getMin(self):
        print("GetMin")
 
    def addChildren(self, depth, player):
        depth -= 1
        if (depth != 0):
            if (player == 1):
                possible_moves = possible_moves_black(self.state)
            else:
                possible_moves = possible_moves_white(self.state)
            for i in range(len(possible_moves)):
                tempArray = self.state[:]
                index = tempArray.index(possible_moves[i][0])
                tempArray[index] = possible_moves[i][1]
                tempScore = adjacentHeuristic(tempArray)
                if (gameOver(tempArray, index)):
                    if (player == 1):
                        tempScore = 999
                    else:
                        tempScore = -999
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
        print(str(self.score))
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
        possible_moves = possible_moves_black(pieces)
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
        possible_moves = possible_moves_white(pieces)
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
