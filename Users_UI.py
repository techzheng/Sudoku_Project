from os import stat_result
from numpy import diff, int_
import pygame, copy, time, random
import generate_sudo
import read_level

def home_window(score):
    background_color = (235, 235, 235)
    text_color = (0, 0, 0)
    line_color = (0, 0, 0)
    shaded_color = (100, 100, 100)
    grid_color = (180, 180, 180)
    hint_text_color = (0, 150, 0)
    text_insert_color = (0, 0, 200)
    # initialize the pygame
    pygame.init()
    # create the screen with 660 pixel in width and 800 pixel in hight
    screen = pygame.display.set_mode((660,800))
    # title font
    title_font = pygame.font.Font(pygame.font.get_default_font(), 40) # need adding a font file 
    # text font, title and icon
    text_font = pygame.font.Font(pygame.font.get_default_font(), 30) # need adding a font file 
    # setup game caption and icon
    pygame.display.set_caption('Sudoku Game')
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    # fill the window background color
    screen.fill(background_color)
    # print text on screen
    value_1 = title_font.render(str('SUDOKU'), True, text_color)
    value_2 = text_font.render(str('Start game'), True, text_color)
    value_3 = text_font.render(str('Quit'), True, text_color)
    screen.blit(value_1, (230, 150))
    screen.blit(value_2, (240, 450))
    screen.blit(value_3, (285, 650))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                if 240 <= position[0] <= 410 and 450 <= position[1] <= 475:
                    diff_puzzle_window(screen, background_color, title_font, text_font, text_color, score, grid_color, hint_text_color, line_color, shaded_color, text_insert_color)
                if 285 <= position[0] <= 365 and 650 <= position[1] <= 675:
                    pygame.quit()
                    return
            if event.type == pygame.QUIT:
                    pygame.quit()
                    return

