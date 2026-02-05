from abc import ABC, abstractmethod
import random

class Player(ABC):
  def __init__(self):
    self.moves = []
    self.position = (0,0)
    self.path=[self.position]
  
  def make_move(self):
    random_move = random.choice(self.moves)
    self.position = tuple(random_move)
    self.path.append(self.position)
    return self.position