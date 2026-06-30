# leetcode: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/2035248789/
#
# 0616-2026 passed 913am!

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #build regular dictionary thr. comprehension
        d = {i: v for i, v in enumerate(nums)}
        
        #build reverse dictionary
        from collections import defaultdict
        reverse = defaultdict(list)
        for k, v in d.items():
            reverse[v].append(k)
        
        result=reverse[target]
        
        if result:
            if len(result) ==2:
                return result
            elif len(result) ==1:
                result.append(result[0])
                return result
            elif len(result) >2:
                min= result[0]
                max = result[len(result)-1]
                result =[]
                result.append(min)
                result.append(max)
                return result
        else:
            return [-1,-1]


        
nums = [5,7,7,8,8,10]
# nums =[1]
# nums = [3,3,3]
my_object = Solution()
print(my_object.searchRange(nums=nums,  target=3))


# d = {i: v for i, v in enumerate(nums)}


