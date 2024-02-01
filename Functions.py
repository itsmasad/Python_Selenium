# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hello {name}')

sayHello('John deo')

# Creating funcion with the default value
def sayHello(name = 'Asad'):
    print(f'Hello {name}')

sayHello()

# Return values
def getSum(num1,num2):
    total = num1 + num2
    return total

print(getSum(1,2))
# Another way to print
num = getSum(6,7)
print(num)

# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
