students_list = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_list.append([name, score])


def get_student_with_min_grade(students):
    return min(students, key=lambda st: st[1])


def get_students_with_min_grade(students):
    ref_student = get_student_with_min_grade(students)
    return list(filter(lambda st: st[1] == ref_student[1], students))


min_grade_students = get_students_with_min_grade(students_list)
students_list = list(filter(lambda s: s not in min_grade_students, students_list))
second_least_students_list = get_students_with_min_grade(students_list)
second_least_students_list.sort(key=lambda st: st[0])
for student in second_least_students_list:
    print(student[0])