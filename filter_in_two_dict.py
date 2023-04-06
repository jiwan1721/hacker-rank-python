x = [{'id': 1, 'name': 'jiwan1'}, {'id': 4, 'name': 'jiwan4'},
     {'id': 3, 'name': 'jiwan3'}, {'id': 2, 'name': 'jiwan2'}]

y = [{'id': 5, 'name': 'jiwan1'}, {'id': 2, 'name': 'jiwan4'},
     {'id': 6, 'name': 'jiwan3'}, {'id': 2, 'name': 'jiwan2'}]

x_ids = [a['id'] for a in x]

# for data in y:
#     if data['id'] not in x_ids:
#         x.append(data)

x+= list(filter(lambda a: a['id'] not in x_ids, y))

print(x, x_ids)