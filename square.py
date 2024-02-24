class Shape:
        def __init__(self, name, length):
                return
        def area():
                return 0
                
class Square(Shape):
        def __init__(self, name, length):
                self.name = name
                self.length = length
        def area(self):
                print('The area is:\n')
                return self.length * self.length
        def describe(self):
                return '\nThis is a:' + self.name
                
s = Square('square',5)
print(s.area())
print(s.describe())
