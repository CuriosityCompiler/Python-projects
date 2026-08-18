import random
print("Welcome to the Number Guessing Game!\n"
      "You have to guess a number between a range of your choice.\n"
      "You have 7 chances to guess the number correctly.\n"
      "Good luck!")
low = int(input("Enter the lower value: "))
high = int(input("Enter the higher value: "))

number =random.randint(low, high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input(f'Guess a number between {low} and {high}:'))
    if guess == number:
        print(f'Congratulations! You guessed the number {number} correctly in {gc} attempts!')
        break
    elif guess < number:
        print('Your guess is too low. Try again.')
    elif guess > number:
        print('Your guess is too high. Try again.')
    elif guess != number and gc == ch:
        print(f'Sorry, you have used all your chances. The correct number was {number}. Better luck next time!')


