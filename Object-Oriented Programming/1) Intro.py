# Creating a basic class template:

class Shape:
    pass


square = Shape()
print(square)



# Defining an __init__ method:

class Shape:
     def __init__(self, name, sides, colour=None):
         self.name = name
         self.sides = sides
         self.colour = colour


try:
    square = Shape()
except TypeError as e:
    print('TypeError:', e)

square = Shape('Square', 4, 'green')
print(square.name)
print(square.sides, square.colour)
