import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=x,y=y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
