import random

number = random.randint(1, 100)  # O 100 está incluso no sorteio

print("What's your name?")
name = input()
print("Hey", name, "Let's start our game to guess the secret number!")

print("What's your first guess? Pick a number? Choose a number from 1 to 100")
guess = int(input())
if guess == number:
    print("Uhuuu! Congrats", name + "!!!")
    print("You guessed the secret number! (" + str(number) + ")")
else:
    while guess != number:
        print("Ops, you didn't get the secret number...")
        if guess > number:
            print("The secret number is LOWER")
        else:
            print("The secret number is HIGHER")
        print("What's your next guess?")
        guess = int(input())
    print("Uhuuu! Congrats", name + "!!!")
    print("You guessed the secret number! (" + str(number) + ")")