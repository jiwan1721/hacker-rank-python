
list_cop = [1,2,43,5,6,7]
new_list = [x for x in list_cop if x>3]
print(new_list)

list1 = [1,2]
list2 = [3,4]
list3 = [5,6]
new_list = [(x,y,z) for x in list1 for y in list2 for z in list3]
print(new_list)
student = ["ramesh","raj","jiwan","rajesh","rajan"]
first_let = input("type letter: ")
new_std = [x for x in student if x.startswith(first_let)]
print(new_std)


''' 
Let's learn about list comprehensions! 
You are given three integers and representing the dimensions
of a cuboid along with an integer . Print a list of all 
possible coordinates given by on a 3D grid where the sum 
of is not equal to . Here, . Please use list comprehensio
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x = [a for a in range(x+1)]
    y = [b for b in range(y+1)]
    z = [c for c in range(z+1)]
    permu = [[j,k,l] for j in x for k in y for l in z]
    permu_num = [e for e in permu if sum(e) !=3]
    print(permu_num)