import os
import generate_sudo
import re


def encrypt(content, N=17947, E=7):
    return [(ord(s) ** E) % N for s in str(content)]


def write_dat(file, content, N=17947, E=7):
    filename = '.'.join(file.split('.')[0:-1]) + '.dat'
    with open(filename, 'w+') as f:
        enc_content = encrypt(content, N, E)
        num_list = [str(x) for x in enc_content]
        f.write(' '.join(num_list))
        f.write('\n')


if __name__ == '__main__':
    L = (1, 2, 3, 4, 5)
    ori_path = os.getcwd()
    dat_path = ori_path + '\data\levels'
    os.chdir(dat_path)
    for i in L:
        for j in L:
            answer = generate_sudo.generate_board_new(
                generate_sudo.generate_board_origin())
            answer_out1 = re.sub(r"(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)",
                                 r"\1,\2,\3,\4,\5,\6,\7,\8,\9", str(answer))
            answer_out2 = re.sub(r'\s+', ',\n', answer_out1)
            puzzle = generate_sudo.generate_puzzle(answer, i + (j-1)*0.2)
            puzzle_out1 = re.sub(r"(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)",
                                 r"\1,\2,\3,\4,\5,\6,\7,\8,\9", str(puzzle))
            puzzle_out2 = re.sub(r'\s+', ',\n', puzzle_out1)
            content = answer_out2 + ',\n' + puzzle_out2
            ori_path = os.getcwd()
            filename = str(i) + '-' + str(j) + '.dat'
            write_dat(filename, content)
