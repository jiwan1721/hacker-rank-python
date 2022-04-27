if __name__ == '__main__':
    nested_list = []
    for _ in range(int(input("enter number of details: "))):
        name = input("enter student name: ")
        score = float(input("enter marks of student: "))
        new_list = [name,score]
        nested_list.append(new_list)
    new_list_1 = [x for [x,y] in nested_list x.sort()]
    for [x,y] in nested_list:
        print(x)
        print(y)
        x.sort()
        print()