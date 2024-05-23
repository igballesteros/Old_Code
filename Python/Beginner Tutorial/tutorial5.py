#and &&
#or ||
#not !

x = 2
y = 3

if x == y and x + y == 5:
    print("and ran")

if x == y or x + y == 5:
    print("or ran")
else:
    print(':(')

print("nested statements")

if x == 2:
    if y == 3:
        print("all work")
