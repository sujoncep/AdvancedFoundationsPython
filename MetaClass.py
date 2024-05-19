# Metaclasses are an OOP concept present in all python code by default. Python provides the functionality to create custom metaclasses by using the keyword type. Type is a metaclass whose instances are classes. Any class created in python is an instance of type metaclass. The type() function can create classes dynamically as calling type() creates a new instance of type metaclass.

class Newsample():
    pass


obj1 = Newsample()
print(type(obj1))

print(type(Newsample))

a = type('pyton', (), {'x': 10})
obj = a()
print(obj.x)


class Player:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.number = 4


# Player = type('Player', (), {'__init__': init})

newObj = Player("ahmad", "70")

# Bulding metaclass


class NewMeta(type):
    __metaclass__ = type


class NewDemo:
    __metaclass__ = NewMeta


newObject = NewDemo()

print(newObject.__metaclass__)
print(NewMeta.__metaclass__)
