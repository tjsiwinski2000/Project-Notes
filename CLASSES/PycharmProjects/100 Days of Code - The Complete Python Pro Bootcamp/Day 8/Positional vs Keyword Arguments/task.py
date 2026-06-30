# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def calculate_love_score(name1,name2):
    keyword1="TRUE"
    keyword2="LOVE"
    love_score_first_digit=0
    love_score_second_digit=0

    combined_names = (name1+name2).upper()
    print(combined_names)
    for letter in keyword1:
        position=combined_names.find(letter)
        if position != -1:
            love_score_first_digit+=combined_names.count(letter)
        #print(f"currently {love_score_first_digit} is the lovescore")
    print(f"Total={love_score_first_digit}")

    for letter2 in keyword2:
        position = combined_names.find(letter2)
        if position != -1:
            love_score_second_digit += combined_names.count(letter2)
        #print(f"currently2 {love_score_second_digit} is the lovescore")
    print(f"Total={love_score_second_digit}")

    love_score= str(love_score_first_digit)+str(love_score_second_digit)
    print(f"Love Score={love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")