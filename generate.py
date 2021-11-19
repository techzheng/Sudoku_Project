import random
import numpy as np
import time
# get all the grids of the row where the grid is located
def get_row(sudo, row):
    """Get all the grids of the row where the grid is located

    Args:
        sudo (list): A 9*9 list of integers
        row (list): The row where the grid is located

    Returns:
        list: All the grids of the row where the grid is located
    """
    return sudo[row, :]


# get all the grids of the column where the grid is located
def get_col(sudo, col):
    """Get all the grids of the column where the grid is located

    Args:
        sudo (list): A 9*9 list of integers
        col (list): The column where the grid is located

    Returns:
        list: All the grids of the column where the grid is located
    """
    return sudo[:, col]


# get all the grids of the small board where the grid is located
def get_board(sudo, row, col):
    """Get all the grid of the small board where the grid is located

    Args:
        sudo (list): A 9*9 list of integers
        row (list): The row where the grid is located
        col (list): The column where the grid is located

    Returns:
        list: All the grids of the small board where the grid is located
    """
    row_start = 3 * (row // 3)
    col_start = 3 * (col // 3)
    return sudo[row_start: row_start+3, col_start: col_start+3]


def generate_board_origin():
    """Generate a 9*9 sudoku

    Returns:
        list: A 9*9 list of integer
    """
    # generate a basic board fulfilled by '0'
    sudo = np.zeros((9, 9), int)
    num = random.randint(1, 9)

    for row in range(9):
        for col in range(9):
            sudo_row = get_row(sudo, row)
            sudo_col = get_col(sudo, col)
            sudo_board = get_board(sudo, row, col)
            if (num in sudo_row) or (num in sudo_col) or (num in sudo_board):
                num = num % 9 + 1
            sudo[row, col] = num
            num = num % 9 + 1
    return sudo


def generate_board_new(sudo):
    for i in range(100):
        change_col = random.choice([0, 3, 6])
        change_col_num = random.sample([0, 1, 2], k=2)
        col_index_1 = change_col + change_col_num[0]
        col_index_2 = change_col + change_col_num[1]
        sudo[:, [col_index_1, col_index_2]] = sudo[:, [col_index_2, col_index_1]]
    
        change_row = random.choice([0, 3, 6])
        change_row_num = random.sample([0, 1, 2], k=2)
        row_index_1 = change_row + change_row_num[0]
        row_index_2 = change_row + change_row_num[1]
        sudo[[row_index_1, row_index_2], :] = sudo[[row_index_2, row_index_1], :]
    

if __name__ == '__main__':
    t0 = time.time()
    print(generate_board_new(generate_board_origin()))
    t1 = time.time()
    print(t1-t0)