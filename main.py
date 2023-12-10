import sys
import pygame
from enemy import Enemy, EnemyWave
from spaceship import Spaceship

def run_game():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spaceship")
    spaceship = Spaceship(WIDTH, HEIGHT,screen)
    #enemy = Enemy(WIDTH, HEIGHT, screen)
    running = True
    clock = pygame.time.Clock()
    #enemies = [Enemy(WIDTH, HEIGHT, screen) for _ in range(1)]  # Create multiple enemies
    # Inside the main game loop:
    enemy_wave = EnemyWave(WIDTH, HEIGHT, screen, spaceship)  # Pass your screen width and height variables here
    while running:
        screen.fill((0, 0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        spaceship.handle_input()       
        spaceship.draw_health_bar(screen)
        enemy_wave.update()
        for enemy in enemy_wave.enemies:
            enemy.draw(screen)

        spaceship.check_collisions(enemy_wave.enemies)

        pygame.display.flip()

        clock.tick(60)  # Cap the frame rate to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()
