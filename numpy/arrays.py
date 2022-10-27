import numpy as np


def arrays(an_array):
    numbers_list = list(map(float, an_array))
    numbers_list.reverse()
    return np.array(numbers_list)


if __name__ == '__main__':
    arr = input().strip().split(' ')
    print(arr)
    result = arrays(arr)
    print(result)
