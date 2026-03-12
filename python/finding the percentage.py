if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, marks = line[0], list(map(float, line[1:]))
        student_marks[name] = marks
    query_name = input()
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print("{:.2f}".format(average))
