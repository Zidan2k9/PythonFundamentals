# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary


import json

#sample json
userJSON = '{"firstName": "John", "lastName": "Doe", "age": 30}'

#parse to dictionary
user = json.loads(userJSON)

print(user)
print(user['firstName'])

car = {'make':'Toyota','model':'Yaris Hybrid','year':2015}

carJSON = json.dumps(car)

print(carJSON)