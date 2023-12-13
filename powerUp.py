import math
import pygame
import random

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, powerUP, initial_x, initial_y, speed=4):
        super().__init__()
        self.color = powerUP["color"]
        self.shape = powerUP["shape"]
        self.attack = powerUP["attack"]
        self.health = powerUP["health"]
        self.maxHealth = powerUP["maxHealth"]
        self.attackRate = powerUP["attackRate"]
        self.laserSpeed = powerUP["laserSpeed"]
        self.size = powerUP["size"]
        self.image = None
        self.rect = None
        self.speed = speed
        self.initial_x = initial_x
        self.initial_y = initial_y
        
        # Create image based on the shape
        if self.shape == "square":
            self.image = pygame.Surface((30, 30))
            self.image.fill(pygame.Color(self.color))
            self.rect = self.image.get_rect()
        elif self.shape == "triangle":
            # Draw triangle using pygame drawing functions
            self.image = pygame.Surface((30, 30))
            self.image.fill(pygame.Color(self.color))
            pygame.draw.polygon(self.image, pygame.Color("black"), [(15, 0), (0, 30), (30, 30)])
            self.rect = self.image.get_rect()
        elif self.shape == "octagon":
            # Draw octagon using pygame drawing functions
            self.image = pygame.Surface((30, 30))
            self.image.fill(pygame.Color(self.color))
            points = [(15 + 10 * math.cos(2 * math.pi * i / 8), 15 + 10 * math.sin(2 * math.pi * i / 8)) for i in range(8)]
            pygame.draw.polygon(self.image, pygame.Color("black"), points)
            self.rect = self.image.get_rect()
        elif self.shape == "pentagon":
            # Draw pentagon using pygame drawing functions
            self.image = pygame.Surface((30, 30))
            self.image.fill(pygame.Color(self.color))
            points = [(15 + 15 * math.cos(2 * math.pi * i / 5), 15 + 15 * math.sin(2 * math.pi * i / 5)) for i in range(5)]
            pygame.draw.polygon(self.image, pygame.Color("black"), points)
            self.rect = self.image.get_rect()
        elif self.shape == "heart":
            # Draw heart using pygame drawing functions
            self.image = pygame.Surface((30, 30))
            self.image.fill(pygame.Color(self.color))
            pygame.draw.polygon(self.image, pygame.Color("black"), [(15, 5), (5, 15), (15, 25), (25, 15)])
            left_heart = pygame.transform.flip(self.image, True, False)
            self.image.blit(left_heart, (15, 0))
            self.rect = self.image.get_rect()
        elif self.shape == "circle":
            self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
            pygame.draw.circle(self.image, pygame.Color(self.color), (15, 15), 15)
            self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(topleft=(initial_x, initial_y))
    def update(self, screen):
        # Move the PowerUp down
        self.rect.y += self.speed
        # Display the PowerUp on the screen
        screen.blit(self.image, self.rect)
    def apply_effect(self, spaceship):
        spaceship_x = spaceship.x
        spaceship_y = spaceship.y
        spaceship_width = spaceship.width
        spaceship_height = spaceship.height
        collision =  (self.rect.x < spaceship_x + spaceship_width and
            self.rect.x + self.rect.width > spaceship_x and
            self.rect.y < spaceship_y + spaceship_height and
            self.rect.y + self.rect.height > spaceship_y)
        if collision:
            if self.attack > 0:
                spaceship.attack *= (1 + self.attack / 100)
            else:
                spaceship.attack *= (1 - abs(self.attack) / 100)

            if self.health > 0:
                spaceship.life = min(spaceship.max_life, spaceship.life + self.health)
            else:
                spaceship.life = max(0, spaceship.life + self.health)

            if self.maxHealth > 0:
                spaceship.max_life += self.maxHealth
            else:
                spaceship.max_life = max(spaceship.max_life + self.maxHealth, spaceship.life)

            if self.attackRate > 0:
                spaceship.fire_rate = min(spaceship.max_fire_rate, spaceship.fire_rate + self.attackRate / 100)
            else:
                spaceship.fire_rate = max(spaceship.min_fire_rate, spaceship.fire_rate + self.attackRate / 100)

            if self.laserSpeed > 0:
                spaceship.laserSpeed = min(spaceship.laserMaxSpeed, spaceship.laserSpeed + self.laserSpeed)
            else:
                spaceship.laserSpeed = max(spaceship.laserMinSpeed, spaceship.laserSpeed + self.laserSpeed)

            if self.size > 0:
                spaceship.width *= (1 + self.size / 100)
                spaceship.height *= (1 + self.size / 100)
            else:
                spaceship.width = max(1, spaceship.width + spaceship.width * self.size / 100)
                spaceship.height = max(1, spaceship.height + spaceship.height * self.size / 100)

            print("life:" + str(spaceship.life),
                "MAXlife:" + str(spaceship.max_life),
                "Fire Rate:" + str(spaceship.fire_rate),
                "LaserSpeed:" + str(spaceship.laserSpeed),
                "Attack:" + str(spaceship.attack),
                "Width:" + str(spaceship.width),
                "Height:" + str(spaceship.height))
            # Destroy the PowerUp upon collision
            self.kill()

        return collision

