from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
import pygame
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    AsteroidField()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 


    

    # game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
        screen.fill('black')

        # #draw
        # player.draw(screen)
        for item in drawable:
            item.draw(screen)

        # update
        updatable.update(dt)
        # clock update
        dt = clock.tick(60)/1000
        # print(f'value of dt: {dt}')
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event('player_hit')
                print("Game Over!")
                sys.exit()
        
        # at the end
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
