# Python has functions for creating, reading, updating, and deleting files.


#open a file
myFile = open('myfile.txt','w')

#Get info

print('Name ' + myFile.name)
print('is closed ',myFile.closed)
print('Opening file ',myFile.mode)

#write to file
myFile.write("I love python")
myFile.write(" and javascript")
myFile.close()

#append to file
myFile = open('myfile.txt','a')
myFile.write(' I also like Java')
myFile.close()

#read from file
myFile = open('myfile.txt','r+')
text = myFile.read(100)
print(text)