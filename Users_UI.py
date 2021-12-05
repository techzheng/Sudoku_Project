from os import stat_result
from numpy import diff, int_
import pygame
import copy
import time
import random
import generate_sudo
import read_level



def home_window(score, curr_diff, curr_puzzle):
    """This function aims to gemerate the home window of the game where users can start and quit the game.

    Args:
        score (int): The points earned by users and can be consumed for the hints.
        curr_diff (int): The stored highest difficulty the user accomplish.
        curr_puzzle (int): The stored highest number of puzzle the user accomplish.
    """
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
    screen = pygame.display.set_mode((660, 800))
    # title font
    title_font = pygame.font.Font(
        pygame.font.get_default_font(), 40)  # need adding a font file
    # text font, title and icon
    text_font = pygame.font.Font(
        pygame.font.get_default_font(), 30)  # need adding a font file
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
    # while true loop to maintain the window
    while True:
        # get event of clicking mouse in game
        for event in pygame.event.get():
            # if the event type is clicking the left button of nouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # obtain the position of the mouse
                position = pygame.mouse.get_pos()
                # if click 'start game'
                if 240 <= position[0] <= 410 and 450 <= position[1] <= 475:
                    diff_puzzle_window(screen, background_color, title_font, text_font, text_color,
                                       score, grid_color, hint_text_color, line_color, shaded_color, text_insert_color, curr_diff, curr_puzzle)
                # if click 'quit game'
                if 285 <= position[0] <= 365 and 650 <= position[1] <= 675:
                    pygame.quit()
                    return
            # if quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                return


