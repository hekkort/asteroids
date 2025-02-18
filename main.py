import pygame
import constants
import circleshape
from player import Player

def main():
    pygame.init()
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    clock = pygame.time.Clock()
    player = Player(x, y)
    dt = 0
    print("Starting asteroids!")
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()