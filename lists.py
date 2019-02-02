# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1,2,3,4,5]

#using constructor
numbers = list((1,2,3,4,5))
fruits = ['Apples','Oranges','Grapes','Pears']

print(numbers)

print(fruits[1])

# get length of array
print(len(fruits))

#append to list
fruits.append('Mangos')

print(fruits)

#remove from list

fruits.remove('Grapes')

#insert into position
fruits.insert(2,'Strawberries')

#remove from position
fruits.pop(3)

#reverse array
fruits.reverse()

#sort
fruits.sort()

#reverse sort
fruits.sort(reverse=True)

print(fruits)