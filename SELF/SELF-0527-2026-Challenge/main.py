#  Advanced (The "Bracket Validator")The Mission: You're building a compiler. Write a function that accepts a string of brackets ((, ), [, ], {, }) and determines if the input string is valid.An input string is valid if:Open brackets are closed by the same type of brackets.Open brackets are closed in the correct order.Test Cases: * "([{}])" $\rightarrow$ True"([)]" $\rightarrow$ False

def bracket_validator(in_string):
    print(f"in_string : {in_string}")
    # remove all characters but [], (), {} 
    cleansed_string = ""
    allowed_chars = "[](){}"
    expected_closing_chars =""
    #remove spaces, etc...
    for c in in_string:
        if c in allowed_chars:
            cleansed_string += c
            
    #odd length must be false
    if len(cleansed_string) % 2 !=0:
        return False
    
    for c in cleansed_string:
        if c == "(":
            expected_closing_chars += ")"
        elif c == "[":
            expected_closing_chars += "]"
        elif c == "{" :
            expected_closing_chars += "}"
    # reverse expected_closing_char string to get appropriate order
    expected_closing_chars=expected_closing_chars[::-1]
    
    half_len = int(len(cleansed_string)/2)
    print(cleansed_string[half_len:])
    print(expected_closing_chars)
    if cleansed_string[half_len:] == expected_closing_chars:
        return True
    else: 
        return False
       
print(bracket_validator("((()))"))