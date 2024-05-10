# The exec() function in Python is used to execute dynamically created Python code. It takes either a string containing Python code, or a precompiled code object, and executes it within the current Python runtime.

from math import *
exec("print('Hi there ')")

code = '''
def greet(name):
    print("Hello,", name)
'''

# Execute the code using exec()
exec(code)

greet('Alice')

insert_code = input('enter your code:')
exec(insert_code)

code2 = '''x=sqrt(16)
print(x)'''
exec(code2)