def diff_puzzle_window(screen, background_color, title_font, text_font, text_color, score, grid_color, hint_text_color, line_color, shaded_color, text_insert_color, curr_diff, curr_puzzle):
    """This function aims to create difficulty and level choosing window.

    Args:
        screen (pygame.Surface): The game window.
        background_color (tuple): The RGB value of the window background color.
        title_font (pygame.font.Font): Font of title.
        text_font (pygame.font.Font): Font of normal text.
        text_color (tuple): The RGB value of the text color.
        score (int): The points earned by users.
        grid_color (tuple): The RGB value of the dark grid color.
        hint_text_color (tuple): The RGB value of the hint text color.
        line_color (tuple): The RGB value of the line color.
        shaded_color (tuple): The RGB value of the selected grid color.
        text_insert_color (tuple): The RGB value of the inserted text color.
    """
    # fill the window background color
    screen.fill(background_color)
    # setup the text on the window
    value_1 = title_font.render(str('Select your difficulty'), True, text_color)
    for i in range(0,5):
        if i+1 <= curr_diff:
            color = text_color
        else:
            color = grid_color
        value = text_font.render(str(i+1), True, color)
        screen.blit(value, (326, 250 + 100*i))
    value_2 = text_font.render(str('Back'), True, text_color)
    # blit all text on the window
    screen.blit(value_1, (130, 150))
    screen.blit(value_2, (450, 700))
    pygame.display.update()
    # initialize a parameter that secure the text while true loop
    status = True
    # initialize difficulty
    diff = 0
    # while true loop to maintain the window
    while status:
        # get event of clicking mouse in game
        for event in pygame.event.get():
            # if the event type is clicking the left button of nouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # obtain the position of the mouse and give corresponding values to variables
                position = pygame.mouse.get_pos()
                # if clicking '1'
                if 326 <= position[0] <= 343 and 250 <= position[1] <= 275:
                    diff = 1
                    if diff <= curr_diff:
                        status = False  # set to false to jump out of the ifinity loop
                # if clicking '2'
                if 326 <= position[0] <= 343 and 350 <= position[1] <= 375:
                    diff = 2
                    if diff <= curr_diff:
                        status = False
                # if clicking '3'
                if 326 <= position[0] <= 343 and 450 <= position[1] <= 475:
                    diff = 3
                    if diff <= curr_diff:
                        status = False
                # if clicking '4'
                if 326 <= position[0] <= 343 and 550 <= position[1] <= 575:
                    diff = 4
                    if diff <= curr_diff:
                        status = False
                # if clicking '5'
                if 326 <= position[0] <= 343 and 650 <= position[1] <= 675:
                    diff = 5
                    if diff <= curr_diff:
                        status = False
                # if clicking on 'back', go back to the home window
                if 450 <= position[0] <= 525 and 700 <= position[1] <= 725:
                    home_window(score)
                
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    # fill the window background color
    screen.fill(background_color)
    # setup the text on the window
    value_3 = title_font.render(str('Select your puzzle'), True, text_color)
    for i in range(0,6):
        if diff == curr_diff:
            if i+1 <= curr_puzzle:
                color = text_color
            else:
                color = grid_color
        else:
            color = text_color
        if i < 5:
            value = text_font.render(str(i+1), True, color)
            screen.blit(value, (326, 250 + 80*i))
        else: 
            value = text_font.render(str('Endless'), True, color)
            screen.blit(value, (275, 250 + 80*i))
    value_4 = text_font.render(str('Back'), True, text_color)
    # blit all text on the window
    screen.blit(value_3, (140, 150))
    screen.blit(value_4, (450, 700))
    pygame.display.update()
    # while true loop to maintain the window
    while True:
        for event in pygame.event.get():
            # if the event type is clicking the left button of nouse, obtain the position and give corresponding values to variables
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                if 326 <= position[0] <= 343 and 250 <= position[1] <= 275:
                    puzzle = 1
                    if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                        sudoku_window(screen, score, text_font, grid_color, background_color, text_color,
                                    hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
                    
                if 326 <= position[0] <= 343 and 330 <= position[1] <= 355:
                    puzzle = 2
                    if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                        sudoku_window(screen, score, text_font, grid_color, background_color, text_color,
                                    hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
                if 326 <= position[0] <= 343 and 410 <= position[1] <= 435:
                    puzzle = 3
                    if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                        sudoku_window(screen, score, text_font, grid_color, background_color, text_color,
                                    hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
                if 326 <= position[0] <= 343 and 490 <= position[1] <= 515:
                    puzzle = 4
                    if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                        sudoku_window(screen, score, text_font, grid_color, background_color, text_color,
                                    hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
                if 326 <= position[0] <= 343 and 570 <= position[1] <= 595:
                    puzzle = 5
                    if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                        sudoku_window(screen, score, text_font, grid_color, background_color, text_color,
                                    hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
                if 275 <= position[0] <= 393 and 650 <= position[1] <= 675:
                    puzzle = 6
                    if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                        sudoku_window(screen, score, text_font, grid_color, background_color, text_color,
                                    hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
                # if click on 'back', start this function over
                if 450 <= position[0] <= 525 and 700 <= position[1] <= 725:
                    diff_puzzle_window(screen, background_color, title_font, text_font, text_color,
                                       score, grid_color, hint_text_color, line_color, shaded_color, text_insert_color, curr_diff, curr_puzzle)
            if event.type == pygame.QUIT:
                pygame.quit()
                return


def sudoku_window(screen, score, text_font, grid_color, background_color, text_color, hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle):
    """This function aims to gemerate the sudoku gaming window.

    Args:
        screen (pygame.Surface): The game window.
        score (int): The points earned by users.
        text_font (pygame.font.Font): Font of normal text.
        grid_color (tuple): The RGB value of the dark grid color.
        background_color (tuple): The RGB value of the window background color.
        text_color (tuple): The RGB value of the text color.
        hint_text_color (tuple): The RGB value of the hint text color.
        line_color (tuple): The RGB value of the line color.
        shaded_color (tuple): The RGB value of the selected grid color.
        text_insert_color (tuple): The RGB value of the inserted text color.
        diff (int): The difficulty selected by users.
        puzzle ([type]): The puzzle number selected by users.
    """
    if puzzle == 6:
        # call function to set up 9*9 grid
        solution = generate_sudo.generate_board_new(
            generate_sudo.generate_board_origin())
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
    dark_grid_loc = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3],
                     [7, 1], [7, 2], [7, 3], [8, 1], [8, 2], [
                         8, 3], [9, 1], [9, 2], [9, 3],
                     [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [
                         5, 6], [6, 4], [6, 5], [6, 6],
                     [1, 7], [1, 8], [1, 9], [2, 7], [2, 8], [
                         2, 9], [3, 7], [3, 8], [3, 9],
                     [7, 7], [7, 8], [7, 9], [8, 7], [8, 8], [8, 9], [9, 7], [9, 8], [9, 9]]
    pygame.display.update()
    # initialize the  initial time for timer
    t0 = time.time()
    # game loop to maintain and quit the window
    while True:
        # show timer
        game_clock(screen, text_font, t0, background_color, text_color)
        # show score
        pygame.draw.rect(screen, background_color, (60, 655, 600, 25))
        value = text_font.render(
            ('Score(pt): ' + str(score)), True, text_color)
        screen.blit(value, (60, 655))
        # capture every operation in the window
        for event in pygame.event.get():
            # if the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                # if the position is inside the grid, run insert function
                if 1 <= position[0]//60 <= 9 and 1 <= position[1]//60 <= 9:
                    update_grid = insert(screen, (position[0]//60, position[1]//60), text_font, grid, update_grid,
                                         background_color, t0, dark_grid_loc, grid_color, text_color, shaded_color, text_insert_color)
                # if the position is inside the 'hint' button
                if 303 <= position[0] <= 365 and 700 <= position[1] <= 725:
                    grid, update_grid, score = hint(screen, grid, update_grid, solution, text_font, t0,
                                                    dark_grid_loc, grid_color, background_color, hint_text_color, text_color, score)
                # if the position is inside the 'back' button
                if 450 <= position[0] <= 525 and 700 <= position[1] <= 725:
                    home_window(score)
            # check if the answer is correct
            # when in 'endless' mode
            if puzzle == 6:
                if update_grid.all() == solution.all():
                    t_tot = time.time() - t0
                    score = win_window_endless(screen, t_tot, text_font, background_color, text_color, score,
                                               grid_color, hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
            # when in normal mode
            if 1 <= puzzle <= 5:
                if update_grid == solution:
                    t_tot = time.time() - t0
                    score = win_window_single(
                        screen, t_tot, text_font, background_color, text_color, score, diff, grid_color, hint_text_color, line_color, shaded_color, text_insert_color, puzzle)
            # if the game is quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return


def grid_setup(screen, grid, text_font, grid_color, line_color, text_color):
    """This function amis to gemerate a game board on the window.

    Args:
        screen (pygame.Surface): The game window.
        grid (list): The generated sudoku puzzle problem list.
        text_font (pygame.font.Font): Font of normal text.
        grid_color (tuple): The RGB value of the dark grid color.
        line_color (tuple): The RGB value of the line color.
        text_color (tuple): The RGB value of the text color.
    """
    # setup background color of grid
    pygame.draw.rect(screen, grid_color, (60, 60, 180, 180))
    pygame.draw.rect(screen, grid_color, (420, 60, 180, 180))
    pygame.draw.rect(screen, grid_color, (240, 240, 180, 180))
    pygame.draw.rect(screen, grid_color, (60, 420, 180, 180))
    pygame.draw.rect(screen, grid_color, (420, 420, 180, 180))
    # setup 9*9 grid by drawing 10 lines
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(screen, line_color,
                             (60*i + 60, 60), (60*i + 60, 600), 5)
            pygame.draw.line(screen, line_color,
                             (60, 60*i + 60), (600, 60*i + 60), 5)
        else:
            pygame.draw.line(screen, line_color,
                             (60*i + 60, 60), (60*i + 60, 600), 2)
            pygame.draw.line(screen, line_color,
                             (60, 60*i + 60), (600, 60*i + 60), 2)
    # write numbers inside the grid
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if 1 <= grid[i][j] <= 9:
                value_1 = text_font.render(str(grid[i][j]), True, text_color)
                screen.blit(value_1, ((j+1)*60 + 23, (i+1)*60 + 19))
    # setup hint button
    value_2 = text_font.render('Hint', True, text_color)
    screen.blit(value_2, (303, 700))
    # setup back button
    value_3 = text_font.render(str('Back'), True, text_color)
    screen.blit(value_3, (450, 700))


def insert(screen, position, text_font, grid, update_grid, background_color, t0, dark_grid_loc, grid_color, text_color, shaded_color, text_insert_color):
    """This function aims to realize thr insert function.

    Args:
        screen (pygame.Surface): The game window.
        position (list): The position of the mouse when clicked.
        text_font (pygame.font.Font): Font of normal text.
        grid (list): The generated sudoku puzzle problem list.
        update_grid (list): The updated sudoku number list according to users filling-in.
        background_color (tuple): The RGB value of the window background color.
        t0 (float): The initial time when a puzzle starts.
        dark_grid_loc (list): The coordination of where the dark background is.
        grid_color (tuple): The RGB value of the dark grid color.
        text_color (tuple): The RGB value of the text color.
        shaded_color (tuple): The RGB value of the selected grid color.
        text_insert_color (tuple): The RGB value of the inserted text color.

    Returns:
        update_grid (list): The updated sudoku number list according to users filling-in.
    """
    while True:
        game_clock(screen, text_font, t0, background_color, text_color)
        if 1 <= position[0] <= 9 and 1 <= position[1] <= 9 and grid[position[1] - 1][position[0] - 1] == 0:
            for event in pygame.event.get():
                # # change the color into dark gray when selected
                pygame.draw.rect(
                    screen, shaded_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                if update_grid[position[1] - 1][position[0] - 1] != 0:
                    value = text_font.render(
                        str(update_grid[position[1] - 1][position[0] - 1]), True, text_insert_color)
                    screen.blit(
                        value, (position[0]*60 + 23, position[1]*60 + 20))
                pygame.display.update()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return update_grid
                if event.type == pygame.KEYDOWN:
                    # checking with backspace (8 is the ascII number of 'backspace')
                    if event.key - 8 == 0:
                        # replace the space with a rectangel with the same color as the background
                        if [position[0], position[1]] in dark_grid_loc:
                            pygame.draw.rect(
                                screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        else:
                            pygame.draw.rect(
                                screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        pygame.display.update()
                        update_grid[position[1] -
                                    1][position[0] - 1] = event.key - 8
                        return update_grid
                    if 1 <= (event.key - 48) <= 9:  # check input for 1-9
                        if [position[0], position[1]] in dark_grid_loc:
                            pygame.draw.rect(
                                screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        else:
                            pygame.draw.rect(
                                screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        value = text_font.render(
                            str(event.key - 48), True, text_insert_color)
                        screen.blit(
                            value, (position[0]*60 + 23, position[1]*60 + 20))
                        pygame.display.update()
                        update_grid[position[1] -
                                    1][position[0] - 1] = event.key - 48
                        return update_grid
                    if event.key == pygame.K_KP1 or event.key == pygame.K_KP2 or event.key == pygame.K_KP3 or event.key == pygame.K_KP4 or event.key == pygame.K_KP5 or event.key == pygame.K_KP6 or event.key == pygame.K_KP7 or event.key == pygame.K_KP8 or event.key == pygame.K_KP9:  # check input for 1-9
                        if [position[0], position[1]] in dark_grid_loc:
                            pygame.draw.rect(
                                screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        else:
                            pygame.draw.rect(
                                screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        if event.key == pygame.K_KP1:
                            num = 1
                        elif event.key == pygame.K_KP2:
                            num = 2
                        elif event.key == pygame.K_KP3:
                            num = 3
                        elif event.key == pygame.K_KP4:
                            num = 4
                        elif event.key == pygame.K_KP5:
                            num = 5
                        elif event.key == pygame.K_KP6:
                            num = 6
                        elif event.key == pygame.K_KP7:
                            num = 7
                        elif event.key == pygame.K_KP8:
                            num = 8
                        elif event.key == pygame.K_KP9:
                            num = 9
                        value = text_font.render(
                            str(num), True, text_insert_color)
                        screen.blit(
                            value, (position[0]*60 + 23, position[1]*60 + 20))
                        pygame.display.update()
                        update_grid[position[1] -
                                    1][position[0] - 1] = num
                        return update_grid
                    else:  # if input a wrong letter, the grid stays the same as before
                        if 1 <= update_grid[position[1] - 1][position[0] - 1] <= 9:
                            if [position[0], position[1]] in dark_grid_loc:
                                pygame.draw.rect(
                                    screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            else:
                                pygame.draw.rect(
                                    screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            value = text_font.render(
                                str(update_grid[position[1] - 1][position[0] - 1]), True, text_insert_color)
                            screen.blit(
                                value, (position[0]*60 + 23, position[1]*60 + 20))
                        else:
                            if [position[0], position[1]] in dark_grid_loc:
                                pygame.draw.rect(
                                    screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            else:
                                pygame.draw.rect(
                                    screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        pygame.display.update()
                        return update_grid
                # change the selecting block after click to another block
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # recover the original block into its background color
                    if [position[0], position[1]] in dark_grid_loc:
                        pygame.draw.rect(
                            screen, grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                    else:
                        pygame.draw.rect(
                            screen, background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                    # if the original block is filled with a number, fill the block with it rather than only background color
                    if 1 <= update_grid[position[1] - 1][position[0] - 1] <= 9:
                        if grid[position[1] - 1][position[0] - 1] == 0:
                            value = text_font.render(
                                str(update_grid[position[1] - 1][position[0] - 1]), True, text_insert_color)
                            screen.blit(
                                value, (position[0]*60 + 23, position[1]*60 + 20))
                    pygame.display.update()
                    # run the insert function again using the different position and no operation to the update_grid
                    position_ = pygame.mouse.get_pos()
                    update_grid = insert(screen, (position_[0]//60, position_[1]//60), text_font, grid, update_grid,
                                         background_color, t0, dark_grid_loc, grid_color, text_color, shaded_color, text_insert_color)
                    return update_grid
        else:
            return update_grid


def game_clock(screen, text_font, t0, background_color, text_color):
    """This function aims to realize the timing and display the real-time click on the screen.

    Args:
        screen (pygame.Surface): The game window.
        text_font (pygame.font.Font): Font of normal text.
        t0 (float): The initial time when a puzzle starts.
        background_color (tuple): The RGB value of the window background color.
        text_color (tuple): The RGB value of the text color.
    """
    pygame.draw.rect(screen, background_color, (60, 610, 600, 25))
    t = time.time() - t0
    value = text_font.render(
        'Time(s): ' + (str(round(t, 1))), True, text_color)
    screen.blit(value, (60, 610))
    pygame.display.update()


def win_window_single(screen, t_tot, text_font, background_color, text_color, score, diff, grid_color, hint_text_color, line_color, shaded_color, text_insert_color, puzzle):
    """This function amis to create a winning window if the puzzle is NOT a endless mode.

    Args:
        screen (pygame.Surface): The game window.
        t_tot (float): The time consumed when doing one puzzle.
        text_font (pygame.font.Font): Font of normal text.
        background_color (tuple): The RGB value of the window background color.
        text_color (tuple): The RGB value of the text color.
        score (int): The points earned by users.
        diff (int): The difficulty selected by users.
        grid_color (tuple): The RGB value of the dark grid color.
        hint_text_color (tuple): The RGB value of the hint text color.
        line_color (tuple): The RGB value of the line color.
        shaded_color (tuple): The RGB value of the selected grid color.
        text_insert_color (tuple): The RGB value of the inserted text color.
        puzzle (int): The puzzle number selected by users.
    """
    score_earned = time_to_score(t_tot, score, diff)
    score = score_earned + score
    while True:
        screen.fill(background_color)
        value_1 = text_font.render('WIN!', True, text_color)
        value_2 = text_font.render(
            'Time: ' + (str(round(t_tot, 1))) + 's', True, text_color)
        value_3 = text_font.render(
            'Score earned: ' + (str(score_earned)) + 'pt', True, text_color)
        value_4 = text_font.render(
            'Total score: ' + (str(score)) + 'pt', True, text_color)
        value_5 = text_font.render('Next level', True, text_color)
        value_6 = text_font.render('Return to menu', True, text_color)
        value_7 = text_font.render('Quit', True, text_color)
        screen.blit(value_1, (278, 50))
        screen.blit(value_2, (240, 150))
        screen.blit(value_3, (185, 250))
        screen.blit(value_4, (195, 350))
        screen.blit(value_5, (245, 450))
        screen.blit(value_6, (210, 550))
        screen.blit(value_7, (285, 650))
        if diff == 5 and puzzle == 5:
            pygame.draw.rect(screen, background_color, (245, 450, 145, 75))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                if 210 <= position[0] <= 440 and 550 <= position[1] <= 575:
                    home_window(score)
                if 245 <= position[0] <= 390 and 450 <= position[1] <= 475:
                    if puzzle <= 4:
                        puzzle += 1
                    elif puzzle == 5:
                        diff += 1
                        puzzle = 1
                    if diff <= 5:
                        sudoku_window(screen, score, text_font, grid_color, background_color, text_color, hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
                if 285 <= position[0] <= 363 and 650 <= position[1] <= 675:
                    pygame.quit()
                    return


def win_window_endless(screen, t_tot, text_font, background_color, text_color, score, grid_color, hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle):
    """This function amis to create a winning window if the puzzle IS a endless mode.

    Args:
        screen (pygame.Surface): The game window.
        t_tot (float): The time consumed when doing one puzzle.
        text_font (pygame.font.Font): Font of normal text.
        background_color (tuple): The RGB value of the window background color.
        text_color (tuple): The RGB value of the text color.
        score (int): The points earned by users.
        grid_color (tuple): The RGB value of the dark grid color.
        hint_text_color (tuple): The RGB value of the hint text color.
        line_color (tuple): The RGB value of the line color.
        shaded_color (tuple): The RGB value of the selected grid color.
        text_insert_color (tuple): The RGB value of the inserted text color.
        diff (int): The difficulty selected by users.
        puzzle (int): The puzzle number selected by users.
    """
    score_earned = time_to_score(t_tot, score, diff)
    score = score_earned + score
    while True:
        screen.fill(background_color)
        value_1 = text_font.render('WIN!', True, text_color)
        value_2 = text_font.render(
            'Time: ' + (str(round(t_tot, 1))) + 's', True, text_color)
        value_3 = text_font.render(
            'Score earned: ' + (str(score_earned)) + 'pt', True, text_color)
        value_4 = text_font.render(
            'Total score: ' + (str(score)) + 'pt', True, text_color)
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
                    sudoku_window(screen, score, text_font, grid_color, background_color, text_color,
                                  hint_text_color, line_color, shaded_color, text_insert_color, diff, puzzle)
                if 210 <= position[0] <= 440 and 580 <= position[1] <= 605:
                    home_window(score)
                if 285 <= position[0] <= 363 and 650 <= position[1] <= 675:
                    pygame.quit()
                    return


def hint(screen, grid, update_grid, solution, text_font, t0, dark_grid_loc, grid_color, background_color, hint_text_color, text_color, score):
    """This function aims to realize the hint for the puzzle and a number of scores will be consumed.

    Args:
        screen (pygame.Surface): The game window.
        grid (list): The generated sudoku puzzle problem list.
        update_grid (list): The updated sudoku number list according to users filling-in.
        solution (list): The solution of the sudoku puzzle.
        t0 (float): The initial time when a puzzle starts.
        dark_grid_loc (list): The coordination of where the dark background is.
        grid_color (tuple): The RGB value of the dark grid color.
        background_color (tuple): The RGB value of the window background color.
        hint_text_color (tuple): The RGB value of the hint text color.
        text_color (tuple): The RGB value of the text color.
        score (int): The points earned by users.

    Returns:
        grid (list): The generated sudoku puzzle problem list.
        update_grid (list): The updated sudoku number list according to users filling-in.
        score (int): The points earned by users.
    """
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
        pygame.draw.rect(screen, grid_color, ((
            (hint_loc[1] + 1)*60 + 5, (hint_loc[0] + 1)*60 + 5, 60 - 8, 60 - 8)))
    else:
        pygame.draw.rect(screen, background_color, ((
            (hint_loc[1] + 1)*60 + 5, (hint_loc[0] + 1)*60 + 5, 60 - 8, 60 - 8)))
    value = text_font.render(
        str(update_grid[hint_loc[0]][hint_loc[1]]), True, hint_text_color)
    screen.blit(value, ((hint_loc[1] + 1)*60 + 23, (hint_loc[0] + 1)*60 + 20))
    pygame.display.update()
    return grid, update_grid, score


def time_to_score(t_tot, score, diff):
    """This function aims to calculate the earned score when a puzzle is finished

    Args:
        t_tot (float): The time consumed when doing one puzzle.
        score (int): The points earned by users.
        diff (int): The difficulty selected by users.
    Returns:
        add_score (int): The calculated earned score.
    """
    add_score = 100
    if add_score + score > 9999:
        add_score = 9999 - score
    return add_score


if __name__ == "__main__":
    home_window(score = 100, curr_diff=4, curr_puzzle=2)
