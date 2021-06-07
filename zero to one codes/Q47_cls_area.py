import math
class Shape:

    def area(self):
        return 0
    

class Square (Shape):
    def __init__(self, s):
        self.s = s
    
    def area(self):
        return self.s **2


class Circle:

    def __init__(self,r):
        self.r = r
    
    def area(self):
        return self.r ** 2 * math.pi


c1 = Circle(3)
print(c1.area())


s1 = Square(5)
print(s1.area())



