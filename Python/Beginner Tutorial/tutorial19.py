# Tutorial 19 - Global vs. Local Variables

var = 9
loop = True
otherVar = 10

# global lets the function look for outside variables

def func(x):
    global loop
    loop = 8
    newVar = 7
    print(var)

    if x == 5:
        return newVar

# will not work, local to function
# print(newVar)

def otherFunc():
    otherVar = 5
    print(otherVar)

# it will print 5 - always uses local
otherFunc()
func(2)
