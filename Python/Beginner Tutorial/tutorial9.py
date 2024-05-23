# Tutorial 9 - Iteration by Item

fruits = ["apples", "pears", "strawberrys"]

for fruit in fruits:
    print(fruit)


for fruit in fruits:
    if fruit == "pears":
        print(fruit)
    else:
        print("not pears")

for x in range(len(fruits)):
    if fruits[x] == "apples":
        print(fruits[x])
    else:
        print("not apples")
