from Models.player import Agent
from enum import Enum
import random
import math



class Q_TABLE(Enum):
    DYNAMIC = 1
    STATIC = 2


class EPSILON_STRATEGY(Enum):
    NORMAL = 1
    DECAY = 2




class QTable:
    __qtable = {} # The data structure will be a dictionnary in case we have dynamic memory states, keys => state, values => actions
    __memory_construction = None 
    __default_number_action = None

    def __init__(self,qtable_construction:Q_TABLE,number_action:int = None,number_state:int = None):
        self.__memory_construction = qtable_construction
        self.__default_number_action = number_action
        self.__initiate_memory(number_action,number_state)

    def __initiate_memory(self,number_action:int,number_state:int = None) -> None:
        if self.__is_static_memory():
            for state_number in range(number_state):
                self.__qtable[state_number] = [ 0 for _ in range(number_action)]

    def __is_static_memory(self) -> bool:
        return self.__memory_construction == Q_TABLE.STATIC
    
    def __is_dynamic_memory(self) -> bool:
        return not self.__is_static_memory()

    def get_number_action(self,state:int) -> int:
        return len(self.__qtable[state])

    def __create_new_state(self,state:int,number_action:int = None) -> bool:
        if self.__is_dynamic_memory() and not self.__check_if_state_exist(state) :
            if number_action is None:
                number_action = self.__default_number_action
            self.__qtable[state] = [a for a in range(number_action)]

    def __check_if_state_exist(self,state:str) -> bool:
        return state in self.__qtable.keys()

    def update_value(self,state:str,action:int,value:float) -> bool:
        self.__qtable[state][action] = value
        return 1

    def get_value(self,state:int,action:int):
        if not self.__check_if_state_exist(state):
            self.__create_new_state(state)
        
        return self.__qtable[state][action]
    
    def get_best_action(self,state:str) -> int:
        if not self.__check_if_state_exist(state):
            self.__create_new_state(state) 
        
        liste_action_value = self.__qtable[state]
        number_action = len(liste_action_value)
        
        max_i_list = [0]
        max_value = - math.inf

        for i in range(number_action):
            value_i = liste_action_value[i]
            if  value_i > max_value:
                max_i_list = [i]
                max_value = value_i
            elif value_i == max_value:
                max_i_list.append(i)
        
        return random.choice(max_i_list)

    def get_choice_list(self,state:str) -> list :
        if not self.__check_if_state_exist(state):
            self.__create_new_state(state) 
        
        choice_list_action = []
        for i in range(len(self.__qtable[state])):
            choice_list_action.append(i)
        
        return choice_list_action
    

    def print_memory(self):
        print(self.__qtable)

    

class QLearningAgent(Agent):
    ## Mandatory
    __epsilon = None
    __alpha = None
    __gamma = None

    __qtable= None

    __epsilon_strategy = None

    ## Optional epsilon
    __epsilon_min = None
    __epsilon_decay = None

    def __init__(self,alpha,gamma,epsilon,Q_table_construction=Q_TABLE.DYNAMIC,Espilon_stategy=EPSILON_STRATEGY.NORMAL,epsilon_min=None,epsilon_decay=None,default_number_action=None,number_state=None):
        super()
        self.__alpha = alpha
        self.__gamma = gamma
        self.__epsilon = epsilon
        self.__epsilon_strategy = Espilon_stategy

        self._initiate_memory(Q_table_construction,default_number_action,number_state)

        if self.__is_decay_epsilon():
            self.__epsilon_min = epsilon_min
            self.__epsilon_decay = epsilon_decay

    def _initiate_memory(self,Q_table_construction,default_number_action,number_state):
        if Q_table_construction == Q_TABLE.DYNAMIC:
            self.__qtable = QTable(Q_table_construction,number_action=default_number_action)
        else:
            self.__qtable = QTable(Q_table_construction,default_number_action,number_state)

    def __is_decay_epsilon(self):
        return self.__epsilon_strategy == EPSILON_STRATEGY.DECAY

    def __update_epsilon(self):
        self.__epsilon = max(self.__epsilon_min , self.__epsilon_decay*self.__epsilon)

    def __is_random_choice(self):
        return random.random() <= self.__epsilon
    

    def __explore(self,state):
        list_choice = self.__qtable.get_choice_list(state)
        chosen_action = random.choice(list_choice)
        return chosen_action
    
    def __exploit(self,state):
        chosen_action =  self.__qtable.get_best_action(state)
        return chosen_action

    def make_a_choice(self,state):
        chosen_action = None
        if self.__is_random_choice():
            chosen_action = self.__explore(state)
        else:
            chosen_action = self.__exploit(state)
        return chosen_action     
    
    def play(self,state):
        return self.__exploit(state)

    def learn(self,current_state,current_action,next_state,reward,end_episode):
        current_q = self.__qtable.get_value(current_state,current_action)

        if end_episode:
            new_current_q = (1-self.__alpha)*current_q + self.__alpha*(reward)

        else:
            next_best_q = self.__qtable.get_value(next_state,self.__qtable.get_best_action(next_state))
            new_current_q = (1-self.__alpha)*current_q + self.__alpha*(reward + self.__gamma * next_best_q )

        self.__qtable.update_value(current_state,current_action,new_current_q)
        
        if end_episode and self.__is_decay_epsilon():
            self.__update_epsilon()

    def print_memory(self): # Use for debug
        self.__qtable.print_memory()