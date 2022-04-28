if __name__ == '__main__':
    nested_list = []
    marks = []
    for _ in range(int(input("enter number of details: "))):
        name = input("enter student name: ")
        score = float(input("enter marks of student: "))
        new_list = [name,score]
        nested_list.append(new_list)
        marks.append(score)
    marks = sorted(set(marks))
    y = marks[1]
    runnerup = [ x for x in nested_list if y==x[1]]
    alphabetical = []
    for i in runnerup:
        alphabetical.append(i[0])
    z = sorted(alphabetical)
    for k in z:
        print(k)
    

    
       


   