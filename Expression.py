# A Python expression is a piece of code that evaluates to a value. It can be as simple as a single variable or constant, or it can be a more complex combination of operators, functions, and operands.

x = eval('10**2')
print(x)

print(eval('sum([10, 3, 3, 4])'))

i = 10
print(eval('i**2'))
print(eval('x+y', {}, {'x': 400, 'y': 100}))

numbers = [1, 1/2, 1/3, 1/4, 1/5]
# squared_numbers is an expression evaluating to [1, 4, 9, 16, 25]
squared_numbers = sum([x ** 2 for x in numbers])
print(f"1, 1/2, 1/3, 1/4, 1/5 ={squared_numbers} ")
