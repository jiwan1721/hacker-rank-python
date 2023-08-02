class Course:
    def __init__(self):
        self.Fee()
        self.available_batches()
    
    def Fee(self):
        raise NotImplementedError
    
    def available_batches(self):
        raise NotImplementedError
    
    def __repr__(self):
        return 'Fee: {0.fee} | Batches Available : {0.batches}'


class DSA(Course):
    """calss fpr Dsa"""
    def Fee(self):
        self.fee = 899
    
    def available_batches(self):
        self.batches = 5
    
    def __str__(self):
        return "DSA"
    
class SDE(Course):
    """class for sed"""
    def Fee(self):
        self.fee = 5000
    
    def available_batches(self):
        self.batches = 5
    
    def __str__(self):
        return "STL"

class ComplexCourse:
    def __repr__(self):
        return 'Fee: {0.fee} | available batches: {0.batches}'

class complexC(ComplexCourse):
    def Fee(self):
        self.fee = 4555
    def available_batches(self):
        self.batches = 34

def counstruct_course(cls):
    course = cls()
    course.Fee()
    course.available_batches()
    return course

dsa = DSA()
sde = SDE()

complex_cou = counstruct_course(complexC) # still confused what is this functio for

print(dsa.fee)
