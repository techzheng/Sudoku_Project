import random
import numpy as np
import time
import copy
import re

# class Seed(object):
#     def __init__(self, seed):
#         self.seed = seed


def generate_board_origin():
    """Generate a 9*9 sudoku

    Returns:
        list: A 9*9 list of integer which represents the original board
    """
    # generate a basic board fulfilled by '0'
    # random.seed = self.seed
    sudo = np.zeros((9, 9), int)
    num = random.randint(1, 9)
    for row in range(9):
        for col in range(9):
            sudo_row = get_row(sudo, row)
            sudo_col = get_col(sudo, col)
            sudo_board = get_board(sudo, row, col)
            while (num in sudo_row) or (num in sudo_col) or (num in sudo_board):
                num = num % 9 + 1
            sudo[row, col] = num
            num = num % 9 + 1
    return sudo


def generate_board_new(sudo):
    """Generate a new sudoku board by exchanging row and column

    Args:
        sudo (list): A 9*9 list of integer

    Returns:
        list: A 9*9 list of integer which represents a new board
    """
    # random.seed = self.seed
    # seed = self.seed
    # refresh = abs(seed) % 100
    for i in range(100):
        change_row = random.choice([0, 3, 6])
        change_row_num = random.sample([0, 1, 2], k=2)
        row_index_1 = change_row + change_row_num[0]
        row_index_2 = change_row + change_row_num[1]
        sudo[[row_index_1, row_index_2], :] = sudo[[row_index_2, row_index_1], :]

        change_col = random.choice([0, 3, 6])
        change_col_num = random.sample([0, 1, 2], k=2)
        col_index_1 = change_col + change_col_num[0]
        col_index_2 = change_col + change_col_num[1]
        sudo[:, [col_index_1, col_index_2]] = sudo[:, [col_index_2, col_index_1]]
    return sudo


def get_row(sudo, row):
    """Get all the grids of the row where the grid is located

    Args:
        sudo (list): A 9*9 list of integer
        row (list): The row where the grid is located

    Returns:
        list: All the grids of the row where the grid is located
    """
    return sudo[row, :]


def get_col(sudo, col):
    """Get all the grids of the column where the grid is located

    Args:
        sudo (list): A 9*9 list of integer
        col (list): The column where the grid is located

    Returns:
        list: All the grids of the column where the grid is located
    """
    return sudo[:, col]


def get_board(sudo, row, col):
    """Get all the grid of the small board where the grid is located

    Args:
        sudo (list): A 9*9 list of integer
        row (list): The row where the grid is located
        col (list): The column where the grid is located

    Returns:
        list: All the grids of the small board where the grid is located
    """
    row_start = row // 3 * 3
    col_start = col // 3 * 3
    return sudo[row_start: row_start+3, col_start: col_start+3]


def generate_puzzle(sudo, level):
    """Generate puzzles

    Args:
        sudo (list): A 9*9 list of integer
        level (integer): The number of grids be erased depends on level, up to 5

    Returns:
        list: A 9*9 list of integer which represents the puzzle
    """
    puzzle = copy.deepcopy(sudo)
    blank_num = round(64 - 10 * (6-level))
    blank_pos = random.sample(range(81), blank_num)

    for blank in blank_pos:
        blank_row = blank // 9
        blank_col = blank % 9
        puzzle[blank_row][blank_col] = 0
    return puzzle


def answer_record(puzzle):
    """Record the position of blanks

    Args:
        puzzle (list): A 9*9 list of integer which represents the puzzle

    Returns:
        list: A list contains the position of blankss
    """
    # find the index of blanks
    answer_index = np.where(puzzle == 0)
    answer_row = answer_index[0]
    answer_col = answer_index[1]
    # convert the index into coordinate form
    answer_position = np.stack((answer_row, answer_col), axis=1).tolist()
    return answer_position


if __name__ == '__main__':
    t0 = time.time()
    # print(generate_board_origin())
    answer = generate_board_new(generate_board_origin())
    answer_out1 = re.sub(r"(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)",
                        r"\1,\2,\3,\4,\5,\6,\7,\8,\9", str(answer))
    answer_out2 = re.sub(r'\s+', ',\n', answer_out1)
    # print(answer)
    # print(answer_out2)

    puzzle = generate_puzzle(answer, 2)
    puzzle_out1 = re.sub(r"(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)",
                        r"\1,\2,\3,\4,\5,\6,\7,\8,\9", str(puzzle))
    puzzle_out2 = re.sub(r'\s+', ',\n', puzzle_out1)
    # print(puzzle)
    # print(puzzle_out2)

    # print(type(puzzle))
    answer_index = answer_record(puzzle)
    # print(answer_index)
    # print(type(answer_index))
    t1 = time.time()
    # print(t1-t0)
