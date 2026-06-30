#1002-2025 TJS
# Import necessary modules / files
import random
import game_data
import art

# Initialize variables , import all data
current_score=0
game_over = False
display_a=[]
display_b=[]

data_list= []
data_list= game_data.data

debug = False

def play_game(display_passed):
    print("\n" *20)
    # Display logo art main
    if not debug:
        print(art.logo)

    # Gain access to global variable
    global current_score
    global  display_a
    global  display_b

    if len(display_b) > 0:
        display_a = display_passed # display_b len is zero first time game played
    else:
       display_a=random.choice(data_list)  # Display A , random entry game_data.py

    print(f"{display_a['name']}, a {display_a['description']}, from {display_a['country']} debug:{display_a['follower_count']}")

    # Display logo art vs
    if not debug:
        print(art.vs)
    print("Against B:")
    # Display B
    # Randomize check display_a != display_b
    display_b=random.choice(data_list)
    print(f"{display_b['name']}, a {display_b['description']}, from {display_b['country']} debug:{display_b['follower_count']}")

    user_choice=input("Who has more followers? Type 'A' or 'B':").lower()

    if user_choice=='a':
        if display_a['follower_count'] > display_b['follower_count']:
            #increment score
            current_score+= 1
            print(f"You're right! Current score: {current_score}.")
            return False
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            return True
    else:
        if display_b['follower_count'] > display_a['follower_count']:
            #increment score
            current_score +=1
            print(f"You're right! Current score: {current_score}.")
            return False
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            return True

while not game_over:
    game_over=play_game(display_b)

# ToDo Choice B now becomes A , pick random person and Display B
# ToDo Force randomization so can't have two identical picks
