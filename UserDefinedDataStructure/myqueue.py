"""
This follows FIFO mechanism -> First in First out
"""

class myqueaue:
    def __init__(self):
        self.data = []
    
    def length(self):
        return len(self.data)

    def enque(self, element):
        if len(self.data) < 5:
            return self.data.append(element)
        else:
            return "overflow"
    
    def deque(self):
        if len(self.data) == 0:
            return "underflow"
        else:
            self.data.pop(0)

b = myqueaue()
b.enque(4)
b.enque(6)
b.enque(7)
print(b.data)
b.deque() # it will pop first inserted item
print(b.data)