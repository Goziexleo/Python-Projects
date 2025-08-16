import random

print("Hi!, Welcome to the Number Guessing Game.\nYou have 7 chances to guess the correct number. Let's start!")
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

print(
    f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")


num = random.randint(low, high)

chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(
            f'Correct! The number was {num}. You guessed it in {guess_counter} attempts.')
        break
    elif guess_counter >= chances and guess != num:
        print(f"Sorry! The number was {num}. Better luck next time!")
    elif guess > num:
        print("Too high!, try a lower number")

    elif guess < num:
        print("Too low!, try a higher number")
