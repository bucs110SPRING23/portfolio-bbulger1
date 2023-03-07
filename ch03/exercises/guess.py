import random
number = random.randrange(1,10)
chances = 3

for attempt in range(3):
    guess = input("Take a guess from 1 to 10... ")
    guess = int(guess)
    if guess != number:
        if attempt != 2:
            if guess > number:
                print("Your guess is wrong and stupid! Guess lower, idiot!")
            else:
                print("Your guess is wrong and stupid! Guess higher, idiot!")
            if attempt == 0:
                print("Only 2 chances left!")
            if attempt == 1:
                print("Only 1 chance left!")
        else:
            print("Nope. Game over... you are a LOSER.")
    else:
        print("Your guess is right and genius! Good job!! :D")
        break