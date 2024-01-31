# A List is a collection which is ordered and changeable. Allows duplicate numbers.

#Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Pears', 'Banana']

#Use a constructor
number2 = list((1, 2, 3, 4, 5))

print(numbers, number2)
print(fruits[0])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)