import math
import random

import pygame


class Enemy:
    def __init__(self, screen_width, screen_height, screen):
        self.screen = screen
        self.width = 20
        self.height = 20
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = screen_width // 4 - self.width // 2
        self.y = screen_height // 4 - self.height // 2
        self.speed = 5
        self.fire_rate = 0.8
        self.last_shot = 0
        self.lasers = []
        self.frame_count = 0
        self.ship_color = (255, 255, 255)  # White color for the rectangle
        self.triangle_color = (255, 0, 0)  # Red color for the triangles
        

    # Methods for drawing, moving, firing lasers, and updating lasers (similar to Spaceship class)
    # ...
    def draw(self, screen):
        pygame.draw.polygon(screen, self.triangle_color, [
            (self.x - self.width // 2, self.y),
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height)
        ])




    def move(self):

        # Move the enemy smoothly horizontally and stay within screen boundaries
        self.x += self.speed
        if self.x <= 0 or self.x >= self.screen_width - self.width:
            self.speed = -self.speed
            self.y += 20  # Move down when changing direction

        # Ensure the enemy stays within screen boundaries
        self.x = max(0, min(self.x, self.screen_width - self.width))
    def fire_laser(self):
        self.frame_count += 1
        
        if self.frame_count % int(self.fire_rate * 60) == 0:
            laser_width = 5
            laser_height = 15
            laser_x = self.x + self.width // 2 - laser_width // 2
            laser_y = self.y + self.height  # Change to add the laser below the ship
            new_laser = {'rect': pygame.Rect(laser_x, laser_y, laser_width, laser_height), 'active': True}
            self.lasers.append(new_laser)

    def update_lasers(self):
        updated_lasers = []
        for laser in self.lasers:
            if laser['active']:
                pygame.draw.rect(self.screen, (255, 255, 255), laser['rect'])
                laser['rect'].y += 8  # Update to move the lasers downwards
                if laser['rect'].top < self.screen_height:  # Check if laser is within the screen
                    updated_lasers.append(laser)
        self.lasers = updated_lasers

    def update(self):
        self.move()
        self.fire_laser()
        self.update_lasers()
        self.draw(self.screen)
