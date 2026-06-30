# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


def find_indices(in_list,target):
    return_list =[]
    for num in in_list:
        principle = num
        temp_list = in_list[:]
        temp_list.remove(principle)
        for num2 in temp_list:
            if principle +num2 == target:
                return_list.append(in_list.index(principle))
                if principle == num2:
                    # accomodating [3,3] issue
                    start_point = in_list.index(principle) +1
                    # The .index(value, start) method allows you to specify a starting position for the search.
                    return_list.append(in_list.index(num2,start_point))
                else:
                    return_list.append(in_list.index(num2))
                return return_list
            
# ✅nums = [2,7,11,15]
# ✅target = 9
# ✅nums = [3,2,4]
# ✅target = 6
nums = [3,3]
target = 6
print(find_indices(nums,target))
            

