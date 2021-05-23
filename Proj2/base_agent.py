#!/usr/bin/env python
import random
import gym_neutreeko
import gym
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

np.set_printoptions(threshold=np.inf)

def writeToFile():
    f = open("base_agent_q_table.txt", "w")
    f.write(str(qtable))
    f.close()

env = gym.make('game-env-v0')
env.render()

action_size = env.action_space.n
#state_size = env.observation_space.n
num_box = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
qtable = np.zeros(num_box + (env.action_space.n,))

state = env.observation_space

#qtable = np.zeros((state_size, action_size))

# Hyperparameter Setup

total_episodes = 200000
learning_rate = 0.8
max_steps = 99
gamma = 0.95 # 0 - current reward, 1 - strives for long-term rewards

epsilon = 1.0
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.001

rewards = []

for episode in tqdm(range(total_episodes)):
    # Reset the environment
    state = env.reset()
    #print(state)
#     print(f"state: {state}")
    step = 0
    done = False
    total_rewards = 0
    
    for step in range(max_steps):
#         print(f"start step...")
        # 3. Choose an action a in the current world state (s)
        ## First we randomize a number
        exp_exp_tradeoff = random.uniform(0, 1)
        
#         print(f"exp_exp_tradeoff: {exp_exp_tradeoff}")
        
        ## If this number > greater than epsilon --> exploitation 
        #(taking the biggest Q value for this state)
        if exp_exp_tradeoff > epsilon:
            #print(f"qtable[state,:] {qtable[state,:]}")
            #action = np.argmax(qtable[state,:])
            action = np.argmax(qtable[state])

        # Else doing a random choice --> exploration
        else:
            action = env.action_space.sample()
            
#         print(f"action is {action}")

        # Take the action (a) and observe the outcome state(s') and reward (r)
        #print(action)
        new_state, reward, done, info = env.step(action)
        
#         print(f"new_state: {new_state}, reward: {reward}, done: {done}, info: {info}")

        # Update Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
        # qtable[new_state,:] : all the actions we can take from new state
        qtable[state][action] = qtable[state][action] + learning_rate * (reward + gamma * np.max(qtable[new_state]) - qtable[state][action])
        #q_value = qtable[state][action]
        #print(new_state)
        #best_q = np.max(qtable[new_state])

        # Q(state, action) <- (1 - a)Q(state, action) + a(reward + rmaxQ(next state, all actions))
        ##################qtable[state][action] = (1 - learning_rate) * q_value + learning_rate * (reward + gamma * best_q)
        #print(qtable[state, action])
#         print(f'qtable: {qtable}')
        
        total_rewards = total_rewards + reward
        
#         print(f'total_rewards {total_rewards}')
        
        # Our new state is state
        state = new_state
        
        #print(f'new state: {state}')
        
        # If done (if we're dead) : finish episode
        if done == True: 
            break
        
    episode += 1
    # Reduce epsilon (because we need less and less exploration)
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode) 
    rewards.append(total_rewards)

print ("Score/time: " +  str(sum(rewards)/total_episodes))
#print(qtable)
print(epsilon)
env.reset()

# Matplotlib decidiu ser dog e não funcionar
# plt.plot(rewards)
# plt.show()


for i in range (50):
    print("------------------")
    action = np.argmax(qtable[state])
    new_state, reward, done, info = env.step(action)
    state = new_state
    env.render()
    if(done): break


writeToFile()

env.reset()


