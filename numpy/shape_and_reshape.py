import numpy as np


def shape_list(a_list):
    array = np.array(a_list)
    array = array.reshape(3, 3)
    return array


if __name__ == '__main__':
    initial_input = list(map(int, input().split()))
    print(shape_list(initial_input))
