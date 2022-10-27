import numpy as np


if __name__ == '__main__':
    data_input = tuple(map(int, input().split()))
    zeros = np.zeros(data_input, dtype=int)
    ones = np.ones(data_input, dtype=int)
    print(zeros)
    print(ones)
