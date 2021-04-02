from display import *
from logic import *
from bot import *
import time

def playervsbot(pieces):
    global queue

    last_piece = -1
    player = 1
    while not gameOver(pieces, last_piece) and not draw(queue):
        
        if (player == 1):
            printBoard(pieces, player)
            piece_chosen = 0
            while ((1 > piece_chosen) or (piece_chosen > 3)):
                try:
                    piece_chosen = int(input("Choose your piece: "))
                except ValueError:
                    print("Input not valid")

            # Error chosing move
            if (player == 1 and not possibleMovesPiece(pieces, get_possible_moves(pieces, "black"), pieces[piece_chosen - 1])):
                piece_chosen = -1
                print("That black piece cannot be moved")
                
            if (player == 1):
                last_piece = piece_chosen - 1
                possible_moves = get_possible_moves(pieces, "black")
                final_moves = printPossibleMoves(pieces, possible_moves, pieces[piece_chosen-1])

            # Choose where to move
            tile_chosen = 0
            while ((1 > tile_chosen) or (tile_chosen > len(final_moves))):
                try:
                    tile_chosen = int(input("Choose the destination: "))
                except ValueError:
                    print("Input not valid")

            # queue.appendleft(pieces)
            
            if (player == 1):
                move(pieces, pieces[piece_chosen - 1], final_moves[tile_chosen - 1])

            #print(adjacentHeuristic(pieces))

            player = playerUpdate(player)
        else:
            printBoardBot(pieces, player)
            start = time.time()
            print(queue)
            (pieces, last_piece) = choose_move_minimax(pieces, queue, 6, player)
            end = time.time()
            print(end-start)
            queue.appendleft(pieces)

            player = playerUpdate(player)

    printBoardBot(pieces, player)

    queue.clear()

def botvsbot(pieces):
    global queue

    last_piece = -1
    player = 1
    while not gameOver(pieces, last_piece) and not draw(queue):
        printBoardBot(pieces, player)
        start = time.time()
        print(queue)
        (pieces, last_piece) = choose_move_minimax(pieces, queue, 6, player)
        end = time.time()
        print(end-start)
        queue.appendleft(pieces)

        player = playerUpdate(player)

    printBoardBot(pieces, player)

    queue.clear()
    


def playervsplayer(pieces): # TODO Draw
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

        # Error chosing move
        if (player == 1 and not possibleMovesPiece(pieces, get_possible_moves(pieces, "black"), pieces[piece_chosen - 1])):
            piece_chosen = -1
            print("That black piece cannot be moved")
        elif (player == 2 and not possibleMovesPiece(pieces, get_possible_moves(pieces, "white"), pieces[piece_chosen + 2])):
            piece_chosen = -1
            print("That white piece cannot be moved")
            
        if (player == 1):
            last_piece = piece_chosen - 1
            possible_moves = get_possible_moves(pieces, "black")
            final_moves = printPossibleMoves(pieces, possible_moves, pieces[piece_chosen-1])
        else:
            last_piece = piece_chosen + 2
            possible_moves = get_possible_moves(pieces, "white")
            final_moves = printPossibleMoves(pieces, possible_moves, pieces[piece_chosen+2])

        # Choose where to move
        tile_chosen = 0
        while ((1 > tile_chosen) or (tile_chosen > len(final_moves))):
            try:
                tile_chosen = int(input("Choose the destination: "))
            except ValueError:
                print("Input not valid")

        # queue.appendleft(pieces)
        
        if (player == 1):
            move(pieces, pieces[piece_chosen - 1], final_moves[tile_chosen - 1])
        else:
            move(pieces, pieces[piece_chosen + 2], final_moves[tile_chosen - 1])

        #print(adjacentHeuristic(pieces))

        player = playerUpdate(player)

    
    printBoard(pieces, player)
    print("Winner: Player " + str(playerUpdate(player)))




#playervsplayer([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)])
#botvsbot([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)])
playervsbot([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)])
#main_menu()

#print(len(possible_moves_black([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)])))

#root = Node([(2, 1), (4, 1), (3, 4), (3, 2), (2, 5), (4, 5)], adjacentHeuristic([(3, 1), (4, 1), (4, 2), (1, 4), (2, 5), (4, 5)]))
#root.addChildren(3, 1)
#root.printTree(0)
#print(str(root.getBestMove(1)))


