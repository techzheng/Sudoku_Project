import pygame, copy, time, random

background_color = (235, 235, 235)
text_color = (0, 0, 0)
line_color = (0, 0, 0)
shaded_color = (100, 100, 100)
text_insert_color = (0, 0, 200)


def running():
    background_color = (235, 235, 235)
    # initialize the pygame
    pygame.init()
    # create the screen with 660 pixel in width and 800 pixel in hight
    screen = pygame.display.set_mode((660,800))
    # text font, title and icon
    text_font = pygame.font.Font(pygame.font.get_default_font(), 30) # need adding a font file 
    # setup game caption and icon
    pygame.display.set_caption('Sudoku Game')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    # fill the window background color
    screen.fill(background_color)
    # call function to set up 9*9 grid
    grid = [[1,9,1,1,3,5,1,8,7],
            [8,1,1,1,9,1,1,5,1],
            [5,3,4,1,6,8,1,2,1],
            [9,7,8,2,1,3,4,6,5],
            [1,1,1,5,1,6,7,9,8],
            [6,1,5,8,7,9,1,1,1],
            [4,2,1,1,1,7,1,1,9],
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
    # copy another updating grid for varifing the answer
    update_grid = copy.deepcopy(grid)
    # run grid setup the draw the grid in the window
    grid_setup(screen, grid, text_font)
    pygame.display.update()
    # initialize the  initial time for timer
    t0 = time.time()
    # game loop to maintain and quit the window
    while True:
        # show timer
        game_clock(screen, text_font, t0)
        # capture every operation in the window
        for event in pygame.event.get():
            # if the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                # if the position is inside the grid, run insert function
                if 1 <= position[0]//60 <= 9 and 1 <= position[1]//60 <= 9:
                    update_grid = insert(screen, (position[0]//60, position[1]//60), text_font, grid, update_grid, background_color, t0)
                # if the position is inside the 'hint' button
                if 303 <= position[0] <= 365 and 700 <= position[1] <= 725:
                    grid, update_grid = hint(screen, grid, update_grid, solution, text_font, t0)
                
                    
            # check if the answer is correct
            if update_grid == solution:
                t_tot = time.time() - t0
                win(screen, t_tot, text_font)
            # if the game is quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def grid_setup(screen, grid, text_font):
    line_color = (0, 0, 0)
    text_color = (0, 0, 0)
    # setup 9*9 grid
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(screen, line_color, (60*i + 60, 60), (60*i + 60, 600), 5)
            pygame.draw.line(screen, line_color, (60, 60*i + 60), (600, 60*i + 60), 5)
        else:
            pygame.draw.line(screen, line_color, (60*i + 60, 60), (60*i + 60, 600), 2)
            pygame.draw.line(screen, line_color, (60, 60*i + 60), (600, 60*i + 60), 2)
    # setup numbers
    for i in range (0, len(grid)):
        for j in range (0, len(grid[i])):
            if 1 <= grid[i][j] <= 9:
                value_1 = text_font.render(str(grid[i][j]), True, text_color)
                screen.blit(value_1, ((j+1)*60 + 23, (i+1)*60 + 19))
    # setup hint button
    value_2 = text_font.render('Hint', True, text_color)
    screen.blit(value_2, (303, 700))

def insert(screen, position, text_font, grid, update_grid, background_color, t0):
    shaded_color = (100, 100, 100)
    text_insert_color = (0, 0, 200)
    while True:
        game_clock(screen, text_font, t0)
        if 1 <= position[0] <= 9 and 1 <= position[1] <= 9 and grid[position[1] - 1][position[0] - 1] == 0:
            for event in pygame.event.get():
                # # change the color into dark gray when selected
                pygame.draw.rect(screen, shaded_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                if update_grid[position[1] - 1][position[0] - 1] != 0:
                    value = text_font.render(str(update_grid[position[1] - 1][position[0] - 1]), True, text_insert_color)
                    screen.blit(value, (position[0]*60 + 23, position[1]*60 + 20))
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
                        if 1 <= update_grid[position[1] - 1][position[0] - 1] <= 9:
                            pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            value = text_font.render(str(update_grid[position[1] - 1][position[0] - 1]), True, text_insert_color)
                            screen.blit(value, (position[0]*60 + 23, position[1]*60 + 20))
                        else: 
                            pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        pygame.display.update()
                        return update_grid 
                # change the selecting block when click to another block  
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # recover the original block into its background color
                    pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                    # if the original block is filled with a number, fill the block with it rather than only background color
                    if 1 <= update_grid[position[1] - 1][position[0] - 1] <= 9:
                        if grid[position[1] - 1][position[0] - 1] == 0:
                            value = text_font.render(str(update_grid[position[1] - 1][position[0] - 1]), True, text_insert_color)
                            screen.blit(value, (position[0]*60 + 23, position[1]*60 + 20))
                    pygame.display.update()
                    # run the insert function again using the different position and no operation to the update_grid
                    position_ = pygame.mouse.get_pos()
                    update_grid = insert(screen, (position_[0]//60, position_[1]//60), text_font, grid, update_grid, background_color, t0) 
                    return update_grid   
        else: 
            return update_grid

def game_clock(screen, text_font, t0):
    pygame.draw.rect(screen, background_color, (60, 610, 600, 70))
    t = time.time() - t0
    value = text_font.render('Time(s): ' + (str(round(t, 1))), True, text_color)
    screen.blit(value, (60, 610))
    pygame.display.update()

def win(screen, t_tot, text_font):
    print('here')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        screen.fill(background_color)
        value_1 = text_font.render('WIN!', True, text_color)
        value_2 = text_font.render('Time: ' + (str(round(t_tot, 1))) + 's', True, text_color)
        screen.blit(value_1, (280, 250))
        screen.blit(value_2, (240, 350))
        pygame.display.update()

def hint(screen, grid, update_grid, solution, text_font, t0):
    game_clock(screen, text_font, t0)
    hint_pool = []
    for i in range(0, len(update_grid)):
        for j in range(0, len(update_grid[i])):
            if grid[i][j] == 0:
                if update_grid[i][j] != solution[i][j]:
                    hint_pool.append([i, j])
    hint_loc = random.choice(hint_pool)
    update_grid[hint_loc[0]][hint_loc[1]] = solution[hint_loc[0]][hint_loc[1]]
    grid[hint_loc[0]][hint_loc[1]] = solution[hint_loc[0]][hint_loc[1]]
    pygame.draw.rect(screen, background_color, (((hint_loc[1] + 1)*60 + 5, (hint_loc[0] + 1)*60 + 5, 60 - 8, 60 - 8)))
    value = text_font.render(str(update_grid[hint_loc[0]][hint_loc[1]]), True, (255, 0, 0))
    screen.blit(value, ((hint_loc[1] + 1)*60 + 23, (hint_loc[0] + 1)*60 + 20))
    pygame.display.update()
    return grid, update_grid

running()

