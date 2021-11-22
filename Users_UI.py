import pygame, copy




def running():
    background_color = (235, 235, 235)
    # initialize the pygame
    pygame.init()
    # create the screen (width, hight)
    screen = pygame.display.set_mode((660,800))
    # text font, title and icon
    text_font = pygame.font.Font(pygame.font.get_default_font(), 30) # need adding a font file 
    pygame.display.set_caption('Sudoku Game')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    # set background color
    screen.fill(background_color)
    # call function to set up 9*9 grid
    grid = [[0,9,0,0,3,5,0,8,7],
            [8,0,0,1,9,0,0,5,0],
            [5,3,4,0,6,8,0,2,1],
            [9,7,8,2,0,3,4,6,5],
            [0,1,0,5,0,6,7,9,8],
            [6,0,5,8,7,9,1,0,0],
            [4,2,0,0,0,7,0,1,9],
            [1,0,9,3,2,4,0,7,6],
            [7,0,6,0,8,0,2,4,0]]
    solution = [[1,9,1,1,3,5,1,8,7],
                [8,1,1,1,9,1,1,5,1],
                [5,3,4,1,6,8,1,2,1],
                [9,7,8,2,1,3,4,6,5],
                [1,1,1,5,1,6,7,9,8],
                [6,1,5,8,7,9,1,1,1],
                [4,2,1,1,1,7,1,1,9],
                [1,1,9,3,2,4,1,7,6],
                [7,1,6,1,8,1,2,4,1]]
    update_grid = copy.deepcopy(grid)
    grid_setup(screen, grid, text_font)
    pygame.display.update()

    # game loop to maintain and quit the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                update_grid = insert(screen, (position[0]//60, position[1]//60), text_font, grid, update_grid, background_color)
            # check if the answer is correct
            if update_grid == solution:
                pygame.quit()
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def grid_setup(screen, grid, text_font):
    line_color = (0, 0, 0)
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(screen, line_color, (60*i + 60, 60), (60*i + 60, 600), 5)
            pygame.draw.line(screen, line_color, (60, 60*i + 60), (600, 60*i + 60), 5)
        else:
            pygame.draw.line(screen, line_color, (60*i + 60, 60), (60*i + 60, 600), 2)
            pygame.draw.line(screen, line_color, (60, 60*i + 60), (600, 60*i + 60), 2)
    
    for i in range (0, len(grid)):
        for j in range (0, len(grid[i])):
            if 1 <= grid[i][j] <= 9:
                value = text_font.render(str(grid[i][j]), True, (0,0,0))
                screen.blit(value, ((j+1)*60 + 23, (i+1)*60 + 19))

def insert(screen, position, text_font, grid, update_grid, background_color):
    shaded_color = (100, 100, 100)
    text_insert_color = (0, 0, 200)
    while True:
        if 1 <= position[0] <= 9 and 1 <= position[1] <= 9 and grid[position[1] - 1][position[0] - 1] == 0:
            for event in pygame.event.get():
                # # change the color into dark gray when selected
                pygame.draw.rect(screen, shaded_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                pygame.display.update()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return update_grid
                if event.type == pygame.KEYDOWN:
                    if event.key - 8 == 0: # checking with backspace (8 is the ascII number of 'backspace')
                        # replace the space with a rectangel with the same color as the background
                        pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        pygame.display.update()
                        update_grid[position[1] - 1][position[0] - 1] = event.key - 8
                        return update_grid
                    if 1 <= (event.key - 48) <= 9: # check input for 1-9
                        pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        value = text_font.render(str(event.key - 48), True, text_insert_color)
                        screen.blit(value, (position[0]*60 + 23, position[1]*60 + 20))
                        pygame.display.update()
                        update_grid[position[1] - 1][position[0] - 1] = event.key - 48
                        return update_grid
                    else: # if input a wrong letter, the grid stays the same as before
                        if 1 <= update_grid[position[1] - 1][position[0] - 1] <=9:
                            pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            value = text_font.render(str(update_grid[position[1] - 1][position[0] - 1]), True, text_insert_color)
                            screen.blit(value, (position[0]*60 + 23, position[1]*60 + 20))
                        else: 
                            pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        pygame.display.update()
                        return update_grid       
        else: 
            return update_grid


running()

