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