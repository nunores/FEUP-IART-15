import random

def generateBoard(board):
    position1 = (0, 0)
    position2 = (0, 0)
    position3 = (0, 0)

    position1 = generatePosition(board)
    board[position1[1]][position1[0]] = 1

    position2 = generatePosition(board)
    board[position2[1]][position2[0]] = 1

    position3 = generatePosition(board)
    board[position3[1]][position3[0]] = 1

    return board, position1, position2, position3

def generatePosition(board):
    while(True):
        temp = (random.randrange(0, 5), random.randrange(0, 5))
        if (board[temp[1]][temp[0]] == 0):
            break
    position = temp
    return position


# Checks if is finished
def check_game_status(position, board):
    if (checkLine(position, board) or checkCol(position, board) or checkDiagonals(position, board)):
        return 1
    return 0

def checkLine(position, board):
    if (board[position[1]][position[0]] != 1):
        return False
    # Look to the left
    if(position[0] > 1 and board[position[1]][position[0]-1] == 1 and board[position[1]][position[0]-2] == 1):
        return True
    # Look to the right
    if(position[0] < 3 and board[position[1]][position[0]+1] == 1 and board[position[1]][position[0]+2] == 1):
        return True
    # look to both sides    
    if(position[0] > 0 and position[0] < 4 and board[position[1]][position[0]+1] == 1 and board[position[1]][position[0]-1] == 1):
        return True
    return False

def checkCol(position, board):
    if (board[position[1]][position[0]] != 1):
        return False
    # Look up
    if(position[1] < 3 and board[position[1]+1][position[0]] == 1 and board[position[1]+2][position[0]] == 1):
        return True
    # Look down
    if(position[1] > 1 and board[position[1]-1][position[0]] == 1 and board[position[1]-2][position[0]] == 1):
        return True
    # Look to both sides
    if(position[1] > 0 and position[1] < 4 and board[position[1]+1][position[0]] == 1 and board[position[1]-1][position[0]] == 1):
        return True
    return False

def checkDiagonals(position, board):
    if (board[position[1]][position[0]] != 1):
        return False
    # Look down and left 
    if (position[0] > 1 and position[1] > 1 and board[position[1]-1][position[0]-1] == 1 and board[position[1]-2][position[0]-2] == 1):
        return True
    # Look up and right
    if (position[0] < 3 and position[1] < 3 and board[position[1]+1][position[0]+1] == 1 and board[position[1]+2][position[0]+2] == 1):
        return True
    # Look up right and down left (middle)
    if (position[0] > 0 and position[0] < 4 and position[1] > 0 and position[1] < 4 and board[position[1]-1][position[0]-1] == 1 and board[position[1]+1][position[0]+1] == 1):
        return True
    # Look up and left
    if (position[0] > 1 and position[1] < 3 and board[position[1]+1][position[0]-1] == 1 and board[position[1]+2][position[0]-2] == 1):
        return True
    # Look down and right
    if (position[0] < 3 and position[1] > 1 and board[position[1]-1][position[0]+1] == 1 and board[position[1]-2][position[0]+2] == 1):
        return True
    # Look up left and down right (middle)
    if (position[0] > 0 and position[0] < 4 and position[1] > 0 and position[1] < 4 and board[position[1]-1][position[0]+1] == 1 and board[position[1]+1][position[0]-1] == 1):
        return True

    return False

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