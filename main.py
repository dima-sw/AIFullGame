import sys
import pygame
from enemy import Enemy, EnemyWave
from game import Game
from spaceship import Spaceship

def run_game():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spaceship")

    #enemy = Enemy(WIDTH, HEIGHT, screen)
    running = True
    clock = pygame.time.Clock()
    game=Game()
    #enemies = [Enemy(WIDTH, HEIGHT, screen) for _ in range(1)]  # Create multiple enemies
    # Inside the main game loop:
    while running:
        screen.fill((0, 0, 0))

        play_rect, quit_rect = game.display_menu(screen)  # Display the main menu

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_rect.collidepoint(mouse_pos):
                    start_game()
                elif quit_rect.collidepoint(mouse_pos):
                    running = False

        pygame.display.flip()




    pygame.quit()
    sys.exit()


def start_game():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Spaceship")
    spaceship = Spaceship(WIDTH, HEIGHT,screen)
    running = True
    clock = pygame.time.Clock()
    game = Game()  # Initialize the game
    enemy_wave = EnemyWave(WIDTH, HEIGHT, screen, spaceship, game)  # Pass your screen width and height variables here
    
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Your game logic goes here...
        spaceship.handle_input()       
        spaceship.draw_health_bar(screen)
        enemy_wave.update()
        for enemy in enemy_wave.enemies:
            enemy.draw(screen)

        spaceship.check_collisions(enemy_wave.enemies)
        game.display_score(screen)  # Display the score on the screen

        pygame.display.flip()

        clock.tick(60)  # Cap the frame rate to 60 FPS

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_game()
