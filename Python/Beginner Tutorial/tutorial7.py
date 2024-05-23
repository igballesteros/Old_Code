# while condition == True:
#     do this

# keyword break - interrupts loop that it is in

loop = True

while loop:
    password = input("Password: ")
    if password == "stop":
        loop = False
