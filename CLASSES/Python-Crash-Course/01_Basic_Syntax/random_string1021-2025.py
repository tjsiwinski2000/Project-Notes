# Review of python concepts, randomizing a string 

import random
# 1. Base string
stemp = "abcdefghi"
# 2. Convert to a list for randomization
stemp = list(stemp)
# 3. stemp is now randomized
random.shuffle(stemp)

# 4a. convert stemp to a string 
password=""
for char in stemp:
    password += char
print(password)

# 4b. convert stemp to a string (alternative solution)
password2 = "".join(stemp)
print(password2)