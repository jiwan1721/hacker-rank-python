
from cgi import test


test_dict = [
    {
        'from_date': '2079-01-34',
        'to_date': '2079-02-34',
        'position': 'intern'
    },
    {
        'from_date': '2079-03-34',
        'to_date': '2079-04-34',
        'position': 'intern'
    },
    {
        'from_date': '2079-05-34',
        'to_date': '2079-06-34',
        'position': 'trainee'
    }
]


def duplicate_position(test_dict):
    intern = 0
    intern_list = []
    for index, value in enumerate(test_dict):
        print(index)
        if value['position'] == 'intern':
            intern = intern+1
            intern_list.append(index)
        if intern == 2:
            test_dict[1]["from_date"] = test_dict[0]['from_date']
            test_dict.pop(intern_list[0])
            intern_list.clear()
            intern = 1
            return test_dict


print(duplicate_position(test_dict))


def clean_data(my_list):
    if len(my_list) <= 1:
        return
    for index, my_dict in enumerate(my_list):
        if index == 0:
            continue
        prev_position = my_list[index-1]
        curr_position = my_list[index]
        if prev_position["position"] == curr_position["position"]:
            temp_from_date = prev_position["from_date"]
            my_list.pop(index-1)
            print(temp_from_date)
            curr_position["from_date"] = temp_from_date
        return my_list

print(clean_data(test_dict))