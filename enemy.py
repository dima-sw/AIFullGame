import math
import random

import pygame


class Enemy:
    def __init__(self, screen_width, screen_height, screen,x, y):
        self.screen = screen
        self.width = 20
        self.height = 20
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = x
        self.y = y
        if random.uniform(-1, 1)>=0:
            self.speed = random.uniform(2, 7)
        else:
            self.speed = random.uniform(-7, -2)
        self.fire_rate = random.uniform(0.1, 3) 
        self.last_shot = 0
        self.lasers = []
        self.frame_count = 0
        self.ship_color = (255, 255, 255)  # White color for the rectangle
        self.triangle_color = (255, 0, 0)  # Red color for the triangles
        self.life = 100
        self.attack = 10
        self.yDown = 40
        

    # Methods for drawing, moving, firing lasers, and updating lasers (similar to Spaceship class)
    # ...
    def draw(self, screen):
        pygame.draw.polygon(screen, self.triangle_color, [
            (self.x - self.width // 2, self.y),
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height)
        ])
        pygame.draw.polygon(screen, self.triangle_color, [
            (self.x - self.width // 2, self.y),
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height)
        ])

        # Calculate health bar width based on enemy's remaining life
        health_bar_width_white = self.width * (self.life / 100)  # Width for the white portion
        health_bar_width_red = self.width - health_bar_width_white  # Width for the red portion

        # Draw the white portion representing the remaining health
        pygame.draw.rect(screen, (255, 255, 255), (self.x - self.width // 2, self.y - 10, health_bar_width_white, 5))

        # Draw the red portion for depleted health
        pygame.draw.rect(screen, (255, 0, 0), (self.x - self.width // 2 + health_bar_width_white, self.y - 10, health_bar_width_red, 5))


    def move(self):

        # Move the enemy smoothly horizontally and stay within screen boundaries
        self.x += self.speed
        if self.x <= 0 or self.x >= self.screen_width - self.width:
            self.speed = -self.speed
            self.y += self.yDown # Move down when changing direction

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
    def off_screen(self, screen_width, screen_height):
        #return self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height
        return self.y > screen_height
    def handle_collision(self, spaceship):
        player_attack = spaceship.attack # Get the player's attack value
        player_lasers = spaceship.lasers  # Get the player's lasers

        for laser in player_lasers:
            if laser['active'] and self.x < laser['rect'].x + laser['rect'].width < self.x + self.width \
                    and self.y < laser['rect'].y + laser['rect'].height < self.y + self.height:
                self.life -= player_attack  # Reduce enemy's life upon collision with player's laser
                laser['active'] = False  # Deactivate the player's laser upon collision
        return self.life <= 0 


class EnemyWave:
    def __init__(self, screen_width, screen_height, screen,spaceship, game):
        self.enemies = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen=screen
        self.spaceship = spaceship  # Pass the spaceship object
        self.game= game
        self.spawn_wave()

    def spawn_wave(self):
        # Clear existing enemies
        self.enemies = []

        grid = []
        grid_width = 10
        cell_size = self.screen_width // grid_width

        for col in range(grid_width):
            grid.append(0)

        num_enemies = random.randint(3, 6)
        for _ in range(num_enemies):
            x = random.randint(0, grid_width - 1)
            y = random.randint(0, self.screen_height // 3)  # Random row within the top 1/3 of the screen

            while grid[x] != 0:
                x = random.randint(0, grid_width - 1)
                y = random.randint(0, self.screen_height // 3)

            enemy = Enemy(self.screen_width, self.screen_height, self.screen, x * cell_size, y)
            self.enemies.append(enemy)
            grid[x] = 1
    def update(self):
        

        for enemy in self.enemies:
            enemy.move()
            enemy.fire_laser()
            enemy.update_lasers()  # Add this line to update enemy lasers
            if enemy.off_screen(self.screen_width, self.screen_height):
                self.enemies.remove(enemy)
            if enemy.handle_collision(self.spaceship):
                self.enemies.remove(enemy)
                self.game.update_score(enemy)

        #for enemy in enemies_to_remove:
            

        if len(self.enemies) == 0:
            self.spawn_wave()