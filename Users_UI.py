import pygame


def main():
    # initialize the pygame
    pygame.init()
    # create the screen (width, hight)
    screen = pygame.display.set_mode((660,800))
    # title and icon
    pygame.display.set_caption('Sudoku Game')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    # set background color
    screen.fill((230, 230, 230))
    # call function to set up 9*9 grid
    grid_setup(screen)

    pygame.display.update()

    # game loop to maintain the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


def grid_setup(screen):
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0,0,0), (60*i + 60, 80), (60*i + 60, 620), 5)
            pygame.draw.line(screen, (0,0,0), (60, 60*i + 80), (600, 60*i + 80), 5)
        else:
            pygame.draw.line(screen, (0,0,0), (60*i + 60, 80), (60*i + 60, 620), 2)
            pygame.draw.line(screen, (0,0,0), (60, 60*i + 80), (600, 60*i + 80), 2)


main()

