# 1010-2025 review

print("Review strengthens memory 1010-2025")

    #30.85 round,2D

run_code = False
if  run_code:
    sTemp = "Hello"
    for i in range(0, 5):
        print(f"{sTemp[i]} {i}")

    print(type(sTemp))
    print(type(int("123")))

    # rounding
    bmi = 84 / 1.65 ** 2  # 30.85399449035813
    print(int(bmi))  # 30 floor
    print(round(bmi))  # 31 round
    print(round(bmi, 2))
    
    # mod function
    number_input=int(input("Please enter a number\n"))
    if (number_input % 2) == 0:
       print(f"{number_input} is even.")
    else:
       print(f"{number_input} is odd.")

    #input combined with possible choices, clever
    user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
    possible_choices=["rock","paper","scissors"]
    print(possible_choices[user_choice])

student_scores = [150, 142, 185, 89]
print(f"student_scores = {student_scores}")
print(f"max student_scores: {max(student_scores)}")

# simple way to do something 4x e.g. make a square
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)




