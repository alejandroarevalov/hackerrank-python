from functools import reduce

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


numbers_list = student_marks[query_name]
result = reduce(lambda a, b: a + b, numbers_list) / len(numbers_list)
print("{:.2f}".format(result))