def diff_puzzle_window(screen, background_color, title_font, text_font, text_color, score, grid_color, hint_text_color, line_color, shaded_color, text_insert_color):

    # fill the window background color
    screen.fill(background_color)
    value_1 = title_font.render(str('Select your difficulty'), True, text_color)
    value_2 = text_font.render(str('1'), True, text_color)
    value_3 = text_font.render(str('2'), True, text_color)
    value_4 = text_font.render(str('3'), True, text_color)
    value_5 = text_font.render(str('4'), True, text_color)
    value_6 = text_font.render(str('5'), True, text_color)
    screen.blit(value_1, (130, 150))
    screen.blit(value_2, (326, 250))
    screen.blit(value_3, (326, 350))
    screen.blit(value_4, (326, 450))
    screen.blit(value_5, (326, 550))
    screen.blit(value_6, (326, 650))
    pygame.display.update()
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                if 326 <= position[0] <= 343 and 250 <= position[1] <= 275:
                    diff = 1
                    status = False
                if 326 <= position[0] <= 343 and 350 <= position[1] <= 375:
                    diff = 2
                    status = False
                if 326 <= position[0] <= 343 and 450 <= position[1] <= 475:
                    diff = 3
                    status = False
                if 326 <= position[0] <= 343 and 550 <= position[1] <= 575:
                    diff = 4
                    status = False
                if 326 <= position[0] <= 343 and 650 <= position[1] <= 675:
                    diff = 5
                    status = False
            if event.type == pygame.QUIT:
                    pygame.quit()
                    return

    screen.fill(background_color)
    value_1 = title_font.render(str('Select your puzzle'), True, text_color)
    value_2 = text_font.render(str('1'), True, text_color)
    value_3 = text_font.render(str('2'), True, text_color)
    value_4 = text_font.render(str('3'), True, text_color)
    value_5 = text_font.render(str('4'), True, text_color)
    value_6 = text_font.render(str('5'), True, text_color)
    value_7 = text_font.render(str('Endless'), True, text_color)
    screen.blit(value_1, (140, 150))
    screen.blit(value_2, (326, 250))
    screen.blit(value_3, (326, 330))
    screen.blit(value_4, (326, 410))
    screen.blit(value_5, (326, 490))
    screen.blit(value_6, (326, 570))
    screen.blit(value_7, (275, 650))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                if 326 <= position[0] <= 343 and 250 <= position[1] <= 275:
                    puzzle = 1
                if 326 <= position[0] <= 343 and 330 <= position[1] <= 355:
                    puzzle = 2
                if 326 <= position[0] <= 343 and 410 <= position[1] <= 435:
                    puzzle = 3
                if 326 <= position[0] <= 343 and 490 <= position[1] <= 515:
                    puzzle = 4
                if 326 <= position[0] <= 343 and 570 <= position[1] <= 595:
                    puzzle = 5
                if 275 <= position[0] <= 393 and 650 <= position[1] <= 675:
                    puzzle = 6
                sudoku_window(screen, score, text_font, grid_color, background_color, text_color, hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
            if event.type == pygame.QUIT:
                    pygame.quit()
                    return

def sudoku_window(screen, score, text_font, grid_color, background_color, text_color, hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle):
    if puzzle == 6:
        # call function to set up 9*9 grid
        solution = generate_sudo.generate_board_new(generate_sudo.generate_board_origin())
        grid = generate_sudo.generate_puzzle(solution, diff)
    if 1 <= puzzle <= 5:
        solution = read_level.decrypt(diff, puzzle)[0]
        grid = read_level.decrypt(diff, puzzle)[1]
    # copy another updating grid for varifing the answer
    update_grid = copy.deepcopy(grid)
    # fill the window background color
    screen.fill(background_color)
    # run grid setup the draw the grid in the window
    grid_setup(screen, grid, text_font, grid_color, line_color, text_color)
    # initialize dark location
    dark_grid_loc = [[1, 1],[1, 2],[1, 3],[2, 1],[2, 2],[2, 3],[3, 1],[3, 2],[3, 3],
                     [7, 1],[7, 2],[7, 3],[8, 1],[8, 2],[8, 3],[9, 1],[9, 2],[9, 3],
                     [4, 4],[4, 5],[4, 6],[5, 4],[5, 5],[5, 6],[6, 4],[6, 5],[6, 6],
                     [1, 7],[1, 8],[1, 9],[2, 7],[2, 8],[2, 9],[3, 7],[3, 8],[3, 9],
                     [7, 7],[7, 8],[7, 9],[8, 7],[8, 8],[8, 9],[9, 7],[9, 8],[9, 9]]
    pygame.display.update()
    # initialize the  initial time for timer
    t0 = time.time()
    # game loop to maintain and quit the window
    while True:
        # show timer
        game_clock(screen, text_font, t0, background_color, text_color)
        # show score
        pygame.draw.rect(screen, background_color, (60, 655, 600, 25))
        value = text_font.render(('Score(pt): ' + str(score)), True, text_color)
        screen.blit(value, (60, 655))
        # capture every operation in the window
        for event in pygame.event.get():
            # if the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                # if the position is inside the grid, run insert function
                if 1 <= position[0]//60 <= 9 and 1 <= position[1]//60 <= 9:
                    update_grid = insert(screen, (position[0]//60, position[1]//60), text_font, grid, update_grid, background_color, t0, dark_grid_loc, grid_color, text_color, shaded_color, text_insert_color)
                # if the position is inside the 'hint' button
                if 303 <= position[0] <= 365 and 700 <= position[1] <= 725:
                    grid, update_grid, score = hint(screen, grid, update_grid, solution, text_font, t0, dark_grid_loc, grid_color, background_color, hint_text_color, text_color, score)
            # check if the answer is correct
            if puzzle == 6:
                if update_grid.all() == solution.all():
                    t_tot = time.time() - t0
                    score = win_window_endless(screen, t_tot, text_font, background_color, text_color, score, grid_color, hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
            if 1 <= puzzle <= 5 :
                if update_grid == solution:
                    t_tot = time.time() - t0
                    score = win_window_single(screen, t_tot, text_font, background_color, text_color, score, diff)
            # if the game is quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def grid_setup(screen, grid, text_font, grid_color, line_color, text_color):
    # setup background color of grid
    pygame.draw.rect(screen, grid_color, (60, 60, 180, 180))
    pygame.draw.rect(screen, grid_color, (420, 60, 180, 180))
    pygame.draw.rect(screen, grid_color, (240, 240, 180, 180))
    pygame.draw.rect(screen, grid_color, (60, 420, 180, 180))
    pygame.draw.rect(screen, grid_color, (420, 420, 180, 180))
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

def insert(screen, position, text_font, grid, update_grid, background_color, t0, dark_grid_loc, grid_color, text_color, shaded_color, text_insert_color):
    while True:
        game_clock(screen, text_font, t0, background_color, text_color)
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
                        if [position[0], position[1]] in dark_grid_loc:
                            pygame.draw.rect(screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        else:
                            pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        pygame.display.update()
                        update_grid[position[1] - 1][position[0] - 1] = event.key - 8
                        return update_grid
                    if 1 <= (event.key - 48) <= 9: # check input for 1-9
                        if [position[0], position[1]] in dark_grid_loc:
                            pygame.draw.rect(screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        else:
                            pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        value = text_font.render(str(event.key - 48), True, text_insert_color)
                        screen.blit(value, (position[0]*60 + 23, position[1]*60 + 20))
                        pygame.display.update()
                        update_grid[position[1] - 1][position[0] - 1] = event.key - 48
                        return update_grid
                    else: # if input a wrong letter, the grid stays the same as before
                        if 1 <= update_grid[position[1] - 1][position[0] - 1] <= 9:
                            if [position[0], position[1]] in dark_grid_loc:
                                pygame.draw.rect(screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            else:
                                pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            value = text_font.render(str(update_grid[position[1] - 1][position[0] - 1]), True, text_insert_color)
                            screen.blit(value, (position[0]*60 + 23, position[1]*60 + 20))
                        else: 
                            if [position[0], position[1]] in dark_grid_loc:
                                pygame.draw.rect(screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            else:
                                pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        pygame.display.update()
                        return update_grid 
                # change the selecting block when click to another block  
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # recover the original block into its background color
                    if [position[0], position[1]] in dark_grid_loc:
                        pygame.draw.rect(screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                    else:
                        pygame.draw.rect(screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                    # if the original block is filled with a number, fill the block with it rather than only background color
                    if 1 <= update_grid[position[1] - 1][position[0] - 1] <= 9:
                        if grid[position[1] - 1][position[0] - 1] == 0:
                            value = text_font.render(str(update_grid[position[1] - 1][position[0] - 1]), True, text_insert_color)
                            screen.blit(value, (position[0]*60 + 23, position[1]*60 + 20))
                    pygame.display.update()
                    # run the insert function again using the different position and no operation to the update_grid
                    position_ = pygame.mouse.get_pos()
                    update_grid = insert(screen, (position_[0]//60, position_[1]//60), text_font, grid, update_grid, background_color, t0, dark_grid_loc, grid_color, text_color, shaded_color, text_insert_color) 
                    return update_grid   
        else: 
            return update_grid

def game_clock(screen, text_font, t0, background_color, text_color):
    pygame.draw.rect(screen, background_color, (60, 610, 600, 25))
    t = time.time() - t0
    value = text_font.render('Time(s): ' + (str(round(t, 1))), True, text_color)
    screen.blit(value, (60, 610))
    pygame.display.update()

def win_window_single(screen, t_tot, text_font, background_color, text_color, score, diff):
    score_earned = time_to_score(t_tot, score, diff)
    score = score_earned + score
    while True:
        screen.fill(background_color)
        value_1 = text_font.render('WIN!', True, text_color)
        value_2 = text_font.render('Time: ' + (str(round(t_tot, 1))) + 's', True, text_color)
        value_3 = text_font.render('Score earned: ' + (str(score_earned)) + 'pt', True, text_color)
        value_4 = text_font.render('Total score: ' + (str(score)) + 'pt', True, text_color)
        value_5 = text_font.render('Return to menu', True, text_color)
        value_6 = text_font.render('Quit', True, text_color)
        screen.blit(value_1, (278, 80))
        screen.blit(value_2, (240, 180))
        screen.blit(value_3, (185, 280))
        screen.blit(value_4, (195, 380))
        screen.blit(value_5, (210, 550))
        screen.blit(value_6, (285, 650))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                if 210 <= position[0] <= 440 and 550 <= position[1] <= 575:
                    home_window(score)
                if 285 <= position[0] <= 363 and 650 <= position[1] <= 675:
                    pygame.quit()
                    return

def win_window_endless(screen, t_tot, text_font, background_color, text_color, score, grid_color, hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle):
    score_earned = time_to_score(t_tot, score, diff)
    score = score_earned + score
    while True:
        screen.fill(background_color)
        value_1 = text_font.render('WIN!', True, text_color)
        value_2 = text_font.render('Time: ' + (str(round(t_tot, 1))) + 's', True, text_color)
        value_3 = text_font.render('Score earned: ' + (str(score_earned)) + 'pt', True, text_color)
        value_4 = text_font.render('Total score: ' + (str(score)) + 'pt', True, text_color)
        value_5 = text_font.render('Continue', True, text_color)
        value_6 = text_font.render('Return to menu', True, text_color)
        value_7 = text_font.render('Quit', True, text_color)
        screen.blit(value_1, (278, 80))
        screen.blit(value_2, (240, 180))
        screen.blit(value_3, (185, 280))
        screen.blit(value_4, (195, 380))
        screen.blit(value_5, (250, 510))
        screen.blit(value_6, (210, 580))
        screen.blit(value_7, (285, 650))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                if 250 <= position[0] <= 385 and 510 <= position[1] <= 535:
                    sudoku_window(screen, score, text_font, grid_color, background_color, text_color, hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
                if 210 <= position[0] <= 440 and 580 <= position[1] <= 605:
                    home_window(score)
                if 285 <= position[0] <= 363 and 650 <= position[1] <= 675:
                    pygame.quit()
                    return

def hint(screen, grid, update_grid, solution, text_font, t0, dark_grid_loc, grid_color, background_color, hint_text_color, text_color, score):
    game_clock(screen, text_font, t0, background_color, text_color)
    score = score - 1
    if score < 0:
        return grid, update_grid, score + 1
    hint_pool = []
    for i in range(0, len(update_grid)):
        for j in range(0, len(update_grid[i])):
            if grid[i][j] == 0:
                if update_grid[i][j] != solution[i][j]:
                    hint_pool.append([i, j])
    hint_loc = random.choice(hint_pool)
    update_grid[hint_loc[0]][hint_loc[1]] = solution[hint_loc[0]][hint_loc[1]]
    grid[hint_loc[0]][hint_loc[1]] = solution[hint_loc[0]][hint_loc[1]]
    if [(hint_loc[1] + 1), (hint_loc[0] + 1)] in dark_grid_loc:
        pygame.draw.rect(screen, grid_color, (((hint_loc[1] + 1)*60 + 5, (hint_loc[0] + 1)*60 + 5, 60 - 8, 60 - 8)))
    else:
        pygame.draw.rect(screen, background_color, (((hint_loc[1] + 1)*60 + 5, (hint_loc[0] + 1)*60 + 5, 60 - 8, 60 - 8)))
    value = text_font.render(str(update_grid[hint_loc[0]][hint_loc[1]]), True, hint_text_color)
    screen.blit(value, ((hint_loc[1] + 1)*60 + 23, (hint_loc[0] + 1)*60 + 20))
    pygame.display.update()
    return grid, update_grid, score

def time_to_score(t_tot, score, diff):
    return 100

if __name__ == "__main__":
    home_window(score = 100)