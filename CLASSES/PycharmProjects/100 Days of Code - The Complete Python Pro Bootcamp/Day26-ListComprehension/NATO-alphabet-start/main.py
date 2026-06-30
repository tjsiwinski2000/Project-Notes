import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
NATO_data_frame= pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {}

#My solution to create NATO_dict; works 1105-2025:835am
# for (index,row) in NATO_data_frame.iterrows():
#     NATO_dict[row.letter] = row.code

#Instructors way to create NATO_dict using comprehension
NATO_dict = {row.letter: row.code for (index,row) in NATO_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user_word = input("Please enter your word\n")
    user_word = user_word.upper()

    try:
        result = [NATO_dict[letter] for letter in list(user_word)]
    except KeyError:
        print("Sorry only letters from the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()