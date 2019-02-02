# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

#int, float, string, bool

x = 1
y =2.5
name = 'Zain'
isCool = True


#multiple assignment
x, y , name , isCool= (1,2.5,'Zain',True)

print(x,y,name,isCool)

#Basic math

a = x + y

#check type
print(type(x))
print(type(y))
print(type(isCool))
print(type(name))

#Casting
x = str(x)
y = int(y)
z = float(y)

#check type again
print(type(x))
print(type(z))
print(z)