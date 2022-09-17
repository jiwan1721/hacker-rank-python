def fizzeBuzze(number,fizzeItem,BuzzeItem):
    for number in range(1,number):
        fizzeNum =number%fizzeItem==0
        buzzeNum=number%BuzzeItem==0
        if fizzeNum and buzzeNum:
            print("fizze","buzze")  
        elif fizzeNum:
            print("fizze") 
        elif buzzeNum:
            print("buzze")
        else:
            print(number)

fizzeBuzze(20,1,2)
