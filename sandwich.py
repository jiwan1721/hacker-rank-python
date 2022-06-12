
my_dict={
    '1':True,
    '2':False,
    '3':False,
    '4':True,
    '5':True,
    '6':False,
    '7':True,
    '8':False,
    '9':False,
    '10':False
    
}

def sandwichFinder(mydict):
    data1 = []
    last_item = list(mydict.values())[::-1]
    for x in last_item:
        if x ==False:
            mydict.popitem()
            continue
        elif x == True:
            break
    item_false=False
    for item,values in mydict.items():

        if values:
            item_false=True
            continue
        if values==False and item_false==True:
            data1.append(item)
    print('data-----',data1)


sandwichFinder(my_dict)