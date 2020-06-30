# Writing a method

class Shape:
    def __init__(self, name, sides, colour=None):
        self.name = name
        self.sides = sides
        self.colour = colour

    def get_info(self):
        return '{} {} with {} sides'.format(self.colour,
                                            self.name,
                                            self.sides)


s = Shape('square', 4, 'green')
print(s.get_info())



# example of classmethod and staticmethod

class Shape:
    def __init__(self, name, sides, colour=None):
        self.name = name
        self.sides = sides
        self.colour = colour

    @classmethod
    def green_shape(cls, name, sides):
        print(cls)
        return cls(name, sides, 'green')

    @staticmethod
    def trapezium_area(a, b, height):
        # area of trapezium = 0.5(a + b)h
        return 0.5 * (a + b) * height


green = Shape.green_shape('rectangle', 4)
print('{} {} with {} sides'.format(green.colour,
                                   green.name,
                                   green.sides))

print(Shape.trapezium_area(5, 7, 4))



# demonstrating differences when calling regular methods, classmethods
# and staticmethods

class Shape:
    def dummy_method(self, *args):
        print('self:', self)
        print('args:', *args)

    @classmethod
    def dummy_classmethod(cls, *args):
        print('cls :', cls)
        print('args:', *args)

    @staticmethod
    def dummy_staticmethod(*args):
        print('args:', *args)


square = Shape()

# calling regular method from instance
square.dummy_method('arg')
print(repr(square.dummy_method) + '\n')

# calling regular method from class
Shape.dummy_method('arg')
print(repr(Shape.dummy_method) + '\n')


# calling classmethod from instance
square.dummy_classmethod('arg')
print(repr(square.dummy_classmethod) + '\n')

# calling classmethod from class
Shape.dummy_classmethod('arg')
print(repr(Shape.dummy_classmethod) + '\n')


# calling staticmethod from instance
square.dummy_staticmethod('arg')
print(repr(square.dummy_staticmethod) + '\n')

# calling staticmethod from class
Shape.dummy_staticmethod('arg')
print(repr(Shape.dummy_staticmethod) + '\n')
