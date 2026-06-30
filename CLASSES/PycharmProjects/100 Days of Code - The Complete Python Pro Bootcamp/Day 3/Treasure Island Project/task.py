print("Welcome to the find Snoopy Game\nYour mission is to find the snoopy.")

first_decision=input("There's a fork in the road you can go Left or Right, "
                     "please enter L or R\n").upper()

if first_decision =="R":
    print("You get eaten by a monkey, GAME OVER")
elif first_decision == "L":
    second_decision=input("The path leads to a river do you swim or wait for a ferry, "
                          "please enter S or F\n").upper()
    if second_decision == "S":
        print("You get eaten by a river shark, GAME OVER")
    elif second_decision == "F":
        third_decision=input("There's a house with three doors Red, Blue, Yellow, "
                             "which door do you choose, please enter B or Y or R\n").upper()
        if third_decision == "B" or third_decision == "R":
            print("YOu get eaten by warthog hiding behind the door, GAME OVER")
        elif third_decision=="Y":
            print("YOU WIN , YOU FOUND THE SNOOPY!")
            print("===================================")
            print(r'''
                                , ----.
                              -  -     `
                        ,__.,'           \
                      .'                 *`
                     /       |   |     / **\
                    .                 / ****.
                    |    mm           | ****|
                     \                | ****|
                      ` ._______      \ ****/
                               \      /`---'
                                 \___(
                                 /~~~~\
                                /      \
                               /      | \
                              |       |  \
                    , ~~ .    |, ~~ . |  |\
                   ( |||| )   ( |||| )(,,,)`
                  ( |||||| )-( |||||| )    | ^
                  ( |||||| ) ( |||||| )    |'/
                  ( |||||| )-( |||||| )___,'-
                   ( |||| )   ( |||| )
                    ` ~~ '     ` ~~ '
''')

