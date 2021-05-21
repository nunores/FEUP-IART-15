# Checks if is finished
def check_game_status(position1, position2, position3):
    if position1[0] == 1 and position1[1] == 3 and position2[0] == 2 and position2[1] == 2 and position3[0] == 3 and position3[1] == 3:
        return 1
    return 0


# def updatePosition(board, action):
#     for i in range(5):
#         for n in range(5):
#             if board[i][n] == 1:
#                 return (n, i)

# Matches actions to movements in board
def move(action, board, x1, y1, x2, y2, x3, y3):
    if action == 0: # Piece x1, y1
        return move_right(board, x1, y1)
    elif action == 1:
        return move_bot_right(board, x1, y1)
    elif action == 2:
        return move_bot(board, x1, y1)
    elif action == 3:
        return move_bot_left(board, x1, y1)
    elif action == 4:
        return move_left(board, x1, y1)
    elif action == 5:
        return move_top_left(board, x1, y1)
    elif action == 6:
        return move_top(board, x1, y1)
    elif action == 7:
        return move_top_right(board, x1, y1)

    elif action == 8: # Piece x2, y2
        return move_right(board, x2, y2)
    elif action == 9:
        return move_bot_right(board, x2, y2)
    elif action == 10:
        return move_bot(board, x2, y2)
    elif action == 11:
        return move_bot_left(board, x2, y2)
    elif action == 12:
        return move_left(board, x2, y2)
    elif action == 13:
        return move_top_left(board, x2, y2)
    elif action == 14:
        return move_top(board, x2, y2)
    elif action == 15:
        return move_top_right(board, x2, y2)
        
    elif action == 16: # Piece x3, y3
        return move_right(board, x3, y3)
    elif action == 17:
        return move_bot_right(board, x3, y3)
    elif action == 18:
        return move_bot(board, x3, y3)
    elif action == 19:
        return move_bot_left(board, x3, y3)
    elif action == 20:
        return move_left(board, x3, y3)
    elif action == 21:
        return move_top_left(board, x3, y3)
    elif action == 22:
        return move_top(board, x3, y3)
    elif action == 23:
        return move_top_right(board, x3, y3)
    else:
        print("Something went wrong")

def move_right(board, x, y):
    if (x == 4 or board[y][x+1] != 0):
        return board, (x, y)
    else:
        newBoard = board
        newBoard[y][x+1] = 1
        newBoard[y][x] = 0
        return move_right(newBoard, x+1, y)

def move_bot_right(board, x, y):
    if (x == 4 or y == 0 or board[y-1][x+1] != 0):
        return board, (x, y)
    else:
        newBoard = board
        newBoard[y-1][x+1] = 1
        newBoard[y][x] = 0
        return move_bot_right(newBoard, x+1, y-1)

def move_bot(board, x, y):
    if (y == 0 or board[y-1][x] != 0):
        return board, (x, y)
    else:
        newBoard = board
        newBoard[y-1][x] = 1
        newBoard[y][x] = 0
        return move_bot(newBoard, x, y-1)

def move_bot_left(board, x, y):
    if (x == 0 or y == 0 or board[y-1][x-1] != 0):
        return board, (x, y)
    else:
        newBoard = board
        newBoard[y-1][x-1] = 1
        newBoard[y][x] = 0
        return move_bot_left(newBoard, x-1, y-1)

def move_left(board, x, y):
    if (x == 0 or board[y][x-1] != 0):
        return board, (x, y)
    else:
        newBoard = board
        newBoard[y][x-1] = 1
        newBoard[y][x] = 0
        return move_left(newBoard, x-1, y)

def move_top_left(board, x, y):
    if (x == 0 or y == 4 or board[y+1][x-1] != 0):
        return board, (x, y)
    else:
        newBoard = board
        newBoard[y+1][x-1] = 1
        newBoard[y][x] = 0
        return move_top_left(newBoard, x-1, y+1)

def move_top(board, x, y):
    if (y == 4 or board[y+1][x] != 0):
        return board, (x, y)
    else:
        newBoard = board
        newBoard[y+1][x] = 1
        newBoard[y][x] = 0
        return move_top(newBoard, x, y+1)

def move_top_right(board, x, y):
    if (x == 4 or y == 4 or board[y+1][x+1] != 0):
        return board, (x, y)
    else:
        newBoard = board
        newBoard[y+1][x+1] = 1
        newBoard[y][x] = 0
        return move_top_right(newBoard, x+1, y+1)