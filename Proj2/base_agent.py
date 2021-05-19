#!/usr/bin/env python
import random
import gym_neutreeko
import gym
import numpy as np
    

env = gym.make('game-env-v0')
env.render()

action_size = env.action_space.n
state_size = env.observation_space.n

state = env.observation_space

qtable = np.zeros((state_size, action_size))

total_episodes = 20000
learning_rate = 0.8
max_steps = 99
gamma = 0.95

epsilon = 1.0
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.001

rewards = []

for episode in range(total_episodes):
    # Reset the environment
    state = env.reset()
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
            action = np.argmax(qtable[state,:])

        # Else doing a random choice --> exploration
        else:
            action = env.action_space.sample()
            
#         print(f"action is {action}")

        # Take the action (a) and observe the outcome state(s') and reward (r)
        new_state, reward, done, info = env.step(action)
        
#         print(f"new_state: {new_state}, reward: {reward}, done: {done}, info: {info}")

        # Update Q(s,a):= Q(s,a) + lr [R(s,a) + gamma * max Q(s',a') - Q(s,a)]
        # qtable[new_state,:] : all the actions we can take from new state
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])
        
#         print(f'qtable: {qtable}')
        
        total_rewards = total_rewards + reward
        
#         print(f'total_rewards {total_rewards}')
        
        # Our new state is state
        state = new_state
        
#         print(f'new state: {state}')
        
        # If done (if we're dead) : finish episode
        if done == True: 
            break
        
    episode += 1
    # Reduce epsilon (because we need less and less exploration)
    epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay_rate*episode) 
    rewards.append(total_rewards)

print ("Score/time: " +  str(sum(rewards)/total_episodes))
print(qtable)
print(epsilon)

env.reset()


