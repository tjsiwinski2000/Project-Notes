# You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

# sumOdd: the sum of the smallest n positive odd numbers.

# sumEven: the sum of the smallest n positive even numbers.

# Return the GCD of sumOdd and sumEven.

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n==1:
            return 1
        even_sum =0
        odd_sum =0
        even_factors=[]
        odd_factors=[]
        for num in range(1,2*n+1,2):
            odd_sum += num
        # print(odd_sum)
        for num in range(2,2*n+2,2) :
            even_sum += num
        # print(even_sum)
            
        # for num in range (1,int(even_sum/2) +1):
        #     if even_sum % num ==0:
        #         even_factors.append(num)
        # replace ^ with comprehension below
        even_factors = [num for num in range(1,int(even_sum/2) +1) if even_sum % num ==0]
        # print(even_factors)
        
        # for num in range(1,int(odd_sum//2)+1):
        #     if odd_sum % num == 0:
        #         odd_factors.append(num)
        # replace ^ with comprehension below
        odd_factors = [num for num in range(1,int(odd_sum//2)+1) if odd_sum % num == 0]
        # print(odd_factors)
        # print(max([num for num in even_factors if num in odd_factors]))
        return max([num for num in even_factors if num in odd_factors])
            

my_object = Solution()
print(my_object.gcdOfOddEvenSums(4))