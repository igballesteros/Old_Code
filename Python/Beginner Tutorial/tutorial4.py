#conditional statements

#if condition == true/false:
#   do this
#
#input comes in as a str variable

age = input("Input your age: ")

if int(age) >= 16:
    print("hey, you are older than 16")
    
else:
    print("You are younger than 16")

#-----------------------------------------------------------

height = input()

if int(height) < 1:
    print("you cannot ride")

elif int(height) > 2:
    print("you cannot ride, over 2m")

else:
    print("you can ride")
    
