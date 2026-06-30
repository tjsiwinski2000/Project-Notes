# =============================
# Leetcode Challenge
# - 311/315 test cases passed before time ran out
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
#Example nums = [-1,0,1,2,-1,-4]
#Output Expected  [[-1,-1,2],[-1,0,1]]
#=====================================

class  Solution(object):
    def threeSum(self, nums):
        sorted_nums=sorted(nums)
        # print(f'sorted_nums: {sorted_nums}')
        #start two pointer logic here
        left = 0 
        right = len(nums) -1
        
        total = 0 
        return_value = []
        my_tuple = (0,0,0) #default
        while True:
            temp = sorted_nums[left] + sorted_nums[left+1] + sorted_nums[right]
            # print(f'temp currently: {temp} : { sorted_nums[left]} , {sorted_nums[left+1]} ,{sorted_nums[right]}')
            if temp < 0:
                if left +1 <right -1:
                    left +=1
                else:
                    # print(f'done ... ran out of values')
                    return return_value
            elif temp ==0:
                my_tuple = (sorted_nums[left] , sorted_nums[left+1] , sorted_nums[right])
                return_value.append(my_tuple)
                if right ==2:
                    # print(f'done ... ran out of values')
                    return return_value
                else:
                    right -=1
                    left = 0
                    # left +=1
                    # right = len(nums)-1
            elif temp >0:
                if right-1 <left +1:
                    right -=1
                else:
                    # print(f'done ... ran out of values')
                    return return_value
                    
                
                    

            
nums = [-1,0,1,2,-1,-4]
myObj=Solution()
result= myObj.threeSum(nums)
print(result)

