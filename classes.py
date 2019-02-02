# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create class
class User:
    #Constructor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

class Customer(User):
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe {self.balance}'



#Init user object
zain = User('Zain Ul-Abdeen','zain@gmail.com',24)
rida = User('Rida Zehra Ul-Abdeen','rida@gmail.com',25)


#edit property
zain.age = 25
zain.has_birthday()

print(zain.name)
print(rida.email)

#call method
print(zain.greeting())

john = Customer('John Doe','john@gmail.com',40)

john.setBalance(500)

print(john.greeting())