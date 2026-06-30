# 2078. Two Furthest Houses With Different Colors
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/
# There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

# Return the maximum distance between two houses with different colors.
# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

# Input: colors = [1,1,1,6,1,1,1]
# Output: 3
# Explanation: In the above image, color 1 is blue, and color 6 is red.
# The furthest two houses with different colors are house 0 and house 3.
# House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
# Note that houses 3 and 6 can also produce the optimal answer

#0325pm this failed
# [9,9,9,18,9,9,9,9,9,18]
# ✅ expected 9
# ❌ my output 3 

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        base = colors[0]
        pMatch=False
        count = None
        # quick solution for [9,9,9,18,9,9,9,9,9,18]
        if colors[0] != colors[len(colors)-1]:
            return len(colors)-1
        
        # [4,4,4,11,4,4,11,4,4,4,4,4] #8
        # create list of unique e.g. [4,11]
        unique_colors = list(set(colors))
        # print(unique_colors)
        
        tuple_list =[]
        for color in unique_colors:
            # enumerate - return (0,4) index,value pairs
            #           - use list comprehension to build list of indexes
            indexes = [i for i, v in enumerate(colors) if v == color]
            min_index = min(indexes)
            max_index = max(indexes)
            #print(f'color:{color} min_index:{min_index}, max_index: {max_index}')
            result = (min_index, max_index)
            tuple_list.append(result)
        #print(tuple_list)
        delta1 = abs(tuple_list[0][0] - tuple_list[1][1])  # min of first, max of second
        delta2 = abs(tuple_list[1][0] - tuple_list[0][1])  # min of second, max of first
        biggest_delta = max(delta1, delta2)
        print(biggest_delta)  # 3
        # for count in range (1,len(colors)-1):
        #     if colors[count] == base:
        #         print(f'base:{base}, colors[{count}]: {colors[count]}')
        #         pMatch = True
        #     else:
        #         if pMatch == True:
        #             return count
        if count is not None:
           return count+1
        else:
           return 1
            

# colors = [1,1,1,6,1,1,1] #3
# colors = [1,8,3,8,3] #4
# colors =[0,1] #1

colors = [9,9,9,18,9,9,9,9,9,18]#9
colors=[4,4,4,11,4,4,11,4,4,4,4,4] #8
my_object = Solution()
print(my_object.maxDistance(colors=colors))