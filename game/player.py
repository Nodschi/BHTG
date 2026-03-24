from config import TP_COOLDOWN
from game.utils import clamp_position

class Player:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.cooldown = 0.0

    def update(self, dt):
        self.cooldown = max(0, self.cooldown - dt)

    def teleport(self, x, y):
        if self.cooldown <= 0:
            x, y = clamp_position(x, y)
            self.pos = [x, y]
            self.cooldown = TP_COOLDOWN