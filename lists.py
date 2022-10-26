def insert_in_list(*args):
    args[0].insert(int(args[1][0]), int(args[1][1]))


def print_list(*args):
    print(args[0])


def remove_from_list(*args):
    args[0].remove(int(args[1][0]))


def append_to_list(*args):
    args[0].append(int(args[1][0]))


def sort_list(*args):
    args[0].sort()


def pop_from_list(*args):
    args[0].pop()


def reverse_list(*args):
    args[0].reverse()


if __name__ == '__main__':
    N = int(input())
    my_list = []
    my_dictionary = {
        'insert': insert_in_list,
        'print': print_list,
        'remove': remove_from_list,
        'append': append_to_list,
        'sort': sort_list,
        'pop': pop_from_list,
        'reverse': reverse_list
    }
    for n in range(0, N):
        input_list = list(input().split())
        instruction = input_list.pop(0)
        my_dictionary[instruction](my_list, input_list)
