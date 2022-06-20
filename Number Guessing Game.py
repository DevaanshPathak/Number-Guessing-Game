import random
def instructions():
    print("Welcome to the guessing game you will have 3 tries to pick a number 1-10")
    print("Good luck!")


instructions()
guess_limit = 1
number = random.randint(1, 10)
user = int(input("What is the number?: "))
while user != number:

    if user > number:
        print("Lower")

    elif user < number:
        print("Higher")

    user = int(input("What is the number?: "))
    guess_limit += 1
    if guess_limit == 3:
        print("------------------------------------------------------")
        print("You ran out of guess the answer was", number, "<--")
        print("------------------------------------------------------")
        break
else:
    print("You guessed it right! The number is", number,
          "and it only took you ", guess_limit, "tries")