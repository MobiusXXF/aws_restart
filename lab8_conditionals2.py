import random

print("**Working with while loops")
print(" ")

print("--Writing the while loop:")
print("Python Game")
print(" ")

print("Welcome the Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You Win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
#Game logic in non-code sentences, "pseudocoding":
#If the user has not guessed the correct answer, enter the loop.
#Ask the user for a guess.
#Is the guess the correct number?
#If the correct guess, tell the user it was the correct guess and exit the loop.
#If the wrong guess, tell the user it was the wrong guess and continue the loop.

