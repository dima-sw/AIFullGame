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
        self.speed = 5
        self.fire_rate = 0.5
        self.last_shot = 0  # Time tracking for shooting
        self.lasers = []
        self.frame_count = 0


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
                laser['rect'].y -= 8
                if laser['rect'].bottom > 0:
                    updated_lasers.append(laser)
        self.lasers = updated_lasers
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.move(keys)
        self.fire_laser()
        self.update_lasers()
        self.draw(self.screen)

