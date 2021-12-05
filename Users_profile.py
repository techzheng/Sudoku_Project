import os
import pathlib
import Users_UI
data = {}
data1 = {}


def encrypt(content, N=17947, E=7):
    """Encrypt level information

    Args:
        content (str): Level information
        N (int, optional): A parameter for RSA encryption algorithm. Defaults to 17947.
        E (int, optional): A parameter for RSA encryption algorithm. Defaults to 7.

    Returns:
        str: Encrypt message
    """
    return [(ord(s) ** E) % N for s in str(content)]


def register(username, score=100, start_level='1-1'):
    ori_path = os.getcwd()
    file_name = ori_path + '/data/users/' + str(username) + '.dat'
    data[score] = start_level
    # print(filename)
    with open(file_name, 'w+') as f:
        enc_content = encrypt(str(list(data.keys())) + str(data[score]))
        num_list = [str(x) for x in enc_content]
        f.write(' '.join(num_list))
        f.write('\n')


def save_profile(username, score, diff, puzzle):
    ori_path = os.getcwd()
    file_name = ori_path + '/data/users/' + str(username) + '.dat'
    data[score] = str(diff) + '-' + str(puzzle)
    # filename = str(username) + '.dat'
    # print(filename)
    with open(file_name, 'w+') as f:
        enc_content = encrypt(str(list(data.keys())) + str(data[score]))
        num_list = [str(x) for x in enc_content]
        f.write(' '.join(num_list))
        f.write('\n')


def read_profile(username, N=17947, D=10103):
    ori_path = os.getcwd()
    file_name = ori_path + '/data/users/' + str(username) + '.dat'
    if os.path.exists(file_name):
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

        info = messages.strip('[').split(']')
        score = int(info[0])
        level = info[1].split('-')
        diff = int(level[0])
        puzzle = int(level[1])
        result = [score, diff, puzzle]
        # print(result)
        return result
    else:
        type_reg = input(
            'This profile does not exist, do you want to register?(y/n)\n')
        if type_reg in ['y', 'Y']:
            register(username)
        if type_reg in ['n', 'N']:
            type_name = input('Please type the name:\n')
            return read_profile(type_name, N=17947, D=10103)


if __name__ == '__main__':
    save_profile('zmz', 10, 2, 2)
    print(read_profile('zmz'))
