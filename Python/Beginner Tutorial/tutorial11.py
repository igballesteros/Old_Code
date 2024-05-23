# Tutorial 11 - Slice operator

fruits = ["Apples", "Pear", "Strawberries"]
text = "Hello, I like Python"

print(fruits[1])
print(text[1])

# slice operator

print(text[::2]) # start:stop:step, remove from right to left

fruits[0:0] = "Blueberries"
