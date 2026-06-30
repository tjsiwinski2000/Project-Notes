#TJS: original idea for hangman algorithm
# example: beekeeper , [guess is "e" return _ee_ee_e_], [guess is "b" return bee_ee_e_]

word_selected="beekeeper"
word_list = list(word_selected)
game_over=False
display_matches=""
first_guess=True

while not game_over:
    guess = input("Guess a letter: ").lower()
    if ("_" in display_matches) :
        game_over=False
    else:
        if  first_guess == False:
            game_over=True

    if first_guess == True:
        for char in word_selected:
            if char == guess:
                display_matches += guess
            else:
                display_matches += "_"
            first_guess = False
    else:
        print("second guess or later")

        #Determine location of [guess] within the [word_selected] string
        positions = [i for i, char in enumerate(word_selected) if char == guess]
        print(positions)
        #turn string in to list so we can modify it
        s_list=list(display_matches)
        #replace characters at those positions
        for pos in positions:
            s_list[pos] = guess
        #recreate the string
        display_matches="".join(s_list)

    print(display_matches)