# Returns list with original position and possible end positions in every direction for every black piece
def possible_moves_black(pieces):
    result = []
    for piece in range(3):
        result.append((pieces[piece], move_right(pieces, pieces[piece])))
        result.append((pieces[piece], move_bot_right(pieces, pieces[piece])))
        result.append((pieces[piece], move_bot(pieces, pieces[piece])))
        result.append((pieces[piece], move_bot_left(pieces, pieces[piece])))
        result.append((pieces[piece], move_left(pieces, pieces[piece])))
        result.append((pieces[piece], move_top_left(pieces, pieces[piece])))
        result.append((pieces[piece], move_top(pieces, pieces[piece])))
        result.append((pieces[piece], move_top_right(pieces, pieces[piece])))
    for i in range(len(result) - 1, 0, -1): # Removes obsolete moves
        if (result[i][0] == result[i][1]):
            result.remove(result[i])
    return result

# Returns list with original position and possible end positions in every direction for every white piece
def possible_moves_white(pieces):
    result = []
    for piece in range(3, 6):
        result.append((pieces[piece], move_right(pieces, pieces[piece])))
        result.append((pieces[piece], move_bot_right(pieces, pieces[piece])))
        result.append((pieces[piece], move_bot(pieces, pieces[piece])))
        result.append((pieces[piece], move_bot_left(pieces, pieces[piece])))
        result.append((pieces[piece], move_left(pieces, pieces[piece])))
        result.append((pieces[piece], move_top_left(pieces, pieces[piece])))
        result.append((pieces[piece], move_top(pieces, pieces[piece])))
        result.append((pieces[piece], move_top_right(pieces, pieces[piece])))
    for i in range(len(result) - 1, 0, -1):
        if (result[i][0] == result[i][1]): # Removes obsolete moves
            result.remove(result[i])
    return result
            
def move_right(pieces, piece):
    if (piece[0] == 5):
        return piece
    else:
        if ((piece[0] + 1, piece[1]) in pieces):
            return piece
        else:
            return move_right(pieces, (piece[0] + 1, piece[1]))
        
def move_bot_right(pieces, piece):
    if (piece[0] == 5 or piece[1] == 1):
        return piece
    else:
        if ((piece[0] + 1, piece[1] - 1) in pieces):
            return piece
        else:
            return move_bot_right(pieces, (piece[0] + 1, piece[1] - 1))
        
def move_bot(pieces, piece):
    if (piece[1] == 1):
        return piece
    else:
        if ((piece[0], piece[1] - 1) in pieces):
            return piece
        else:
            return move_bot(pieces, (piece[0], piece[1] - 1))
        
def move_bot_left(pieces, piece):
    if (piece[0] == 1 or piece[1] == 1):
        return piece
    else:
        if ((piece[0] - 1, piece[1] - 1) in pieces):
            return piece
        else:
            return move_bot_left(pieces, (piece[0] - 1, piece[1] - 1))
        
def move_left(pieces, piece):
    if (piece[0] == 1):
        return piece
    else:
        if ((piece[0] - 1, piece[1]) in pieces):
            return piece
        else:
            return move_left(pieces, (piece[0] - 1, piece[1]))
        
def move_top_left(pieces, piece):
    if (piece[0] == 1 or piece[1] == 5):
        return piece
    else:
        if ((piece[0] - 1, piece[1] + 1) in pieces):
            return piece
        else:
            return move_top_left(pieces, (piece[0] - 1, piece[1] + 1))
        
def move_top(pieces, piece):
    if (piece[1] == 5):
        return piece
    else:
        if ((piece[0], piece[1] + 1) in pieces):
            return piece
        else:
            return move_top(pieces, (piece[0], piece[1] + 1))
        
def move_top_right(pieces, piece):
    if (piece[0] == 5 or piece[1] == 5):
        return piece
    else:
        if ((piece[0] + 1, piece[1] + 1) in pieces):
            return piece
        else:
            return move_top_right(pieces, (piece[0] + 1, piece[1] + 1))
    
# Prints the Board taking into account the current player
def printBoard(pieces, player):
    for i in range(5, 0, -1):
        print("|-----|-----|-----|-----|-----|")
        for j in range(1, 6):
            if((j, i) in pieces):
                index = pieces.index((j, i))
                if(index < 3): # Blacks
                    if(player == 1): 
                        print("|  " + str(index+1) + "  ", end="")
                    else:
                        print("|  B  ", end="")

                else: # Whites
                    if(player == 2):
                        print("|  " + str(index-2) + "  ", end="") # As if index is % 3, considering the array order doesn't change
                    else:
                        print("|  W  ", end="")
            else:
                print("|     ", end="")
        print("|")
    print("|-----|-----|-----|-----|-----|")
    
def printPossibleMoves(pieces, possible_moves, piece_chosen):
    
    final_moves = []
    
    for i in range(len(possible_moves)):
        if (possible_moves[i][0] == piece_chosen): # Removes obsolete moves
            final_moves.append(possible_moves[i][1])

    for i in range(5, 0, -1):
        print("|-----|-----|-----|-----|-----|")
        for j in range(1, 6):
            if((j, i) in pieces):
                index = pieces.index((j, i))
                if(index < 3): # Blacks
                    print("|  B  ", end="")
                else: # Whites
                    print("|  W  ", end="")
            elif ((j, i) in final_moves):
                print("|  " + str(final_moves.index((j, i)) + 1) + "  ", end="")
            else:
                print("|     ", end="")
        print("|")
    print("|-----|-----|-----|-----|-----|")

    return final_moves

# Initial Board example
""" 
|-----|-----|-----|-----|-----|
|     |  w  |     |  w  |     |
|-----|-----|-----|-----|-----|
|     |     |  2  |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |  w  |     |     |
|-----|-----|-----|-----|-----|
|     |  1  |     |  3  |     |
|-----|-----|-----|-----|-----| """

# Returns the next player to play
def playerUpdate(player):
    if(player == 1):
        return 2
    elif (player == 2): 
        return 1
    

def printPiece(piece):
    return "(" + str(piece[0]) + ", " + str(piece[1]) + ")"


def move(pieces, piece_chosen, tile_chosen):   
    for i in range(len(pieces)):
        if(piece_chosen == pieces[i]):
            pieces[i] = tile_chosen
    
    
def gameLoop(pieces, player):

    printBoard(pieces, player)

    # Choose what to move
    piece_chosen = 0
    while ((1 > piece_chosen) or (piece_chosen > 3)):
        piece_chosen = int(input("Choose your piece: "))
    possible_moves = possible_moves_black(pieces)
    final_moves = printPossibleMoves(pieces, possible_moves, pieces[piece_chosen-1])
    
    # Choose where to move
    tile_chosen = 0
    while ((1 > tile_chosen) or (tile_chosen > len(final_moves))):
        tile_chosen = int(input("Choose the destination: "))
    
    move(pieces, pieces[piece_chosen - 1], final_moves[tile_chosen - 1])
    printBoard(pieces, 2)
    playerUpdate(player)


gameLoop([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)], 1)







#print(possible_moves_white([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)]))



