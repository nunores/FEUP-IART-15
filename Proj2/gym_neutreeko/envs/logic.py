# Returns the next player to play
def playerUpdate(player):
    if(player == 1):
        return 2
    elif (player == 2): 
        return 1
    

def draw(tempQueue):
    global queue

    if (len(queue) == 13):
        if (tempQueue[0] == tempQueue[4] and tempQueue[4] == tempQueue[8] and tempQueue[8] == tempQueue[12]):
            return True
    return False

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