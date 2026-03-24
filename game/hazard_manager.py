
from game.hazards import Hazard


class HazardManager:
    def __init__(self):
        self.hazards: list[Hazard] = []

    def add_hazard(self, hazard: Hazard):
        self.hazards.append(hazard)

    def update_hazards(self, dt):

        for i, hazard in enumerate(self.hazards):
            hazard.update(dt)
            if not hazard.life(dt):
                self.hazards.pop(i)

    def draw_hazards(self, surface):
        for hazard in self.hazards:
            hazard.draw(surface)

    def collision(self, player_pos):
        for hazard in self.hazards:
            if hazard.collide_with(player_pos):
                return True
        return False