my_dict = [
    {"a":1,"b":2},
    {"a":1,"b":2},
    {"a":2,"c":3},
    {"a":1,"b":2},
    {"a":2,"c":3},
    {"a":2,"c":3},
    {"a":3}
]
def removedict(my_dict):
    if not isinstance(my_dict, list):
        return f"sorry expected list but got {type(mydict)}"
    if not my_dict:
        return "list may not be empty"
    unique_dist=[item for item in my_dict if my_dict.count(item)==1]
    double_list=[]
    for item in my_dict:
        if my_dict.count(item)>1:
            indixes = [i for i in range(len(my_dict)) if my_dict[i] == item]
            count = my_dict.count(item)
            for i in reversed(indixes):
                my_dict.pop(i)
            item['count']=count
            double_list.append(item)
    return unique_dist+double_list

print(removedict(my_dict))
