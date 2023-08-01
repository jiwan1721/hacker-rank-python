from abc import ABCMeta, abstractmethod
import copy

class Bachelor(metaclass = ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None
    
    @abstractmethod
    def courses(self):
        pass

    def get_type(self):
        return self.type
    
    def get_id(self):
        return self.id
    
    def set_id(self, sid):
        self.id = sid
    
    def clone(self):
        return copy.copy(self)

class CSIT(Bachelor):
    def __init__(self):
        super().__init__()
        self.type = "Bsc csit courses are good."
    
    def courses(self):
        print("------- we have multiple courses.")
    
class BCA(Bachelor):
    def __init__(self):
        super().__init__()
        self.type = "BCA have multiple couses."
    
    def courses(self):
        super().courses()

class CoursesCache:
    cache = {}

    @staticmethod
    def get_courses(sid):
        courses = CoursesCache.cache.get(sid, None)
        return courses.clone()
    
    @staticmethod
    def load():
        bca = BCA()
        bca.set_id('1')
        CoursesCache.cache[bca.get_id()] = bca

        csit = CSIT()
        csit.set_id("3")
        CoursesCache.cache[csit.get_id()] = csit


CoursesCache.load()
sde = CoursesCache.get_courses("1")
print(sde.get_type())


b = BCA()
b.get_type()


