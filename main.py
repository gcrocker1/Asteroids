import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        updatable.update(dt)
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000    # This ticks the game at 60 fps, and also saves the delta time (time between loop iterations/frames) in seconds into dt

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()