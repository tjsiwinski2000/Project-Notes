# Python Challenge #2: Convert Binary Numbers to Decimal

# The challenge: Write a function that converts a binary number to its decimal equivalent.

# Decimal    Binary
# -------    --------------
# 2          10
# 5          101
# 17         10001
# 23         10111
# 10012      10011100011100

def convert_bin_dec(in_num):
    print(f'binary: {in_num}')
    in_num_len = len(in_num)-1
    deciml = 0
    for count in range(in_num_len,-1,-1):
        current_digit = in_num[count]
        if current_digit =="1":
            deciml += 2 ** (in_num_len - count)
        # print(f'Current Digit:{current_digit}\tCurrent Decimal value:{deciml} ' )
    return deciml
        
my_num='10111'
print(convert_bin_dec(my_num))

# solution on freecode camp
# https://www.freecodecamp.org/news/python-coding-challenges-for-beginners/#heading-python-challenge-1-check-if-a-list-is-sorted
def binary_to_decimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

