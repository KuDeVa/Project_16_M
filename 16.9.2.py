class Rectangle:
    def __init__(self, w, l): # width (ширина), length (длинна)
        self.width = w
        self.length = l

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(17,35)
print(newRectangle.rectangle_area())
