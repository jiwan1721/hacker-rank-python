def timeConversion(s):
    x = s.split(":")
    y=[]
    if x[0] =="12" and "AM" in x[2]:
        x[0] = "00"
        x[2] = x[2].replace("AM", "")
        return ":".join(x)
    elif "PM" in x[2] and int(x[0]) != 12:
        x[0] = str(int(x[0])+12)
        x[2] = x[2].replace("PM", "")
        return ":".join(x)
    else:
        if "AM" in x[2]:
            x[2] = x[2].replace("AM", "")
            return ":".join(x)
        else:
            x[2] = x[2].replace("PM", "")
            return ":".join(x)

time = "12:45:54PM"
print(timeConversion(time))

def grade(result):
    res = []
    for r in result:
        remainder = r%5
        if remainder ==0 and r >=40:
                res.append(r)
        elif remainder == 3:
            x = r+2
            if x>=40:
                res.append(x)
            else:
                res.append(r)
        elif remainder == 4:
            x = r+1
            if x>=40:
                res.append(x)
            else:
                res.append(r)
        elif remainder==2 and r>40:
            res.append(r)
        else:
            res.append(r)
            



    print(len(res))

result = [80,96,18,75,80,60,60,15,45,10,5,46,33,60,14,71,65]
print(len(result))

print(grade(result))