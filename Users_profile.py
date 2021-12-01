import os
data = {}

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


def register(username, init_score=100):
    data[username] = User(username, init_score)
    filename = str(username) + '.dat'
    print(filename)
    with open(filename, 'w+') as f:
        # enc_content = encrypt(data)
        f.write(str(data))
        f.write('\n')



class User(object):
    def __init__(self, username, init_score):
        self.username = username
        self.score = init_score

    def user_info(self, score):
        pass

if __name__ == '__main__':
    ori_path = os.getcwd()
    dat_path = ori_path + '/data/users'
    os.chdir(dat_path)

    # print(dat_path)
    register('zmz')
    print(str(data))