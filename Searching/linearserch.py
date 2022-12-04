

def linear_search(my_list, key):
    for index in range(0,len(my_list)):
        if (my_list[index]==key):
            return index
    else:
        return "not found"

my_list = [4,56,7,8]
print(linear_search(my_list, 78))