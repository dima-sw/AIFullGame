import sys
import pygame
from enemy import Enemy
from spaceship import Spaceship

def run_game():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spaceship")
    spaceship = Spaceship(WIDTH, HEIGHT,screen)
    enemy = Enemy(WIDTH, HEIGHT, screen)
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        spaceship.handle_input()
        enemy.update()
        pygame.display.flip()

        clock.tick(60)  # Cap the frame rate to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()
