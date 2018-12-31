if __name__ == '__main__':
    student_infos = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_infos.append([name, score])

    scores = sorted({student_info[1] for student_info in student_infos})
    result = sorted(student_info[0] for student_info in student_infos if student_info[1] == scores[1])
    print('\n'.join(result))
