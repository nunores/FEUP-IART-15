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


def printBoardBot(pieces, player):
    for i in range(5, 0, -1):
        print("|-----|-----|-----|-----|-----|")
        for j in range(1, 6):
            if((j, i) in pieces):
                index = pieces.index((j, i))
                if(index < 3): # Blacks
                    print("|  B  ", end="")

                else: # Whites
                    print("|  W  ", end="")
            else:
                print("|     ", end="")
        print("|")
    print("|-----|-----|-----|-----|-----|")
    

def printPiece(piece):
    return "(" + str(piece[0]) + ", " + str(piece[1]) + ")"


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



