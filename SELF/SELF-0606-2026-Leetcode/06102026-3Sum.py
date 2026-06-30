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

import itertools
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_sequences = list(itertools.combinations(nums,3))
        temp = [sorted(item) for item in all_sequences if sum(item) ==0]
        #temp = set(tuple(item) for item in nums if sum(item)==0)
        unique_tuples = set(tuple(item) for item in temp)
        return( list(unique_tuples ))
        
myObj = Solution()
nums = [-1,0,1,2,-1,-4]
#Output Expected  [[-1,-1,2],[-1,0,1]]
result=myObj.threeSum(nums=nums)
print(result)


