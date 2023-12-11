import pygame


class Game:
    def __init__(self):
        # Other existing code...
        self.score = 0  # Initialize score to zero

    def update_score(self, enemy):
        fire_rate_effect = 1 / max(abs(enemy.fire_rate), 0.01)
        # Calculate score based on enemy attributes and add it to the total score
        enemy_score = (enemy.attack) * (abs(enemy.speed)) * (fire_rate_effect)
      
        self.score += int(enemy_score)  # Increment the score

    def display_score(self, screen):
        font = pygame.font.SysFont(None, 36)
        text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        screen.blit(text, (10, 10))  # Display the score at (10, 10) on the screen

    def display_menu(self, screen):
        font = pygame.font.Font(None, 36)
        WHITE = (255, 255, 255)
        width, height = screen.get_width(), screen.get_height()

        # Texts for the buttons
        play_text = font.render("Play", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)

        # Rectangles for buttons
        play_rect = play_text.get_rect(center=(width // 2, height // 2 - 50))
        quit_rect = quit_text.get_rect(center=(width // 2, height // 2 + 50))

        # Display buttons on the screen
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)

        return play_rect, quit_rect