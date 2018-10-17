# Writing a method

class Shape:
    def __init__(self, name, sides, colour=None):
        self.name = name
        self.sides = sides
        self.colour = colour

    def getInfo(self):
        return '{} {} with {} sides'.format(self.colour,
                                            self.name,
                                            self.sides)


s = Shape('square', 4, 'green')
print(s.getInfo())



# example of classmethod and staticmethod

class Shape:
    def __init__(self, name, sides, colour=None):
        self.name = name
        self.sides = sides
        self.colour = colour

    @classmethod
    def greenShape(cls, name, sides):
        print(cls)
        return cls(name, sides, 'green')

    @staticmethod
    def trapezium_area(a, b, height):
        # area of trapezium = 0.5(a + b)h
        return 0.5 * (a + b) * height


green = Shape.greenShape('rectangle', 4)
print('{} {} with {} sides'.format(green.colour,
                                   green.name,
                                   green.sides))

print(Shape.trapezium_area(5, 7, 4))



# demonstrating differences when calling regular methods, classmethods
# and staticmethods

class Shape:
    def dummyMethod(self, *args):
        print('self:', self)
        print('args:', *args)

    @classmethod
    def dummyClassmethod(cls, *args):
        print('cls :', cls)
        print('args:', *args)

    @staticmethod
    def dummyStaticmethod(*args):
        print('args:', *args)


square = Shape()

# calling regular method from instance
square.dummyMethod('arg')
print(repr(square.dummyMethod) + '\n')

# calling regular method from class
Shape.dummyMethod('arg')
print(repr(Shape.dummyMethod) + '\n')


# calling classmethod from instance
square.dummyClassmethod('arg')
print(repr(square.dummyClassmethod) + '\n')

# calling classmethod from class
Shape.dummyClassmethod('arg')
print(repr(Shape.dummyClassmethod) + '\n')


# calling staticmethod from instance
square.dummyStaticmethod('arg')
print(repr(square.dummyStaticmethod) + '\n')

# calling staticmethod from class
Shape.dummyStaticmethod('arg')
print(repr(Shape.dummyStaticmethod) + '\n')
