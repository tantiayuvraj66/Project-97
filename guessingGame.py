import random
from re import I
from ssl import _create_default_https_context
randomNumber = (random.randint(1, 9))
chances = 0
print("NUMBER GUESSING GAME")
print("Choose a number between 1 and 9 as your guess:")
while chances < 5:
    guess = int(input("Put your best guess here: "))
    if guess < randomNumber:
        print("Please select a number that is more than ", guess)
        chances = chances + 1
    elif guess > randomNumber:
        print("Please select a number that is less than ", guess)
        chances = chances + 1
    elif guess == randomNumber:
        print("Your guess was correct, so congrats!")
        break

if not chances < 5:
    print("You lost because the number was ", randomNumber)