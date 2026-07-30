# You are given an integer n.

# Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.

# Let sum be the sum of digits in x.

# Return an integer representing the value of x * sum.

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        clean_s = s.replace('0','')
        # if s == clean_s:
        if len(s) == 1:
                return n **2 
        else:
            x= int(clean_s)
            my_sum = sum([int(num) for num in s])
            return x * my_sum
   
my_object = Solution
print(my_object.sumAndMultiply(my_object,n=11))