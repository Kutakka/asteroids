import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import Asteroid
from asteroidfield import *
from shot import *

def main():
    pygame.init
    print("Starting Asteroids!")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS, shots)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateable.update(dt)
        for obj in asteroids:
            if obj.collision_check(player_1) == True:
                print("Game over!")
                sys.exit()
            for shot in shots:
                if obj.collision_check(shot):
                    shot.kill()
                    obj.split()
        for object in drawable:
            object.draw(screen)
        for shot in shots:
            shot.update(dt)
            shot.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)/1000)


if __name__ == "__main__":
    main()