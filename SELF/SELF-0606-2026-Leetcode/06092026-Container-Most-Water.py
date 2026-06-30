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
# =============================

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # create a list of tuples (cartesian coordinates)
        new_list = []
        # var to hold greatest area determined
        max_area = 0 
        count =0
        for count in range(0,len(height)):
            x=count+1
            y=height[count]
            temp = (x,y)
            new_list.append(temp)
        # create shallow copy of list we just created
        new_list2=new_list[:]
        for item in new_list:
            x1 = item[0]
            y1 = item[1]
            for item2 in new_list2:
                x2=item2[0]
                y2=item2[1]
                horizontal_distance =abs(x1-x2)
                vertical_distance = min(y1,y2)
                count +=1
                area = horizontal_distance * vertical_distance
                print(f'Count:{count} area: {area}')
           
                if area > max_area:
                    max_area = area 
                # print(f'{x1},{y1} to {x2},{y2} = {area}')
            # remove first item in list since redundant comparisons
            new_list2 = new_list2[1:]
            # print(new_list2)
        return max_area
        
height = [1,8,6,2,5,4,8,3,7]  
# height = [1,2,3]
myObj = Solution()
result=myObj.maxArea(height=height)
print(result)