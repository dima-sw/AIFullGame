import pygame


class Game:

    def __init__(self):
        # Other existing code...
        self.score = 0  # Initialize score to zero
        self.scoreToHeart = 100


    def update_score(self, enemy):
        fire_rate_effect = 1 / max(abs(enemy.fire_rate), 0.01)
        # Calculate score based on enemy attributes and add it to the total score
        enemy_score = (enemy.attack) * (abs(enemy.speed)) * (fire_rate_effect)
      
        self.score += int(enemy_score)  # Increment the score
        if self.score >= self.scoreToHeart:
            self.spaceship.hearts += 1
            self.scoreToHeart+=(self.scoreToHeart/2)

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
    def display_name_input(self, screen):
        input_font = pygame.font.SysFont(None, 36)
        button_font = pygame.font.SysFont(None, 24)
        input_text = ""
        input_active = True
        save_button = pygame.Rect(10, 50, 140, 40)  # Define button dimensions and position
        save_color = (150, 150, 150)
        save_text = button_font.render("Save Score", True, (0, 0, 0))

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if save_button.collidepoint(mouse_pos):
                        input_active = False  # End input when button is clicked
                        name = input_text.strip()  # Get the entered name
                        self.save_score(name, self.score)  # Call save_score method

            screen.fill((0, 0, 0))
            # Display text input field
            text_surface = input_font.render("Enter Your Name: " + input_text, True, (255, 255, 255))
            screen.blit(text_surface, (10, 10))

            # Draw save button
            pygame.draw.rect(screen, save_color, save_button)
            screen.blit(save_text, (save_button.x + 10, save_button.y + 10))

            pygame.display.flip()

    def save_score(self, name, score):
        with open("scores.txt", "a") as file:
            file.write(f"{name}: {score}\n")