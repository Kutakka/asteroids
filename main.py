import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import Asteroid
from asteroidfield import *
def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)/1000)


if __name__ == "__main__":
    main()