class shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(shape):
    def __init__(self, length , width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self): 
        return self.length * self.width
    
class Circle(shape): 
    def __init__(self,radius , width , length):
        super().__init__(width,length)
        self.radius = radius


def area(radius):
    return math.pi * radius ** 2

import math
def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()



