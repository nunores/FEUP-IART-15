from display import *
from logic import *
from bot import *
import time

def botvsbot(pieces):
    last_piece = -1
    player = 1
    while not gameOver(pieces, last_piece):
        printBoard(pieces, player)

        #print(pieces)
        
        last_piece = choose_move_adjacent(pieces, player)

        time.sleep(1)

        player = playerUpdate(player)


def main(pieces):

    player = 1
    last_piece = -1

    while not gameOver(pieces, last_piece):

        printBoard(pieces, player)

        # Choose what to move
        piece_chosen = 0
        while ((1 > piece_chosen) or (piece_chosen > 3)):
            try:
                piece_chosen = int(input("Choose your piece: "))
            except ValueError:
                print("Input not valid")

        if (player == 1 and not possibleMovesPiece(pieces, possible_moves_black(pieces), pieces[piece_chosen - 1])):
            piece_chosen = -1
            print("That black piece cannot be moved")
        elif (player == 2 and not possibleMovesPiece(pieces, possible_moves_white(pieces), pieces[piece_chosen + 2])):
            piece_chosen = -1
            print("That white piece cannot be moved")
            
        if (player == 1):
            last_piece = piece_chosen - 1
            possible_moves = possible_moves_black(pieces)
            final_moves = printPossibleMoves(pieces, possible_moves, pieces[piece_chosen-1])
        else:
            last_piece = piece_chosen + 2
            possible_moves = possible_moves_white(pieces)
            final_moves = printPossibleMoves(pieces, possible_moves, pieces[piece_chosen+2])

            
        

        # Choose where to move
        tile_chosen = 0
        while ((1 > tile_chosen) or (tile_chosen > len(final_moves))):
            try:
                tile_chosen = int(input("Choose the destination: "))
            except ValueError:
                print("Input not valid")
        
        if (player == 1):
            move(pieces, pieces[piece_chosen - 1], final_moves[tile_chosen - 1])
        else:
            move(pieces, pieces[piece_chosen + 2], final_moves[tile_chosen - 1])

        print(adjacentHeuristic(pieces, player))

        player = playerUpdate(player)

    
    printBoard(pieces, player)
    print("Winner: Player " + str(playerUpdate(player)))




#main([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)])
#botvsbot([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)])

#print(len(possible_moves_black([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)])))

root = Node([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)], 0)
root.addChildren(3, 1)
root.printTree(0)


#print(getNumAdjacents([(2, 1), (4, 1), (3, 4), (1, 4), (2, 5), (3, 5)], 2))

#print(possible_moves_white([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)]))



