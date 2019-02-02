# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#simple tuple
fruitTuple = ('Apple','Orange','Mango')
#Using constructor
#fruitTuple = tuple(('Apple','Orange','Mango'))

#print(fruitTuple)

#get single value
#print(fruitTuple[1])

#Cannot change values in tuples
#fruitTuple[1] = 'Grape'

#Tuples with one value should have trailing comma
secondTuple = ('Apple',)
del secondTuple #you cannot delete individual elements from a tuple but you can delete the whole tuple

print(fruitTuple)

#get length of tuple
#print(len(fruitTuple))
 


# A Set is a collection which is unordered and unindexed. No duplicate members.

fruitSet = {'Apple','Orange','Mango'} 

print(fruitSet)

#check if element is in set
print('Apple' in fruitSet)

#add to set
fruitSet.add('Grape')

#remove from set
fruitSet.remove('Grape')

#clear set
fruitSet.clear()

print(fruitSet)

#Delete fruit set
del fruitSet