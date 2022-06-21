import string,random

def randpassword():
    number = string.digits
    punc=string.punctuation
    randomPassword = list(string.ascii_letters+number+punc)

    length_password = random.randrange(8,15)
    random.shuffle(randomPassword)
    password = ''.join(random.choice(randomPassword)for i in range(length_password))
    last_value=password[-1]
    if last_value in number or last_value in punc :
        print('------')
        return randpassword()
    else:
        return password
print(randpassword())
