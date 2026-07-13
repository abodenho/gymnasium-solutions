from abc import ABC, abstractmethod

class Agent(ABC): # Abstact class
    @abstractmethod
    def _initiate_memory(self):
        pass

    @abstractmethod
    def make_a_choice(self,state):
        pass

    @abstractmethod
    def play(self,state):
        pass

    @abstractmethod
    def learn(self):
        pass
