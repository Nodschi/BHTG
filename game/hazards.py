

import pygame
from config import PLAYER_SIZE


class Hazard():
    def __init__(self, pos):
        self.pos = list(pos)

    def update(self, dt):
        pass
    def draw(self, surface):
        pass
    def collide_with(self, player_pos):
        return False
    def life(self, dt):
        pass


# ------------
# Circle Zone
# ------------
class CircleZone(Hazard):
    def __init__(self, pos, radius, lifetime, max_radius, growth_speed, color=(255, 0, 0)):
        super().__init__(pos)
        self.radius = radius
        self.max_radius = max_radius
        self.growth_speed = growth_speed
        self.color = color
        self.lifetime = lifetime

    def update(self, dt):
        self.lifetime -= dt
        self.radius += self.growth_speed * dt

        if self.radius >= self.max_radius:
            self.radius = self.max_radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def collide_with(self, player_pos):
        dx = self.pos[0] - player_pos[0] # x
        dy = self.pos[1] - player_pos[1] # y

        distance = (dx ** 2 + dy ** 2) ** 0.5

        return distance < (self.radius + PLAYER_SIZE)

    def life(self, dt):
        if self.lifetime <= 0:
            return False
        return True


# ---------------
# Rectanlge Zone
# ---------------
class RectZone(Hazard):
    def __init__(self, pos, width, height, lifetime, color=(255, 0, 0)):
        super().__init__(pos) 
        self.width = width
        self.height = height
        self.lifetime = lifetime
        self.color = color
    
    def update(self, dt):
        self.lifetime -= dt

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.pos[0], self.pos[1], self.width, self.height])

    def collide_with(self, player_pos):
        w = self.width
        h = self.height

        closest_x = max(self.pos[0], min(player_pos[0], self.pos[0] + w))
        closest_y = max(self.pos[1], min(player_pos[1], self.pos[1] + h))
        
        distance_x = player_pos[0] - closest_x
        distance_y = player_pos[1] - closest_y

        squared_distance = distance_x**2 + distance_y**2

        if squared_distance < PLAYER_SIZE**2:
            return True
        return False

    def life(self, dt):
        if self.lifetime <= 0:
            return False
        return True
    
    
# -----------------------
# Straight Moving Bullet
# -----------------------
class StraightBullet(Hazard):
    def __init__(self, pos, radius, velocity, speed, lifetime, color=(255, 0, 0)):
        super().__init__(pos)
        self.radius = radius
        self.velocity = velocity
        self.speed = speed
        self.lifetime = lifetime
        self.color = color

    def update(self, dt):
        self.pos[0] += self.velocity[0] * dt * self.speed # x
        self.pos[1] += self.velocity[1] * dt * self.speed # y
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)
    def collide_with(self, player_pos):
        dx = self.pos[0] - player_pos[0] # x
        dy = self.pos[1] - player_pos[1] # y

        distance = (dx ** 2 + dy ** 2) ** 0.5

        return distance < (self.radius + PLAYER_SIZE)
    def life(self, dt):
        if self.lifetime <= 0:
            return False
        return True
    
# -----------------------
# Straving Moving Bullet
# -----------------------

class StravingBullet(Hazard):
    def __init__(self, pos, radius, velocity, speed, lifetime, color=(255, 0, 0)):
        super().__init__(pos)
        self.radius = radius
        self.velocity = velocity
        self.speed = speed
        self.lifetime = lifetime
        self.color = color