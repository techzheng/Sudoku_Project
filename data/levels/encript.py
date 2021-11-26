import os


def encrypt(content, N=45236, E=9):
    return [(ord(s) ** E) % N for s in str(content)]


# def decrypt(enc_content, N=45236, D=20086):
#     return ''.join([chr((s ** D) % N) for s in enc_content])


def write_dat(file, content, N=45236, E=9):
    filename = '.'.join(file.split('.')[0:-1]) + '.dat'
    with open(filename, 'w+') as f:
        enc_content = encrypt(content, N, E)
        num_list = [str(x) for x in enc_content]
        f.write(' '.join(num_list))
        f.write('\n')


if __name__ == '__main__':
    content = [[[5,7,6,1,8,9,3,2,4],
 [8,1,9,4,2,3,6,5,7],
 [2,4,3,7,5,6,9,8,1],
 [3,5,4,8,6,7,1,9,2],
 [6,8,7,2,9,1,4,3,5],
 [9,2,1,5,3,4,7,6,8],
 [4,6,5,9,7,8,2,1,3],
 [7,9,8,3,1,2,5,4,6],
 [1,3,2,6,4,5,8,7,9]],
[[5,7,6,1,8,9,3,2,4],
 [8,1,9,4,2,3,6,5,7],
 [2,0,3,7,5,6,9,8,1],
 [0,5,4,0,0,0,1,9,0],
 [0,8,7,2,9,1,4,3,5],
 [9,2,1,0,0,0,7,6,0],
 [4,6,5,9,0,8,2,1,3],
 [7,9,8,3,1,2,5,4,6],
 [1,3,2,6,0,0,8,7,9]]]
    os.chdir("D:\Github\Sudoku_Project\data\levels")
    write_dat('1-1.dat', content)
    print(os.getcwd())