from abc import ABC, abstractmethod

class Agent(ABC): # Abstact class

    @abstractmethod
    def _initiate_memory(self):
        pass

    @abstractmethod
    def play(self,state):
        pass

    @abstractmethod
    def learn(self):
        pass


class Memory(ABC): # Abstact class
    
    @abstractmethod
    def update_value(self,state,action,value):
        pass

    @abstractmethod
    def get_value(self,state,action):
        pass

    @abstractmethod
    def get_best_action(self,state):
        pass

    @abstractmethod
    def get_random_action(self,state):
        pass
