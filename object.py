class circle:
    def __init__(self,radius):
        self.radius=radius
        print("radius of the circle is:",self.radius)
    def perimeter(self):
        print(self.radius*2*22/7)
    def area(self):
        print(self.radius*self.radius*22/7)
num=circle(12)
num.perimeter()
num.area()