import pygame

# initialize the pygame
pygame.init()

# create the screen (width, hight)
screen = pygame.display.set_mode((800,800))

# running will ture to false if the game stop
running = True

# game loop to maintain the window
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
