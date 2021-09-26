myfile = open('conditional.py')

print(myfile.read())
print("=========")
print(myfile.read())  #this will read empty charcater as we r at the end of file
print(myfile.seek(0))  #take cursor to 0 byte
print(myfile.tell())   #check cursor byte

print(myfile.read(5))  #rrad only 5 charcter in file
print(myfile.readline())
print(myfile.readlines())

myfile.seek(0)
for line in myfile.readlines():
    if line.startswith("Cisco"):
        print(line)

newfile = open('Tips','w')
newfile.write("\nthis line is typed using file Readfile.py")
newfile.close()