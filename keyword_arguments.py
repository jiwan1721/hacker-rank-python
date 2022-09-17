def add(a,b,c):
    print('sum: ',a+b+c)
add(3,4,5)

def add1(*num):
    sum = 0
    for n in num:
        sum =sum +n
        print('sum: ',sum)
    return sum
x = int(input("\nenter number: "))
y = int(input("\nenter number: "))
print(add1(x,y))

def introduction(**data):
    # print("\n Data type of argument", type(data))
    # for i , j in data.items():
    #     print("{} is {}".format(i,j))
    for key,value in data.items():
        print("{} is {}".format(key,value))
        
introduction(firstname = "sita", lastname = "rana", age = 45, email= "sita@gamil.com")

def argm(**values):
    for key,values in values.items():
        print("your value{}".format(values))
argm(name= "jiwan chand",age ="34",subject="intern")