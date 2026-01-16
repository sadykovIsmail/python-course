import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    # ✅ FIXED METHOD
    def get_amount_inside(self, other):
        fit_width = self.width // other.width
        fit_height = self.height // other.height
        return fit_width * fit_height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, value):
        self.width = value
        self.height = value

    def set_width(self, value):
        self.set_side(value)

    def set_height(self, value):
        self.set_side(value)

    def __str__(self):
        return f"Square(side={self.width})"
