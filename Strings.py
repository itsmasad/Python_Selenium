# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

# String Formatting
name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))