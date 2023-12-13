import pygame
import sys

class Spaceship:
    def __init__(self, screen_width, screen_height, screen):
        self.screen = screen
        self.width = 40
        self.height = 40
        self.screenWidth=screen_width
        self.screenHeight = screen_height
        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height // 2 - self.height // 2
        self.speed = 10
        self.fire_rate = 0.5
        self.min_fire_rate = 0.05
        self.max_fire_rate = 1
        self.last_shot = 0  # Time tracking for shooting
        self.lasers = []
        self.frame_count = 0
        self.life = 100
        self.max_life = 100
        self.hearts = 3
        self.attack = 100
        self.laserSpeed = 15
        self.laserMinSpeed=2
        self.laserMaxSpeed=20


    def draw(self, screen):
        # Draw the spaceship
        pygame.draw.polygon(screen, (255, 255, 255), [
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height)
        ])

        pygame.draw.rect(screen, (255, 255, 255), (self.x + self.width // 4, self.y + self.height, self.width // 2, self.height // 2))

        pygame.draw.polygon(screen, (255, 0, 0), [
            (self.x + self.width // 4, self.y + self.height),
            (self.x - 5, self.y + self.height + self.height // 2),
            (self.x + self.width // 4, self.y + self.height + self.height // 2)
        ])

        pygame.draw.polygon(screen, (255, 0, 0), [
            (self.x + 3 * self.width // 4, self.y + self.height),
            (self.x + self.width + 5, self.y + self.height + self.height // 2),
            (self.x + 3 * self.width // 4, self.y + self.height + self.height // 2)
        ])

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        self.x = max(0, min(self.x, self.screenWidth - self.width))
        self.y = max(0, min(self.y, self.screenHeight - self.height))

    def fire_laser(self):
        self.frame_count += 1
        
        if self.frame_count % int(self.fire_rate * 60) == 0:
            laser_width = 5
            laser_height = 15
            laser_x = self.x + self.width // 2 - laser_width // 2
            laser_y = self.y - laser_height
            new_laser = {'rect': pygame.Rect(laser_x, laser_y, laser_width, laser_height), 'active': True}
            self.lasers.append(new_laser)
        


    def update_lasers(self):
        updated_lasers = []
        for laser in self.lasers:
            if laser['active']:
                pygame.draw.rect(self.screen, (255, 255, 255), laser['rect'])
                laser['rect'].y -= self.laserSpeed
                if laser['rect'].bottom > 0:
                    updated_lasers.append(laser)
        self.lasers = updated_lasers
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.move(keys)
        self.fire_laser()
        self.update_lasers()
        self.draw(self.screen)
    
    def check_collisions(self, enemies):
        for enemy in enemies:
            for laser in enemy.lasers:
                if laser['active'] and self.x < laser['rect'].x + laser['rect'].width < self.x + self.width \
                        and self.y < laser['rect'].y + laser['rect'].height < self.y + self.height:
                    self.life -= enemy.attack  # Reduce spaceship's life upon collision with enemy's laser
                    laser['active'] = False  # Deactivate the enemy's laser upon collision
                    if self.life <= 0:
                        self.hearts -= 1
                        self.life = self.max_life  # Reset life to 100%
        return self.hearts
    def draw_health_bar(self, screen):
        # Calculate health bar width based on player's remaining life
        health_bar_width_white = 200 * (self.life / 100)  # Width for the white portion
        health_bar_width_red = 200 - health_bar_width_white  # Width for the red portion

        # Draw the white portion representing the remaining health
        pygame.draw.rect(screen, (255, 255, 255), (600, 20, health_bar_width_white, 10))

        # Draw the red portion for depleted health
        pygame.draw.rect(screen, (255, 0, 0), (600 + health_bar_width_white, 20, health_bar_width_red, 10))
        self.draw_hearts(screen)
    
    def draw_hearts(self, screen):
        heart_color = (255, 0, 0)
        heart_size = 20
        heart_padding = 10
        heart_spacing = 30
        start_x = 10
        start_y = 50

        for i in range(self.hearts):
            heart_x = start_x + (heart_size + heart_padding + heart_spacing) * i

            # Draw the left half of the heart (rotated triangle)
            triangle_points = [
                (heart_x + heart_size // 15, start_y + heart_size // 3),
                (heart_x + 3 * heart_size // 3, start_y + heart_size // 3),
                (heart_x + heart_size // 2, start_y + heart_size)
            ]
            pygame.draw.polygon(screen, heart_color, triangle_points)

            # Draw the right half of the heart (circles)
            pygame.draw.circle(screen, heart_color, (heart_x + heart_size // 4, start_y + heart_size // 4), heart_size // 4)
            pygame.draw.circle(screen, heart_color, (heart_x + 3 * heart_size // 4, start_y + heart_size // 4), heart_size // 4)