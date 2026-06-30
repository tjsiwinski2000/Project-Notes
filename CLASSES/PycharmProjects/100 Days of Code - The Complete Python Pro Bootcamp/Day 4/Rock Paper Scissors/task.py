rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import  random
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

#Declare list that contains vars->ASCII art
possible_choices=[rock,paper,scissors]

#Display ASCII art for user's choice
print(possible_choices[user_choice])

computer_choice=random.randint(0,2)
#Display ASCII art for computer's choice
print(f"Computer chose:\n{possible_choices[computer_choice]}")

#Declare three lists
#...each list represents possible outcomes for a user's choice; outcomes listed in appropriate order
#...e.g. user_rock[0] would be outcome user:rock and computer: rock
user_rock=["Both chose rock, tie", "Computer chose paper, computer wins", "Computer chose scissors, you win."]
user_paper=["Computer chose rock, you win", "Both chose paper, tie","Computer chose scissors, computer wins" ]
user_scissors=["Computer chose rock, computer wins", "Computer chose paper, you win","Both chose scissors, tie" ]

#Nested list of above three lists
determine_win_lose=[user_rock, user_paper, user_scissors]

#Pick appropriate list in nested list and appropriate entry within "appropriate list"
print(determine_win_lose[user_choice][computer_choice])