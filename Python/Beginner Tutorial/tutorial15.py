# Tutorial 15 - .count() and .find()

# .count(), .find()

string = "Hello"

# finds index of what you are looking for
print(string.find("l"))

# counts how many of one elements are on a string/list
string1 = "afio masdoifjoasidnfoiasdnc o;ashfoasd"
print(string1.count("a"))

string2 = input("Please type something: ")
if string2.count("_") > 0:
    print("Not good")
else:
    print("Good")
