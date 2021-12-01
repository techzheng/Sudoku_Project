import os
data = {}
data1 = {'a': 1}
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


def register(username, score=100, level = '1-1'):
    data[score] = level
    filename = str(username) + '.dat'
    # print(filename)
    with open(filename, 'w+') as f:
        enc_content = encrypt(str(list(data.keys())) + str(data[score]))
        num_list = [str(x) for x in enc_content]
        f.write(' '.join(num_list))
        f.write('\n')

def save_profile(username, score, level):
    # data[score]
    pass

if __name__ == '__main__':
    ori_path = os.getcwd()
    dat_path = ori_path + '/data/users'
    os.chdir(dat_path)

    # print(dat_path)
    register('zmz')