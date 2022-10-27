import numpy as np


if __name__ == '__main__':
    input_list = []
    N, M, P = map(int, input().split())
    for x in range(0, N):
        input_list.append(list(map(int, input().split())))
    array1 = np.array(input_list)
    input_list = []
    for x in range(0, M):
        input_list.append(list(map(int, input().split())))
    array2 = np.array(input_list)
    print(np.concatenate((array1, array2), axis=0))
