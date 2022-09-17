from unittest import result

name = "jiWan chand thyt.akuri fgjkljdlgkjdflgjdfkWERWR SKDJFSLf"

def nameUpper(name):
    name=name.lower()
    result=[]
    capital_letter_index=[]
    for index,value in enumerate(name):
        if index==0:
            result.append(name[0].upper())
            continue
        if value==" ":
            result.append(name[index])
            upperLetter = name[index+1]
            result.append(upperLetter.upper())
            capital_letter_index.append(index+2)
            continue
        result.append(value)
    for i in capital_letter_index:
        result.pop(i)
    
    original_result="".join(result)
    return original_result
        


print(nameUpper(name))