# 0609-2026 
# 52 / 65 test cases passe but time limit exceeded.
# ✅ IDEA remove first entry from new_list2 at the completion of the for loop to prevent a redundant comparison (TJS: this helps but didn't solve time constraint issue)
# ✅ IDEA:instead of lists use dictionary, which requires re-write.

# =============================
# =============================
# Leetcode Challenge 
# https://leetcode.com/problems/container-with-most-water/submissions/2027667678/
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# =============================# =============================
# This solution is from Gemini TJS: 0610-2026
# - it cleverly reduces number of calculations from 53 to 8
# - over larger data sets that difference is telling
# =============================# =============================
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        count = 0 # TJS
        while left < right:
            # Width is the index difference
            width = right - left
            #print(f"width is now {width}, right: {right} , left:{left}")
            # Water height is bounded by the shorter wall
            current_height = min(height[left], height[right])
           
            # Calculate and update max area
            
            area = width * current_height
            count += 1
            print(f'Count:{count} area: {area}')
           
            #print(f'current area: {area}, max area {max_area}')
            if area > max_area:
                max_area = area
            
                
            # Crucial step: move the pointer pointing to the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
        
height = [1,8,6,2,5,4,8,3,7]  
# height = [1,2,3]
myObj = Solution()
result=myObj.maxArea(height=height)
print(result)