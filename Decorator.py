# a decorator is a design pattern that allows you to modify the behavior of a function or a method. Decorators are typically used to add functionality to functions or methods in a clean, readable, and reusable way.

def adding(num):
    return num+1


print(adding(10))


def addingNew(num):
    def addingone(num):
        return num+1
    total = addingone(num)
    return total


print(addingNew(40))


def newCapital(func):
    def newInner():
        theFunc = func()
        upperCase = theFunc.upper()
        return upperCase

    return newInner


def greeting():
    return "Hi there"


decorating = newCapital(greeting)

print(decorating)
