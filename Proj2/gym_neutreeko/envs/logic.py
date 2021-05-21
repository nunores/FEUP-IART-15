def check_game_status(position):
    if position[0] == 4 and position[1] == 4:
        return 1
    return 0


def updatePosition(board):
    for i in range(5):
        for n in range(5):
            if board[i][n] == 1:
                return (n, i)

# Matches actions to movements in board
def move(action, board, x, y):
    if action == 0:
        return move_right(board, x, y)
    elif action == 1:
        return move_bot_right(board, x, y)
    elif action == 2:
        return move_bot(board, x, y)
    elif action == 3:
        return move_bot_left(board, x, y)
    elif action == 4:
        return move_left(board, x, y)
    elif action == 5:
        return move_top_left(board, x, y)
    elif action == 6:
        return move_top(board, x, y)
    elif action == 7:
        return move_top_right(board, x, y)
    else:
        print("Something went wrong")

def move_right(board, x, y):
    if (x == 4 or board[y][x+1] != 0):
        return board
    else:
        newBoard = board
        newBoard[y][x+1] = 1
        newBoard[y][x] = 0
        return move_right(newBoard, x+1, y)

def move_bot_right(board, x, y):
    if (x == 4 or y == 0 or board[y-1][x+1] != 0):
        return board
    else:
        newBoard = board
        newBoard[y-1][x+1] = 1
        newBoard[y][x] = 0
        return move_bot_right(newBoard, x+1, y-1)

def move_bot(board, x, y):
    if (y == 0 or board[y-1][x] != 0):
        return board
    else:
        newBoard = board
        newBoard[y-1][x] = 1
        newBoard[y][x] = 0
        return move_bot(newBoard, x, y-1)

def move_bot_left(board, x, y):
    if (x == 0 or y == 0 or board[y-1][x-1] != 0):
        return board
    else:
        newBoard = board
        newBoard[y-1][x-1] = 1
        newBoard[y][x] = 0
        return move_bot_left(newBoard, x-1, y-1)

def move_left(board, x, y):
    if (x == 0 or board[y][x-1] != 0):
        return board
    else:
        newBoard = board
        newBoard[y][x-1] = 1
        newBoard[y][x] = 0
        return move_left(newBoard, x-1, y)

def move_top_left(board, x, y):
    if (x == 0 or y == 4 or board[y+1][x-1] != 0):
        return board
    else:
        newBoard = board
        newBoard[y+1][x-1] = 1
        newBoard[y][x] = 0
        return move_top_left(newBoard, x-1, y+1)

def move_top(board, x, y):
    if (y == 4 or board[y+1][x] != 0):
        return board
    else:
        newBoard = board
        newBoard[y+1][x] = 1
        newBoard[y][x] = 0
        return move_top(newBoard, x, y+1)

def move_top_right(board, x, y):
    if (x == 4 or y == 4 or board[y+1][x+1] != 0):
        return board
    else:
        newBoard = board
        newBoard[y+1][x+1] = 1
        newBoard[y][x] = 0
        return move_top_right(newBoard, x+1, y+1)