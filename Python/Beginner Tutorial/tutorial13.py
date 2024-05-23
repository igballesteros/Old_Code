# Tutorial 13 - Reading a Text File

file = open("file.txt", "r")
f = file.readlines()

newList = []

# One way to remove \n
#for line in f:
#    if line[-1] == "\n": # -1 is the last character in a string
#        newList.append(line[:-1])
#    else:
#        newList.append(line)

#print(newList)

# Other way

for line in f :
    newList.append(line.strip())

print(newList)

file.close()
