# leetcode challenge 
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# claude suggestions
# Your solution works, but there are two issues worth flagging:
# 1. It's not O(log n) — the problem requires binary search. Building a dictionary is O(n). For a LeetCode submission this would likely still pass, but it doesn't meet the stated requirement.
# 2. Your result handling can be simplified — since the list is already sorted, the first and last elements are always the min and max:

if result:
    return [result[0], result[-1]]
else:
    return [-1, -1]
# That covers all cases (1 item, 2 items, 10 items) without the if/elif chain.

# class Solution(object):
    def searchRange(self, nums, target):
        def find_left(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo

        def find_right(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi

        left = find_left(nums, target)
        right = find_right(nums, target)

        if left <= right and right < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]
    
#=================================================
# my implementation based on casual review of AI's solution
    
def left(list,tgt):
    for index in range(0,len(list)):
        if list[index] == tgt:
            return index
    return -1

def right(list,tgt):
    for index in range(len(list)-1, 0,-1):
        if list[index] == tgt:
            return index
    return -1

nums = [5,7,7,8,8,10]
target = 8

print(f'{left(nums,target)},{right(nums,target)}')