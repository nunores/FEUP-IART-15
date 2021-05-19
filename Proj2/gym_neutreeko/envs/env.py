import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding

def check_game_status(position):
    if position[0] == 4 and position[1] == 4:
        return 1
    return 0

def updatePosition(board):
    for i in range(5):
        for n in range(5):
            if board[i][n] == 1:
                return (n, i)

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
        
class NeutreekoEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(8)
        self.observation_space = spaces.Discrete(25)
        #self.observation_space = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([2, 2, 2, 2, 2]), dtype = np.int)   
        self.reset()

    def reset(self):
        """Resets the environment to an initial state and returns an initial observation.
        Note that this function should not reset the environment's random number generator(s); random variables in the 
        environment's state should be sampled independently between multiple calls to `reset()`. In other words, each 
        call of 'reset()' should yield an environment suitable for a new episode, independent of previous episodes.
        Returns:
            observation (object): the initial observation.
        """

        self.board = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, -1, 0, -1, 0]]
        self.done = False
        self.position = (1, 0)
        return 0

    def step(self, action):
        """Run one timestep of the environment's dynamics. When end of episode is reached, you are responsible for calling 
        'reset()' to reset this environment's state.
        Accepts an action and returns a tuple (observation, reward, done, info).
        Arguments:
            action (object): an action provided by the agent
        Returns:
            observation (object): agent's observation of the current environment
            reward (float) : amount of reward returned after previous action
            done (bool): whether the episode has ended, in which case further step() calls will return undefined results
            info (dict): contains auxiliary diagnostic information (helpful for debugging, and sometimes learning)
        """
        assert self.action_space.contains(action)

        if self.done:
            return self.position[0] + self.position[1]*5, 0, True, None

        reward = -0.05

        self.board = move(action, self.board, self.position[0], self.position[1])
        self.position = updatePosition(self.board)
        status = check_game_status(self.position)

        if status == 1:
            self.done = True
            reward += 1

        return self.position[0] + self.position[1]*5, reward, self.done, None

    def render(self, mode='human'):
        """Renders the environment.
        The set of supported modes varies per environment. (And some environments do not support rendering at all.) 
        By convention, if mode is:
        - human: render to the current display or terminal and return nothing. Usually for human consumption.
        - rgb_array: Return an numpy.ndarray with shape (x, y, 3), representing RGB values for an x-by-y pixel image, 
        suitable for turning into a video.
        - ansi: Return a string (str) or StringIO.StringIO containing a terminal-style text representation. The text 
        can include newlines and ANSI escape sequences (e.g. for colors).
        Note:
            Make sure that your class's metadata 'render.modes' key includes the list of supported modes. It's recommended 
            to call super() in implementations to use the functionality of this method.
        Args:
            mode (str): the mode to render with
        Example:
        class MyEnv(Env):
            metadata = {'render.modes': ['human', 'rgb_array']}
            def render(self, mode='human'):
                if mode == 'rgb_array':
                    return np.array(...) # return RGB frame suitable for video
                elif mode == 'human':
                    ... # pop up a window and render
                else:
                    super(MyEnv, self).render(mode=mode) # just raise an exception
        """
        for i in range(4, -1, -1):
            print(self.board[i])
 
    def close(self):
        """Performs any necessary cleanup.
        Environments will automatically close() themselves when
        garbage collected or when the program exits.
        """
        pass
