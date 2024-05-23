# Tutorial 17 - Optional Parameters


# param text='2' defauls param to 2

def func(x=4, text='2'):
    print(x)
    if text == "1":
        print("Text is 1")
    else:
        print("Text is not 1")

# to change second... parameters you have to change the ones
# from before

func()
