if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    unique_scores = sorted(list(set([student[1] for student in students])))
    second_lowest = unique_scores[1]
    result_names = [student[0] for student in students if student[1] == second_lowest]
    
    result_names.sort()
    for name in result_names:
        print(name)
