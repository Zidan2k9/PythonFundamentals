# If/ Else conditions are used to decide to do something based on something being true or false

x= 10
y=10
# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#simple if
if x==y:
    print(f'{x} is equal to {y}')

#if/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')


#else if - elif
if x > y:
    print(f'{x} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')



# nested if
if x > 2:
    if x <= 10:
        print(f'{x} is less than 2 and greater than 10')

# Logical operators (and, or, not) - Used to combine conditional statements


# and

if x > 2 and x <= 10:
    print(f'{x} is less than 2 and greater than 10')

#or

if x > 2 or x <= 10:
    print(f'{x} is less than 2 and greater than 10')

#not

if not(x == y):
    print('the not conditional')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object


numbers = [1,2,3,4,5,6]

# in

if x in numbers:
    print(x in numbers)

#not in

if x not in numbers:
    print('not in the list')



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

#is 
if x is y:
    print(x is y)


if x is not y:
    print('is not')