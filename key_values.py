if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
 
    query_name = input()
    for key in student_marks.keys():
        if key==query_name:
            y = student_marks.get(key)
            print(y)
            y = sum(y)
            print(y)
            z = y/3
            print(z)
        else:
            break
    marks=0
