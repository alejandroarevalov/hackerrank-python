if __name__ == '__main__':
    n = int(input())
    values = tuple(map(int, input().split()))
    real_tuple = (1, 2)
    print(hash(values))
    print(hash(real_tuple))

