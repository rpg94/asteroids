from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # x = self.position[0]
        # y = self.position[1]
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1= self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteriod1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteriod2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteriod1.velocity = vector1 * 1.2
        asteriod2.velocity = vector2 * 1.2
        
