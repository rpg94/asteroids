import pygame
from typing import Sequence

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: Sequence[pygame.sprite.Group] = ()
    
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers) # type: ignore
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, circleshape_obj):
        distance = self.position.distance_to(circleshape_obj.position)
        if distance <= self.radius + circleshape_obj.radius:
            return True
        return False
