# 0929-2025 Number guessing game, no hints or base code provided
#
import random
number_to_guess=random.randint(1,100)
import tj_art
print(tj_art.logo)
print(f"debug: {number_to_guess}")

def process_guess(guess,remaining ):
    """ input: current guess and remaining number of  guesses, output: -1 (solved) or guesses_remaining -1 """
    if number_to_guess == guess:
        print(f"You got it! The answer was {guess}")
        return -1
    else:
        remaining -= 1
        print(f"You have {remaining} attempts remaining to guess the number")
        if guess > number_to_guess:
            print("Too high.")
        else:
            print("Too low.")
        return remaining

# prompt variables
openingStatement= "Im thinking of a number between 1 and 100."
difficultyPrompt="Choose a difficulty. Type 'easy' or 'hard':"
guestPrompt="Make a guess:"


print(openingStatement)
difficulty=input(difficultyPrompt).lower()
num_guess_remaining=0
if difficulty == 'easy':
    num_guess_remaining = 10
else:
    num_guess_remaining =5


print(f"You have {num_guess_remaining} attempts remaining to guess the number")

while num_guess_remaining >0:
    current_guess=int(input(guestPrompt))
    num_guess_remaining = process_guess(current_guess,num_guess_remaining)

if num_guess_remaining == 0:
    print("You've run out of guesses, you lose.")
