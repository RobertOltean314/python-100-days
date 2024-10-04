import random

number = random.randint(1,100)

print("I'm thinking of a number between 1 and 100")
user_choice : str = str(input("Choose a difficulty: 'easy', 'normal', 'hard' "))
guesses = 0

if user_choice == "easy":
    guesses = 10
elif user_choice == "normal":
    guesses = 7
elif user_choice == "hard":
    guesses = 5

while guesses != 0:
    guess : int = int(input("Pick a number: "))

    if guess == number:
        print("You guessed it!")
        break
    else:
        if guess < number:
            print("Your number is too low")
        else:
            print("Your number is too high")
        guesses -= 1

if guess == 0:
    print(f"We're sorry, you didn't guessed it... the number was {number}")