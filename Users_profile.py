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
    print(filename)
    with open(filename, 'w+') as f:
        # enc_content = encrypt(data)
        f.write(str(list(data.keys())) + str(data[score]))
        f.write('\n')



# class User(object):
#     def __init__(self, username, score):
#         self.username = username
#         self.score = score

#     def user_info(self, score):
#         pass

if __name__ == '__main__':
    ori_path = os.getcwd()
    dat_path = ori_path + '/data/users'
    os.chdir(dat_path)

    # print(dat_path)
    register('a')
    print(str(data.keys()))