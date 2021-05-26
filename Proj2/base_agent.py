#!/usr/bin/env python
import random
import gym_neutreeko
import gym
import numpy as np
import pickle
import time
from tqdm import tqdm

np.set_printoptions(threshold=np.inf)

def pickleWrite(qtable):
    pickle_out = open("base_agent.pickle", "wb")
    pickle.dump(qtable, pickle_out)
    pickle_out.close()

def pickleRead():
    pickle_in = open("base_agent.pickle", "rb")
    return pickle.load(pickle_in)

def writeToFile(qtable):
    f = open("base_agent_q_table.txt", "w")
    f.write(str(qtable))
    f.close()

def learn():
    # Env Setup
    env = gym.make('game-env-v0')

    action_size = env.action_space.n
    num_box = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
    qtable = np.zeros(num_box + (env.action_space.n,))

    state = env.observation_space

    # Hyperparameter Setup

    total_episodes = 20000000
    learning_rate = 0.8
    max_steps = 99
    gamma = 0.5 # 0 - current reward, 1 - strives for long-term rewards

    epsilon = 1.0
    max_epsilon = 1.0
    min_epsilon = 0.01
    decay_rate = 0.005

    rewards = []

    for episode in tqdm(range(total_episodes)):
        # Reset the environment
        state = env.reset()

        step = 0
        done = False
        total_rewards = 0
        
        for step in range(max_steps):
            ## First we randomize a number
            exp_exp_tradeoff = random.uniform(0, 1)
                        
            ## If this number > greater than epsilon --> exploitation 
            #(taking the biggest Q value for this state)
            if exp_exp_tradeoff > epsilon:
                action = np.argmax(qtable[state])

            # Else doing a random choice --> exploration
            else:
                action = env.action_space.sample()
                
            # Take the action (a) and observe the outcome state(s') and reward (r)
            new_state, reward, done, info = env.step(action)
            

            qtable[state][action] = qtable[state][action] + learning_rate * (reward + gamma * np.max(qtable[new_state]) - qtable[state][action])

            total_rewards = total_rewards + reward
                        
            # Our new state is state
            state = new_state
                        
            # If done (if we're dead) : finish episode
            if done == True: 
                break
            
        episode += 1

        # Reduce epsilon (because we need less and less exploration)
        epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode) 
        rewards.append(total_rewards)

    print ("Score/time: " +  str(sum(rewards)/total_episodes))
    env.reset()

    response = askSave()
    if(response == "1"):
        pickleWrite(qtable)
    writeToFile(qtable)


def askSave():
    response = None
    while (response != "1" and response != "2"):
        print("Do you wish to save the results?")
        print("1.Yes")
        print("2.No")
        response = str(input())
    return response

def play():
    env = gym.make('game-env-v0')
    state = env.reset()
    qtable = pickleRead()
    env.render()
    time.sleep(2)
    for i in range(50): # Max 50 plays, otherwise he's very dumb
        print("")
        action = np.argmax(qtable[state])
        new_state, reward, done, info = env.step(action)
        state = new_state
        env.render()
        time.sleep(2)
        if(done): break

def askLearn():
    response = None
    while (response != "1" and response != "2"):
        print("Do you wish for the agent to learn or to play?")
        print("1.Learn")
        print("2.Play")
        response = str(input())
    return response

response = askLearn()

if(response == "1"):
    learn()
elif (response == "2"):
    play()



