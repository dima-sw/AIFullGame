import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Spaceship parameters
ship_width = 40
ship_height = 40
ship_x = WIDTH // 2 - ship_width // 2
ship_y = HEIGHT // 2 - ship_height // 2
ship_speed = 5  # Adjust the speed as needed

# Function to draw the spaceship
def draw_spaceship(x, y):
    pygame.draw.polygon(screen, WHITE, [
        (x + ship_width // 2, y),
        (x, y + ship_height),
        (x + ship_width, y + ship_height)
    ])

    pygame.draw.rect(screen, WHITE, (x + ship_width // 4, y + ship_height, ship_width // 2, ship_height // 2))

    pygame.draw.polygon(screen, RED, [
        (x + ship_width // 4, y + ship_height),
        (x - 5, y + ship_height + ship_height // 2),
        (x + ship_width // 4, y + ship_height + ship_height // 2)
    ])

    pygame.draw.polygon(screen, RED, [
        (x + 3 * ship_width // 4, y + ship_height),
        (x + ship_width + 5, y + ship_height + ship_height // 2),
        (x + 3 * ship_width // 4, y + ship_height + ship_height // 2)
    ])

def fire_laser():
    # Parametri del laser (posizione e dimensioni)
    laser_width = 5
    laser_height = 15
    laser_x = ship_x + ship_width // 2 - laser_width // 2  # In base alla posizione della navicella
    laser_y = ship_y - laser_height  # Sopra la navicella
    new_laser = {'rect': pygame.Rect(laser_x, laser_y, laser_width, laser_height), 'active': True}
    lasers.append(new_laser)

# Variable to track time for laser firing
laser_timer = 0
fire_rate = 0.2  # Interval between laser shots
laser_active = False  # Flag to indicate if the laser is active
laser = None  # Variable to store the current laser object
lasers = [] 
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_x -= ship_speed
    if keys[pygame.K_RIGHT]:
        ship_x += ship_speed
    if keys[pygame.K_UP]:
        ship_y -= ship_speed
    if keys[pygame.K_DOWN]:
        ship_y += ship_speed
    
    # Fire laser at regular intervals
    if laser_timer <= 0:
        # Fire laser
        laser_active = True
        laser = fire_laser()
        laser_timer = fire_rate  # Reset timer after firing
    else:
        laser_timer -= 0.01  # Decrease timer by frame time


    index = 0
    while index < len(lasers):
        laser = lasers[index]
        pygame.draw.rect(screen, WHITE, laser['rect'])
        laser['rect'].y -= 8  # Muovi il laser verso l'alto
        if laser['rect'].bottom <= 0:
            laser['active'] = False
            #if not laser['active']:
            lasers.pop(index)
        else:
            index += 1

  

    # Keep the ship within the screen boundaries
    ship_x = max(0, min(ship_x, WIDTH - ship_width))
    ship_y = max(0, min(ship_y, HEIGHT - ship_height))

    # Draw spaceship
    draw_spaceship(ship_x, ship_y)

    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
