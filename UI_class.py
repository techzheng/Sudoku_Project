import pygame
import copy
import time
import random
import generate_sudo
import read_level
import start_game


class UI:
    """The UI class aims to establish all the game window operation gy using the pygame pachage.
    """

    def __init__(self):
        """This funtion aims to initialize the global variables.
        """
        # initialize RGB values for involved colors
        self.background_color = (235, 235, 235)
        self.text_color = (0, 0, 0)
        self.line_color = (0, 0, 0)
        self.shaded_color = (100, 100, 100)
        self.grid_color = (180, 180, 180)
        self.hint_text_color = (0, 150, 0)
        self.text_insert_color = (0, 0, 200)
        # initialize dark location
        self.dark_grid_loc = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3],
                              [7, 1], [7, 2], [7, 3], [8, 1], [8, 2], [
            8, 3], [9, 1], [9, 2], [9, 3],
            [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [
            5, 6], [6, 4], [6, 5], [6, 6],
            [1, 7], [1, 8], [1, 9], [2, 7], [2, 8], [
            2, 9], [3, 7], [3, 8], [3, 9],
            [7, 7], [7, 8], [7, 9], [8, 7], [8, 8], [8, 9], [9, 7], [9, 8], [9, 9]]
        # initialize the pygame
        pygame.init()
        # initialize the screen with 660 pixel in width and 800 pixel in hight
        self.screen = pygame.display.set_mode((660, 800))
        # initialize title font
        self.title_font = pygame.font.Font('verdana.ttf', 40)
        # initialize text font
        self.text_font = pygame.font.Font('verdana.ttf', 30)
        # initialize icon file
        self.icon = pygame.image.load('icon.png')

    def home_window(self, score, curr_diff, curr_puzzle, username):
        """This function aims to gemerate the home window of the game where users can start and quit the game.

        Args:
            score (int): The points earned by users and can be consumed for the hints.
            curr_diff (int): The stored highest difficulty the user accomplish.
            curr_puzzle (int): The stored highest number of puzzle the user accomplish.
            username (str): The input username to locate saving file.
        """
        # setup game caption and icon
        pygame.display.set_caption('Sudoku Game')
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        # fill the window background color
        self.screen.fill(self.background_color)
        # print text on screen
        value_1 = self.title_font.render(str('SUDOKU'), True, self.text_color)
        value_2 = self.text_font.render(
            str('Start game'), True, self.text_color)
        value_3 = self.text_font.render(str('Quit'), True, self.text_color)
        self.screen.blit(value_1, (230, 150))
        self.screen.blit(value_2, (240, 450))
        self.screen.blit(value_3, (285, 650))
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
                    if 240 <= position[0] <= 410 and 450 <= position[1] <= 490:
                        self.diff_puzzle_window(
                            score, curr_diff, curr_puzzle, username)
                    # if click 'quit game'
                    if 285 <= position[0] <= 365 and 650 <= position[1] <= 690:
                        pygame.quit()
                        return
                # if quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

    def diff_puzzle_window(self, score, curr_diff, curr_puzzle, username):
        """This function aims to create difficulty and level choosing window.

        Args:
            score (int): The points earned by users.
            curr_diff (int): The stored highest difficulty the user accomplish.
            curr_puzzle (int): The stored highest number of puzzle the user accomplish.
            username (str): The input username to locate saving file.
        """
        # fill the window background color
        self.screen.fill(self.background_color)
        # setup the text on the window
        value_1 = self.title_font.render(
            str('Select your difficulty'), True, self.text_color)
        for i in range(0, 5):
            if i+1 <= curr_diff:
                color = self.text_color
            else:
                color = self.grid_color
            value = self.text_font.render(str(i+1), True, color)
            self.screen.blit(value, (326, 250 + 100*i))
        value_2 = self.text_font.render(str('Back'), True, self.text_color)
        # blit all text on the window
        self.screen.blit(value_1, (130, 150))
        self.screen.blit(value_2, (450, 700))
        pygame.display.update()
        # initialize a parameter that secure the text while true loop
        status = True
        # while true loop to maintain the window
        while status:
            # get event of clicking mouse in game
            for event in pygame.event.get():
                # if the event type is clicking the left button of nouse
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # obtain the position of the mouse and give corresponding values to variables
                    position = pygame.mouse.get_pos()
                    # if clicking '1'
                    if 326 <= position[0] <= 343 and 250 <= position[1] <= 290:
                        diff = 1
                        if diff <= curr_diff:
                            status = False  # set to false to jump out of the ifinity loop
                    # if clicking '2'
                    elif 326 <= position[0] <= 343 and 350 <= position[1] <= 390:
                        diff = 2
                        if diff <= curr_diff:
                            status = False
                    # if clicking '3'
                    elif 326 <= position[0] <= 343 and 450 <= position[1] <= 490:
                        diff = 3
                        if diff <= curr_diff:
                            status = False
                    # if clicking '4'
                    elif 326 <= position[0] <= 343 and 550 <= position[1] <= 590:
                        diff = 4
                        if diff <= curr_diff:
                            status = False
                    # if clicking '5'
                    elif 326 <= position[0] <= 343 and 650 <= position[1] <= 690:
                        diff = 5
                        if diff <= curr_diff:
                            status = False
                    # if clicking on 'back', go back to the home window
                    elif 450 <= position[0] <= 525 and 700 <= position[1] <= 740:
                        self.home_window(score, curr_diff,
                                         curr_puzzle, username)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

        # fill the window background color
        self.screen.fill(self.background_color)
        # setup the text on the window
        value_3 = self.title_font.render(
            str('Select your puzzle'), True, self.text_color)
        # change the color if the puzzle is still lock
        for i in range(0, 6):
            if diff == curr_diff:
                if i+1 <= curr_puzzle:
                    color = self.text_color
                else:
                    color = self.grid_color
            else:
                color = self.text_color
            if i < 5:
                value = self.text_font.render(str(i+1), True, color)
                self.screen.blit(value, (326, 250 + 80*i))
            else:
                value = self.text_font.render(str('Endless'), True, color)
                self.screen.blit(value, (275, 250 + 80*i))
        value_4 = self.text_font.render(str('Back'), True, self.text_color)
        # blit all text on the window
        self.screen.blit(value_3, (140, 150))
        self.screen.blit(value_4, (450, 700))
        pygame.display.update()
        # while true loop to maintain the window
        while True:
            for event in pygame.event.get():
                # if the event type is clicking the left button of nouse, obtain the position and give corresponding values to variables
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    position = pygame.mouse.get_pos()
                    # if click '1'
                    if 326 <= position[0] <= 343 and 250 <= position[1] <= 290:
                        puzzle = 1
                        if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                            self.sudoku_window(
                                score, diff, puzzle, curr_diff, curr_puzzle, username)
                    # if click '2'
                    elif 326 <= position[0] <= 343 and 330 <= position[1] <= 370:
                        puzzle = 2
                        if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                            self.sudoku_window(
                                score, diff, puzzle, curr_diff, curr_puzzle, username)
                    # if click '3'
                    elif 326 <= position[0] <= 343 and 410 <= position[1] <= 450:
                        puzzle = 3
                        if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                            self.sudoku_window(
                                score, diff, puzzle, curr_diff, curr_puzzle, username)
                    # if click '4'
                    elif 326 <= position[0] <= 343 and 490 <= position[1] <= 530:
                        puzzle = 4
                        if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                            self.sudoku_window(
                                score, diff, puzzle, curr_diff, curr_puzzle, username)
                    # if click '5'
                    elif 326 <= position[0] <= 343 and 570 <= position[1] <= 610:
                        puzzle = 5
                        if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                            self.sudoku_window(
                                score, diff, puzzle, curr_diff, curr_puzzle, username)
                    # if click 'endless', puzzle is set as 6
                    elif 275 <= position[0] <= 393 and 650 <= position[1] <= 690:
                        puzzle = 6
                        if (diff == curr_diff and puzzle <= curr_puzzle) or (diff < curr_diff):
                            self.sudoku_window(
                                score, diff, puzzle, curr_diff, curr_puzzle, username)
                    # if click on 'back', start this function over
                    if 450 <= position[0] <= 525 and 700 <= position[1] <= 740:
                        self.diff_puzzle_window(
                            score, curr_diff, curr_puzzle, username)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

    def sudoku_window(self, score, diff, puzzle, curr_diff, curr_puzzle, username):
        """This function aims to gemerate the sudoku gaming window.

        Args:
            score (int): The points earned by users.
            diff (int): The difficulty selected by users.
            puzzle (int): The puzzle number selected by users.
            curr_diff (int): The stored highest difficulty the user accomplish.
            curr_puzzle (int): The stored highest number of puzzle the user accomplish.
            username (str): The input username to locate saving file.
        """
        if puzzle == 6:
            # call function to set up 9*9 grid
            solution = generate_sudo.generate_board_new(
                generate_sudo.generate_board_origin())
            grid = generate_sudo.generate_puzzle(solution, diff)
        else:
            solution = read_level.decrypt(diff, puzzle)[0]
            grid = read_level.decrypt(diff, puzzle)[1]
        # copy another updating grid for varifing the answer
        update_grid = copy.deepcopy(grid)
        # fill the window background color
        self.screen.fill(self.background_color)
        # run grid setup the draw the grid in the window
        self.grid_setup(grid)
        pygame.display.update()
        # initialize the  initial time for timer
        t0 = time.time()
        # game loop to maintain and quit the window
        while True:
            # show timer
            self.game_clock(t0)
            # show score
            pygame.draw.rect(
                self.screen, self.background_color, (60, 655, 600, 40))
            value = self.text_font.render(
                ('Score(pt): ' + str(score)), True, self.text_color)
            self.screen.blit(value, (60, 655))
            # capture every operation in the window
            for event in pygame.event.get():
                # if the mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    position = pygame.mouse.get_pos()
                    # if the position is inside the grid, run insert function
                    if 1 <= position[0]//60 <= 9 and 1 <= position[1]//60 <= 9:
                        update_grid = self.insert(
                            (position[0]//60, position[1]//60), grid, update_grid, t0)
                    # if the position is inside the 'hint' button
                    if 303 <= position[0] <= 365 and 700 <= position[1] <= 740:
                        grid, update_grid, score = self.hint(
                            grid, update_grid, solution, t0, score)
                    # if the position is inside the 'back' button
                    if 450 <= position[0] <= 525 and 700 <= position[1] <= 740:
                        self.home_window(score, curr_diff,
                                         curr_puzzle, username)
                # check if the answer is correct
                # when in 'endless' mode
                if puzzle == 6:
                    if update_grid.all() == solution.all():
                        t_tot = time.time() - t0
                        score = self.win_window_endless(
                            t_tot, score, diff, puzzle, curr_diff, curr_puzzle, username)
                # when in normal mode
                if 1 <= puzzle <= 5:
                    if update_grid == solution:
                        t_tot = time.time() - t0
                        score = self.win_window_single(
                            t_tot, score, diff, puzzle, curr_diff, curr_puzzle, username)
                # if the game is quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

    def grid_setup(self, grid):
        """This function amis to gemerate a game board on the window.

        Args:
            grid (list): The generated sudoku puzzle problem list.
        """
        # setup background color of grid
        pygame.draw.rect(self.screen, self.grid_color, (60, 60, 180, 180))
        pygame.draw.rect(self.screen, self.grid_color, (420, 60, 180, 180))
        pygame.draw.rect(self.screen, self.grid_color, (240, 240, 180, 180))
        pygame.draw.rect(self.screen, self.grid_color, (60, 420, 180, 180))
        pygame.draw.rect(self.screen, self.grid_color, (420, 420, 180, 180))
        # setup 9*9 grid by drawing 10 lines
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, self.line_color,
                                 (60*i + 60, 60), (60*i + 60, 600), 5)
                pygame.draw.line(self.screen, self.line_color,
                                 (60, 60*i + 60), (600, 60*i + 60), 5)
            else:
                pygame.draw.line(self.screen, self.line_color,
                                 (60*i + 60, 60), (60*i + 60, 600), 2)
                pygame.draw.line(self.screen, self.line_color,
                                 (60, 60*i + 60), (600, 60*i + 60), 2)
        # write numbers inside the grid
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if 1 <= grid[i][j] <= 9:
                    value_1 = self.text_font.render(
                        str(grid[i][j]), True, self.text_color)
                    self.screen.blit(value_1, ((j+1)*60 + 21, (i+1)*60 + 12))
        # setup hint button
        value_2 = self.text_font.render('Hint', True, self.text_color)
        self.screen.blit(value_2, (303, 700))
        # setup back button
        value_3 = self.text_font.render(str('Back'), True, self.text_color)
        self.screen.blit(value_3, (450, 700))

    def insert(self, position, grid, update_grid, t0):
        """This function aims to realize inserting numbers into the gameboards.

        Args:
            position (list): The position of the mouse when clicked.
            grid (list): The generated sudoku puzzle problem list.
            update_grid (list): The updated sudoku number list according to users filling-in.
            t0 (float): The initial time when a puzzle starts.

        Returns:
            update_grid (list): The updated sudoku number list according to users filling-in.
        """
        while True:
            # show clock on the screen
            self.game_clock(t0)
            # if the clicking position is inside the grid
            if 1 <= position[0] <= 9 and 1 <= position[1] <= 9 and grid[position[1] - 1][position[0] - 1] == 0:
                for event in pygame.event.get():
                    # change the color into dark gray when selected
                    pygame.draw.rect(
                        self.screen, self.shaded_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                    if update_grid[position[1] - 1][position[0] - 1] != 0:
                        value = self.text_font.render(
                            str(update_grid[position[1] - 1][position[0] - 1]), True, self.text_insert_color)
                        self.screen.blit(
                            value, (position[0]*60 + 21, position[1]*60 + 12))
                    pygame.display.update()
                    if event.type == pygame.KEYDOWN:
                        # checking with backspace (8 is the ascII number of 'backspace')
                        if event.key - 8 == 0:
                            # replace the space with a rectangel with the same color as the background
                            if [position[0], position[1]] in self.dark_grid_loc:
                                pygame.draw.rect(
                                    self.screen, self.grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            else:
                                pygame.draw.rect(
                                    self.creen, self.background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            pygame.display.update()
                            # change the updated grid according to the input
                            update_grid[position[1] -
                                        1][position[0] - 1] = event.key - 8
                            return update_grid
                        # check input for 1-9 on the keyboard
                        if 1 <= (event.key - 48) <= 9:
                            if [position[0], position[1]] in self.dark_grid_loc:
                                pygame.draw.rect(
                                    self.screen, self.grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            else:
                                pygame.draw.rect(
                                    self.screen, self.background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            value = self.text_font.render(
                                str(event.key - 48), True, self.text_insert_color)
                            self.screen.blit(
                                value, (position[0]*60 + 21, position[1]*60 + 12))
                            pygame.display.update()
                            update_grid[position[1] -
                                        1][position[0] - 1] = event.key - 48
                            return update_grid
                        # check input for 1-9 on the keyboard
                        if event.key == pygame.K_KP1 or event.key == pygame.K_KP2 or event.key == pygame.K_KP3 or event.key == pygame.K_KP4 or event.key == pygame.K_KP5 or event.key == pygame.K_KP6 or event.key == pygame.K_KP7 or event.key == pygame.K_KP8 or event.key == pygame.K_KP9:  # check input for 1-9
                            if [position[0], position[1]] in self.dark_grid_loc:
                                pygame.draw.rect(
                                    self.screen, self.grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            else:
                                pygame.draw.rect(
                                    self.screen, self.background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
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
                            value = self.text_font.render(
                                str(num), True, self.text_insert_color)
                            self.screen.blit(
                                value, (position[0]*60 + 21, position[1]*60 + 12))
                            pygame.display.update()
                            update_grid[position[1] -
                                        1][position[0] - 1] = num
                            return update_grid
                        # if input a wrong letter, the grid stays the same as before
                        else:
                            if 1 <= update_grid[position[1] - 1][position[0] - 1] <= 9:
                                if [position[0], position[1]] in self.dark_grid_loc:
                                    pygame.draw.rect(
                                        self.screen, self.grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                                else:
                                    pygame.draw.rect(
                                        self.screen, self.background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                                value = self.text_font.render(
                                    str(update_grid[position[1] - 1][position[0] - 1]), True, self.text_insert_color)
                                self.screen.blit(
                                    value, (position[0]*60 + 21, position[1]*60 + 12))
                            else:
                                if [position[0], position[1]] in self.dark_grid_loc:
                                    pygame.draw.rect(
                                        self.screen, self.grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                                else:
                                    pygame.draw.rect(
                                        self.screen, self.background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                            pygame.display.update()
                            return update_grid
                    # change the selecting block after click to another block
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        # recover the original block into its background color
                        if [position[0], position[1]] in self.dark_grid_loc:
                            pygame.draw.rect(
                                self.screen, self.grid_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        else:
                            pygame.draw.rect(
                                self.screen, self.background_color, (position[0]*60 + 5, position[1]*60 + 5, 60 - 8, 60 - 8))
                        # if the original block is filled with a number, fill the block with it rather than only background color
                        if 1 <= update_grid[position[1] - 1][position[0] - 1] <= 9:
                            if grid[position[1] - 1][position[0] - 1] == 0:
                                value = self.text_font.render(
                                    str(update_grid[position[1] - 1][position[0] - 1]), True, self.text_insert_color)
                                self.screen.blit(
                                    value, (position[0]*60 + 21, position[1]*60 + 12))
                        pygame.display.update()
                        # run the insert function again using the different position and no operation to the update_grid
                        position_ = pygame.mouse.get_pos()
                        update_grid = self.insert(
                            (position_[0]//60, position_[1]//60), grid, update_grid, t0)
                        return update_grid
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return update_grid
            else:
                return update_grid

    def game_clock(self, t0):
        """This function aims to realize the timing and display the real-time click on the screen.

        Args:
            t0 (float): The initial time when a puzzle starts.
        """
        pygame.draw.rect(self.screen, self.background_color,
                         (60, 610, 600, 40))
        t = time.time() - t0
        value = self.text_font.render(
            'Time(s): ' + (str(round(t, 1))), True, self.text_color)
        self.screen.blit(value, (60, 610))
        pygame.display.update()

    def win_window_single(self, t_tot, score, diff, puzzle, curr_diff, curr_puzzle, username):
        """This function amis to create a winning window if the puzzle is NOT a endless mode.

        Args:
            screen (pygame.Surface): The game window.
            t_tot (float): The time consumed when doing one puzzle.
            score (int): The points earned by users.
            diff (int): The difficulty selected by users.
            puzzle (int): The puzzle number selected by users.
            curr_diff (int): The stored highest difficulty the user accomplish.
            curr_puzzle (int): The stored highest number of puzzle the user accomplish.
            username (str): The input username to locate saving file.
        """
        # calculate the score changing
        score_earned = self.time_to_score(t_tot, score, diff)
        score = score_earned + score
        # change the current diff and puzzle if winning the current puzzle
        if puzzle == curr_puzzle and diff == curr_diff:
            if puzzle < 5:
                curr_puzzle += 1
            else:
                curr_puzzle = 1
                curr_diff += 1
        # save game
        start_game.save_profile(username, score, curr_diff, curr_puzzle)
        # show botton
        while True:
            self.screen.fill(self.background_color)
            value_1 = self.text_font.render('WIN!', True, self.text_color)
            value_2 = self.text_font.render(
                'Time: ' + (str(round(t_tot, 1))) + 's', True, self.text_color)
            value_3 = self.text_font.render(
                'Score earned: ' + (str(score_earned)) + 'pt', True, self.text_color)
            value_4 = self.text_font.render(
                'Total score: ' + (str(score)) + 'pt', True, self.text_color)
            value_5 = self.text_font.render(
                'Next level', True, self.text_color)
            value_6 = self.text_font.render(
                'Return to menu', True, self.text_color)
            value_7 = self.text_font.render('Quit', True, self.text_color)
            self.screen.blit(value_1, (280, 80))
            self.screen.blit(value_2, (240, 180))
            self.screen.blit(value_3, (185, 280))
            self.screen.blit(value_4, (195, 380))
            self.screen.blit(value_5, (245, 480))
            self.screen.blit(value_6, (210, 580))
            self.screen.blit(value_7, (285, 680))
            # if reaching 5-5, which is the last puzzle, there is no 'next level' button
            if diff == 5 and puzzle == 5:
                pygame.draw.rect(
                    self.screen, self.background_color, (245, 480, 145, 75))
            pygame.display.update()
            # get mouse clicking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    position = pygame.mouse.get_pos()
                    # return to home page
                    if 210 <= position[0] <= 440 and 580 <= position[1] <= 620:
                        self.home_window(score, curr_diff,
                                         curr_puzzle, username)
                    # next level
                    if 245 <= position[0] <= 390 and 480 <= position[1] <= 520:
                        if puzzle <= 4:
                            puzzle += 1
                        elif puzzle == 5:
                            diff += 1
                            puzzle = 1
                        if diff <= 5:
                            self.sudoku_window(
                                score, diff, puzzle, curr_diff, curr_puzzle, username)
                    if 285 <= position[0] <= 363 and 680 <= position[1] <= 720:
                        pygame.quit()
                        return

    def win_window_endless(self, t_tot, score, diff, puzzle, curr_diff, curr_puzzle, username):
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
        # calculate the score changing
        score_earned = self.time_to_score(t_tot, score, diff)
        score = score_earned + score
        # save game
        start_game.save_profile(username, score, curr_diff, curr_puzzle)
        # show buttom
        while True:
            self.screen.fill(self.background_color)
            value_1 = self.text_font.render('WIN!', True, self.text_color)
            value_2 = self.text_font.render(
                'Time: ' + (str(round(t_tot, 1))) + 's', True, self.text_color)
            value_3 = self.text_font.render(
                'Score earned: ' + (str(score_earned)) + 'pt', True, self.text_color)
            value_4 = self.text_font.render(
                'Total score: ' + (str(score)) + 'pt', True, self.text_color)
            value_5 = self.text_font.render('Continue', True, self.text_color)
            value_6 = self.text_font.render(
                'Return to menu', True, self.text_color)
            value_7 = self.text_font.render('Quit', True, self.text_color)
            self.screen.blit(value_1, (280, 80))
            self.screen.blit(value_2, (240, 180))
            self.screen.blit(value_3, (185, 280))
            self.screen.blit(value_4, (195, 380))
            self.screen.blit(value_5, (250, 510))
            self.screen.blit(value_6, (210, 580))
            self.screen.blit(value_7, (285, 650))
            pygame.display.update()
            # get mouse clicking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    position = pygame.mouse.get_pos()
                    # next random board with same difficulty
                    if 250 <= position[0] <= 385 and 510 <= position[1] <= 550:
                        self.sudoku_window(
                            score, diff, puzzle, curr_diff, curr_puzzle, username)
                    # return to home page
                    if 210 <= position[0] <= 440 and 580 <= position[1] <= 620:
                        self.home_window(score, curr_diff,
                                         curr_puzzle, username)
                    if 285 <= position[0] <= 363 and 650 <= position[1] <= 690:
                        pygame.quit()
                        return

    def hint(self, grid, update_grid, solution, t0, score):
        """This function aims to realize the hint for the puzzle and a number of scores will be consumed.

        Args:
            grid (list): The generated sudoku puzzle problem list.
            update_grid (list): The updated sudoku number list according to users filling-in.
            solution (list): The solution of the sudoku puzzle.
            t0 (float): The initial time when a puzzle starts.
            score (int): The points earned by users.

        Returns:
            grid (list): The generated sudoku puzzle problem list.
            update_grid (list): The updated sudoku number list according to users filling-in.
            score (int): The points earned by users.
        """
        self.game_clock(t0)
        # use 100 score to use each hint
        score = score - 100
        # if score is not enough, hint will not be active and return directly
        if score < 0:
            return grid, update_grid, score + 100
        # initialize hint_pool
        hint_pool = []
        # fill hint_pool with coordinates of all blank and incorrect numbers
        for i in range(0, len(update_grid)):
            for j in range(0, len(update_grid[i])):
                if grid[i][j] == 0:
                    if update_grid[i][j] != solution[i][j]:
                        hint_pool.append([i, j])
        # randomly choose a coordinate from the pool
        hint_loc = random.choice(hint_pool)
        # change the update_grid and original grid
        update_grid[hint_loc[0]][hint_loc[1]
                                 ] = solution[hint_loc[0]][hint_loc[1]]
        grid[hint_loc[0]][hint_loc[1]] = solution[hint_loc[0]][hint_loc[1]]
        # show numbers on the grid
        if [(hint_loc[1] + 1), (hint_loc[0] + 1)] in self.dark_grid_loc:
            pygame.draw.rect(self.screen, self.grid_color, ((
                (hint_loc[1] + 1)*60 + 5, (hint_loc[0] + 1)*60 + 5, 60 - 8, 60 - 8)))
        else:
            pygame.draw.rect(self.screen, self.background_color, ((
                (hint_loc[1] + 1)*60 + 5, (hint_loc[0] + 1)*60 + 5, 60 - 8, 60 - 8)))
        value = self.text_font.render(
            str(update_grid[hint_loc[0]][hint_loc[1]]), True, self.hint_text_color)
        self.screen.blit(
            value, ((hint_loc[1] + 1)*60 + 21, (hint_loc[0] + 1)*60 + 12))
        pygame.display.update()
        return grid, update_grid, score

    def time_to_score(self, t_tot, score, diff):
        """This function aims to calculate the earned score when a puzzle is finished

        Args:
            t_tot (float): The time consumed when doing one puzzle.
            score (int): The points earned by users.
            diff (int): The difficulty selected by users.
        Returns:
            add_score (int): The calculated earned score.
        """
        # the fixed obtained score is 100 for difficulty 1 puzzles
        if diff == 1:
            add_score = 100
            # if the comsumed time is less than 100s, bonus score will be added
            if t_tot < 100:
                add_score += 100 - int(t_tot)
        # same as above for following condition
        elif diff == 2:
            add_score = 200
            if t_tot < 200:
                add_score += 200 - int(t_tot)
        elif diff == 3:
            add_score = 300
            if t_tot < 300:
                add_score += 300 - int(t_tot)
        elif diff == 4:
            add_score = 400
            if t_tot < 400:
                add_score += 400 - int(t_tot)
        elif diff == 5:
            add_score = 500
            if t_tot < 500:
                add_score += 500 - int(t_tot)
        # the max score is set as 999999
        if add_score + score > 99999:
            add_score = 99999 - score
        return add_score


if __name__ == "__main__":
    UI().home_window(99999, 4, 2, 'zmz')
