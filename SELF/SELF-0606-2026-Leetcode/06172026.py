# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

# Instead of square brackets [], use parentheses (). This creates a generator expression, which evaluates items one at a time (lazily). Passing it to next() extracts just the first item and stops immediatel
# numbers = [10, 15, 20, 25, 30]
# # Get the first number greater than 18
# first_match = next(n for n in numbers if n > 18)
# print(first_match)  # Output: 20

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return next(n for n in range(1,10**5) if n not in nums)

# nums = [1,2,0]
# nums = [3,4,-1,1]      
nums = [7,8,9,11,12]

my_object = Solution()
print(my_object.firstMissingPositive(nums))
