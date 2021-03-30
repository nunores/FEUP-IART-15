# Returns list with original position and possible end positions in every direction for every black piece
""" def possible_moves_black(pieces):
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
    return result """

# Returns the possible moves considering the current state and the player color
def get_possible_moves(pieces, color):
    result = []

    if(color == "white"):
        min = 3
        max = 6
    elif (color == "black"):
        min = 0
        max = 3
    for piece in range(min, max):
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
    

def possibleMovesPiece(pieces, possible_moves, piece_chosen):
    final_moves = []
    
    for i in range(len(possible_moves)):
        if (possible_moves[i][0] == piece_chosen): # Removes obsolete moves
            final_moves.append(possible_moves[i][1])

    return final_moves


# Returns the next player to play
def playerUpdate(player):
    if(player == 1):
        return 2
    elif (player == 2): 
        return 1
    

def move(pieces, piece_chosen, tile_chosen):   
    for i in range(len(pieces)):
        if(piece_chosen == pieces[i]):
            pieces[i] = tile_chosen

# Last_piece is the index of the last played piece
def gameOver(pieces, last_piece):
    if(last_piece >= 3):
        return (checkLine("white", pieces, last_piece) or checkDiagonals("white", pieces, last_piece) or checkColumn("white", pieces, last_piece))
    else:
        return (checkLine("black", pieces, last_piece) or checkDiagonals("black", pieces, last_piece) or checkColumn("black", pieces, last_piece))
        

def checkLine(color, pieces, last_piece):
    black_array = pieces[:3]
    white_array = pieces[3:6]

    if(color == "black"):
        if ((pieces[last_piece][0] + 1, pieces[last_piece][1]) in black_array):
            if((pieces[last_piece][0] + 2, pieces[last_piece][1]) in black_array):
                return True
            if((pieces[last_piece][0] - 1, pieces[last_piece][1]) in black_array):
                return True
        if ((pieces[last_piece][0] - 1, pieces[last_piece][1]) in black_array):
            if((pieces[last_piece][0] - 2, pieces[last_piece][1]) in black_array):
                return True
        return False
    else:
        if ((pieces[last_piece][0] + 1, pieces[last_piece][1]) in white_array):
            if((pieces[last_piece][0] + 2, pieces[last_piece][1]) in white_array): 
                return True
            if((pieces[last_piece][0] - 1, pieces[last_piece][1]) in white_array):
                return True
        if ((pieces[last_piece][0] - 1, pieces[last_piece][1]) in white_array):
            if((pieces[last_piece][0] - 2, pieces[last_piece][1]) in white_array):
                return True
        return False

def checkColumn(color, pieces, last_piece):
    black_array = pieces[:3]
    white_array = pieces[3:6]

    if(color == "black"):
        if ((pieces[last_piece][0], pieces[last_piece][1] + 1) in black_array):
            if((pieces[last_piece][0], pieces[last_piece][1] + 2) in black_array):  
                return True
            if((pieces[last_piece][0], pieces[last_piece][1] - 1) in black_array):
                return True
        if ((pieces[last_piece][0], pieces[last_piece][1] - 1) in black_array):
            if((pieces[last_piece][0], pieces[last_piece][1] - 2) in black_array):
                return True
        return False
    else:
        if ((pieces[last_piece][0], pieces[last_piece][1] + 1) in white_array):
            if((pieces[last_piece][0], pieces[last_piece][1] + 2) in white_array):
                return True
            if((pieces[last_piece][0], pieces[last_piece][1] - 1) in white_array):
                return True
        if ((pieces[last_piece][0], pieces[last_piece][1] - 1) in white_array):
            if((pieces[last_piece][0], pieces[last_piece][1] - 2) in white_array):
                return True
        return False

def checkDiagonals(color, pieces, last_piece):
    black_array = pieces[:3]
    white_array = pieces[3:6]

    if(color == "black"):
        if ((pieces[last_piece][0] + 1, pieces[last_piece][1] + 1) in black_array):
            if((pieces[last_piece][0] + 2, pieces[last_piece][1] + 2) in black_array):
                return True
            if((pieces[last_piece][0] - 1, pieces[last_piece][1] - 1) in black_array):
                return True
        if ((pieces[last_piece][0] - 1, pieces[last_piece][1] - 1) in black_array):
            if((pieces[last_piece][0] - 2, pieces[last_piece][1] - 2) in black_array):
                return True     
        if ((pieces[last_piece][0] - 1, pieces[last_piece][1] + 1) in black_array):
            if((pieces[last_piece][0] - 2, pieces[last_piece][1] + 2) in black_array):
                return True
            if((pieces[last_piece][0] + 1, pieces[last_piece][1] - 1) in black_array):
                return True
        if ((pieces[last_piece][0] + 1, pieces[last_piece][1] - 1) in black_array):
            if((pieces[last_piece][0] + 2, pieces[last_piece][1] - 2) in black_array):
                return True
        return False
    else:
        if ((pieces[last_piece][0] + 1, pieces[last_piece][1] + 1) in white_array):
            if((pieces[last_piece][0] + 2, pieces[last_piece][1] + 2) in white_array):
                return True
            if((pieces[last_piece][0] - 1, pieces[last_piece][1] - 1) in white_array):
                return True
        if ((pieces[last_piece][0] - 1, pieces[last_piece][1] - 1) in white_array):
            if((pieces[last_piece][0] - 2, pieces[last_piece][1] - 2) in white_array):
                return True     
        if ((pieces[last_piece][0] - 1, pieces[last_piece][1] + 1) in white_array):
            if((pieces[last_piece][0] - 2, pieces[last_piece][1] + 2) in white_array):
                return True
            if((pieces[last_piece][0] + 1, pieces[last_piece][1] - 1) in white_array):
                return True
        if ((pieces[last_piece][0] + 1, pieces[last_piece][1] - 1) in white_array):
            if((pieces[last_piece][0] + 2, pieces[last_piece][1] - 2) in white_array):
                return True
        return False

def getLastPieceIndex(array1, array2):
    for i in range(len(array1)):
        if (array1[i] != array2[i]):
            return i
    return -1 # Arrays are equal
    