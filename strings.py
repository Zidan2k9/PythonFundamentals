# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Zain'
age = 24

#concatenate

print('Hello my name is ' + name + ' and I am ' + str(age))

# String Formatting


#Arguments by position
print('{},{},{}'.format('a','b','c'))
print('{1},{2},{0}'.format('a','b','c'))


#arguments by name

print('My name is {name} and I am {age}'.format(name='Zain',age='24'))

#F Strings (Python 3.6 +)

print(f'My name is {name} and I am {age}')

# String Methods

s = 'hello there world'

#capitalize first letter
print(s.capitalize())

# capitalize all
print(s.upper())

#all lower case
print(s.lower())


#swap case
print(s.swapcase())

#Get length of string
print(len(s))

#Replace
print(s.replace('world','everyone'))

#count
sub = 'h'
print(s.count(sub))