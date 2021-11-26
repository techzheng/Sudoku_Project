import os


def decrypt(file_name, N=17947, D=10103):
    """Read and decrypted level information

    Args:
        file_name (str): The file name
        N (int, optional): A parameter for RSA encryption algorithm. Defaults to 17947.
        D (int, optional): A parameter for RSA encryption algorithm. Defaults to 10103.

    Returns:
        str: The decrypt level information
    """
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
    return messages


if __name__ == '__main__':
    ori_path = os.getcwd()
    dat_path = ori_path + '\data\levels'
    os.chdir(dat_path)
    messages = decrypt('5-5.dat')
    print(messages)
