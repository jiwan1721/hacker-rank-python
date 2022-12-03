
"""
This follows LIFO mechanism --> Last in First out
"""

class mystack:
    def __init__(self):
        self.data =[]
    
    def length(self):
        return len(self.data)
    
    def is_full(self):
        if len(self.data)== 5:
            return True
        else:
            return False
    
    def push(self, element):
        if len(self.data)<5:
            self.data.append(element)
        else:
            return "overflow"
    
    def pop(self):
        if len(self.data)==0:
            return "underflow"
        else:
            return self.data.pop()

a = mystack()
a.push(10)
a.push(12)
a.push(12)
a.push(12)
a.push(34)
print(a.length())
print(a.is_full())
print(a.push(45))
print(a.pop()) #LIFO 34 is poped first