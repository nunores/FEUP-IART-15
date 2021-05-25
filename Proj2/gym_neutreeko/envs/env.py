import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding
from .logic import *
        
class NeutreekoEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        #self.action_space = spaces.Discrete(8)
        #self.observation_space = spaces.Discrete(25)
        self.action_space = spaces.Discrete(24)
        self.observation_space = spaces.Box(np.array([0, 0, 0, 0, 0, 0]), np.array([4, 4, 4, 4, 4, 4]), dtype = np.int)   
        self.reset()

    def reset(self):
        """Resets the environment to an initial state and returns an initial observation.
        Note that this function should not reset the environment's random number generator(s); random variables in the 
        environment's state should be sampled independently between multiple calls to `reset()`. In other words, each 
        call of 'reset()' should yield an environment suitable for a new episode, independent of previous episodes.
        Returns:
            observation (object): the initial observation.
        """

        self.board, self.position1, self.position2, self.position3 = generateBoard([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, -1, 0, -1, 0]])
        self.done = False
        return tuple([self.position1[0], self.position1[1], self.position2[0], self.position2[1], self.position3[0], self.position3[1]])

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
            return tuple([self.position1[0], self.position2[1], self.position2[0], self.position2[1], self.position3[0], self.position3[1]]), 0, True, None

        reward = -0.05

        
        if (action < 8):
            (self.board, self.position1) = move(action, self.board, self.position1[0], self.position1[1], self.position2[0], self.position2[1], self.position3[0], self.position3[1])
        elif (action < 16):
            (self.board, self.position2) = move(action, self.board, self.position1[0], self.position1[1], self.position2[0], self.position2[1], self.position3[0], self.position3[1])
        else:
            (self.board, self.position3) = move(action, self.board, self.position1[0], self.position1[1], self.position2[0], self.position2[1], self.position3[0], self.position3[1])

        status = check_game_status(self.position1, self.board)

        if status == 1:
            self.done = True
            reward += 1

        return tuple([self.position1[0], self.position2[1], self.position2[0], self.position2[1], self.position3[0], self.position3[1]]), reward, self.done, None

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
        print("|-----|-----|-----|-----|-----|")
        for i in range(4, -1, -1):
            print("|", end='')
            for n in range (5):
                if (self.board[i][n] == 0):
                    print("     |", end='')
                elif (self.board[i][n] == 1):
                    print("  X  |", end='')
                elif (self.board[i][n] == -1):
                    print("  O  |", end='')
            print("")
            print("|-----|-----|-----|-----|-----|")
 
    def close(self):
        """Performs any necessary cleanup.
        Environments will automatically close() themselves when
        garbage collected or when the program exits.
        """
        pass
