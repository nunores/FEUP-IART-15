from logic import possible_moves_black, possible_moves_white


# Heuristic that considers the amount of adjacent pieces of a given player and the same for the other player, subtracting them
def adjacentHeuristic(pieces, player):
    if (player == 1):
        myScore = getNumAdjacents(pieces, 1)
        opponentScore = getNumAdjacents(pieces, 2)
        score = myScore - opponentScore
    else:
        myScore = getNumAdjacents(pieces, 2)
        opponentScore = getNumAdjacents(pieces, 1)
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
    
    if (player == 1):
        possible_moves = possible_moves_black(pieces)
        score = -4 # Worse possible score
        indexMove = 0

        for i in range(len(possible_moves) - 1):
            tempArray = pieces[:] # Copy by value
            index = tempArray.index(possible_moves[i][0])
            tempArray[index] = possible_moves[i][1]
            tempScore = adjacentHeuristic(tempArray, 1)
            if (tempScore > score):
                score = tempScore
                indexMove = i
            if (score == 3): # Best possible score
                break
        pieces[pieces.index(possible_moves[indexMove][0])] = possible_moves[indexMove][1]
    else:
        possible_moves = possible_moves_white(pieces)
        score = -4 # Worse possible score
        indexMove = 0

        for i in range(len(possible_moves) - 1):
            tempArray = pieces[:]
            index = tempArray.index(possible_moves[i][0])
            tempArray[index] = possible_moves[i][1]
            tempScore = adjacentHeuristic(tempArray, 2)
            if (tempScore > score):
                score = tempScore
                indexMove = i
            if (score == 3): # Best possible score
                break
        pieces[pieces.index(possible_moves[indexMove][0])] = possible_moves[indexMove][1]

    return pieces.index(possible_moves[indexMove][1])
