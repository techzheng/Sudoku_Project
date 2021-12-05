import os


def decrypt(diff, puzzle, N=17947, D=10103):
    """Read and decrypted level information.

    Args:
        diff (int): The difficulty.
        puzzle (int): The level.
        N (int, optional): A parameter for RSA encryption algorithm. Defaults to 17947.
        D (int, optional): A parameter for RSA encryption algorithm. Defaults to 10103.

    Returns:
        str: The decrypt level information.
    """
    ori_path = os.getcwd()
    # dat_path = ori_path + '/' + str(diff) + '-' + str(puzzle) + '.dat'
    # os.chdir(dat_path)
    file_name = ori_path + '/data/levels/' + str(diff) + '-' + str(puzzle) + '.dat'
    messages = str()
    with open(file_name, 'r') as file:
        lines = file.readlines()
        message_list = []
        for i in range(len(lines)):
            column_list = lines[i].strip().split(" ")
            message_list.append(column_list)
        for i in range(len(message_list)):
            for j in range(len(message_list[i])):
                message_list[i][j] = int(message_list[i][j])
    for i in range(0, len(message_list)):
        messages = messages + ''.join([chr((s ** D) % N)
                                      for s in message_list[i]])
        if i < len(message_list)-1:
            messages = messages + '\n'

    # convert str messages to list
    row_list = []
    solution = []
    grid = []
    for i in range(0, len(messages)//2):
        if messages[i] != '[' and messages[i] != ']' and messages[i] != ',' and messages[i] != '\n':
            row_list.append(int(messages[i]))
            if len(row_list) == 9:
                solution.append(row_list)
                row_list = []
    for i in range(len(messages)//2, len(messages)):
        if messages[i] != '[' and messages[i] != ']' and messages[i] != ',' and messages[i] != '\n':
            row_list.append(int(messages[i]))
            if len(row_list) == 9:
                grid.append(row_list)
                row_list = []
    
    return solution, grid
            

if __name__ == '__main__':
    # ori_path = os.getcwd()
    # dat_path = ori_path + '/data/levels'
    # os.chdir(dat_path)
    messages = decrypt(5, 5)
    print(messages[0], messages[1])
