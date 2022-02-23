class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Стороны треугольника: a = {self.a}, b = {self.b}, c = {self.c}'


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f'Стороны прямоугольника: x = {self.x}, y = {self.y}')



triangle_1 = Triangle(20, 25, 27)
rectangle_1 = Rectangle(15, 35)

print(str(triangle_1))
print(str(rectangle_1))

