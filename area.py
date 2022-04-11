area of circle
class circle():
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*self.radius**2

a=circle(2)
print(a.area())
print(a.perimeter())
