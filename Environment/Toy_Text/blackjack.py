import gymnasium as gym
from Models.Reinforcement_Learning.q_learning import QLearningAgent,Q_TABLE,EPSILON_STRATEGY
from Environment.Toy_Text.template_toy_text import *

env_train = gym.make('Blackjack-v1', natural=False, sab=False)


env_test = gym.make('Blackjack-v1', natural=False, sab=False,render_mode="human")


NUMBER_EPISODE = 1000000
NUMBER_TEST = 100

ALPHA = 0.1
GAMMA = 0.999

EPSILON = 0.80
EPSILON_MODE = EPSILON_STRATEGY.DECAY
EPSILON_MIN = 0.1
EPSILON_DECAY = 0.9

MEMORY_MODE = Q_TABLE.DYNAMIC
NUMBER_ACTION = len([*range(env_train.action_space.n)])

NUMBER_STATE = 1
for i in env_train.observation_space:
    NUMBER_STATE *= int(i.n)


Agent = QLearningAgent(ALPHA,GAMMA,EPSILON,MEMORY_MODE,EPSILON_MODE,EPSILON_MIN,EPSILON_DECAY,NUMBER_ACTION,NUMBER_STATE)

play_game(env_train,env_test,Agent,NUMBER_EPISODE,NUMBER_TEST)