# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Zain','Rida','Zaid','Mom','Dad']

for person in people:
    print('Current person is ' , person)

#Break out 

for person in people:
    
    if person == 'Zaid':
        break
    print('Current person is ' , person)


#Continue
for person in people:
    if person == 'Mom':
        continue
    print('Current person is ', person)

#Range
for i in range(len(people)):
    print('Current person',people[i])

for i in range(0,11):
    print('Number ',i)

# While loops execute a set of statements as long as a condition is true.

count = 0

while count <= 10:
    print('Count ', count)
    count += 1
