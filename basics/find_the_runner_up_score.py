if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr_to_list = list(arr)
max_to_remove = max(arr_to_list)
filtered_list = list(filter(lambda x: x != max_to_remove, arr_to_list))
print(max(filtered_list))