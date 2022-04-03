class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

class Square(Rectangle):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def Area (self):
        return self.length * self.breadth

class Cube(Rectangle):
    def __init__(self, length, breadth,height):
        super().__init__(length, breadth)
        self.height = height

    def Volume(self):
        return self.length * self.breadth * self.height

square = Square(3,3)
cube = Cube(3,3,3)
print(square.Area())
print(cube.Volume())