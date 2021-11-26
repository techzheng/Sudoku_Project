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
    content = [[[2,1,9,4,3,5,6,7,8]
 [5,4,3,7,6,8,9,1,2]
 [9,8,7,2,1,3,4,5,6]
 [6,5,4,8,7,9,1,2,3]
 [3,2,1,5,4,6,7,8,9]
 [4,3,2,6,5,7,8,9,1]
 [1,9,8,3,2,4,5,6,7]
 [7,6,5,9,8,1,2,3,4]]
[[8,7,6,1,9,2,3,4,5]
 [0,1,9,4,3,0,0,7,8]
 [5,0,3,7,6,0,9,0,2]
 [9,8,0,2,1,3,4,5,6]
 [6,5,0,8,7,9,1,2,3]
 [0,2,0,5,4,6,7,8,0]
 [4,3,2,0,5,7,8,9,1]
 [1,9,8,3,2,4,5,6,7]
 [7,6,5,9,0,1,2,3,0]]]
    os.chdir("D:\Github\Sudoku_Project\data\levels")
    write_dat('1-2.dat', content)
    print(os.getcwd())