# Write a one-line Python expression that takes a list of numbers and returns a new list containing only the numbers that are prime.

# To check if a number is prime in Python, the most efficient standard approach is to test if it is divisible by any integer from 2 up to the square root of the number. [
#     validate-if-input-number-is-prime)

# Example: [4, 7, 10, 13, 15, 17, 21] → [7, 13, 17]

# Give it a shot — let me know what you come up with and I'll check i

my_list = [4, 7, 10, 13, 15, 17, 21]
import math
def is_prime(current_num):
    for index in range(2,int(math.sqrt(current_num)+1)):
        if current_num % index == 0:
            return False
    return True
        
print( [num for num in my_list if is_prime(num)])