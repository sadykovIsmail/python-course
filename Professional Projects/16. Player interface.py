import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        # assumes moves are already defined in subclass
        move = random.choice(self.moves)
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]
        self.position = (new_x, new_y)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

# Example subclass for testing
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(1,0), (-1,0), (0,1), (0,-1)]  # initial moves

    def level_up(self):
        self.moves.extend([(1,1), (1,-1), (-1,1), (-1,-1)])

# Test
p = Pawn()
print("Before move:", p.position)
print("Moved to:", p.make_move())
print("Path:", p.path)
