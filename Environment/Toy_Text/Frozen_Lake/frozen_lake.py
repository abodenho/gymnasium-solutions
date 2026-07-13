import gymnasium as gym
from Models.Reinforcement_Learning.Q_learning import Qlearning,Q_TABLE,EPSILON_STRATEGY
from Environment.Toy_Text.template_toy_text import *

env_train = gym.make(
    'FrozenLake-v1',
    desc=None,
    map_name="4x4",
    is_slippery=True,
)

env_test = gym.make(
    'FrozenLake-v1',
    desc=None,
    map_name="4x4",
    is_slippery=True,
    render_mode="human"
)



NUMBER_EPISODE = 100000
NUMBER_TEST = 1

ALPHA = 0.1
GAMMA = 0.999

EPSILON = 0.80
EPSILON_MODE = EPSILON_STRATEGY.DECAY
EPSILON_MIN = 0.1
EPSILON_DECAY = 0.9

MEMORY_MODE = Q_TABLE.STATIC
NUMBER_ACTION = len([*range(env_train.action_space.n)])
NUMBER_STATE = int(env_train.observation_space.n)

Agent = Qlearning(ALPHA,GAMMA,EPSILON,MEMORY_MODE,EPSILON_MODE,EPSILON_MIN,EPSILON_DECAY,NUMBER_ACTION,NUMBER_STATE)


play_game(env_train,env_test,Agent,NUMBER_EPISODE,NUMBER_TEST)