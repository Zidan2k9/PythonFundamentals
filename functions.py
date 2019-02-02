# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#create function
def sayHello(name='John Doe'):
    """
    Prints Hello and then the name
    """
    print('Hello ' + name)

sayHello('Zain')

#Return value
def getSum(num1,num2):
    total = num1 + num2
    return total



numSum = getSum(2,3)
print(numSum)

def AddOneToNum(num):
    num += 1
    return num

num = 5
newNum = AddOneToNum(num)
print(newNum)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(9,2))

AddOneToNum = lambda num : num + 1
print(AddOneToNum(5))