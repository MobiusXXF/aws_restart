myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print("--Formal introduction to 'Concantenation':")
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print("--Working with input strings:")
name = input("What is your name? ")
print("Hi " + name + ", Welcome to your hello world...")
print("--Formatting output strings:")
color = input("What is your favourite color?  ")
car = input("What is your favourite car?  ")
print("{}, you like a {} {}!".format(name,color,car))
