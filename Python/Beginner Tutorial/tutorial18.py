# Tutorial 18 - Try and except

text = input("Username: ")

try:
    number = int(text)
    print(number)
    
except:
    print("Invalid Usernames")
