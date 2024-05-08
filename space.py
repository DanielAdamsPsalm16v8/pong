import pygame

# Initialize Pygame
pygame.init()

x = 800
y = 600

# Set display size
display_width = x
display_height = y
display_size = (display_width, display_height)

# Create the display surface
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption('Pygame Template')


# Colors
white = (255, 255, 255)
black = (0,0,0)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("W pressed")
            elif event.key == pygame.K_a:
                print("A pressed")
            elif event.key == pygame.K_s:
                print("S pressed")
            elif event.key == pygame.K_d:
                print("D pressed")



    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

