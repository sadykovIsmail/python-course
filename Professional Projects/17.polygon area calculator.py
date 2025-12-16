import math
class Rectangle:
    def __init__(self):
        
        self.width = 0
        self.height = 0
    
    #setter
    def set_width(self, value: int):
        self.width = value
        return f"Width set to: {self.width}"
        
    #setter
    def set_height(self, value: int):
        self.height = value
        return f"Width set to: {self.height}"
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        

class Square(Rectangle):
    pass
    
    
rectangle = Rectangle()

print(rectangle.set_width(3))
print(rectangle.set_height(2))
print(rectangle.get_area())
print(rectangle.get_perimeter())
print(rectangle.get_diagonal())
