import random
import math
number = random.randrange(1,1000)
correct = False
tries = 1

while 1:
    guess = input("Take a guess from 1 to 1000... ")
    guess = int(guess)
    if guess != number:
        if guess > number:
           print("Wrong! Try guessing lower.")
        else:
           print("Wrong! Try guessing higher.")
        tries += 1
    else:
        print("Your guess is right and genius! Good job!! :D")
        print("It took you", tries, "attempts to get it right.")
        break