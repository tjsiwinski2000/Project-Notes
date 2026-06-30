# You are given an integer array nums.
# You replace each element in nums with the sum of its digits.
# Return the minimum element in nums after all replacements.

# Example 1:
# Input: nums = [10,12,13,14]
# Output: 1

# Explanation:bnums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

# Example 2:
# Input: nums = [1,2,3,4]

# Output: 1 Explanation:nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

# Example 3:
# Input: nums = [999,19,199]
# Output: 10
# Explanation: nums becomes [27, 10, 19] after all replacements, with minimum element 10.
#
#https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/?envType=daily-question&envId=2026-06-18

class Solution:
    def minElement(self, nums: list[int]) -> int:
        smallest=10000
        for num in nums:
            print(f'num: {num}')
            temp=sum([int(item) for item in list(str(num))])
            smallest= min(smallest,temp)
        return smallest

#both solutions work, experimenting with runtime and memory usage
class Solution:
    def minElement(self, nums: list[int]) -> int:
        out_list =[]
        for num in nums:
            # print(f'num: {num}')
            temp=sum([int(item) for item in list(str(num))])
            out_list.append(temp)
        return min(out_list)

my_obj = Solution()
my_obj = Solution()
nums = [10,12,13,14]
nums = [1,2,3,4]
nums = [999,19,199]
print(my_obj.minElement(nums=nums))
# {sum([int(item) for item in list(str(num))] )}

 