# An ISBN-10 (International Standard Book Number) consists of 9 digits plus a check digit.

# To validate an ISBN-10, you use a specific formula. 

# If the digits are $x_1, x_2, \dots, x_{10}$, the check formula is:$$(10x_1 + 9x_2 + 8x_3 + 7x_4 + 6x_5 + 5x_6 + 4x_7 + 3x_8 + 2x_9 + 1x_{10}) \pmod{11} == 0$$

# Note: The 10th character ($x_{10}$) can sometimes be an 'X', which represents the value 10.

def isbn_helper(in_value):
    cleansed_value=''
    for n in in_value:
        if n.isnumeric() :
            cleansed_value += n
        elif n=='X':
            cleansed_value += 'X'
    # return(cleansed_value)
    count =10
    total = 0
    for n in cleansed_value:
        value = 10 if n == 'X' else int(n)
        total += count * value
        count -=1
        #debug print(f'Total currently is {total} and n is {n}')
    #debug print(f'Total is : {total}')
    # decision pont 10 digit number return boolean if mod 11 = 0
    #                9 digit number calculate & return 10th digit
    if len(cleansed_value) ==9:
        for num in range(0,11):
            # temp_value_str = cleansed_value + str(num)
            temp_value_int = total + num
            if temp_value_int % 11 == 0:
                if num <= 9 :
                    return cleansed_value + str(num)
                else:
                    return cleansed_value + 'X'
    else:
        if total % 11 == 0:
            return True
        else:
            return False
        
        

# Test 1: Valid ISBN (with hyphens) -> Should return True
print(isbn_helper("0-306-40615-2")) 

# Test 2: Invalid ISBN -> Should return False
print(isbn_helper("0-306-40615-5")) 

# Test 3: Valid ISBN ending in 'X' -> Should return True
print(isbn_helper("0-12-345678-X")) 

# Test 4: Generating the 10th digit -> Should return "0306406152"
print(isbn_helper("030640615")) 

# Test 5: Generating the 10th digit when it's 10 -> Should return "012345678X"
print(isbn_helper("012345678"))