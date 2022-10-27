import numpy as np


def transpose(an_array):
    return np.transpose(an_array)


def flatten(an_array):
    return an_array.flatten()


if __name__ == '__main__':
    m, n = input().split()
    input_matrix = []
    for x in range(0, int(m)):
        line = list(map(int, input().split()))
        input_matrix.append(line)
    print(transpose(np.matrix(input_matrix)))
    print(flatten(np.array(input_matrix)))
