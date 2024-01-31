# A Tuple is a collection which is ordered and unchangeable. Allows duplicate memebers.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

# Single value needs trailing comma
fruits1 = ('Apples',)
print(fruits1, type(fruits1))

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'pears'

# Delete tuple
# del fruits
print(fruits)

# Get lenth
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set ( it is created with curly brases)
fruits_set = {'Apples', 'Bananas', 'Mangos'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)