# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# simple dictionary

person = {
    'firstName':'John',
    'lastName':'Doe',
    'age':30
}



#using a constructor

#person = dict(firstName='John',lastName='Doe',age=30)

#Access value
print(person['firstName'])
print(person.get('lastName'))

#Add key/value
person['phone'] = '555-555-555'

#get keys
print(person.keys())

#get values
print(person.items())

#make copy
person2 = person.copy()
person['city'] = 'Letterkenny'


#remove item
del(person['age'])
person.pop('phone')

#clear
person.clear

#get length
print(len(person2))

print(person)

#list of dictionary

people = [
    {'name':'Martha','age':40},
    {'name':'Bob','age':20}
]

print(people[1]['name'])