# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]
#
# TJS: n= 2 , Output: ["(()),()()"]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return_list=[]
        basic_pair ="()"
        if n == 1:
            return "()"
        else:
            # stack one
            temp = n * basic_pair
            return_list.append(temp)
            # stack two
            temp = n * "(" 
            temp += n * ")"
            return_list.append(temp)
            # stack three
            if n > 2 :
                temp =''
                for count in range(1,n):
                    temp +=basic_pair
                    print(f'stack three temp: {temp}, count:{count}')
                temp = "(" + temp + ")"
            return_list.append(temp)
            
            return return_list
                        
        
 
n=3     
my_object = Solution()
print(my_object.generateParenthesis(n))