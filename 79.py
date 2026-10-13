Instance methods :Rectangle area and perimeter
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of Rectangle:", self.length * self.breadth)

    def perimeter(self):
        print("Perimeter of Rectangle:", 2 * (self.length + self.breadth))


r1 = Rectangle(10, 5)

R
r1.area()
r1.perimeter()