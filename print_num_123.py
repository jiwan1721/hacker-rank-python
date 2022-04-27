'''print_num_123.py'''
''' 
he included code stub will read an integer,

, from STDIN.

Without using any string methods, try to print the following:

Note that "

" represents the consecutive values in between.

Example
Print the string .

'''




if __name__ == '__main__':
    n = int(input())
    y = []
    for x in range(n):
        x+=1
        y.append(x)
    y= str(y)
    y = y.replace(',','')
    y = y.replace(' ','')
    y = y.replace('[','')
    y = y.replace(']','')
    print(y)